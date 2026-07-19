import streamlit as st

st.set_page_config(page_title="Cricbuzz LiveStats", page_icon="🏏")

st.title("🏏 Cricbuzz LiveStats Dashboard")

st.markdown("""
Welcome to the **Cricbuzz LiveStats Dashboard**.

This project is built using **Python, Streamlit, MySQL, and Cricbuzz RapidAPI** to provide cricket analytics and database operations.
""")

st.markdown("---")

st.header("🎯 Project Objectives")

st.markdown("""
- Display Live Cricket Matches
- Show Top Player Statistics
- Perform SQL Analytics
- Manage Player Records using CRUD
- Learn Database Management
""")

st.markdown("---")

st.header("✨ Features")

st.markdown("""
✅ Live Match Dashboard

✅ Top Player Statistics

✅ SQL Analytics (25 Queries)

✅ CRUD Operations

✅ CSV Download

✅ MySQL Database

✅ Cricbuzz API Integration
""")

st.markdown("---")

st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- Python
- Streamlit
- MySQL
- Pandas
""")

with col2:
    st.markdown("""
- RapidAPI
- Cricbuzz API
- Requests
- SQL
""")

st.markdown("---")

st.header("📂 Database")

st.markdown("""
- 13 Database Tables

- 25 SQL Queries

- Live Cricket Data

- Relational Database Design
""")

st.markdown("---")

st.header("📌 Navigation")

st.info("""
Use the left sidebar to explore:

🏠 Home

📊 Dashboard

🏏 Live Matches

📈 Top Stats

🗃 CRUD Operations

📋 SQL Analytics
""")

st.markdown("---")

st.success("Project Developed using Python • Streamlit • MySQL")