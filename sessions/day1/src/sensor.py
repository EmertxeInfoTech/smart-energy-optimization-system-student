"""
SensorSimulator — Day 1
=======================
Responsibility: Generate one sensor reading per simulation cycle.

Temperature must change gradually (not randomly) so that the hysteresis
control logic is visible on the dashboard — if temperature jumped randomly,
the AC would toggle every cycle and the hysteresis band would be meaningless.

Key design decision — AC-state-dependent drift:
  AC ON  → room cools → drift biased negative
  AC OFF → room heats → drift biased positive
Students will watch this feedback loop live on the temperature chart.
"""

import random
from datetime import datetime
from config import (
    TEMP_MIN, TEMP_MAX, HUMIDITY_MIN, HUMIDITY_MAX, TEMP_INIT,
    DRIFT_AC_ON_MIN, DRIFT_AC_ON_MAX,
    DRIFT_AC_OFF_MIN, DRIFT_AC_OFF_MAX,
)


class SensorSimulator:

    def __init__(self):
        # Pre-filled: starting temperature is above the default threshold so
        # the AC activates from cycle 1 — makes the opening demo more engaging.
        self.last_temp = TEMP_INIT

    # -----------------------------------------------------------------------
    # Private helpers
    # -----------------------------------------------------------------------

    def _clamp(self, value, min_val, max_val):
        """Return value clamped to the range [min_val, max_val]."""
        # TODO: return value bounded between min_val and max_val
        # HINT: use Python's built-in max() and min() together
        pass

    def _next_temperature(self, ac_state):
        """
        Return the next temperature value with drift biased by AC state.

        If the AC was ON last cycle the room should cool (drift negative).
        If the AC was OFF last cycle the room should heat (drift positive).
        """
        # TODO 1: choose drift range based on ac_state
        #         if ac_state is True  → random.uniform(DRIFT_AC_ON_MIN,  DRIFT_AC_ON_MAX)
        #         if ac_state is False → random.uniform(DRIFT_AC_OFF_MIN, DRIFT_AC_OFF_MAX)
        # HINT: use an if/else and random.uniform(a, b)

        # TODO 2: compute new_temp = self.last_temp + drift
        #         then clamp it to [TEMP_MIN, TEMP_MAX] using _clamp()

        # TODO 3: update self.last_temp to new_temp
        #         return new_temp rounded to 1 decimal place
        # HINT: round(value, 1)
        pass

    # -----------------------------------------------------------------------
    # Public interface
    # -----------------------------------------------------------------------

    def get_data(self, ac_state=False):
        """
        Return one complete sensor reading as a dict.

        Args:
            ac_state (bool): the AC state from the previous cycle,
                             used to bias the temperature drift direction.

        Returns:
            dict with keys:
                "temperature" (float)  — °C, changes gradually each cycle
                "humidity"    (float)  — %, random within range
                "occupancy"   (int)    — 1 = occupied, 0 = empty
                "hour"        (int)    — current hour (0–23) from system clock
        """
        # TODO 1: get temperature by calling _next_temperature(ac_state)

        # TODO 2: generate humidity — random float in [HUMIDITY_MIN, HUMIDITY_MAX]
        #         rounded to 1 decimal place

        # TODO 3: generate occupancy — 1 or 0, weighted 70% occupied / 30% empty
        # HINT: random.choices([1, 0], weights=[70, 30])[0]
        #       A 50/50 split turns the AC off too often for a useful demo.

        # TODO 4: get the current hour from datetime.now().hour

        # TODO 5: return a dict with all four values using the exact key names above
        pass
