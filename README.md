<div align="center">

# 🏏 Cricbuzz LiveStats Dashboard

### AI-Powered Live Cricket Analytics & SQL Dashboard

<p>
Track live cricket matches, analyze player & team performance, execute advanced SQL analytics, and visualize insights through an interactive dashboard.
</p>

<p>
<i>📊 Analyze smarter. Query faster. Visualize better.</i>
</p>

<br>

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>

<br>

<img src="https://img.shields.io/badge/Cricbuzz_API-00C853?style=for-the-badge"/>
<img src="https://img.shields.io/badge/REST_API-009688?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SQL_Analytics-FF6F00?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Data_Visualization-6A1B9A?style=for-the-badge"/>

<br><br>

<img src="https://img.shields.io/badge/Project-B.Tech%20Major%20Project-orange?style=flat-square"/>
<img src="https://img.shields.io/badge/License-Academic-success?style=flat-square"/>
<img src="https://img.shields.io/badge/Database-MySQL-blue?style=flat-square"/>
<img src="https://img.shields.io/badge/API-Cricbuzz-success?style=flat-square"/>
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square"/>

</div>

---

## 🚀 Project Highlights

✨ Live Match Tracking

📊 Interactive Dashboard

🏏 Team & Player Statistics

📋 25+ SQL Analytical Queries

📈 Data Visualization

🗃 Complete CRUD Operations

⚡ Real-Time API Integration

📥 CSV Export Support

---

# 📑 Table of Contents

- [📖 Project Overview](#-project-overview)
- [✨ Key Features](#-key-features)
- [🛠 Tech Stack](#-tech-stack)
- [🏗 System Architecture](#-system-architecture)
- [🗄 Database Design](#-database-design)
- [📸 Application Screenshots](#-application-screenshots)
- [📊 SQL Analytics](#-sql-analytics)
- [📂 Project Structure](#-project-structure)
- [⚙ Installation](#-installation)
- [🚀 Future Enhancements](#-future-enhancements)
- [👩‍💻 Author](#-author)

---

# 📖 Project Overview

Cricbuzz LiveStats Dashboard is a comprehensive cricket analytics platform that integrates **live cricket data**, **SQL analytics**, **interactive dashboards**, and **database management** into one application.

The project demonstrates how REST APIs, relational databases, and data visualization techniques can be combined to create a modern sports analytics platform.

Instead of manually searching multiple websites for statistics, users can access live match information, player records, team performance, and advanced SQL reports from one centralized dashboard.

---

## 🎯 Objectives

- Fetch live cricket data using Cricbuzz RapidAPI.
- Store structured data in MySQL.
- Build an interactive analytics dashboard with Streamlit.
- Perform advanced SQL analysis on cricket datasets.
- Visualize insights using charts and tables.
- Demonstrate CRUD operations with relational databases.
- Provide an educational project for DBMS, Python, and API integration.

---

# ✨ Key Features

| Module             | Description                               |
| ------------------ | ----------------------------------------- |
| 🏠 Home            | Introduction and project navigation       |
| 📊 Dashboard       | Overall project statistics and KPI cards  |
| 🏏 Live Matches    | Live score and match information          |
| 📈 Top Statistics  | Highest team scores and comparisons       |
| 👤 Player Records  | Manage player information                 |
| 🗃 CRUD Operations | Create, Read, Update & Delete player data |
| 📋 SQL Analytics   | Execute 25+ analytical SQL queries        |
| 📊 Charts          | Interactive visualizations                |
| 📥 CSV Export      | Download SQL results                      |

---

# 🛠 Tech Stack

| Category             | Technology         |
| -------------------- | ------------------ |
| Programming Language | Python             |
| Framework            | Streamlit          |
| Database             | MySQL              |
| Data Processing      | Pandas             |
| API                  | Cricbuzz RapidAPI  |
| SQL                  | MySQL              |
| Charts               | Streamlit Charts   |
| IDE                  | Visual Studio Code |
| Version Control      | Git & GitHub       |

---

# 🏗 System Architecture

```text
                      🏏 Cricbuzz RapidAPI
                               │
                               ▼
                    REST API Integration Layer
                               │
                               ▼
                    Python Service Layer (Backend)
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
     MySQL Database      SQL Analytics        CRUD Operations
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ▼
                  Streamlit Interactive Dashboard
                               │
                               ▼
                            End User
```

---

# 🗄 Database Design

The project follows a **normalized relational database** to efficiently manage cricket information.

## 📋 Database Tables

| Table             | Description                   |
| ----------------- | ----------------------------- |
| 🏏 Teams          | Stores team details           |
| 👤 Players        | Player information            |
| 🏟 Venues         | Match venue details           |
| 📅 Matches        | Match schedules               |
| 📊 Match Scores   | Innings and score information |
| 🏆 Match Results  | Final match results           |
| 🥇 Series         | Tournament and series details |
| 🎯 Batting Stats  | Individual batting statistics |
| 🎳 Bowling Stats  | Individual bowling statistics |
| 🧤 Fielding Stats | Catch, stumpings & run-outs   |
| 🤝 Partnerships   | Partnership records           |
| 🪙 Toss Details   | Toss winner and decision      |
| 📝 Innings        | Innings-wise information      |

---

## 📌 Database Features

- Relational Database Design
- Primary & Foreign Key Relationships
- Data Integrity
- Normalized Tables
- SQL-Based Analytics
- Fast Query Execution

---

# 📸 Application Screenshots

## 🏠 Home Page

> Overview of the application and navigation.

![Home](assets/home.png)

---

## 📊 Dashboard

> Displays KPI cards, charts, and summary statistics.

![Dashboard](assets/dashboard.png)

---

## 🏏 Live Matches

> Shows live cricket matches fetched from Cricbuzz RapidAPI.

![Live Matches](assets/live_matches.png)

---

## 📈 Top Statistics

> Visual comparison of top-performing teams and scores.

![Top Statistics](assets/top_stats.png)

---

## 🗃 CRUD Operations

> Add, view, and manage player records stored in MySQL.

![CRUD](assets/crud.png)

---

## 📋 SQL Analytics

> Execute analytical SQL queries and export results.

![SQL Analytics](assets/sql_analytics.png)

---

# 📊 SQL Analytics

The dashboard includes **25+ analytical SQL queries** for exploring cricket data.

### Some featured queries include:

- ✅ Indian Players
- ✅ Overseas Players
- ✅ Team Win Percentage
- ✅ Highest ODI Scores
- ✅ Top Run Scorers
- ✅ Bowling Performance Analysis
- ✅ Fielding Statistics
- ✅ Toss Decision Analysis
- ✅ Match Result Summary
- ✅ Partnership Records
- ✅ Venue-wise Statistics
- ✅ Player Career Summary
- ✅ Recent Batting Performance
- ✅ Series-wise Match Count
- ✅ Team Performance Comparison

---

## 📈 Analytics Features

- Interactive SQL execution
- Dynamic result tables
- CSV export
- Fast query processing
- Cricket statistics analysis
- Performance comparison
- Team & player insights

---

# 📂 Project Structure

```text
cricbuzz_livestats/
│
├── app.py
├── requirements.txt
├── README.md
│
├── database/
│   └── db_connection.py
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
│   ├── dashboard_services.py
│   ├── live_match_service.py
│   ├── top_stats_service.py
│   ├── crud_services.py
│   └── sql_services.py
│
├── assets/
│   ├── home.png
│   ├── dashboard.png
│   ├── live_matches.png
│   ├── top_stats.png
│   ├── crud.png
│   └── sql_analytics.png
│
└── notebooks/
```

---

## 📁 Project Modules

### 🏠 Home

Provides project overview and navigation.

### 📊 Dashboard

Displays KPIs, charts, and summary statistics.

### 🏏 Live Matches

Fetches real-time match information from Cricbuzz RapidAPI.

### 📈 Top Statistics

Analyzes team scores and cricket performance.

### 🗃 CRUD Operations

Manages player records stored in MySQL.

### 📋 SQL Analytics

Runs analytical SQL queries and exports results.

---

# ⚙ Installation

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ritikatripathi11111/-Cricbuzz_LiveStats
```

### 2️⃣ Navigate to the Project Folder

```bash
cd cricbuzz-livestats
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

- Install MySQL
- Create a database
- Import the provided SQL file
- Update your database credentials in:

```text
database/db_connection.py
```

### 5️⃣ Configure Cricbuzz API

Add your RapidAPI credentials inside the API service file.

```python
API_KEY = "YOUR_RAPIDAPI_KEY"
```

### 6️⃣ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# ▶️ How to Use

After launching the application, you can explore the following modules:

### 🏠 Home

- Project overview
- Navigation
- Feature summary

### 📊 Dashboard

- KPI cards
- Match statistics
- Team insights
- Charts

### 🏏 Live Matches

- View live cricket matches
- Match status
- Venue details
- Team information

### 📈 Top Statistics

- Highest team scores
- Performance comparison
- Interactive charts

### 🗃 CRUD Operations

- Add player
- View players
- Update records
- Delete records

### 📋 SQL Analytics

- Execute analytical SQL queries
- View results instantly
- Export results as CSV

---

# 📊 Learning Outcomes

This project helped in understanding:

- REST API Integration
- Python Programming
- Streamlit Dashboard Development
- MySQL Database Design
- SQL Query Optimization
- CRUD Operations
- Data Visualization
- Data Analytics
- Git & GitHub
- Project Deployment

---

# 🚀 Future Enhancements

The project can be extended with:

- 🔐 User Authentication
- 👥 Multi-user Support
- 🌙 Dark Mode
- 📱 Responsive Mobile UI
- 🤖 AI-based Match Prediction
- 📊 Advanced Interactive Charts
- 📈 Player Comparison Dashboard
- 🏆 Tournament Analytics
- 📄 PDF Report Generation
- ☁ Cloud Database Integration
- 🚀 Streamlit Cloud Deployment

---

# 🙏 Acknowledgements

Special thanks to:

- Cricbuzz RapidAPI for providing live cricket data.
- Streamlit for simplifying dashboard development.
- MySQL for efficient relational database management.
- Pandas for data manipulation and analysis.
- The open-source community for valuable learning resources.

---

# 👩‍💻 Author

## Ritika Tripathi

**B.Tech – Computer Science & Engineering**

Allenhouse Institute of Technology, Kanpur

### Technical Skills

- Python
- MySQL
- SQL
- Streamlit
- Pandas
- REST API
- Data Analytics
- Data Visualization
- Git & GitHub

---

# 📜 License

This project has been developed for **academic and educational purposes** as part of a B.Tech major project.

---

<div align="center">

# ⭐ Support the Project

If you found this project useful,

### ⭐ Star this repository

It helps others discover the project and motivates future improvements.

---

### 💙 Thank you for visiting!

**Made with ❤️ using Python, Streamlit, MySQL & Cricbuzz RapidAPI**

</div>
