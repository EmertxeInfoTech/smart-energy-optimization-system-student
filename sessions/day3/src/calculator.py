"""
EnergyCalculator — Day 3
========================
Responsibility: Calculate energy consumed each cycle and maintain a
running cumulative total across all cycles.

Two rates (defined in config.py):
  RATE_ON  = 2.0 units/cycle  — AC is actively cooling
  RATE_OFF = 0.1 units/cycle  — standby power (control board, sensors)

Why charge standby energy when AC is OFF?
  Real AC units consume a small amount even when idle.
  It also ensures the energy chart never flatlines, making ON vs OFF
  periods clearly visible as spikes vs a low baseline.
"""

from config import RATE_ON, RATE_OFF


class EnergyCalculator:

    def __init__(self):
        # Pre-filled: these are the only three attributes this class needs.
        self.cumulative = 0.0
        self.rate_on    = RATE_ON
        self.rate_off   = RATE_OFF

    def compute(self, ac_state):
        """
        Calculate energy consumed this cycle, add it to the running total,
        and return the cycle energy.

        Args:
            ac_state (bool): True if AC is ON, False if OFF

        Returns:
            float: energy consumed this cycle (2.0 if ON, 0.1 if OFF)
        """
        # TODO 1: set cycle_energy to self.rate_on if ac_state is True,
        #         otherwise self.rate_off
        # HINT: use a ternary — cycle_energy = self.rate_on if ac_state else self.rate_off

        # TODO 2: add cycle_energy to self.cumulative

        # TODO 3: return cycle_energy rounded to 2 decimal places
        pass

    def get_cumulative(self):
        """Return total energy consumed since the simulation started."""
        # TODO: return self.cumulative rounded to 2 decimal places
        pass

    def reset(self):
        """Reset the cumulative total to zero (used to restart the energy counter)."""
        # TODO: set self.cumulative back to 0.0
        pass
