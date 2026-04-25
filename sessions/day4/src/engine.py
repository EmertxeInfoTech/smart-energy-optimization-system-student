from config import DEFAULT_THRESHOLD, DEFAULT_BUFFER, DEFAULT_OP_START, DEFAULT_OP_END


class DecisionEngine:
    def __init__(self):
        self.ac_state   = False
        self.last_reason = "Simulation starting..."

    def evaluate(self, data, threshold=DEFAULT_THRESHOLD, buffer=DEFAULT_BUFFER,
                 op_start=DEFAULT_OP_START, op_end=DEFAULT_OP_END):
        temp      = data["temperature"]
        occupancy = data["occupancy"]
        hour      = data["hour"]
        upper     = round(threshold + buffer, 1)
        lower     = round(threshold - buffer, 1)

        # Rule 1: Room is unoccupied — highest priority
        if occupancy == 0:
            self.ac_state    = False
            self.last_reason = "Rule 1: Room is unoccupied → AC OFF"
            return self.ac_state

        # Rule 2: Outside operational hours
        if not (op_start <= hour < op_end):
            self.ac_state    = False
            self.last_reason = f"Rule 2: Outside operational hours ({hour:02d}:00) → AC OFF"
            return self.ac_state

        # Rule 3: Temperature above upper hysteresis bound → turn ON
        if temp > upper:
            self.ac_state    = True
            self.last_reason = f"Rule 3: {temp}°C > upper threshold {upper}°C → AC ON"
            return self.ac_state

        # Rule 4: Temperature below lower hysteresis bound → turn OFF
        if temp < lower:
            self.ac_state    = False
            self.last_reason = f"Rule 4: {temp}°C < lower threshold {lower}°C → AC OFF"
            return self.ac_state

        # Rule 5: Within hysteresis band → hold current state
        state_str        = "ON" if self.ac_state else "OFF"
        self.last_reason = (
            f"Rule 5: {temp}°C within band ({lower}°C – {upper}°C)"
            f" → Holding {state_str}"
        )
        return self.ac_state
