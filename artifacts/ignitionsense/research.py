"""Educational summaries and official NASA reference links."""

import streamlit as st

CASES = [
    {
        "title": "Apollo 1",
        "date": "27 JAN 1967",
        "category": "Pre-launch oxygen fire · Ground test",
        "summary": (
            "During a pre-launch ground test, fire spread rapidly through the Apollo 1 "
            "command module's pressurized, pure-oxygen atmosphere. Gus Grissom, "
            "Ed White, and Roger Chaffee died. Combustible cabin materials and "
            "the difficulty of opening the hatch contributed to the disaster."
        ),
        "lesson": (
            "Control ignition sources and material flammability; evaluate atmosphere "
            "composition and pressure together; design rapid emergency egress. "
            "This occurred on Earth, not in microgravity."
        ),
        "url": "https://www.nasa.gov/feature/55-years-ago-the-apollo-1-fire-and-its-aftermath",
    },
    {
        "title": "Apollo 13",
        "date": "13 APR 1970",
        "category": "Oxygen tank explosion · In flight",
        "summary": (
            "An oxygen tank in the service module exploded after damaged electrical "
            "insulation led to a short and fire inside the tank. The spacecraft lost "
            "critical oxygen and electrical power. The crew used the lunar module "
            "as a lifeboat and returned safely to Earth."
        ),
        "lesson": (
            "Verify component compatibility, electrical protection, testing procedures, "
            "and redundant life-support capability. This was a service-module tank "
            "failure, not an open cabin flame."
        ),
        "url": "https://www.nasa.gov/history/nasa-lewis-aided-apollo-13-investigation/",
    },
    {
        "title": "1997 Fire Aboard Space Station Mir",
        "date": "24 FEB 1997",
        "category": "Oxygen-generator fire · Orbital station",
        "summary": (
            "A solid-fuel oxygen generator ignited aboard Mir, producing flames and "
            "dense smoke while six crew members were aboard. The crew used protective "
            "breathing equipment and extinguishers to control the fire. All survived."
        ),
        "lesson": (
            "Keep breathing protection and suppression equipment accessible, protect "
            "evacuation routes, and train crews for smoke-filled conditions. "
            "Oxygen-generation hardware can itself be a fire source."
        ),
        "url": "https://www.nasa.gov/history/25-years-ago-fire-aboard-space-station-mir/",
    },
]


def render_case_studies():
    st.subheader("Historical Space Fire Case Studies")
    st.write("Three incidents that show why prevention, system design, and crew training matter.")
    for case in CASES:
        with st.container(border=True):
            st.caption(f'{case["date"]}  /  {case["category"]}')
            st.subheader(case["title"])
            context, lesson = st.columns([1.25, 1], gap="large")
            with context:
                st.write("**What happened**")
                st.write(case["summary"])
            with lesson:
                st.write("**Safety lessons**")
                st.write(case["lesson"])
            st.link_button("Read NASA's account", case["url"], icon=":material/open_in_new:")
    st.caption(
        "These incidents provide historical context only. They are not calibration "
        "data for the risk score, and their conditions are not reproduced by the controls."
    )


def render_references():
    st.subheader("NASA Data Reference")
    st.info(
        "The system's educational context is based on the **NASA PSI (Physical Sciences "
        "Informatics) Data Repository for Combustion Science** and **NASA Combustion "
        "Science Investigations**. The app is referenced against NASA's **FLEX** "
        "(Flame Extinguishment Experiment) and **BASS** (Burning and Suppression of Solids) "
        "microgravity combustion datasets and published experiment descriptions. "
        "**These are research references only:** this prototype does not ingest those "
        "datasets, and its illustrative scoring weights are not derived from or validated by NASA."
    )
    a, b = st.columns(2, gap="large")
    with a:
        st.markdown(
            "**NASA PSI repository**  \n"
            "[Explore combustion investigations](https://www.nasa.gov/physical-sciences-informatics-psi/psi-investigations-by-research-area/)  \n"
            "[BASS-II investigation · PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25)"
        )
    with b:
        st.markdown(
            "**NASA Combustion Science Investigations**  \n"
            "[Combustion science overview](https://www1.grc.nasa.gov/space/iss-research/iss-fcf/combustion-science/)  \n"
            "[FLEX experiment fact sheet (PDF)](https://www.nasa.gov/wp-content/uploads/2025/07/flame-extinguishment-experiment-flex.pdf)"
        )
