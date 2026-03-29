import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Global Integrity Dashboard", layout="wide")

# Custom CSS for a professional "Trust" aesthetic
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATA ENGINE (The Real-Time Backbone) ---
def get_realtime_data():
    # In a real industry app, this would be an API call to the Hospital Database
    return {
        "Ethical Justice": np.random.randint(85, 100),
        "Spiritual Sensitivity": np.random.randint(90, 100),
        "Clinical Competence": np.random.randint(92, 100),
        "Institutional Integrity": np.random.randint(80, 95),
        "Patient Agency": np.random.randint(75, 95),
        "Timestamp": datetime.now().strftime("%H:%M:%S")
    }

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("ESCA+ Ethics Model")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=100)
role = st.sidebar.selectbox("Select User Role", ["Global Administrator", "Medical Professional", "Patient/Tourist"])

st.sidebar.info(f"Viewing as: **{role}**")
st.sidebar.markdown("---")
st.sidebar.write("Reframing Islamic Medical Tourism through Ethical-Spiritual-Clinical Alignment.")

# --- MAIN DASHBOARD ---
st.title("🏥 ESCA+ Real-Time Hospital Integrity Dashboard")
st.subheader("Bridging Faith and Medical Systems through Data Transparency")

data = get_realtime_data()
overall_score = sum([v for k, v in data.items() if k != "Timestamp"]) / 5

# Top Level Metrics
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Overall Integrity", f"{overall_score:.1f}%", "+1.2%")
col2.metric("Ethical Justice", f"{data['Ethical Justice']}%", "Stable")
col3.metric("Spiritual Sensitivity", f"{data['Spiritual Sensitivity']}%", "-0.5%")
col4.metric("Clinical Competence", f"{data['Clinical Competence']}%", "+0.8%")
col5.metric("Patient Agency", f"{data['Patient Agency']}%", "+2.1%")

st.markdown("---")

# Visualizing the 5 Domains
left_col, right_col = st.columns([2, 1])

with left_col:
    st.write("### 📈 Real-Time Domain Performance (Live Feed)")
    # Create a trend chart
    chart_data = pd.DataFrame({
        'Domain': list(data.keys())[:-1],
        'Score': [data[k] for k in list(data.keys())[:-1]]
    })
    fig = px.bar(chart_data, x='Domain', y='Score', color='Domain', 
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    fig.update_layout(showlegend=False, yaxis_range=[0,100])
    st.plotly_chart(fig, use_container_width=True)

with right_col:
    st.write("### ⚖️ Ethical Integrity Radar")
    # Radar chart for holistic view
    radar_df = pd.DataFrame(dict(
        r=[data[k] for k in list(data.keys())[:-1]],
        theta=list(data.keys())[:-1]))
    fig_radar = px.line_polar(radar_df, r='r', theta='theta', line_close=True)
    fig_radar.update_traces(fill='toself')
    st.plotly_chart(fig_radar, use_container_width=True)

# --- ROLE SPECIFIC FEATURES ---
st.markdown("---")

if role == "Patient/Tourist":
    st.write("### 👋 Welcome Patient: Your Agency Portal")
    with st.expander("Submit a 'Micro-Negotiation' (Ijtihad) Decision"):
        st.write("Did you choose to prioritize clinical speed over a religious preference today?")
        choice = st.radio("Reason for deviation:", ["Emergency Urgency", "Personal Comfort", "No Alternative Available"])
        feedback = st.text_area("How can we improve your spiritual-clinical alignment?")
        if st.button("Submit to Hospital Ledger"):
            st.success("Your decision has been logged. This contributes to the 'Patient Agency' domain score.")

elif role == "Global Administrator":
    st.write("### 🛡️ Institutional Integrity Audit")
    col_a, col_b = st.columns(2)
    col_a.write("**Transparency Logs (Ethical Justice)**")
    col_a.dataframe(pd.DataFrame({
        "Patient ID": ["MT-102", "MT-105", "MT-110"],
        "Quoted Price": ["$5,000", "$12,000", "$3,500"],
        "Final Bill": ["$5,050", "$12,100", "$3,450"],
        "Status": ["✅ Fair", "✅ Fair", "✅ Refunded Variance"]
    }))
    
    col_b.write("**Marketing vs. Reality (Sincerity Index)**")
    col_b.info("AI Analysis: 92% of marketing claims about 'Compassionate Care' match real-time patient sentiment analysis.")

# --- FOOTER ---
st.write(f"**Last Sync with Hospital API:** {data['Timestamp']}")
if st.button("Refresh Live Feed"):
    st.rerun()
