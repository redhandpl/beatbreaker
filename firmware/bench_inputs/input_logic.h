#pragma once

#include <stdint.h>

namespace bench {

constexpr uint16_t kAngleMask = 0x3FFF;
constexpr int32_t kCountsPerTurn = 16384;

enum class JogStatus : uint8_t {
    Ok,
    ParityError,
    SensorError,
    NotReady,
    CordicOverflow,
    FieldTooStrong,
    FieldTooWeak,
};

inline bool hasEvenParity(uint16_t word) {
    word ^= word >> 8;
    word ^= word >> 4;
    word ^= word >> 2;
    word ^= word >> 1;
    return (word & 1U) == 0;
}

inline uint16_t readCommand(uint16_t address) {
    uint16_t command = (address & kAngleMask) | 0x4000U;
    if (!hasEvenParity(command)) {
        command |= 0x8000U;
    }
    return command;
}

inline JogStatus decodeResponse(uint16_t word, uint16_t& data) {
    if (!hasEvenParity(word)) {
        return JogStatus::ParityError;
    }
    if ((word & 0x4000U) != 0) {
        return JogStatus::SensorError;
    }
    data = word & kAngleMask;
    return JogStatus::Ok;
}

inline JogStatus checkDiagnostics(uint16_t data) {
    if ((data & 0x0100U) == 0) {
        return JogStatus::NotReady;
    }
    if ((data & 0x0200U) != 0) {
        return JogStatus::CordicOverflow;
    }
    if ((data & 0x0400U) != 0) {
        return JogStatus::FieldTooStrong;
    }
    if ((data & 0x0800U) != 0) {
        return JogStatus::FieldTooWeak;
    }
    return JogStatus::Ok;
}

class AngleTracker {
public:
    void reset() { havePrevious_ = false; }

    // Motion is unambiguous only below half a revolution between valid samples.
    bool update(uint16_t angle, int16_t& delta) {
        delta = 0;
        if (!havePrevious_) {
            previous_ = angle;
            havePrevious_ = true;
            return false;
        }
        int32_t difference = static_cast<int32_t>(angle) - previous_;
        previous_ = angle;
        if (difference == 8192 || difference == -8192) {
            return false;
        }
        if (difference > 8192) {
            difference -= kCountsPerTurn;
        } else if (difference < -8192) {
            difference += kCountsPerTurn;
        }
        delta = static_cast<int16_t>(difference);
        return true;
    }

private:
    bool havePrevious_ = false;
    uint16_t previous_ = 0;
};

class ButtonDebouncer {
public:
    explicit ButtonDebouncer(uint32_t debounceMs) : debounceMs_(debounceMs) {}

    void reset(bool pressed, uint32_t now) {
        stable_ = candidate_ = pressed;
        changedAt_ = now;
    }

    bool update(bool pressed, uint32_t now) {
        if (pressed != candidate_) {
            candidate_ = pressed;
            changedAt_ = now;
        }
        if (candidate_ != stable_ && static_cast<uint32_t>(now - changedAt_) >= debounceMs_) {
            stable_ = candidate_;
            return true;
        }
        return false;
    }

    bool pressed() const { return stable_; }

private:
    const uint32_t debounceMs_;
    uint32_t changedAt_ = 0;
    bool stable_ = false;
    bool candidate_ = false;
};

}  // namespace bench
