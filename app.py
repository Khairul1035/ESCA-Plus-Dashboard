import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Ethics Dashboard", layout="wide", page_icon="🏥")

# --- VISITOR COUNTER LOGIC ---
def update_visitor_count():
    file_path = "visitor_count.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f: f.write("0")
    with open(file_path, "r") as f: current_count = int(f.read())
    new_count = current_count + 1
    with open(file_path, "w") as f: f.write(str(new_count))
    return new_count

# --- MOCK DATA ENGINE ---
def get_realtime_metrics():
    return {
        "Ethical Justice": np.random.randint(88, 100),
        "Spiritual Sensitivity": np.random.randint(90, 100),
        "Clinical Competence": np.random.randint(94, 100),
        "Institutional Integrity": np.random.randint(85, 98),
        "Patient Agency": np.random.randint(80, 96)
    }

# --- SIDEBAR: RESEARCHER PROFILE & CLOCK ---
st.sidebar.title("👨‍🔬 Research Information")
st.sidebar.markdown(f"""
**Lead Researcher:**  
**MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL**  
*Jabatan Kemajuan Islam Malaysia (JAKIM)*
""")

st.sidebar.markdown("---")
now = datetime.now()
st.sidebar.write("📅 **Current Date:**")
st.sidebar.info(now.strftime("%B %d, %Y"))
st.sidebar.write("⏰ **System Time:**")
st.sidebar.info(now.strftime("%H:%M:%S"))

visitors = update_visitor_count()
st.sidebar.markdown("---")
st.sidebar.metric(label="👥 Total Project Visitors", value=visitors)

st.sidebar.markdown("---")
role = st.sidebar.selectbox("Access Level", ["Global Admin", "Doctor/Clinical Staff", "Patient/Tourist"])

# --- MAIN DASHBOARD HEADER ---
st.title("🏥 ESCA+ Real-Time Hospital Integrity Dashboard")
st.markdown(f"**Research Framework:** *Reframing Islamic Medical Tourism through the ESCA+ Ethics Model*")

# --- LIVE METRICS ---
data = get_realtime_metrics()
overall_score = sum(data.values()) / 5

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Overall Integrity", f"{overall_score:.1f}%", "+0.4%")
col2.metric("Ethical Justice", f"{data['Ethical Justice']}%")
col3.metric("Spiritual Sensitivity", f"{data['Spiritual Sensitivity']}%")
col4.metric("Clinical Competence", f"{data['Clinical Competence']}%")
col5.metric("Patient Agency", f"{data['Patient Agency']}%")

st.markdown("---")

# --- VISUALIZATIONS ---
left_col, right_col = st.columns([2, 1])
with left_col:
    st.write("### 📈 Live Domain Performance")
    chart_df = pd.DataFrame({'Domain': list(data.keys()), 'Score': list(data.values())})
    fig = px.bar(chart_df, x='Domain', y='Score', color='Score', color_continuous_scale='Viridis', range_y=[0, 100])
    st.plotly_chart(fig, use_container_width=True)
with right_col:
    st.write("### ⚖️ Alignment Radar")
    radar_df = pd.DataFrame(dict(r=list(data.values()), theta=list(data.keys())))
    fig_radar = px.line_polar(radar_df, r='r', theta='theta', line_close=True)
    fig_radar.update_traces(fill='toself', line_color='#1f77b4')
    st.plotly_chart(fig_radar, use_container_width=True)

st.markdown("---")

# --- NEW SECTION: 10 EDUCATIONAL CASE STUDIES ---
st.header("📚 ESCA+ Education Center: Hospital Case Studies")
st.write("Explore how the ESCA+ dashboard resolves common ethical-clinical tensions in modern healthcare.")

# Creating an interactive selection for the 10 cases
case_list = [
    "1. Emergency vs. Modesty Preference",
    "2. Non-Halal Medicine Substitutes",
    "3. Price Transparency for Foreign Tourists",
    "4. End-of-Life Care & Spiritual Consultation",
    "5. Clinical Error & Institutional Sincerity",
    "6. Patient Decision (Ijtihad) in Complex Surgery",
    "7. Staff Competency vs. Religious Compliance",
    "8. Language Barriers & Ethical Justice",
    "9. Profit-Driven Overtreatment Risks",
    "10. Privacy during Multidisciplinary Rounds"
]

selected_case = st.selectbox("Select a Case Study to Review:", case_list)

# Define the logic for the 10 cases
cases_content = {
    "1. Emergency vs. Modesty Preference": {
        "Domain": "Spiritual Sensitivity (SS) & Patient Agency (PA)",
        "Scenario": "A female patient requires urgent abdominal scanning, but only male technicians are on shift.",
        "How Dashboard Helps": "The **Patient Agency portal** allows the patient to log a 'Micro-negotiation.' The dashboard tracks the 'Gender Match Success Rate,' prompting management to hire more female night-shift staff based on real-time data trends."
    },
    "2. Non-Halal Medicine Substitutes": {
        "Domain": "Spiritual Sensitivity (SS) & Clinical Competence (CC)",
        "Scenario": "A life-saving drug contains porcine-derived stabilizers. No halal alternative is immediately available.",
        "How Dashboard Helps": "The **Real-time Inventory Log** flags non-halal ingredients. It alerts the doctor to consult the patient's agency, ensuring the 'Necessity' (*Dharurah*) is explained and documented ethically."
    },
    "3. Price Transparency for Foreign Tourists": {
        "Domain": "Ethical Justice (EJ)",
        "Scenario": "A medical tourist from the Middle East is charged double the local rate for the same cardiac procedure.",
        "How Dashboard Helps": "The **Transparency Ledger** monitors bill variance. If a foreigner’s bill exceeds the standard deviation of local costs without clinical justification, an alert is sent to the Auditor to ensure 'Adl' (Justice)."
    },
    "4. End-of-Life Care & Spiritual Consultation": {
        "Domain": "Spiritual Sensitivity (SS)",
        "Scenario": "A terminally ill patient wants to discuss Maqasid al-Shariah perspectives on withdrawing life support.",
        "How Dashboard Helps": "The **Spiritual Consultation Tracker** ensures a qualified chaplain is dispatched within 30 minutes, logging the hospital's commitment to holistic care beyond just clinical outcome."
    },
    "5. Clinical Error & Institutional Sincerity": {
        "Domain": "Institutional Integrity (II)",
        "Scenario": "A surgical error occurs. The marketing department wants to hide it to protect the 'Islamic Branding.'",
        "How Dashboard Helps": "The **Sincerity Index** forces transparency. By logging errors alongside branding claims, the dashboard identifies the 'Marketing-Reality Gap,' preventing symbolic Islamisation from overriding clinical truth."
    },
    "6. Patient Decision (Ijtihad) in Complex Surgery": {
        "Domain": "Patient Agency (PA)",
        "Scenario": "A patient refuses a higher-success surgery because it involves a long hospital stay during Ramadan.",
        "How Dashboard Helps": "The **Shared Decision-Making (SDM) Log** documents the patient's rationale. It protects the hospital from liability while honoring the patient's right to perform their own 'Grassroots Ijtihad'."
    },
    "7. Staff Competency vs. Religious Compliance": {
        "Domain": "Clinical Competence (CC)",
        "Scenario": "A hospital claims to be Shariah-compliant but neglects JCI safety standards in the operation theater.",
        "How Dashboard Helps": "The **'Ilm (Knowledge) Score** monitors clinical safety in real-time. It proves that religious adherence must always align with high-tier medical expertise, preventing 'Compliance over Quality'."
    },
    "8. Language Barriers & Ethical Justice": {
        "Domain": "Ethical Justice (EJ)",
        "Scenario": "A Japanese medical tourist cannot understand the consent forms provided in English/Malay.",
        "How Dashboard Helps": "The **Access Equity Monitor** tracks the use of translation services. It ensures 'Moral Lucidity'—that every patient, regardless of origin, has equal access to understanding their treatment."
    },
    "9. Profit-Driven Overtreatment Risks": {
        "Domain": "Ethical Justice (EJ) & Institutional Integrity (II)",
        "Scenario": "Administrators pressure doctors to perform unnecessary C-sections on high-paying international patients.",
        "How Dashboard Helps": "The **Clinical Necessity Audit** compares surgery rates between locals and tourists. If the tourist rate is suspiciously higher, the 'Ethical Justice' score drops, signaling a profit-vs-piety conflict."
    },
    "10. Privacy during Multidisciplinary Rounds": {
        "Domain": "Spiritual Sensitivity (SS)",
        "Scenario": "A large group of male students enters a female patient's room for observation without checking her modesty preference.",
        "How Dashboard Helps": "The **Dignity Alignment Index** captures immediate patient feedback. Patients can report 'Privacy Breaches' via the mobile app, allowing ward managers to correct staff behavior in real-time."
    }
}

# Displaying the Selected Case
st.subheader(selected_case)
case_data = cases_content[selected_case]
st.write(f"**Primary ESCA+ Domain:** {case_data['Domain']}")
st.warning(f"**Clinical/Ethical Dilemma:** {case_data['Scenario']}")
st.success(f"**Dashboard Solution:** {case_data['How Dashboard Helps']}")

st.markdown("---")

# --- FOOTER ---
st.caption(f"© 2025 ESCA+ Ethics Model | Lead Researcher: MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL | Current Sync: {now.strftime('%H:%M:%S')}")
if st.button("Refresh All Data Streams"):
    st.rerun()
