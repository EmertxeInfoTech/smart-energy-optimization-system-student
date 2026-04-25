import random
from datetime import datetime
from config import (
    TEMP_MIN, TEMP_MAX, HUMIDITY_MIN, HUMIDITY_MAX, TEMP_INIT,
    DRIFT_AC_ON_MIN, DRIFT_AC_ON_MAX,
    DRIFT_AC_OFF_MIN, DRIFT_AC_OFF_MAX,
)


class SensorSimulator:
    def __init__(self):
        self.last_temp = TEMP_INIT

    def _clamp(self, value, min_val, max_val):
        return max(min_val, min(max_val, value))

    def _next_temperature(self, ac_state):
        # Drift direction depends on whether AC was ON or OFF last cycle
        if ac_state:
            drift = random.uniform(DRIFT_AC_ON_MIN, DRIFT_AC_ON_MAX)   # cooling trend
        else:
            drift = random.uniform(DRIFT_AC_OFF_MIN, DRIFT_AC_OFF_MAX) # heating trend

        new_temp = self._clamp(self.last_temp + drift, TEMP_MIN, TEMP_MAX)
        self.last_temp = new_temp
        return round(new_temp, 1)

    def get_data(self, ac_state=False):
        return {
            "temperature": self._next_temperature(ac_state),
            "humidity":    round(random.uniform(HUMIDITY_MIN, HUMIDITY_MAX), 1),
            "occupancy":   random.choices([1, 0], weights=[70, 30])[0],
            "hour":        datetime.now().hour,
        }
