#include <Arduino.h>
#include <SPI.h>
#include "input_logic.h"

#if !defined(CONFIG_IDF_TARGET_ESP32S3)
#error "Select an ESP32-S3 board. This sketch is not for ESP32/ESP32-S2/ESP32-C3."
#endif

constexpr uint8_t kFaderPin = 1;
constexpr uint8_t kPotPin = 7;
constexpr uint8_t kButtonPin = 4;
constexpr uint8_t kSckPin = 15;
constexpr uint8_t kMosiPin = 16;
constexpr uint8_t kMisoPin = 17;
constexpr uint8_t kCsPin = 18;
constexpr uint32_t kBaud = 115200;
constexpr uint32_t kSampleMs = 1;
constexpr uint32_t kReportMs = 100;
constexpr uint32_t kDebounceMs = 20;
constexpr uint32_t kSpiHz = 1000000;
constexpr uint16_t kDiagnosticsRegister = 0x3FFD;
constexpr uint16_t kMagnitudeRegister = 0x3FFE;
constexpr uint16_t kAngleRegister = 0x3FFF;
constexpr uint16_t kClearErrorRegister = 0x0001;

struct JogReading {
    bench::JogStatus status = bench::JogStatus::NotReady;
    uint16_t angle = 0;
    uint16_t diagnostics = 0;
    uint16_t magnitude = 0;
    bool magneticTelemetryValid = false;
};

bench::ButtonDebouncer button(kDebounceMs);
bench::AngleTracker angleTracker;
JogReading jog;
uint16_t faderRaw = 0;
uint16_t potRaw = 0;
uint32_t buttonPresses = 0;
uint32_t buttonReleases = 0;
uint32_t jogInvalidSamples = 0;
int32_t deltaSinceReport = 0;
int64_t positionCounts = 0;
uint32_t lastSample = 0;
uint32_t lastReport = 0;

uint16_t transferFrame(uint16_t command) {
    digitalWrite(kCsPin, LOW);
    delayMicroseconds(1);
    const uint16_t response = SPI.transfer16(command);
    delayMicroseconds(1);
    digitalWrite(kCsPin, HIGH);
    delayMicroseconds(1);
    return response;
}

bench::JogStatus readRegister(uint16_t address, uint16_t& data) {
    transferFrame(bench::readCommand(address));
    const bench::JogStatus status = bench::decodeResponse(transferFrame(0x0000), data);
    if (status == bench::JogStatus::SensorError) {
        // Reading 0x0001 clears the latched SPI error; it does not program OTP.
        transferFrame(bench::readCommand(kClearErrorRegister));
        transferFrame(0x0000);
    }
    return status;
}

JogReading readJog() {
    JogReading result;
    SPI.beginTransaction(SPISettings(kSpiHz, MSBFIRST, SPI_MODE1));
    result.status = readRegister(kDiagnosticsRegister, result.diagnostics);
    if (result.status == bench::JogStatus::Ok) {
        result.status = readRegister(kMagnitudeRegister, result.magnitude);
        result.magneticTelemetryValid = result.status == bench::JogStatus::Ok;
    }
    if (result.status == bench::JogStatus::Ok) {
        result.status = readRegister(kAngleRegister, result.angle);
    }
    SPI.endTransaction();
    if (result.status == bench::JogStatus::Ok) {
        result.status = bench::checkDiagnostics(result.diagnostics);
    }
    return result;
}

const char* statusName(bench::JogStatus status) {
    switch (status) {
        case bench::JogStatus::Ok: return "OK";
        case bench::JogStatus::ParityError: return "SPI_PARITY";
        case bench::JogStatus::SensorError: return "SPI_ERROR";
        case bench::JogStatus::NotReady: return "NOT_READY";
        case bench::JogStatus::CordicOverflow: return "CORDIC_OVERFLOW";
        case bench::JogStatus::FieldTooStrong: return "FIELD_TOO_STRONG";
        case bench::JogStatus::FieldTooWeak: return "FIELD_TOO_WEAK";
    }
    return "UNKNOWN";
}

void sampleInputs(uint32_t now) {
    faderRaw = analogRead(kFaderPin);
    potRaw = analogRead(kPotPin);
    if (button.update(digitalRead(kButtonPin) == LOW, now)) {
        if (button.pressed()) {
            ++buttonPresses;
        } else {
            ++buttonReleases;
        }
    }

    jog = readJog();
    if (jog.status != bench::JogStatus::Ok) {
        ++jogInvalidSamples;
        angleTracker.reset();
        return;
    }
    int16_t delta = 0;
    const bool hadPrevious = angleTracker.update(jog.angle, delta);
    if (hadPrevious) {
        deltaSinceReport += delta;
        positionCounts += delta;
    }
}

void reportInputs(uint32_t now) {
    Serial.printf("%lu,%u,%u,%u,%lu,%lu,%s,",
                  static_cast<unsigned long>(now), faderRaw, potRaw,
                  button.pressed() ? 1U : 0U,
                  static_cast<unsigned long>(buttonPresses),
                  static_cast<unsigned long>(buttonReleases), statusName(jog.status));
    if (jog.status == bench::JogStatus::Ok) {
        Serial.printf("%u,%.3f,", jog.angle, jog.angle * (360.0 / bench::kCountsPerTurn));
    } else {
        Serial.print("NA,NA,");
    }
    Serial.printf("%ld,%lld,", static_cast<long>(deltaSinceReport),
                  static_cast<long long>(positionCounts));
    if (jog.magneticTelemetryValid) {
        Serial.printf("%u,%u,", jog.diagnostics & 0x00FFU, jog.magnitude);
    } else {
        Serial.print("NA,NA,");
    }
    Serial.printf("%lu\n", static_cast<unsigned long>(jogInvalidSamples));
    deltaSinceReport = 0;
}

void setup() {
    Serial.begin(kBaud);
    pinMode(kFaderPin, INPUT);
    pinMode(kPotPin, INPUT);
    pinMode(kButtonPin, INPUT_PULLUP);
    digitalWrite(kCsPin, HIGH);
    pinMode(kCsPin, OUTPUT);
    SPI.begin(kSckPin, kMisoPin, kMosiPin, kCsPin);
    pinMode(kMisoPin, INPUT_PULLDOWN);
    analogReadResolution(12);
    analogSetPinAttenuation(kFaderPin, ADC_11db);
    analogSetPinAttenuation(kPotPin, ADC_11db);
    const uint32_t now = millis();
    button.reset(digitalRead(kButtonPin) == LOW, now);
    lastSample = lastReport = now;
    Serial.println("# redController direct-input bench; no MIDI; 115200 baud");
    Serial.println("# GPIO: fader=1 pot=7 button=4 SCK=15 MOSI=16 MISO=17 CSn=18");
    Serial.println("# Raw ADC counts are not calibrated travel or voltage; 3.3V may saturate ADC.");
    Serial.println("ms,fader_raw,pot_raw,button_pressed,presses,releases,jog_status,angle_raw,angle_deg,delta_counts,position_counts,agc,magnitude,invalid_samples");
}

void loop() {
    const uint32_t now = millis();
    if (static_cast<uint32_t>(now - lastSample) >= kSampleMs) {
        lastSample = now;
        sampleInputs(now);
    }
    if (static_cast<uint32_t>(now - lastReport) >= kReportMs) {
        lastReport = now;
        reportInputs(now);
    }
    delay(1);
}
