import streamlit as st
import pandas as pd
import feedparser
from datetime import datetime
import urllib.parse

st.set_page_config(page_title="Wealth Management Trends", layout="wide")
st.title("📈 Wealth Management Trends Dashboard – USA")
st.caption("Strategy Dashboard for Financial Services | Built by Virtual BCG/McKinsey")

# ---- USER FILTERS ----
st.sidebar.header("🎯 Filter Trends")
segment = st.sidebar.selectbox("Client Segment", ["All", "HNW", "Mass Affluent", "Gen Z"])
theme = st.sidebar.multiselect("Investment Theme", ["ESG", "Digital Wealth", "Alternatives", "AI", "Wealth Transfer"], default=["Digital Wealth"])

# ---- KEY TRENDS (STATIC) ----
st.header("🔍 Key Trends in U.S. Wealth Management")
st.markdown("Customized based on selected filters.")

trend_bullets = {
    "ESG": "🔵 ESG compliance under pressure; Gen Z prioritizes values-aligned investing.",
    "Digital Wealth": "🟠 Digital onboarding & hybrid robo models growing fastest in mass affluent segments.",
    "Alternatives": "🟣 Alternatives (private credit, PE, crypto) now 17% of HNW portfolios.",
    "AI": "🟢 Advisors leveraging AI copilots for planning, risk, and engagement.",
    "Wealth Transfer": "🟡 $84T in intergenerational wealth transfer is reshaping priorities."
}

for t in theme:
    st.markdown(f"- {trend_bullets[t]}")

# ---- GOOGLE NEWS & PERPLEXITY TREND SEARCH ----
st.header("🧠 Explore Real-Time Trends (Search Engines)")

search_query = f"{segment if segment != 'All' else ''} wealth management " + " ".join(theme)
encoded_query = urllib.parse.quote(search_query)

col1, col2 = st.columns(2)
with col1:
    st.subheader("🔎 Google News")
    st.markdown(f"[Search Google News for '{search_query}'](https://news.google.com/search?q={encoded_query})", unsafe_allow_html=True)

with col2:
    st.subheader("🔍 Perplexity (Preview Mode)")
    st.markdown(f"[Simulate Perplexity Search](https://www.perplexity.ai/search?q={encoded_query})", unsafe_allow_html=True)

# ---- LIVE INDUSTRY NEWS FROM FINEXTRA ----
st.header("🔴 Real-Time News (Finextra)")

feed_url = "https://www.finextra.com/rss/news.aspx?topic=Wealth%20Management"
feed = feedparser.parse(feed_url)

if feed.entries:
    for entry in feed.entries[:5]:
        st.markdown(f"🔗 [{entry.title}]({entry.link})  \n<small>{entry.published}</small>", unsafe_allow_html=True)
else:
    st.warning("Unable to fetch Finextra feed. Try again later.")

# ---- COMPETITOR SNAPSHOT ----
st.header("🏦 Key Competitors Overview")

competitors_df = pd.DataFrame({
    "Firm": ["Morgan Stanley", "Fidelity", "Vanguard", "Betterment", "Empower"],
    "Model": ["Full-Service", "Hybrid", "Hybrid", "Robo", "Robo/Advisor"],
    "AUM ($B)": [1400, 4100, 8400, 35, 1.2],
    "Digital Maturity (1–5)": [4, 4, 3, 5, 5]
})
st.dataframe(competitors_df, use_container_width=True)

# ---- MARKET IMPACT VISUALIZATION ----
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

# ---- STRATEGIC RECOMMENDATIONS ----
st.header("🧭 Strategy Playbook")

st.markdown("""
#### Strategic Levers Based on Filters:
- 📱 Double down on **mobile-first** + AI-enhanced advisor tools.
- 🤝 Launch partnerships with **fintechs** focused on alternatives or digital advice.
- 📊 Use **behavioral segmentation** to target Gen Z vs. HNW clients.
- 🌱 Offer **ESG screening tools** for values-aligned investors.
""")

# ---- FOOTER ----
st.markdown("---")
st.caption(f"Dashboard refreshed: {datetime.now().strftime('%B %d, %Y – %I:%M %p')}")
