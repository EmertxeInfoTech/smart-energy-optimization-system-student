from config import RATE_ON, RATE_OFF


class EnergyCalculator:
    def __init__(self):
        self.cumulative = 0.0
        self.rate_on    = RATE_ON
        self.rate_off   = RATE_OFF

    def compute(self, ac_state):
        cycle_energy     = self.rate_on if ac_state else self.rate_off
        self.cumulative += cycle_energy
        return round(cycle_energy, 2)

    def get_cumulative(self):
        return round(self.cumulative, 2)

    def reset(self):
        self.cumulative = 0.0
