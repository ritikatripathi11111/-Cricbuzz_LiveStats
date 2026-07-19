import streamlit as st
import pandas as pd

from services.dashboard_services import get_dashboard_counts
from services.top_stats_service import get_top_scores

st.title("📊 Dashboard")

st.markdown("""
Welcome to the **Cricbuzz LiveStats Dashboard**.

Monitor cricket statistics, team performance, and database insights from one place.
""")

st.markdown("---")

# ================= Dashboard Metrics =================

teams, venues, matches, scores = get_dashboard_counts()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🏏 Teams", teams)

with col2:
    st.metric("🏟 Venues", venues)

with col3:
    st.metric("📅 Matches", matches)

with col4:
    st.metric("📊 Scores", scores)

st.markdown("---")

# ================= Team Score Overview =================

st.subheader("📈 Top Team Scores")

data = get_top_scores()

if data:

    df = pd.DataFrame(data)

    left, right = st.columns([2, 1])

    with left:
        st.dataframe(df, use_container_width=True)

    with right:
        st.bar_chart(
            df.set_index("team_name")["runs"]
        )

        top_team = df.iloc[0]

        st.success(
            f"🏆 Highest Score\n\n"
            f"{top_team['team_name']} - {top_team['runs']} Runs"
        )

else:
    st.warning("No Team Score Data Available")

st.markdown("---")

# ================= Dashboard Summary =================

st.subheader("📌 Dashboard Summary")

st.info("""
This dashboard provides a quick overview of the Cricbuzz LiveStats database.

Use the navigation menu to explore:

• 🏏 Live Matches

• 📈 Top Team Statistics

• 🗃 CRUD Operations

• 📊 SQL Analytics
""")

st.markdown("---")

# ================= Features =================

st.subheader("✨ Key Features")

feature1, feature2 = st.columns(2)

with feature1:
    st.success("""
✔ Dashboard Overview

✔ Live Match Information

✔ Team Score Statistics

✔ CRUD Operations
""")

with feature2:
    st.success("""
✔ SQL Analytics

✔ Data Visualization

✔ CSV Download

✔ MySQL Database Integration
""")

st.markdown("---")

# ================= Technology Stack =================

st.subheader("💻 Technology Stack")

st.write("""
- Python
- Streamlit
- MySQL
- Pandas
- Cricbuzz RapidAPI
""")

st.markdown("---")

st.caption("🏏 Cricbuzz LiveStats Dashboard | Python • Streamlit • MySQL")