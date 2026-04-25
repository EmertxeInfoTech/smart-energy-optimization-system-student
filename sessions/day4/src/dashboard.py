import time
from datetime import datetime

import pandas as pd
import streamlit as st

from config import (
    DEFAULT_THRESHOLD, DEFAULT_BUFFER, DEFAULT_ENERGY_LIMIT,
    DEFAULT_OP_START, DEFAULT_OP_END, REFRESH_INTERVAL,
    LOG_DISPLAY_COUNT, HIGH_TEMP_ALERT_DELTA,
)
from sensor import SensorSimulator
from engine import DecisionEngine
from calculator import EnergyCalculator
from logger import DataLogger


def init_session():
    if "simulator" not in st.session_state:
        st.session_state.simulator  = SensorSimulator()
        st.session_state.engine     = DecisionEngine()
        st.session_state.calculator = EnergyCalculator()
        st.session_state.logger     = DataLogger()


def render_sidebar():
    st.sidebar.header("Control Parameters")

    threshold = st.sidebar.slider(
        "Temperature Threshold (°C)",
        min_value=20.0, max_value=35.0,
        value=float(DEFAULT_THRESHOLD), step=0.5,
    )
    buffer = st.sidebar.slider(
        "Hysteresis Buffer (°C)",
        min_value=0.5, max_value=3.0,
        value=float(DEFAULT_BUFFER), step=0.5,
    )
    energy_limit = st.sidebar.number_input(
        "Energy Limit (units)",
        min_value=10, max_value=200,
        value=int(DEFAULT_ENERGY_LIMIT),
    )
    op_start = st.sidebar.number_input(
        "Operational Start Hour (0–12)",
        min_value=0, max_value=12,
        value=int(DEFAULT_OP_START),
    )
    op_end = st.sidebar.number_input(
        "Operational End Hour (13–23)",
        min_value=13, max_value=23,
        value=int(DEFAULT_OP_END),
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Hysteresis Band**")
    st.sidebar.markdown(
        f"- AC turns **ON** above **{threshold + buffer:.1f}°C**\n"
        f"- AC turns **OFF** below **{threshold - buffer:.1f}°C**\n"
        f"- Band width: **{buffer * 2:.1f}°C**"
    )

    return {
        "threshold":    threshold,
        "buffer":       buffer,
        "energy_limit": energy_limit,
        "op_start":     op_start,
        "op_end":       op_end,
    }


def render_decision_reason(reason):
    if "Rule 1" in reason or "Rule 2" in reason:
        st.warning(f"🔍 **Decision:** {reason}")
    elif "Rule 3" in reason:
        st.error(f"🔍 **Decision:** {reason}")
    elif "Rule 4" in reason:
        st.success(f"🔍 **Decision:** {reason}")
    else:
        st.info(f"🔍 **Decision:** {reason}")


def render_dashboard(records, params):
    latest = records[-1]
    upper  = params["threshold"] + params["buffer"]
    lower  = params["threshold"] - params["buffer"]

    # --- Alerts ---
    if latest["temperature"] > params["threshold"] + HIGH_TEMP_ALERT_DELTA:
        st.error("⚠️ High Temperature Alert — Room temperature is critically high.")
    if latest["cumulative_energy"] > params["energy_limit"]:
        st.warning("⚠️ Energy Limit Exceeded — Cumulative usage has crossed the configured limit.")

    # --- Decision reason ---
    render_decision_reason(latest["reason"])

    st.markdown("---")

    # --- Sensor readings + AC status ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperature (°C)", f"{latest['temperature']:.1f}")
    col2.metric("Humidity (%)",     f"{latest['humidity']:.1f}")
    col3.metric("Occupancy",        "Occupied" if latest["occupancy"] else "Empty")

    if latest["ac_state"]:
        col4.success("🟢 AC: ON")
    else:
        col4.error("🔴 AC: OFF")

    # --- Energy metrics ---
    st.markdown("---")
    e1, e2 = st.columns(2)
    e1.metric("Cycle Energy (units)",      f"{latest['cycle_energy']:.2f}",
              help="2.0 when AC is ON · 0.1 when AC is OFF")
    e2.metric("Cumulative Energy (units)", f"{latest['cumulative_energy']:.2f}")

    st.markdown("---")

    # --- Temperature chart with hysteresis threshold bands ---
    st.subheader("Temperature vs Thresholds")
    st.caption(
        f"Upper threshold (AC ON): {upper:.1f}°C  |  "
        f"Lower threshold (AC OFF): {lower:.1f}°C"
    )
    temp_df = pd.DataFrame({
        "Temperature (°C)":      [r["temperature"]    for r in records],
        f"AC ON above ({upper:.1f}°C)":  [upper for _ in records],
        f"AC OFF below ({lower:.1f}°C)": [lower for _ in records],
    })
    st.line_chart(temp_df)

    # --- Cycle energy chart ---
    st.subheader("Cycle Energy")
    st.caption("2.0 units when AC is ON · 0.1 units when AC is OFF")
    energy_df = pd.DataFrame({
        "Cycle Energy (units)": [r["cycle_energy"] for r in records],
    })
    st.line_chart(energy_df)

    # --- Recent log table ---
    st.markdown("---")
    st.subheader("Recent Log (last 10 cycles)")
    table = [
        {
            "Time":       r["timestamp"],
            "Temp (°C)":  r["temperature"],
            "Hum (%)":    r["humidity"],
            "Occupied":   "Yes" if r["occupancy"] else "No",
            "AC":         "ON"  if r["ac_state"]  else "OFF",
            "Cycle (u)":  r["cycle_energy"],
            "Total (u)":  r["cumulative_energy"],
            "Reason":     r["reason"],
        }
        for r in reversed(records[-10:])
    ]
    st.dataframe(table, use_container_width=True)


def run_cycle(params):
    data      = st.session_state.simulator.get_data(st.session_state.engine.ac_state)
    ac_state  = st.session_state.engine.evaluate(
                    data,
                    threshold=params["threshold"],
                    buffer=params["buffer"],
                    op_start=params["op_start"],
                    op_end=params["op_end"],
                )
    cycle_energy = st.session_state.calculator.compute(ac_state)

    record = {
        "timestamp":         datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature":       data["temperature"],
        "humidity":          data["humidity"],
        "occupancy":         data["occupancy"],
        "hour":              data["hour"],
        "ac_state":          ac_state,
        "cycle_energy":      cycle_energy,
        "cumulative_energy": st.session_state.calculator.get_cumulative(),
        "reason":            st.session_state.engine.last_reason,
    }
    st.session_state.logger.store(record)


def main():
    st.set_page_config(
        page_title="Smart Energy Optimization System",
        page_icon="⚡",
        layout="wide",
    )
    st.title("⚡ Smart Energy Optimization System")
    st.caption("Emertxe Information Technologies — Real-time HVAC Simulation Dashboard")

    init_session()
    params = render_sidebar()
    run_cycle(params)

    records = st.session_state.logger.get_latest(LOG_DISPLAY_COUNT)
    if records:
        render_dashboard(records, params)
    else:
        st.info("Simulation starting…")

    time.sleep(REFRESH_INTERVAL)
    st.rerun()


if __name__ == "__main__":
    main()
