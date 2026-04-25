"""
Streamlit Dashboard — Day 5
===========================
Responsibility: Display live sensor data, AC status, energy metrics,
decision reason, charts, and alerts.  Collect control parameters from
the sidebar and pass them into the simulation loop each cycle.

Key Streamlit concepts introduced today:
  st.session_state     — a dict that persists across reruns; used to keep
                         class instances alive between Streamlit refreshes
  st.rerun()           — re-executes the entire script from the top,
                         triggering the next simulation cycle
  st.sidebar.*         — widgets rendered in the left sidebar panel
  st.metric()          — large display cards for key numbers
  st.line_chart()      — time-series chart from a pandas DataFrame
  st.error/warning/success/info()  — colour-coded banners

Why session_state?
  Every time Streamlit refreshes (via st.rerun), it re-executes the whole
  script.  Without session_state, all class instances would be recreated,
  resetting ac_state, cumulative energy, and temperature history to zero
  on every cycle.  session_state is the fix.

Run with:
    streamlit run src/dashboard.py
"""

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


# ---------------------------------------------------------------------------
# Session state initialisation
# ---------------------------------------------------------------------------

def init_session():
    """
    Create class instances on the very first load and store them in
    st.session_state so they survive across reruns.

    This function is called every cycle but the if-guard ensures the
    instances are only created once.
    """
    # TODO: if "simulator" is NOT already in st.session_state, create and
    #       store all four instances:
    #         st.session_state.simulator  = SensorSimulator()
    #         st.session_state.engine     = DecisionEngine()
    #         st.session_state.calculator = EnergyCalculator()
    #         st.session_state.logger     = DataLogger()
    # HINT: use  if "simulator" not in st.session_state:
    pass


# ---------------------------------------------------------------------------
# Sidebar controls
# ---------------------------------------------------------------------------

def render_sidebar():
    """
    Render the sidebar control panel and return the current parameter values.

    Returns:
        dict with keys: threshold, buffer, energy_limit, op_start, op_end
    """
    st.sidebar.header("Control Parameters")

    # TODO 1: temperature threshold slider
    #         label  : "Temperature Threshold (°C)"
    #         range  : 20.0 – 35.0,  default DEFAULT_THRESHOLD,  step 0.5
    # HINT: st.sidebar.slider("label", min_value=..., max_value=..., value=..., step=...)
    threshold = ...

    # TODO 2: hysteresis buffer slider
    #         label  : "Hysteresis Buffer (°C)"
    #         range  : 0.5 – 3.0,  default DEFAULT_BUFFER,  step 0.5
    buffer = ...

    # TODO 3: energy limit number input
    #         label  : "Energy Limit (units)"
    #         range  : 10 – 200,  default int(DEFAULT_ENERGY_LIMIT)
    # HINT: st.sidebar.number_input(...)
    energy_limit = ...

    # TODO 4: operational hours — two number inputs
    #         Start: label "Operational Start Hour (0–12)", range 0–12, default DEFAULT_OP_START
    #         End:   label "Operational End Hour (13–23)",  range 13–23, default DEFAULT_OP_END
    op_start = ...
    op_end   = ...

    # Pre-filled: live hysteresis band summary — updates instantly when sliders move
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Hysteresis Band**")
    st.sidebar.markdown(
        f"- AC turns **ON** above **{threshold + buffer:.1f}°C**\n"
        f"- AC turns **OFF** below **{threshold - buffer:.1f}°C**\n"
        f"- Band width: **{buffer * 2:.1f}°C**"
    )

    # TODO 5: return all five values as a dict
    # HINT: keys must match exactly what run_cycle() and render_dashboard() expect:
    #       "threshold", "buffer", "energy_limit", "op_start", "op_end"
    pass


# ---------------------------------------------------------------------------
# Decision reason banner
# ---------------------------------------------------------------------------

def render_decision_reason(reason):
    """
    Display a colour-coded banner showing which rule fired this cycle.

    Colour convention:
      Yellow  (st.warning) → Rule 1 or Rule 2  — occupancy / time override
      Red     (st.error)   → Rule 3            — room hot, AC turning ON
      Green   (st.success) → Rule 4            — room cooled, AC turning OFF
      Blue    (st.info)    → Rule 5            — hysteresis, holding state
    """
    # TODO: check which rule appears in the reason string and call the
    #       matching Streamlit function, passing  f"🔍 **Decision:** {reason}"
    # HINT: use  "Rule 1" in reason  or  "Rule 2" in reason  for the first case
    pass


# ---------------------------------------------------------------------------
# Main dashboard layout
# ---------------------------------------------------------------------------

def render_dashboard(records, params):
    """
    Render all dashboard panels: alerts, reason banner, metric cards,
    energy metrics, temperature chart, energy chart, and the log table.

    Args:
        records (list[dict]): latest records from DataLogger.get_latest()
        params  (dict):       current control parameters from render_sidebar()
    """
    latest = records[-1]
    upper  = params["threshold"] + params["buffer"]
    lower  = params["threshold"] - params["buffer"]

    # --- Alert banners ---
    # TODO 1: high-temperature alert
    #         if latest["temperature"] > params["threshold"] + HIGH_TEMP_ALERT_DELTA:
    #             st.error("⚠️ High Temperature Alert — Room temperature is critically high.")
    # TODO 2: energy limit alert
    #         if latest["cumulative_energy"] > params["energy_limit"]:
    #             st.warning("⚠️ Energy Limit Exceeded — Cumulative usage has crossed the configured limit.")

    # --- Decision reason ---
    # TODO 3: call render_decision_reason() with latest["reason"]

    st.markdown("---")

    # --- Sensor readings + AC status (4 columns) ---
    # TODO 4: create four columns with st.columns(4) then populate:
    #   col1 → col1.metric("Temperature (°C)", f"{latest['temperature']:.1f}")
    #   col2 → col2.metric("Humidity (%)",     f"{latest['humidity']:.1f}")
    #   col3 → col3.metric("Occupancy",        "Occupied" if latest["occupancy"] else "Empty")
    #   col4 → col4.success("🟢 AC: ON")  or  col4.error("🔴 AC: OFF")
    # HINT: col1, col2, col3, col4 = st.columns(4)

    st.markdown("---")

    # --- Energy metrics (2 columns) ---
    # TODO 5: create two columns and show:
    #   col1 → st.metric("Cycle Energy (units)",      f"{latest['cycle_energy']:.2f}")
    #   col2 → st.metric("Cumulative Energy (units)", f"{latest['cumulative_energy']:.2f}")

    st.markdown("---")

    # --- Temperature vs thresholds chart ---
    # TODO 6: build a DataFrame with three series and display it
    #   Column 1: "Temperature (°C)"              → [r["temperature"] for r in records]
    #   Column 2: f"AC ON above ({upper:.1f}°C)"  → [upper] * len(records)
    #   Column 3: f"AC OFF below ({lower:.1f}°C)" → [lower] * len(records)
    # Then:
    #   st.subheader("Temperature vs Thresholds")
    #   st.caption(f"Upper: {upper:.1f}°C  |  Lower: {lower:.1f}°C")
    #   st.line_chart(temp_df)
    # HINT: pd.DataFrame({ "col name": [value, value, ...] })

    # --- Cycle energy chart ---
    # TODO 7: build a single-column DataFrame and display it
    #   Column: "Cycle Energy (units)" → [r["cycle_energy"] for r in records]
    # Then:
    #   st.subheader("Cycle Energy")
    #   st.caption("2.0 units when AC is ON · 0.1 units when AC is OFF")
    #   st.line_chart(energy_df)

    # --- Recent log table — pre-filled ---
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


# ---------------------------------------------------------------------------
# One simulation cycle
# ---------------------------------------------------------------------------

def run_cycle(params):
    """
    Execute one full simulation cycle: sense → decide → calculate → log.
    Pre-filled so students can focus on the dashboard layout.
    """
    data         = st.session_state.simulator.get_data(st.session_state.engine.ac_state)
    ac_state     = st.session_state.engine.evaluate(
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


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    # Pre-filled: page configuration
    st.set_page_config(
        page_title="Smart Energy Optimization System",
        page_icon="⚡",
        layout="wide",
    )
    st.title("⚡ Smart Energy Optimization System")
    st.caption("Emertxe Information Technologies — Real-time HVAC Simulation Dashboard")

    # TODO 1: call init_session() to ensure class instances exist in session_state
    # TODO 2: call render_sidebar() and store the returned dict as  params
    # TODO 3: call run_cycle(params) to execute one simulation step
    # TODO 4: retrieve records:
    #         records = st.session_state.logger.get_latest(LOG_DISPLAY_COUNT)
    # TODO 5: if records is non-empty, call render_dashboard(records, params)
    #         otherwise show  st.info("Simulation starting…")
    # TODO 6: pause and trigger the next cycle:
    #         time.sleep(REFRESH_INTERVAL)
    #         st.rerun()
    # HINT: st.rerun() re-executes the whole script — it is what makes the
    #       dashboard refresh automatically every 2 seconds.


if __name__ == "__main__":
    main()
