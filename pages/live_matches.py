import streamlit as st
from services.live_match_service import get_live_matches

st.title("🏏 Live Cricket Matches")

st.markdown("""
View the latest cricket matches along with teams, venue and match status.
""")

st.markdown("---")

matches = get_live_matches()

if not matches:
    st.warning("No Live Matches Available")

if matches:

    for match in matches:

        with st.container():

            st.subheader(f"{match['team1']} 🆚 {match['team2']}")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Match:** {match['match_desc']}")
                st.write(f"**Format:** {match['match_format']}")

            with col2:
                st.write(f"**Venue:** {match['ground']}, {match['city']}")
                st.write(f"**Status:** {match['status']}")

            st.info(match["state"])

            st.markdown("---")

else:

    st.warning("No Live Matches Found")
    
    
st.caption("🏏 Cricbuzz LiveStats | Live Matches")