import streamlit as st
import pandas as pd

from services.top_stats_service import get_top_scores

st.title("📈 Top Team Statistics")

st.markdown("""
View the highest team scores stored in the Cricbuzz LiveStats database.
""")

st.markdown("---")

data = get_top_scores()

if data:

    df = pd.DataFrame(data)

    st.subheader("🏏 Top Team Scores")

    st.dataframe(df, use_container_width=True)

    st.markdown("---")

    st.subheader("📊 Runs Comparison")

    chart = df.set_index("team_name")["runs"]

    st.bar_chart(chart)

    st.markdown("---")

    top_team = df.iloc[0]

    st.success(
        f"🏆 Highest Score : {top_team['team_name']} - {top_team['runs']} Runs"
    )

    st.info(f"Total Teams Displayed : {len(df)}")

else:

    st.warning("No Statistics Available")

st.markdown("---")

st.caption("🏏 Cricbuzz LiveStats | Top Team Statistics")