"""
Simulation Loop — Day 4
=======================
Responsibility: Wire all five core classes together and run the
simulation loop in the terminal (no dashboard needed).

Pipeline each cycle:
  SensorSimulator → DecisionEngine → EnergyCalculator → DataLogger → print

This file is the first time students see the full pipeline running end-to-end.
It is also useful for testing core logic without launching Streamlit.

Run with:
    python3 src/main.py
Stop with:
    Ctrl+C
"""

import time
from datetime import datetime

from config import (
    DEFAULT_THRESHOLD, DEFAULT_BUFFER,
    DEFAULT_OP_START, DEFAULT_OP_END,
    REFRESH_INTERVAL,
)
from sensor import SensorSimulator
from engine import DecisionEngine
from calculator import EnergyCalculator
from logger import DataLogger


def main():
    # TODO 1: create one instance of each of the four classes:
    #         SensorSimulator, DecisionEngine, EnergyCalculator, DataLogger
    # HINT: these MUST be created once here and reused every cycle.
    #       Creating them inside the loop would reset all state (ac_state,
    #       cumulative energy, last_temp) back to zero each iteration.

    # Pre-filled: terminal output header
    print("Smart Energy Optimization System — Emertxe Information Technologies")
    print("Starting simulation... Press Ctrl+C to stop.")
    print("-" * 75)
    print(f"{'Time':<22} {'Temp':>6} {'Hum':>5} {'Occ':>4} {'AC':>4} {'Cycle':>7} {'Total':>8}")
    print("-" * 75)

    try:
        while True:
            # TODO 2: generate sensor data
            #         call simulator.get_data(), passing engine.ac_state
            #         so the temperature drift direction reflects the previous cycle
            data = ...

            # TODO 3: run the decision engine
            #         call engine.evaluate() with data and the four config defaults:
            #         threshold, buffer, op_start, op_end
            ac_state = ...

            # TODO 4: calculate energy for this cycle
            #         call calculator.compute() with ac_state
            cycle_energy = ...

            # TODO 5: build the record dict with all required keys:
            #   "timestamp"         → datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #   "temperature"       → data["temperature"]
            #   "humidity"          → data["humidity"]
            #   "occupancy"         → data["occupancy"]
            #   "hour"              → data["hour"]
            #   "ac_state"          → ac_state
            #   "cycle_energy"      → cycle_energy
            #   "cumulative_energy" → calculator.get_cumulative()
            record = {
                ...
            }

            # TODO 6: store the record in the logger
            # HINT: logger.store(record)

            # Pre-filled: print one formatted row to the terminal
            print(
                f"{record['timestamp']:<22}"
                f"{record['temperature']:>5.1f}°C"
                f"{record['humidity']:>5.1f}%"
                f"{'Yes' if record['occupancy'] else 'No':>5}"
                f"{'ON' if record['ac_state'] else 'OFF':>5}"
                f"{record['cycle_energy']:>7.1f}"
                f"{record['cumulative_energy']:>8.1f}"
            )

            # TODO 7: pause before the next cycle
            #         call time.sleep() with REFRESH_INTERVAL
            ...

    except KeyboardInterrupt:
        # Pre-filled: summary printed when the user stops with Ctrl+C
        print("\n" + "-" * 75)
        print(f"Simulation stopped after {logger.count()} cycles.")
        print(f"Total energy consumed: {calculator.get_cumulative():.2f} units")


if __name__ == "__main__":
    main()
