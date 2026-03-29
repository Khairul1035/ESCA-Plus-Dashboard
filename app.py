import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
import os

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Ethics Dashboard", layout="wide", page_icon="🏥")

# --- VISITOR COUNTER LOGIC ---
# This function reads and updates a local file to track visitors
def update_visitor_count():
    file_path = "visitor_count.txt"
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("0")
    
    with open(file_path, "r") as f:
        current_count = int(f.read())
    
    new_count = current_count + 1
    
    with open(file_path, "w") as f:
        f.write(str(new_count))
    
    return new_count

# --- MOCK DATA ENGINE (The Real-Time Backbone) ---
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

# Real-time Date and Time
now = datetime.now()
st.sidebar.write("📅 **Current Date:**")
st.sidebar.info(now.strftime("%B %d, %Y"))
st.sidebar.write("⏰ **System Time:**")
st.sidebar.info(now.strftime("%H:%M:%S"))

# Visitor Counter Display
visitors = update_visitor_count()
st.sidebar.markdown("---")
st.sidebar.metric(label="👥 Total Project Visitors", value=visitors)

# Role Selection
st.sidebar.markdown("---")
role = st.sidebar.selectbox("Access Level", ["Global Admin", "Doctor/Clinical Staff", "Patient/Tourist"])

# --- MAIN DASHBOARD HEADER ---
st.title("🏥 ESCA+ Real-Time Hospital Integrity Dashboard")
st.markdown(f"**Research Framework:** *Reframing Islamic Medical Tourism through the ESCA+ Ethics Model*")
st.info("This dashboard provides live analytical insights into the Ethical-Spiritual-Clinical Alignment of healthcare facilities.")

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
    chart_df = pd.DataFrame({
        'Domain': list(data.keys()),
        'Score': list(data.values())
    })
    fig = px.bar(chart_df, x='Domain', y='Score', color='Score', 
                 color_continuous_scale='Viridis', range_y=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.write("### ⚖️ Alignment Radar")
    radar_df = pd.DataFrame(dict(r=list(data.values()), theta=list(data.keys())))
    fig_radar = px.line_polar(radar_df, r='r', theta='theta', line_close=True)
    fig_radar.update_traces(fill='toself', line_color='#1f77b4')
    st.plotly_chart(fig_radar, use_container_width=True)

# --- PRACTICAL INDUSTRY INTERFACE ---
if role == "Global Admin":
    st.write("### 🛡️ Institutional Integrity & Compliance Ledger")
    st.table(pd.DataFrame({
        "Audit Item": ["Halal Pharmacy Verification", "Gender-Matching Accuracy", "Price Transparency", "Patient Agency Log"],
        "Status": ["✅ Verified", "✅ 98% Match", "✅ Compliant", "✅ Active"],
        "Last Sync": [now.strftime("%H:%M"), now.strftime("%H:%M"), "Today", "Real-time"]
    }))

elif role == "Patient/Tourist":
    st.write("### 👋 Patient Agency Portal")
    st.write("Empowering you to negotiate between medical necessity and spiritual values.")
    st.button("Request Spiritual Consultation")
    st.button("View My Modesty Preferences")

# --- FOOTER ---
st.markdown("---")
st.caption(f"© 2025 ESCA+ Model | Developed by {now.year} {now.strftime('%A')} | Project Status: Live Data Stream")
