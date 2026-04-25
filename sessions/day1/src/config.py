"""
Configuration — Day 1
=====================
All default values for the Smart Energy Optimization System live here.
Every other module imports from this file — no magic numbers elsewhere.

Task: Fill in every constant marked with TODO.
      The values come from Section 4 of the SRS (Docs/requirements.md).
"""

# ---------------------------------------------------------------------------
# Sensor simulation ranges
# ---------------------------------------------------------------------------

# TODO: set TEMP_MIN — minimum simulated temperature (°C)
TEMP_MIN = ...

# TODO: set TEMP_MAX — maximum simulated temperature (°C)
TEMP_MAX = ...

# TODO: set HUMIDITY_MIN and HUMIDITY_MAX (%)
HUMIDITY_MIN = ...
HUMIDITY_MAX = ...

# TODO: set TEMP_INIT — the starting temperature for the simulation
# HINT: set it above the default threshold so the AC turns ON from cycle 1,
#       making the very first demo cycle more interesting to watch
TEMP_INIT = ...

# ---------------------------------------------------------------------------
# Temperature drift per cycle — pre-filled, do not change
# ---------------------------------------------------------------------------
# These control how fast the room heats or cools each cycle.
# Biasing drift by AC state creates a realistic feedback loop:
#   AC ON  → room cools  → AC eventually turns OFF
#   AC OFF → room heats  → AC eventually turns ON
# Students will observe this oscillation on the dashboard chart.

DRIFT_AC_ON_MIN  = -2.0   # AC ON  → cooling trend (negative = temperature drops)
DRIFT_AC_ON_MAX  =  0.5
DRIFT_AC_OFF_MIN = -0.5   # AC OFF → heating trend
DRIFT_AC_OFF_MAX =  2.0

# ---------------------------------------------------------------------------
# Decision Engine defaults
# ---------------------------------------------------------------------------

# TODO: set DEFAULT_THRESHOLD — the target room temperature (°C)
# HINT: refer to FR-3 in requirements.md for the specified default
DEFAULT_THRESHOLD = ...

# TODO: set DEFAULT_BUFFER — the hysteresis half-width (°C)
# HINT: with threshold=26 and buffer=1.5:
#         AC turns ON  above  26 + 1.5 = 27.5°C
#         AC turns OFF below  26 - 1.5 = 24.5°C
DEFAULT_BUFFER = ...

# Pre-filled: operational hours — AC is only permitted to run between these hours
DEFAULT_OP_START = 6    # 06:00
DEFAULT_OP_END   = 23   # 23:00

# ---------------------------------------------------------------------------
# Energy rates (units per cycle)
# ---------------------------------------------------------------------------

# TODO: set RATE_ON  — energy consumed per cycle when AC is ON
# TODO: set RATE_OFF — energy consumed per cycle when AC is OFF (standby)
# HINT: refer to FR-4 in requirements.md for the exact values
RATE_ON  = ...
RATE_OFF = ...

# ---------------------------------------------------------------------------
# Dashboard settings — pre-filled, do not change
# ---------------------------------------------------------------------------

DEFAULT_ENERGY_LIMIT  = 50.0   # alert fires when cumulative energy exceeds this
REFRESH_INTERVAL      = 2      # seconds between simulation cycles
LOG_DISPLAY_COUNT     = 50     # number of records shown on the dashboard charts
HIGH_TEMP_ALERT_DELTA = 5.0    # °C above threshold that triggers the high-temp alert
