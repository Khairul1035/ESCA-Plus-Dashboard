import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# --- 1. DASHBOARD CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Global Ethics Dashboard", layout="wide", page_icon="🏥")

# --- 2. VISITOR COUNTER LOGIC ---
def update_visitor_count():
    file_path = "visitor_count.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f: f.write("0")
    with open(file_path, "r") as f: current_count = int(f.read())
    new_count = current_count + 1
    with open(file_path, "w") as f: f.write(str(new_count))
    return new_count

# --- 3. DATA ENGINES (MOCK DATA FOR SIMULATION) ---
def get_esca_metrics():
    return {
        "Ethical Justice": np.random.randint(88, 100),
        "Spiritual Sensitivity": np.random.randint(90, 100),
        "Clinical Competence": np.random.randint(94, 100),
        "Institutional Integrity": np.random.randint(85, 98),
        "Patient Agency": np.random.randint(80, 96)
    }

def get_jci_metrics():
    # Global Clinical Standards (JCI) Metrics
    return {
        "Patient Safety": np.random.randint(92, 100),
        "Efficiency": np.random.randint(88, 97),
        "Clinical Outcomes": np.random.randint(90, 99),
        "Management": np.random.randint(85, 95)
    }

# --- 4. SIDEBAR: RESEARCHER, CLOCK, VISITOR & AI ---
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
st.sidebar.metric(label="👥 Total Project Visitors", value=visitors)

# PREDICTIVE AI EARLY WARNING SYSTEM (EWS)
st.sidebar.markdown("---")
st.sidebar.subheader("🚨 Predictive AI (EWS)")
risk_score = np.random.randint(0, 100)
if risk_score > 80:
    st.sidebar.error("**High Risk Warning:** Potential drop in 'Institutional Integrity' detected based on billing patterns. Audit required.")
elif risk_score > 50:
    st.sidebar.warning("**Moderate Alert:** Spiritual Sensitivity trend is declining in Ward 4B. Monitor staff-patient ratios.")
else:
    st.sidebar.success("**Safe Zone:** All ESCA+ domains are trending upward for the next 48 hours.")

st.sidebar.markdown("---")
role = st.sidebar.selectbox("Access Level", ["Global Admin", "Clinical Auditor", "Patient/Tourist"])

# --- 5. MAIN DASHBOARD: HEADER ---
st.title("🏥 ESCA+ Real-Time Hospital Integrity Dashboard")
st.markdown(f"**Research Framework:** *Reframing Islamic Medical Tourism through the ESCA+ Ethics Model*")

# LIVE ESCA+ KPI METRICS
esca_data = get_esca_metrics()
overall_score = sum(esca_data.values()) / 5

st.subheader("🛡️ Current ESCA+ Ethics Performance")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Overall Integrity", f"{overall_score:.1f}%", "+0.4%")
col2.metric("Ethical Justice", f"{esca_data['Ethical Justice']}%")
col3.metric("Spiritual Sensitivity", f"{esca_data['Spiritual Sensitivity']}%")
col4.metric("Clinical Competence", f"{esca_data['Clinical Competence']}%")
col5.metric("Patient Agency", f"{esca_data['Patient Agency']}%")

st.markdown("---")

# --- 6. DUAL-COMPLIANCE MODE (JCI VS ESCA+) ---
st.header("⚖️ Dual-Compliance Mode: Clinical vs. Ethical Alignment")
st.write("Monitoring the balance between JCI clinical safety and ESCA+ Islamic moral imperatives.")

jci_data = get_jci_metrics()
left_col, right_col = st.columns(2)

with left_col:
    st.write("### 📊 Alignment Radar")
    fig_dual = go.Figure()
    fig_dual.add_trace(go.Scatterpolar(r=list(esca_data.values()), theta=list(esca_data.keys()), fill='toself', name='ESCA+ (Ethics)'))
    fig_dual.add_trace(go.Scatterpolar(r=list(jci_data.values()), theta=list(jci_data.keys()), fill='toself', name='JCI (Clinical)', line_color='orange'))
    fig_dual.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True)
    st.plotly_chart(fig_dual, use_container_width=True)

with right_col:
    st.write("### 🧠 AI Tension Analysis")
    if esca_data['Spiritual Sensitivity'] < jci_data['Efficiency']:
        st.info("💡 **Tension:** Efficiency is currently overriding Spiritual Sensitivity. Audit ward modesty protocols.")
    else:
        st.success("✅ **Harmony:** Hospital is successfully balancing rapid clinical flow with patient modesty needs.")
    st.progress(overall_score/100, text=f"Total Integrity Alignment: {overall_score:.1f}%")

st.markdown("---")

# --- 7. LIVE PATIENT JOURNEY SIMULATOR (USA CASE) ---
st.header("🏃‍♂️ Live Patient Journey Simulator (Practical Implementation)")
st.write("**Scenario:** Road Accident Patient from USA (Non-Muslim Cultural Context)")

journey_stage = st.select_slider(
    "Slide to simulate the Dashboard action at each stage of care:",
    options=["1. Admission", "2. Emergency Room", "3. Ward Recovery", "4. Billing & Discharge"]
)

col_icon, col_action = st.columns([1, 4])

if journey_stage == "1. Admission":
    col_icon.image("https://cdn-icons-png.flaticon.com/512/3502/3502688.png", width=120)
    col_action.subheader("Stage: Initial Admission")
    col_action.write("**Dashboard Tracking (Ethical Justice):** Prevents 'Tourist Pricing' spikes. Transparency ledger locks the standard clinical rate automatically.")
    col_action.info("ESCA+ Objective: Ensuring Fairness (Adl) for global patients regardless of religious background.")

elif journey_stage == "2. Emergency Room":
    col_icon.image("https://cdn-icons-png.flaticon.com/512/809/809957.png", width=120)
    col_action.subheader("Stage: Life-Saving Care")
    col_action.write("**Dashboard Tracking (Clinical Competence):** Live monitoring of JCI Trauma Protocols. Safety takes 100% priority.")
    col_action.success("ESCA+ Objective: Scientific Rigor (Ilm) is the highest ethical duty in life-threatening emergencies.")

elif journey_stage == "3. Ward Recovery":
    col_icon.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=120)
    col_action.subheader("Stage: In-Patient Stay")
    col_action.write("**Dashboard Tracking (Spiritual Sensitivity):** Logs cultural dietary needs and privacy preferences. Ensures non-Muslims feel respected within a Shariah-compliant space.")
    col_action.warning("ESCA+ Objective: Respecting Human Dignity (Karamah) beyond boundaries.")

elif journey_stage == "4. Billing & Discharge":
    col_icon.image("https://cdn-icons-png.flaticon.com/512/2489/2489756.png", width=120)
    col_action.subheader("Stage: Final Financial Audit")
    col_action.write("**Dashboard Tracking (Institutional Integrity):** Verifies all charges against the initial quote. Provides an 'Ethical Integrity Receipt' for international insurance.")
    col_action.error("ESCA+ Objective: Eradicating Market Exploitation and building Global Trust (Amanah).")

st.markdown("---")

# --- 8. 10 EDUCATIONAL CASE STUDIES ---
st.header("📚 ESCA+ Education Center: Case Study Analysis")
case_list = [
    "1. Emergency vs. Modesty Preference", "2. Non-Halal Medicine Substitutes", "3. Price Transparency for Foreign Tourists",
    "4. End-of-Life Care & Spiritual Consultation", "5. Clinical Error & Institutional Sincerity", "6. Patient Decision (Ijtihad) in Complex Surgery",
    "7. Staff Competency vs. Religious Compliance", "8. Language Barriers & Ethical Justice", "9. Profit-Driven Overtreatment Risks",
    "10. Privacy during Multidisciplinary Rounds"
]
selected_case = st.selectbox("Select a Case Study to Review:", case_list)

cases_content = {
    "1. Emergency vs. Modesty Preference": "Dashboard flags 'Gender Match Lag'. Management re-allocates female staff from non-emergency wards using ESCA+ live data.",
    "2. Non-Halal Medicine Substitutes": "Real-time inventory flags porcine ingredients. System prompts doctor to explain medical necessity (Dharurah) to the patient via Agency portal.",
    "3. Price Transparency for Foreign Tourists": "Ethics dashboard detects billing variance higher than 10%. Admin is alerted to correct the bill for justice (Adl).",
    "4. End-of-Life Care & Spiritual Consultation": "Spiritual Care tracker ensures chaplain/expert dispatch within 30 mins to honor patient's existential needs.",
    "5. Clinical Error & Institutional Sincerity": "Radar chart shows drop in Integrity despite high Clinical scores, exposing branding-reality gaps to auditors.",
    "6. Patient Decision (Ijtihad) in Complex Surgery": "Documents patient's personal choice to delay surgery for religious reasons, protecting hospital liability via documented agency.",
    "7. Staff Competency vs. Religious Compliance": "Integrates JCI safety metrics to ensure religious rituals do not replace clinical safety standards.",
    "8. Language Barriers & Ethical Justice": "Access Equity Monitor tracks translation use to ensure every tourist understands their treatment plan (Moral Lucidity).",
    "9. Profit-Driven Overtreatment Risks": "Audit compares surgery rates of tourists vs locals to prevent exploitation in the name of medical tourism.",
    "10. Privacy during Multidisciplinary Rounds": "Dignity Alignment Index captures patient complaints of privacy breaches, triggering immediate staff training alerts."
}
st.subheader(selected_case)
st.success(f"**How Dashboard Resolves This:** {cases_content[selected_case]}")

# --- 9. FOOTER ---
st.markdown("---")
st.caption(f"© 2025 ESCA+ Ethics Model | Lead Researcher: MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL | Data Stream: Active | Sync: {now.strftime('%H:%M:%S')}")
if st.button("Re-simulate All Live Streams"):
    st.rerun()
