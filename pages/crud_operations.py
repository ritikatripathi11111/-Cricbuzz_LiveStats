import streamlit as st
import pandas as pd

from services.player_service import (
    get_players,
    add_player,
    delete_player
)

st.title("🗃 Player Management")

st.markdown("""
Manage player records using Create, Read and Delete operations.
""")

st.markdown("---")
# --------------------------
# Add Player
# --------------------------

st.subheader("➕ Add New Player")

with st.form("player_form"):

    name = st.text_input("Player Name")
    team = st.text_input("Team Name")

    matches = st.number_input(
        "Matches",
        min_value=0,
        step=1
    )

    runs = st.number_input(
        "Runs",
        min_value=0,
        step=1
    )

    submitted = st.form_submit_button("Add Player")

    if submitted:

        add_player(name, team, matches, runs)

        st.success("✅ Player Added Successfully")

        st.rerun()


# --------------------------
# View Players
# --------------------------
st.markdown("---")

st.subheader("📋 Player Records")

players = get_players()

if players:

    df = pd.DataFrame(players)

    st.dataframe(df, use_container_width=True)
    st.success(f"Total Players : {len(players)}")

else:

    st.warning("No Players Found")


# --------------------------
# Delete Player
# --------------------------
st.markdown("---")

st.subheader("🗑 Delete Player")

player_ids = [player["player_id"] for player in players]

selected_id = st.selectbox(
    "Select Player ID",
    player_ids
)

if st.button("❌ Delete Player"):

    delete_player(selected_id)

    st.success("✅ Player Deleted Successfully")

    st.rerun()
    
    
    
st.markdown("---")

st.caption("🏏 Cricbuzz LiveStats | CRUD Operations")