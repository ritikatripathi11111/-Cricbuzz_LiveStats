<div align="center">

# 🏏 Cricbuzz LiveStats Dashboard

### Live Cricket Analytics Platform powered by Python, Streamlit & MySQL

**📊 Track Live Matches • Analyze Team Statistics • Execute SQL Analytics • Manage Player Records**

<br>

<img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/REST_API-009688?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Cricbuzz_API-00C853?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Data_Analytics-6A1B9A?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SQL-FF6F00?style=for-the-badge"/>

<br><br>

<img src="https://img.shields.io/badge/License-Academic-success?style=flat-square"/>
<img src="https://img.shields.io/badge/Project-B.Tech%20Major%20Project-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/Database-MySQL-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/API-Cricbuzz-success?style=flat-square"/>
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square"/>

</div>

---

<div align="center">

## 🚀 Bringing Live Cricket Data & SQL Analytics Together

**Live Match Tracking → Team Statistics → Player Management → SQL Analytics → Interactive Visualizations**

</div>

---

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Streamlit-Framework-FF4B4B?style=for-the-badge&logo=streamlit"/>
<img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql"/>
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas"/>
<img src="https://img.shields.io/badge/API-Cricbuzz-success?style=for-the-badge"/>

</p>

<p align="center">
A modern cricket analytics platform that combines live match data, SQL analytics, player management, and interactive dashboards in one place.
</p>

</div>

---

# 📑 Table of Contents

- 📖 Project Overview
- ✨ Features
- 🛠 Tech Stack
- 🏗 Project Architecture
- 🗄 Database Schema
- 📸 Screenshots
- ⚙ Installation
- 📊 SQL Analytics
- 📂 Project Structure
- 🚀 Future Enhancements
- 👩‍💻 Author

---

# 📖 Project Overview

**Cricbuzz LiveStats Dashboard** is a data-driven cricket analytics application built with **Python, Streamlit, MySQL, and Cricbuzz RapidAPI**.

The dashboard fetches cricket data, stores it in a relational database, and presents it through an interactive web interface. It also includes SQL-based analytics, player management, and visual insights, making it suitable for learning database systems, API integration, and dashboard development.

---

# ✨ Features

| Feature               | Description                               |
| --------------------- | ----------------------------------------- |
| 🏠 Home Page          | Project overview and navigation           |
| 📊 Dashboard          | KPI cards with charts and statistics      |
| 🏏 Live Matches       | View live match details from Cricbuzz API |
| 📈 Top Statistics     | Team score analysis with visualizations   |
| 🗃 CRUD Operations    | Add, view, and delete player records      |
| 📋 SQL Analytics      | Execute 25 analytical SQL queries         |
| 📊 Data Visualization | Interactive charts and graphs             |
| 📥 CSV Export         | Download SQL query results                |

---

# 🛠 Tech Stack

| Category             | Technology        |
| -------------------- | ----------------- |
| Programming Language | Python            |
| Frontend             | Streamlit         |
| Database             | MySQL             |
| Data Analysis        | Pandas            |
| API                  | Cricbuzz RapidAPI |
| Visualization        | Streamlit Charts  |
| SQL                  | MySQL             |

---

# 🏗 Project Architecture

```text
          Cricbuzz API
                │
                ▼
        Python Service Layer
                │
                ▼
         MySQL Database
                │
                ▼
      Streamlit Dashboard UI
```

---

# 🗄 Database Schema

The project uses a normalized relational database consisting of the following tables:

- 🏏 Teams
- 👤 Players
- 🏟 Venues
- 📅 Matches
- 📊 Match Scores
- 🏆 Match Results
- 🎯 Player Batting Statistics
- 🎳 Player Bowling Statistics
- 🧤 Player Fielding Statistics
- 🤝 Partnerships
- 🥇 Series
- 🪙 Toss Details
- 📝 Innings

---

# 📸 Application Screenshots

## 🏠 Home

![Home](assets/home.png)

---

## 📊 Dashboard

![Dashboard](assets/dashboard.png)

---

## 🏏 Live Matches

![Live Matches](assets/live_matches.png)

---

## 📈 Top Statistics

![Top Stats](assets/top_stats.png)

---

## 🗃 CRUD Operations

![CRUD](assets/crud.png)

---

## 📋 SQL Analytics

![SQL Analytics](assets/sql_analytics.png)

---

# 📊 SQL Analytics

The dashboard includes **25 analytical SQL queries**, such as:

- ✅ Indian Players
- ✅ Team Wins
- ✅ Top ODI Run Scorers
- ✅ Match Results
- ✅ Bowling Performance
- ✅ Fielding Statistics
- ✅ Toss Analysis
- ✅ Partnerships
- ✅ Player Rankings
- ✅ Career Summary
- ✅ Recent Batting Form

---

# 📂 Project Structure

```text
cricbuzz_livestats/
│── app.py
│── requirements.txt
│── README.md
│
├── pages/
│   ├── home.py
│   ├── dashboard.py
│   ├── live_matches.py
│   ├── top_stats.py
│   ├── crud_operations.py
│   └── sql_queries.py
│
├── services/
│
├── database/
│
├── assets/
│
└── notebooks/
```

---

# ⚙ Installation

```bash
git clone https://github.com/your-username/cricbuzz-livestats.git

cd cricbuzz-livestats

pip install -r requirements.txt

streamlit run app.py
```

---

# 🚀 Future Enhancements

- 🔐 User Authentication
- 🌙 Dark Mode
- 📱 Mobile Responsive UI
- 📊 Advanced Interactive Charts
- 🤖 AI-based Match Prediction
- 👥 Player Comparison Dashboard
- 📄 PDF Report Generation

---

# 👩‍💻 Author

**Ritika Tripathi**

🎓 B.Tech – Computer Science Engineering  
🏫 Allenhouse Institute of Technology, Kanpur

---

<div align="center">

### ⭐ If you found this project useful, don't forget to star the repository!

**Made with ❤️ using Python, Streamlit & MySQL**

</div>
