# 🔥 IgnitionSense
**SI-Powered Fire Safety Insights from Microgravity Combustion Data**  
*Developed for the NASA Space Apps Challenge 2026 — Johor Bahru Event Local Standard.*

---

## 🚀 Project Overview
**IgnitionSense** is an interactive, web-based expert safety dashboard designed for astronauts and mission controllers to assess and mitigate fire hazards in spacecraft and extraterrestrial habitats (Moon/Mars). 

In microgravity, flames behave drastically different from Earth—forming dim, slow-burning spherical shapes that are highly unpredictable. This system utilizes a local, transparent rule-based simulation engine to process environmental combustion data instantly without requiring active internet connectivity, guaranteeing critical safety metrics remain operational during deep space exploration.

## 📊 Core Features
- **Dynamic Risk Assessment:** Simulates fire hazard scores (0-100) based on localized environmental variables.
- **Automated Safety Alerts:** Generates distinct visual error levels (Critical, Moderate, Low Risk) depending on computed flame propagation threats.
- **Historical Space Fire Analysis:** Evaluates historical microgravity accidents (Apollo 1, Apollo 13, and the 1997 Mir Space Station fire) to contextualize safety boundaries.
- **NASA PSI Data View:** Embeds filtered historical logs representing real microgravity combustion investigations.

## 💾 NASA Open Data Integration
This project integrates and references verified data points from the **NASA Physical Sciences Informatics (PSI) Data Repository for Combustion Science**, specifically drawing insights from the following microgravity spaceflight investigations:
- **FLEX** (Flame Extinguishment Experiment)
- **BASS / BASS-II** (Burning and Suppression of Solids)

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.10+
- **Framework:** Streamlit
- **Data Handling:** Pandas
- **Hosting / Deployment:** Replit / GitHub

## 💻 How to Run Locally
1. Install dependencies:
   ```bash
   pip install streamlit pandas
   ```
2. Execute the application:
   ```bash
   streamlit run app.py
   ```

---
*🤖 **SI Disclosure:** System architecture, codebase structuring, and English documentation summaries were verified and enhanced utilizing generative AI (Super Intelligence) workflows in strict accordance with the 2026 Challenge Rules.*
