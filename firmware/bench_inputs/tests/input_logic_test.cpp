#include "../input_logic.h"

#include <assert.h>
#include <stdio.h>
#include <initializer_list>

using bench::JogStatus;

uint16_t responseWord(uint16_t data, bool error = false) {
    uint16_t word = (data & 0x3FFFU) | (error ? 0x4000U : 0U);
    unsigned ones = 0;
    for (unsigned bit = 0; bit < 15; ++bit) {
        ones += (word >> bit) & 1U;
    }
    return word | ((ones & 1U) ? 0x8000U : 0U);
}

void checkProtocol() {
    assert(bench::readCommand(0x3FFF) == 0xFFFF);
    assert(bench::readCommand(0x3FFD) == 0x7FFD);
    assert(bench::readCommand(0x3FFE) == 0x7FFE);
    assert(bench::readCommand(0x0001) == 0x4001);
    for (unsigned address = 0; address <= 0x3FFF; ++address) {
        const uint16_t command = bench::readCommand(address);
        assert((command & 0x3FFFU) == address);
        assert((command & 0x4000U) != 0);
        unsigned ones = 0;
        for (unsigned bit = 0; bit < 16; ++bit) {
            ones += (command >> bit) & 1U;
        }
        assert((ones & 1U) == 0);
    }
    for (uint16_t data : {uint16_t{0}, uint16_t{1}, uint16_t{8192}, uint16_t{16383}}) {
        const uint16_t word = responseWord(data);
        uint16_t decoded = 123;
        assert(bench::decodeResponse(word, decoded) == JogStatus::Ok);
        assert(decoded == data);
        for (unsigned bit = 0; bit < 16; ++bit) {
            decoded = 123;
            assert(bench::decodeResponse(word ^ (1U << bit), decoded) == JogStatus::ParityError);
            assert(decoded == 123);
        }
        assert(bench::decodeResponse(responseWord(data, true), decoded) == JogStatus::SensorError);
    }
    uint16_t decoded = 123;
    assert(bench::decodeResponse(0xFFFF, decoded) == JogStatus::SensorError);
    assert(bench::decodeResponse(0, decoded) == JogStatus::Ok);
    assert(bench::checkDiagnostics(decoded) == JogStatus::NotReady);
    assert(bench::checkDiagnostics(0x0100) == JogStatus::Ok);
    assert(bench::checkDiagnostics(0x01FF) == JogStatus::Ok);
    assert(bench::checkDiagnostics(0x0300) == JogStatus::CordicOverflow);
    assert(bench::checkDiagnostics(0x0500) == JogStatus::FieldTooStrong);
    assert(bench::checkDiagnostics(0x0900) == JogStatus::FieldTooWeak);
    puts("PASS: read commands, all addresses, zero/full-scale data, every single-bit corruption, error flags and magnetic diagnostics");
}

void checkAngle() {
    bench::AngleTracker tracker;
    int16_t delta = 123;
    assert(!tracker.update(16380, delta));
    assert(delta == 0);
    assert(tracker.update(2, delta) && delta == 6);
    assert(tracker.update(16380, delta) && delta == -6);
    assert(tracker.update(16380, delta) && delta == 0);
    tracker.reset();
    assert(!tracker.update(4000, delta) && delta == 0);
    assert(tracker.update(4001, delta) && delta == 1);
    assert(!tracker.update(12193, delta) && delta == 0);
    assert(tracker.update(12192, delta) && delta == -1);
    tracker.reset();
    assert(!tracker.update(9000, delta));
    assert(!tracker.update(808, delta) && delta == 0);
    tracker.reset();
    assert(!tracker.update(0, delta));
    int64_t total = 0;
    for (unsigned count = 1; count <= 3U * bench::kCountsPerTurn; ++count) {
        assert(tracker.update(count & bench::kAngleMask, delta));
        total += delta;
    }
    assert(total == 3 * bench::kCountsPerTurn);
    puts("PASS: bidirectional angle wrap, stationary samples, invalid-data recovery, ambiguous half-turn rejection and three full turns");
}

void checkButton() {
    bench::ButtonDebouncer button(20);
    button.reset(false, 0);
    assert(!button.update(true, 1));
    assert(!button.update(false, 4));
    assert(!button.update(true, 7));
    assert(!button.update(true, 26));
    assert(button.update(true, 27) && button.pressed());
    assert(!button.update(true, 500));
    assert(!button.update(false, 501));
    assert(!button.update(true, 505));
    assert(!button.update(false, 508));
    assert(!button.update(false, 527));
    assert(button.update(false, 528) && !button.pressed());
    button.reset(true, 600);
    assert(button.pressed() && !button.update(true, 900));
    assert(!button.update(false, 901));
    assert(button.update(false, 921));
    button.reset(false, UINT32_MAX - 10U);
    assert(!button.update(true, UINT32_MAX - 5U));
    assert(!button.update(true, 13));
    assert(button.update(true, 14) && button.pressed());
    puts("PASS: press/release bounce, held input, startup-held button and millis rollover");
}

int main() {
    checkProtocol();
    checkAngle();
    checkButton();
}
