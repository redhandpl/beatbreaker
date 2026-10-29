# ESP32-S3 direct-input bench

Standalone **Arduino C++** firmware for one fader, one potentiometer, one normally-open button and one **AS5048A SPI** jog sensor. It prints CSV to a serial monitor. It does **not** send MIDI, switch NUDGE/SCRATCH modes, use PCF8575/74HC4067, or change the approved controller design.

This is a separate diagnostic bench, not completion of the project's V0.1 gate. Full-controller power/wiring approval and physical tests remain open. No firmware has been uploaded by the assistant.

## Files and language

- `bench_inputs.ino`: the Arduino sketch, compiled as C++, not interpreted on the board.
- `input_logic.h`: SPI response validation, magnetic diagnostics, angle wrap and button debounce.
- `tests/input_logic_test.cpp`: deterministic host regression tests; not compiled into the sketch.

The compiler builds ESP32-S3 machine code. Upload writes that firmware to the board's flash. Afterward the board runs `setup()` once and `loop()` repeatedly whenever powered; the computer is only needed for programming and observing the serial output.

## Before wiring or uploading

1. Identify the actual ESP32-S3 board/module and its flash/PSRAM variant. The project's DevKitC-1 drawing is a reference, not confirmation of your actual board.
2. Identify the real AS5048A breakout's header labels and supply circuit. The retained [100x100 pinout image](../../elements/AS5048A_pinouts.jpg) is insufficient to assign physical header positions. **Do not infer them from this table or from a similar module.** AS5048B/I2C and quadrature encoders are not supported by this sketch.
3. Confirm the sensor board can run with **3.3 V supply and 3.3 V SPI signals**. The AS5048A IC supports a 3.3 V mode, but its supply-pin connections depend on that mode and the breakout. Do not blindly connect a board terminal marked `5V` to 3V3 or bridge supply pins without its actual schematic.
4. Use only one computer USB connection for this bench. Leave the RS-25-5/mains supply, Raspberry Pi, DAC, LED power and all other external supplies disconnected. Never apply 5 V to an ESP32 input. Make/inspect wiring with USB disconnected.
5. Identify fader/pot end terminals and wipers using the actual part documentation or an unpowered resistance measurement. Identify the button's actual normally-open contact pair; legs of a four-leg tactile button may already be connected in pairs.
6. Upload replaces the firmware currently on the ESP32. Preserve any existing source/firmware before choosing Upload.

## Proposed bench pin allocation

Use **GPIO labels**, not an assumed physical header-pin number. This temporary allocation is not the complete E01 allocation: GPIO4 is borrowed for the direct button and GPIO7 bypasses the future mux.

| Bench signal | ESP32-S3 GPIO | Connection after actual terminals are verified |
|---|---:|---|
| Fader wiper | 1 / ADC1 | Wiper to GPIO1; outer ends to 3V3 and GND |
| Potentiometer wiper | 7 / ADC1 | Wiper to GPIO7; outer ends to 3V3 and GND |
| Normally-open button | 4 | Contact between GPIO4 and GND; internal pull-up enabled, pressed = LOW |
| AS5048A clock | 15 | Verified sensor `CLK`/`SCK` |
| AS5048A command input | 16 | Verified sensor `MOSI` |
| AS5048A response output | 17 | Verified sensor `MISO` |
| AS5048A chip select | 18 | Verified sensor `CSn`, active LOW |
| Sensor ground | GND | Common ground |
| Sensor supply | **Requires breakout confirmation** | Use only its verified 3.3 V configuration; no physical supply-pin order assigned here |

PWM and other unused sensor outputs stay unconnected. Do not connect this temporary GPIO4 button simultaneously to another circuit.

The ADC reports 12-bit **raw counts**, not calibrated travel, resistance or voltage. ESP32-S3's documented range at maximum Arduino attenuation is approximately 0–3100 mV, so a wiper supplied from 3V3 can saturate before the end of travel. This program deliberately does not claim full-travel linearity or scale raw counts into a calibrated control value. Do not use 5 V to fix a low reading. Analog endpoint calibration or a source-backed analog front end is separate work.

## Arduino IDE: compile and upload

Reference build: **esp32 by Espressif Systems 3.3.12**, generic **ESP32S3 Dev Module** (`esp32:esp32:esp32s3`). Generic-board compilation does not identify the actual module or qualify its flash/PSRAM settings.

1. Open **Arduino IDE**.
2. In **Settings → Additional boards manager URLs**, add the official index if not already present: `https://espressif.github.io/arduino-esp32/package_esp32_index.json`.
3. In **Boards Manager**, install **esp32 by Espressif Systems 3.3.12** if missing. The package can also be installed with the CLI below without persisting the additional URL in IDE settings.
4. Open `bench_inputs.ino` from this directory; keep `input_logic.h` next to it.
5. Select your verified ESP32-S3 board. For the generic reference build choose **ESP32S3 Dev Module**. Do not guess another board's memory settings.
6. Initial UART workflow for a board with a USB-to-UART connector: use that connector, set **USB CDC On Boot → Disabled**, and select its serial port. `Serial` then uses UART0. Do not connect a second USB power source.
7. Click **Verify** to compile. Click **Upload** only after the board/settings and wiring are confirmed.
8. If automatic download mode fails, use the actual board manufacturer's BOOT/RESET procedure. A common DevKit procedure is to hold BOOT, tap RESET, start upload and release BOOT when connection begins; verify this applies to your board.
9. Open **Serial Monitor**, **115200 baud**. Reset the board to see the banner/header again.

If the actual board has only native USB, its USB CDC settings and port differ: with **USB CDC On Boot → Enabled**, `Serial` uses native USB instead of UART0. The same source uses `Serial`, but that is not the reference UART build. Identify the board before choosing this route; do not connect both USB connectors just to find the output.

## Optional command-line workflow

Run from the repository root. `arduino-cli` may be on PATH; the existing Arduino IDE also bundles it at:

```sh
ARDUINO_CLI='/Applications/Arduino IDE.app/Contents/Resources/app/lib/backend/resources/arduino-cli'
INDEX='https://espressif.github.io/arduino-esp32/package_esp32_index.json'
"$ARDUINO_CLI" core update-index --additional-urls "$INDEX"
"$ARDUINO_CLI" core install esp32:esp32@3.3.12 --additional-urls "$INDEX"
"$ARDUINO_CLI" compile --fqbn esp32:esp32:esp32s3 firmware/bench_inputs
"$ARDUINO_CLI" board list
```

Select the actual board's port from that output and set the shell variable `PORT` to it. Only after confirming the board, settings and overwrite intent:

```sh
"$ARDUINO_CLI" upload --fqbn esp32:esp32:esp32s3 --port "$PORT" firmware/bench_inputs
"$ARDUINO_CLI" monitor --port "$PORT" --config baudrate=115200
```

Close Serial Monitor before uploading if it owns the port. No port name is guessed or hard-coded in this project.

## Reading the output

A CSV row is emitted approximately every 100 ms; inputs are scheduled approximately every 1 ms. These are bench defaults, not measured latency guarantees. Serial output and ADC/SPI work can stretch the interval. There is no wait-for-monitor loop at startup.

| Column | Meaning |
|---|---|
| `ms` | Milliseconds since boot, unsigned 32-bit wrap |
| `fader_raw`, `pot_raw` | Latest unfiltered 0–4095 ADC readings; disconnected ADC inputs float |
| `button_pressed` | Debounced contact: 1 pressed, 0 released |
| `presses`, `releases` | Accepted transitions since boot; button held at boot does not create a synthetic press |
| `jog_status` | SPI/magnetic diagnostic status below |
| `angle_raw`, `angle_deg` | 14-bit absolute angle / degrees; `NA` when invalid, not a physical calibration certificate |
| `delta_counts` | Signed net motion since the preceding report, including valid samples earlier in a window that later faults |
| `position_counts` | Accumulated valid signed motion; 16384 counts = one revolution; not an absolute position across outages |
| `agc`, `magnitude` | Sensor magnetic telemetry, or `NA` when those register reads failed; magnitude is not a calibrated mT value |
| `invalid_samples` | Samples rejected for SPI or magnetic errors, cumulative since boot |

There is no rotation filter, direction inversion or zero-position programming. Positive rotation is the sensor's increasing-angle direction; compare it with your physical view. At each invalid sample, motion tracking drops its old baseline. The first recovered valid sample establishes a new baseline, avoiding a fake jump but losing movement during the outage. Exactly half-turn steps are ambiguous and discarded. Like any wrapped-angle tracker, direction assumes less than half a turn between successive valid samples.

Button debounce is 20 ms, a bench starting value rather than a measured hardware requirement. A complete press/release shorter than the debounce interval can be ignored. Changing the debounce or sampling defaults requires rerunning the applicable checks and measuring the hardware.

### Jog statuses

- `OK`: response parity/error flag and sampled diagnostic flags passed; not proof of mechanical alignment or absolute accuracy.
- `SPI_PARITY`: corrupted response. Check verified SPI wiring, ground, signal levels and connections.
- `SPI_ERROR`: device reported a communication error. The sketch reads the clear-error register, discards the sample and tries normally on the next scheduled sample.
- `NOT_READY`: offset compensation not finished, or invalid/missing communication returning zeros. A weak internal MISO pull-down reduces floating-input ambiguity but does not prove a sensor is present.
- `CORDIC_OVERFLOW`: sensor reports invalid angle/magnitude.
- `FIELD_TOO_STRONG`, `FIELD_TOO_WEAK`: magnetic warning. Raw angle is not accepted for motion; AGC/magnitude remain visible if their reads succeeded. Inspect the actual magnet and installation against the sensor documentation; no new magnet-gap dimension is selected here.

SPI uses MODE1, MSB first, 1 MHz and separate 16-bit command/response frames with chip-select timing margins. Reads are pipelined. Parity covers all 16 bits. Only read commands, NOP and the read-to-clear error register are used; the sketch never writes zero-position or OTP programming registers.

## Bench procedure

1. Start with the ESP32 alone: confirm boot/output and identify the correct port. An absent jog is an expected fault, not a valid zero-angle reading.
2. Disconnect USB, attach verified fader/pot/button wiring, reconnect. Move each analog control independently; check button press/release counters, held state and contact bounce.
3. Disconnect USB and attach the sensor only after confirming its header and 3.3 V configuration. Rotate the actual magnet/jog slowly in both directions and across 0/360 degrees. Observe status, angle, signed motion and invalid samples.
4. Check stationary readings and the existing jog's full mechanical press travel. AS5048A does not itself detect a hand resting on a stationary platter; no touch sensor or mechanical redesign is included.
5. Repeat simultaneous input movement. Record actual board/module, connections, behavior and faults. Electrical/mechanical acceptance thresholds remain engineer-owned; this diagnostic run does not close the complete-controller prototype gates.

## Host regression checks

From the repository root, create the task-controlled output directory, then run:

```sh
mkdir -p tmp/esp32-bench-inputs
clang++ -std=c++17 -Wall -Wextra -Werror -pedantic \
  firmware/bench_inputs/tests/input_logic_test.cpp \
  -o tmp/esp32-bench-inputs/input_logic_test
tmp/esp32-bench-inputs/input_logic_test
```

The checks cover command parity/address boundaries, every single-bit corruption of representative responses, device errors, zero/disconnected diagnostics, field warnings, angle wrap/recovery/ambiguity and debouncing across timer rollover. They do not emulate the complete ESP32 ADC/SPI peripherals or prove electrical operation.

## Executed verification

- Official Espressif Arduino core **3.3.12** and its toolchain are available in the existing Arduino installation. No third-party sensor library was added.
- Host regression executable passed with Apple clang17, C++17, `-Wall -Wextra -Werror -pedantic`: command/response integrity, magnetic flags, angle wrap/recovery/ambiguity and button bounce/held/rollover cases.
- The actual sketch's `setup()`/`loop()` also ran with temporary **simulated Arduino/SPI I/O**. CSV analog/button output, pipelined register reads, valid angle zero, wrap, parity rejection/recovery, latched-error clearing and magnetic-error output passed. This was not execution on an ESP32 or a physical sensor.
- Real cross-compilation produced ESP32-S3 ELF/application/merged images for `esp32:esp32:esp32s3`. The compiled helper matches the source after Arduino's generated `#line` directive. `esptool5.3.1 --chip esp32s3 image-info` confirmed chipID9, a319968-byte application, valid checksum and valid image hash. Reference image settings are4MB flash/DIO/80MHz, not detected hardware settings.
- All27 protected prior source/CAD/electrical inputs and all five approved B25-ELEC-02 files remained byte-identical. Temporary test adapters, host executables and target build outputs were removed after inspection; the permanent regression source remains.
- No upload, serial-port connection, powered reading, electrical fit or physical jog test was performed. Recompile for the verified actual board before upload; this is not a prequalified binary release.

## Sources and remaining limits

- [AS5048A/AS5048B datasheet v1-11](https://download.mikroe.com/documents/datasheets/AS5048A_datasheet.pdf), SPI operation/register/diagnostic and 3.3 V supply sections. This defines the IC protocol, not the purchased breakout header order.
- [Arduino-ESP32 ADC API](https://docs.espressif.com/projects/arduino-esp32/en/latest/api/adc.html).
- [Arduino-ESP32 Tools menu and serial selection](https://docs.espressif.com/projects/arduino-esp32/en/latest/guides/tools_menu.html).
- [Project electrical baseline and unresolved gates](../../schematics/electronics/E01/DJC_Electrical_Rev_E01_definition.json).

Actual board/module identity, readable sensor header/supply topology, terminal identification, powered readings, timing/noise, full jog travel and flash/upload behavior require hardware confirmation. No CAD, approved drawing, PCB, mains, power-source combination or NUDGE/SCRATCH change is included.
