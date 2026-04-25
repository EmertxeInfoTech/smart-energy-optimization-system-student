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
    simulator  = SensorSimulator()
    engine     = DecisionEngine()
    calculator = EnergyCalculator()
    logger     = DataLogger()

    print("Smart Energy Optimization System — Emertxe Information Technologies")
    print("Starting simulation... Press Ctrl+C to stop.")
    print("-" * 75)
    print(f"{'Time':<22} {'Temp':>6} {'Hum':>5} {'Occ':>4} {'AC':>4} {'Cycle':>7} {'Total':>8}")
    print("-" * 75)

    try:
        while True:
            data     = simulator.get_data(engine.ac_state)
            ac_state = engine.evaluate(
                data,
                threshold=DEFAULT_THRESHOLD,
                buffer=DEFAULT_BUFFER,
                op_start=DEFAULT_OP_START,
                op_end=DEFAULT_OP_END,
            )
            cycle_energy = calculator.compute(ac_state)

            record = {
                "timestamp":         datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "temperature":       data["temperature"],
                "humidity":          data["humidity"],
                "occupancy":         data["occupancy"],
                "hour":              data["hour"],
                "ac_state":          ac_state,
                "cycle_energy":      cycle_energy,
                "cumulative_energy": calculator.get_cumulative(),
            }
            logger.store(record)

            print(
                f"{record['timestamp']:<22}"
                f"{record['temperature']:>5.1f}°C"
                f"{record['humidity']:>5.1f}%"
                f"{'Yes' if record['occupancy'] else 'No':>5}"
                f"{'ON' if record['ac_state'] else 'OFF':>5}"
                f"{record['cycle_energy']:>7.1f}"
                f"{record['cumulative_energy']:>8.1f}"
            )

            time.sleep(REFRESH_INTERVAL)

    except KeyboardInterrupt:
        print("\n" + "-" * 75)
        print(f"Simulation stopped after {logger.count()} cycles.")
        print(f"Total energy consumed: {calculator.get_cumulative():.2f} units")


if __name__ == "__main__":
    main()
