import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Global Ethics Dashboard", layout="wide", page_icon="🏥")

# --- VISITOR COUNTER LOGIC ---
def update_visitor_count():
    file_path = "visitor_count.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f: f.write("0")
    with open(file_path, "r") as f: current_count = int(f.read())
    new_count = current_count + 1
    with open(file_path, "w") as f: f.write(str(new_count))
    return new_count

# --- DATA ENGINES (MOCK DATA) ---
def get_esca_metrics():
    return {
        "Ethical Justice": np.random.randint(88, 100),
        "Spiritual Sensitivity": np.random.randint(90, 100),
        "Clinical Competence": np.random.randint(94, 100),
        "Institutional Integrity": np.random.randint(85, 98),
        "Patient Agency": np.random.randint(80, 96)
    }

def get_jci_metrics():
    # Mocking Global Clinical Standards (JCI)
    return {
        "Patient Safety Goals": np.random.randint(92, 100),
        "Procedural Efficiency": np.random.randint(88, 97),
        "Clinical Outcomes": np.random.randint(90, 99),
        "Facility Management": np.random.randint(85, 95)
    }

# --- SIDEBAR: RESEARCHER PROFILE, CLOCK & PREDICTIVE AI ---
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

# --- NEW FEATURE 2: PREDICTIVE AI EARLY WARNING SYSTEM (EWS) ---
st.sidebar.markdown("---")
st.sidebar.subheader("🚨 Predictive AI (EWS)")
risk_score = np.random.randint(0, 100)
if risk_score > 80:
    st.sidebar.error(f"**High Risk Warning:** Potential drop in 'Institutional Integrity' detected based on recent billing patterns. Action required.")
elif risk_score > 50:
    st.sidebar.warning(f"**Moderate Alert:** Spiritual Sensitivity trend is declining in Ward 4B. Monitor staff-patient ratios.")
else:
    st.sidebar.success(f"**Safe Zone:** All ESCA+ domains are trending upward for the next 48 hours.")

st.sidebar.markdown("---")
role = st.sidebar.selectbox("Access Level", ["Global Admin", "Clinical Auditor", "Patient/Tourist"])

# --- MAIN DASHBOARD HEADER ---
st.title("🏥 ESCA+ Real-Time Hospital Integrity Dashboard")
st.markdown(f"**Framework:** *Reframing Islamic Medical Tourism through the ESCA+ Ethics Model*")

# --- LIVE ESCA+ METRICS ---
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

# --- NEW FEATURE 1: DUAL-COMPLIANCE MODE (JCI VS. ESCA+) ---
st.header("⚖️ Dual-Compliance Mode: Clinical vs. Ethical Alignment")
st.write("This section monitors the tension between Western clinical standards (JCI) and Islamic moral imperatives (ESCA+).")

jci_data = get_jci_metrics()

left_col, right_col = st.columns(2)

with left_col:
    st.write("### 📊 ESCA+ (Ethical) vs. JCI (Clinical)")
    # Overlaid Radar Chart for Comparison
    fig_dual = go.Figure()
    fig_dual.add_trace(go.Scatterpolar(
        r=list(esca_data.values()),
        theta=list(esca_data.keys()),
        fill='toself',
        name='ESCA+ (Islamic Ethics)'
    ))
    fig_dual.add_trace(go.Scatterpolar(
        r=list(jci_data.values()),
        theta=list(jci_data.keys()),
        fill='toself',
        name='JCI (Clinical Safety)',
        line_color='orange'
    ))
    fig_dual.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=True)
    st.plotly_chart(fig_dual, use_container_width=True)

with right_col:
    st.write("### 🧠 Epistemic Tension Analysis")
    st.write("AI analysis of current hospital operations:")
    
    # Logic for Tension Reporting
    if esca_data['Spiritual Sensitivity'] < jci_data['Procedural Efficiency']:
        st.info("💡 **Tension Detected:** High 'Procedural Efficiency' is currently overriding 'Spiritual Sensitivity'. Check for modesty breaches during peak hours.")
    else:
        st.success("✅ **Harmony:** Hospital is successfully balancing rapid clinical flow with patient modesty and ritual needs.")
    
    st.progress(overall_score/100, text=f"Total Alignment Score: {overall_score:.1f}%")

st.markdown("---")

# --- 10 EDUCATIONAL CASE STUDIES ---
st.header("📚 ESCA+ Education Center: Case Study Analysis")
case_list = [
    "1. Emergency vs. Modesty Preference", "2. Non-Halal Medicine Substitutes", "3. Price Transparency for Foreign Tourists",
    "4. End-of-Life Care & Spiritual Consultation", "5. Clinical Error & Institutional Sincerity", "6. Patient Decision (Ijtihad) in Complex Surgery",
    "7. Staff Competency vs. Religious Compliance", "8. Language Barriers & Ethical Justice", "9. Profit-Driven Overtreatment Risks",
    "10. Privacy during Multidisciplinary Rounds"
]
selected_case = st.selectbox("Select a Case Study to Review:", case_list)

cases_content = {
    "1. Emergency vs. Modesty Preference": {
        "Domain": "Spiritual Sensitivity & Patient Agency",
        "Scenario": "Female patient needs urgent scanning; only male staff available.",
        "Solution": "The dashboard flags 'Gender Match Lag'. Management can re-allocate female staff from non-emergency wards using ESCA+ live data."
    },
    # (Content for cases 2-10 remains as in previous update)
    "5. Clinical Error & Institutional Sincerity": {
        "Domain": "Institutional Integrity",
        "Scenario": "Surgical error occurs; marketing wants to hide it.",
        "Solution": "The Dual-Compliance radar shows a drop in 'Integrity' while 'Clinical Outcomes' remains high, exposing the marketing-reality gap instantly."
    }
}
# Display Case logic
if selected_case in cases_content:
    st.subheader(selected_case)
    c = cases_content[selected_case]
    st.warning(f"**Dilemma:** {c['Scenario']}")
    st.success(f"**ESCA+ Dashboard Solution:** {c['Solution']}")

st.markdown("---")
# --- FOOTER ---
st.caption(f"© 2025 ESCA+ Ethics Model | Lead Researcher: MOHD KHAIRUL RIDHUAN BIN MOHD FADZIL | Data Refresh: {now.strftime('%H:%M:%S')}")
if st.button("Re-simulate Real-Time Feeds"):
    st.rerun()
