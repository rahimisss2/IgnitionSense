"""IgnitionSense: an educational microgravity combustion demonstrator."""

import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import streamlit as st

from risk_model import FUEL_POINTS, GRAVITY_POINTS, assess
from research import render_case_studies, render_references

st.set_page_config(
    page_title="IgnitionSense | Flame in Freefall",
    page_icon=":material/local_fire_department:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.caption("NASA SPACE APPS CHALLENGE  /  FLAME IN FREEFALL")
title, status = st.columns([4, 1], vertical_alignment="center")
with title:
    st.title("IgnitionSense")
    st.write("Understanding fire beyond Earth. Explore combustion risk in reduced gravity.")
with status:
    st.badge("EDUCATIONAL SIMULATION", color="orange")

st.caption(
    "A scenario dashboard for astronauts, mission controllers, and curious explorers. "
    "Not live telemetry, a trained AI model, or an operational safety system."
)
st.divider()

dashboard, history, logs = st.tabs(
    ["Risk Assessment", "Historical Space Fire Case Studies", "NASA PSI Experimental Logs"]
)

with dashboard:
    left, right = st.columns([1, 1.45], gap="large")
    with left, st.container(border=True):
        st.caption("01 / DEFINE YOUR ENVIRONMENT")
        st.subheader("Input Parameters")
        st.write("Configure a scenario, then run an assessment.")
        oxygen = st.slider(
            "Oxygen/Oxidizer Level",
            min_value=15,
            max_value=40,
            value=21,
            step=1,
            format="%d%%",
            help="Oxygen volume fraction in the illustrative atmosphere; not a generic oxidizer model.",
        )
        st.caption("15% minimum · 21% Earth reference · 40% maximum")
        gravity = st.radio(
            "Gravity Environment",
            list(GRAVITY_POINTS),
            key="gravity_environment",
            help="Select one gravity environment. The filled circle marks your selection.",
        )
        fuel = st.radio(
            "Fuel/Material Type",
            list(FUEL_POINTS),
            key="fuel_material_type",
            help="Select one material. Run the assessment to apply your selections.",
        )
        st.caption(
            "Other conditions are unspecified. Pressure, ventilation, ignition energy, "
            "geometry, and exact material chemistry are not modeled."
        )
        run = st.button(
            "Run SI Risk Assessment",
            type="primary",
            width="stretch",
            icon=":material/analytics:",
        )
        if run:
            with st.spinner("Simulating SI data analysis — evaluating scenario factors…"):
                time.sleep(1.25)
                st.session_state["assessment"] = {
                    **assess(oxygen, gravity, fuel),
                    "oxygen": oxygen,
                    "gravity": gravity,
                    "fuel": fuel,
                    "time": datetime.now(timezone.utc).strftime("%H:%M:%S UTC"),
                }

    with right, st.container(border=True):
        st.caption("02 / INTERPRET YOUR SCENARIO")
        st.subheader("SI Predictive Insights")
        result = st.session_state.get("assessment")
        if result is None:
            st.info("Ready for assessment. Set the environmental parameters and select Run SI Risk Assessment.")
            st.metric("Fire Hazard Score", "— / 100")
            st.progress(0, text="Awaiting a scenario")
            st.write("**Explore what changes fire behavior**")
            st.write(
                "Oxygen enrichment can intensify combustion. Without buoyancy in "
                "microgravity, some flames can become spherical and diffusion-controlled. "
                "Ventilation and material properties remain important."
            )
            st.caption("No prediction has been generated. The spinner simulates analysis, not an external AI request.")
        else:
            if (oxygen, gravity, fuel) != (result["oxygen"], result["gravity"], result["fuel"]):
                st.warning("Inputs changed. Results below describe the last run; run the assessment again to update.")
            metric, label = st.columns([1.2, 1])
            with metric:
                st.metric("Fire Hazard Score", f'{result["score"]} / 100')
            with label:
                st.badge(f'{result["level"].upper()} RISK', color=result["color"])
                st.caption(f'Last run · {result["time"]}')
            st.progress(result["score"] / 100, text="Illustrative index · not a probability")
            if result["score"] >= 70:
                st.error(
                    "**CRITICAL — High modeled fire hazard.** Spherical flame propagation "
                    "can occur under low-flow microgravity conditions. Oxygen enrichment "
                    "can accelerate combustion. This warning is educational, not a detection "
                    "of a real fire."
                )
            elif result["score"] >= 40:
                st.warning(
                    "**CAUTION — Moderate modeled fire hazard.** The selected conditions "
                    "warrant attention in this demonstration. Reduced buoyancy can alter "
                    "flame spread and smoke transport; a moderate score does not establish safety."
                )
            else:
                st.success(
                    "**LOW modeled fire hazard.** These inputs produce a lower illustrative "
                    "score, not proof of a safe or nonflammable environment. Approved fire "
                    "prevention and emergency procedures still apply."
                )
            st.caption(
                f'ASSESSED SCENARIO · {result["oxygen"]}% O₂ · '
                f'{result["gravity"]} · {result["fuel"]}'
            )
            st.write("**Why this score?**")
            st.write(
                f'Oxygen contribution **+{result["oxygen_points"]:.1f}** · '
                f'Gravity contribution **+{result["gravity_points"]}** · '
                f'Material contribution **+{result["fuel_points"]}** · Base **+10**'
            )
            if result["gravity"] == "Microgravity 0g":
                st.write(
                    "In microgravity, weakened buoyant convection can permit rounded, "
                    "diffusion-dominated flames. Forced airflow can change this behavior; "
                    "not every space fire is spherical."
                )
            else:
                st.write(
                    "Lunar and Martian gravity retain some buoyancy. The lower gravity "
                    "weight here is a teaching assumption, not a universal physical risk ranking."
                )
            st.write(
                {
                    "Solid Polymer": "Polymer burning depends on composition, thickness, geometry, and airflow.",
                    "Liquid Propellant": "Propellant hazards depend strongly on chemistry; some fuels carry their own oxidizer. This simplified model does not represent those reactions.",
                    "Electrical Insulation": "Insulation can be both a combustible material and part of an electrical ignition pathway.",
                }[result["fuel"]]
            )

    with st.expander("Model methodology & limitations"):
        st.write(
            "This is a deterministic, hand-weighted educational model. No NASA dataset "
            "is downloaded, ingested, or used to train or calibrate the score. No AI "
            "service is called when running an assessment."
        )
        st.code(
            "score = round(clamp(10 + 45 × (oxygen_percent − 15) / 25\n"
            "                    + gravity_weight + material_weight, 0, 100))\n"
            "gravity_weight: microgravity 25, lunar 14, martian 5\n"
            "material_weight: solid polymer 10, liquid propellant 20,\n"
            "                 electrical insulation 15\n"
            "low: 0–39 | moderate: 40–69 | high: 70–100",
            language="text",
        )
        st.write(
            "Higher oxygen and microgravity deliberately receive higher weights to "
            "support the challenge scenario. Actual gravity effects are condition-dependent. "
            "Scores are neither ignition probabilities nor physical flame simulations. "
            "Do not change spacecraft oxygen, ventilation, or suppression systems based on this app."
        )

with history:
    render_case_studies()

with logs:
    st.subheader("NASA PSI Experimental Logs")
    st.write(
        "These illustrative logs demonstrate how filtered samples from the NASA "
        "Physical Sciences Informatics (PSI) Combustion Science repository could "
        "be displayed. The six rows were supplied for this demo and have not "
        "been verified as actual NASA experimental records."
    )
    st.caption("Illustrative sample data · Not used to calculate the Fire Hazard Score")
    data_path = Path(__file__).resolve().parents[2] / "nasa_data.csv"
    try:
        experimental_logs = pd.read_csv(data_path)
    except (OSError, pd.errors.ParserError, pd.errors.EmptyDataError) as exc:
        st.error(f"Unable to load nasa_data.csv: {exc}")
    else:
        st.dataframe(
            experimental_logs,
            hide_index=True,
            width="stretch",
            column_config={
                "Experiment_ID": "Experiment ID",
                "Oxygen_Pct": st.column_config.NumberColumn("Oxygen (%)", format="%d"),
                "Flame_Spread_Rate_m_s": st.column_config.NumberColumn(
                    "Flame spread rate (m/s)", format="%.3f"
                ),
                "Risk_Level": "Risk level",
            },
        )

st.divider()
render_references()
st.caption(
    "SI disclosure · The code and summaries were enhanced using generative AI (SI) tools. "
    "Runtime assessments use a transparent rule-based simulation, not generative AI inference."
)
st.caption(
    "IgnitionSense · Independent NASA Space Apps Challenge project · "
    "Not affiliated with or endorsed by NASA. For education only; follow certified mission procedures."
)
