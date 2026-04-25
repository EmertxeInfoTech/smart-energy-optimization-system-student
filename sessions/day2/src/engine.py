"""
DecisionEngine — Day 2
======================
Responsibility: Apply five priority-ordered rules each cycle to decide
whether the AC should be ON or OFF.  Maintains AC state across cycles
so the hysteresis band (Rule 5) can hold the current state without switching.

Rule priority (highest → lowest):
  Rule 1  Room is unoccupied          → AC OFF  (overrides everything)
  Rule 2  Outside operational hours   → AC OFF
  Rule 3  temp > upper threshold      → AC ON
  Rule 4  temp < lower threshold      → AC OFF
  Rule 5  temp within hysteresis band → hold current state (no change)

Why hysteresis?
  Without it, if temperature oscillates around 26°C the AC would toggle
  ON and OFF every single cycle — unrealistic and damaging to real equipment.
  The buffer zone (e.g. 24.5–27.5°C) forces the AC to commit to a state
  until temperature moves far enough in one direction.
"""

from config import DEFAULT_THRESHOLD, DEFAULT_BUFFER, DEFAULT_OP_START, DEFAULT_OP_END


class DecisionEngine:

    def __init__(self):
        # Pre-filled: AC starts OFF; reason is shown on the dashboard from cycle 1.
        self.ac_state    = False
        self.last_reason = "Simulation starting..."

    def evaluate(self, data, threshold=DEFAULT_THRESHOLD, buffer=DEFAULT_BUFFER,
                 op_start=DEFAULT_OP_START, op_end=DEFAULT_OP_END):
        """
        Evaluate sensor data and return the new AC state (bool).
        Also updates self.last_reason with a human-readable explanation
        of which rule fired — this is displayed on the dashboard.

        Args:
            data      (dict):  sensor reading from SensorSimulator.get_data()
            threshold (float): target room temperature in °C
            buffer    (float): hysteresis half-width in °C
            op_start  (int):   first hour AC is permitted to run (e.g. 6 → 06:00)
            op_end    (int):   last  hour AC is permitted to run (e.g. 23 → 23:00)

        Returns:
            bool: True = AC ON, False = AC OFF
        """
        temp = data["temperature"]
        occ  = data["occupancy"]
        hour = data["hour"]

        # TODO: compute upper and lower hysteresis bounds
        # HINT: upper = round(threshold + buffer, 1)
        #       lower = round(threshold - buffer, 1)
        #       Rounding keeps the reason strings readable (e.g. 27.5 not 27.500001)
        upper = ...
        lower = ...

        # --- Rule 1: occupancy check — highest priority ---
        # TODO: if occ == 0, set self.ac_state = False
        #       set self.last_reason = "Rule 1: Room is unoccupied → AC OFF"
        #       return self.ac_state immediately
        # HINT: return early so lower-priority rules are never reached

        # --- Rule 2: operational hours check ---
        # TODO: if the current hour is outside [op_start, op_end),
        #       set self.ac_state = False
        #       set self.last_reason = f"Rule 2: Outside operational hours ({hour:02d}:00) → AC OFF"
        #       return self.ac_state immediately
        # HINT: the condition is  NOT (op_start <= hour < op_end)

        # --- Rule 3: temperature above upper bound → turn ON ---
        # TODO: if temp > upper,
        #       set self.ac_state = True
        #       set self.last_reason = f"Rule 3: {temp}°C > upper threshold {upper}°C → AC ON"
        #       return self.ac_state immediately

        # --- Rule 4: temperature below lower bound → turn OFF ---
        # TODO: if temp < lower,
        #       set self.ac_state = False
        #       set self.last_reason = f"Rule 4: {temp}°C < lower threshold {lower}°C → AC OFF"
        #       return self.ac_state immediately

        # --- Rule 5: within hysteresis band → hold current state ---
        # TODO: build the reason string, e.g.:
        #       "Rule 5: 26.0°C within band (24.5°C – 27.5°C) → Holding ON"
        #       set self.last_reason to this string
        #       return self.ac_state unchanged
        # HINT: this is the default fall-through — no if needed here.
        #       Use  ("ON" if self.ac_state else "OFF")  for the state word.
        pass
