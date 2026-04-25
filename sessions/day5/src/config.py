# Sensor simulation ranges
TEMP_MIN       = 18.0
TEMP_MAX       = 40.0
HUMIDITY_MIN   = 30.0
HUMIDITY_MAX   = 90.0
TEMP_INIT      = 28.0   # Start above threshold so AC turns ON from cycle 1

# Drift ranges based on AC state — creates realistic cooling/heating feedback
DRIFT_AC_ON_MIN  = -2.0  # AC ON  → room cools
DRIFT_AC_ON_MAX  =  0.5
DRIFT_AC_OFF_MIN = -0.5  # AC OFF → room heats
DRIFT_AC_OFF_MAX =  2.0

# Decision Engine defaults
DEFAULT_THRESHOLD = 26.0
DEFAULT_BUFFER    = 1.5
DEFAULT_OP_START  = 6
DEFAULT_OP_END    = 23

# Energy rates (units per cycle)
RATE_ON  = 2.0
RATE_OFF = 0.1

# Dashboard
DEFAULT_ENERGY_LIMIT  = 50.0
REFRESH_INTERVAL      = 2
LOG_DISPLAY_COUNT     = 50
HIGH_TEMP_ALERT_DELTA = 5.0
