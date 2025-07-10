import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(page_title="Wealth Management Trends", layout="wide")
st.title("📈 Wealth Management Trends Dashboard – USA")
st.caption("Strategy Dashboard for Financial Services | Built by Virtual BCG/McKinsey")

st.header("🔍 Key Trends in U.S. Wealth Management")

with st.container():
    if st.button("🔄 Refresh Trends"):
        st.success("Live insights updated (demo mode).")
    
    st.markdown("""
    - **Direct Indexing** projected to grow 3x by 2027 – BlackRock, Schwab leading.
    - **AI + Hybrid Advisory** models are mainstream: Vanguard pilots conversational AI.
    - **Alternative Assets** (private credit, PE, crypto) gain traction: 17% of HNW portfolios.
    - **Wealth Transfer** from Boomers to Millennials: $84T over 20 years.
    - **Fee Compression** + Regulation (Reg BI) reshaping margins.
    """)

st.header("🏦 Key Competitors Overview")

competitors_df = pd.DataFrame({
    "Firm": ["Morgan Stanley", "Fidelity", "Vanguard", "Betterment", "Empower"],
    "Model": ["Full-Service", "Hybrid", "Hybrid", "Robo", "Robo/Advisor"],
    "AUM ($B)": [1400, 4100, 8400, 35, 1.2],
    "Digital Maturity (1–5)": [4, 4, 3, 5, 5]
})

st.dataframe(competitors_df, use_container_width=True)

st.header("📊 Market Impact Dashboard")

market_df = pd.DataFrame({
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Robo AUM ($B)": [250, 310, 370, 420, 510],
    "Advisor Attrition Rate (%)": [8, 10, 11, 12, 13]
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("Robo AUM Growth")
    st.line_chart(market_df.set_index("Year")["Robo AUM ($B)"])

with col2:
    st.subheader("Advisor Attrition Rate")
    st.bar_chart(market_df.set_index("Year")["Advisor Attrition Rate (%)"])

st.header("🧭 Strategic Playbook")

st.markdown("""
#### For Large Financial Institutions:
- 🎯 **Digitally empower advisors** with real-time insights, AI co-pilots & mobile CRM.
- 🤝 **Partner or acquire** fintechs offering personalization or niche AI solutions.
- 🧠 **Segment HNW vs. mass affluent** with tailored onboarding & communication.
- 🧬 **Invest in behavioral analytics** to reduce churn and boost wallet share.
- 🌱 **Lead in ESG transparency** with interactive tools for values-based investing.
""")

st.markdown("---")
st.caption(f"Dashboard refreshed: {datetime.now().strftime('%B %d, %Y – %I:%M %p')}")
