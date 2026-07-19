import streamlit as st
import pandas as pd
from services.sql_services import execute_query

# -------------------- PAGE HEADER --------------------

st.set_page_config(page_title="SQL Analytics", page_icon="📊")

st.title("📊 SQL Analytics Dashboard")

st.markdown("""
Run SQL queries on the **Cricbuzz LiveStats Database** and analyze the results.
""")

st.markdown("---")

st.subheader("📝 Select a Query")

st.info(
    "Choose any SQL query from the dropdown below and click **Run Query** to view the results."
)

# -------------------- SQL QUERIES --------------------

queries = {

    "Question 1 - Indian Players":

"""

SELECT

player_name,

team_name,

matches,

runs

FROM players

WHERE team_name='India';

""",



"Question 2 - Matches Played":

"""

SELECT

m.match_desc,

t1.team_name AS Team1,

t2.team_name AS Team2,

v.ground,

v.city

FROM matches m

JOIN teams t1

ON m.team1_id=t1.team_id

JOIN teams t2

ON m.team2_id=t2.team_id

JOIN venues v

ON m.venue_id=v.venue_id;

""",



"Question 3 - Top ODI Run Scorers":

"""

SELECT

p.player_name,

b.runs_scored,

b.batting_average,

b.centuries

FROM player_batting_stats b

JOIN players p

ON p.player_id=b.player_id

WHERE format='ODI'

ORDER BY runs_scored DESC

LIMIT 10;

""",



"Question 4 - Large Stadiums":

"""

SELECT

ground,

city,

country,

capacity

FROM venues

WHERE capacity>50000

ORDER BY capacity DESC;

""",



"Question 5 - Team Wins":

"""

SELECT

t.team_name,

COUNT(*) AS total_wins

FROM match_results mr

JOIN teams t

ON mr.winner_team_id=t.team_id

GROUP BY t.team_name

ORDER BY total_wins DESC;

""",



"Question 6 - Players By Team":

"""

SELECT

team_name,

COUNT(*) AS total_players

FROM players

GROUP BY team_name;

""",



"Question 7 - Highest Score By Format":

"""

SELECT

format,

MAX(highest_score) AS HighestScore

FROM player_batting_stats

GROUP BY format;

""",



"Question 8 - Series Started in 2025":

"""

SELECT

series_name,

host_country,

match_type,

start_date,

total_matches

FROM series

WHERE YEAR(start_date)=2025;

""",



"Question 9 - All-rounders (Runs & Wickets)":

"""

SELECT

p.player_name,

b.runs_scored,

bw.wickets_taken,

b.format

FROM players p

JOIN player_batting_stats b

ON p.player_id=b.player_id

JOIN player_bowling_stats bw

ON p.player_id=bw.player_id

WHERE b.runs_scored>1000

AND bw.wickets_taken>0;

""",



"Question 10 - Match Results":

"""

SELECT

m.match_desc,

t.team_name AS Winner,

mr.victory_margin,

mr.victory_type,

mr.toss_decision

FROM match_results mr

JOIN matches m

ON mr.match_id=m.match_id

JOIN teams t

ON mr.winner_team_id=t.team_id;

""",



"Question 11 - Player Performance Across Formats":

"""

SELECT

p.player_name,

b.format,

b.runs_scored,

b.batting_average,

b.strike_rate

FROM players p

JOIN player_batting_stats b

ON p.player_id=b.player_id

ORDER BY p.player_name;

""",



"Question 12 - Toss Decisions":

"""

SELECT

decision,

COUNT(*) AS TotalMatches

FROM toss_details

GROUP BY decision;

""",



"Question 13 - Best Partnerships":

"""

SELECT

p1.player_name AS Batsman1,

p2.player_name AS Batsman2,

partnership_runs

FROM partnerships pt

JOIN players p1

ON pt.batsman1_id=p1.player_id

JOIN players p2

ON pt.batsman2_id=p2.player_id

ORDER BY partnership_runs DESC;

""",



"Question 14 - Bowling Performance":

"""

SELECT

p.player_name,

bw.format,

bw.wickets_taken,

bw.economy_rate

FROM player_bowling_stats bw

JOIN players p

ON p.player_id=bw.player_id

ORDER BY wickets_taken DESC;

""",



"Question 15 - Fielding Performance":

"""

SELECT

p.player_name,

f.catches,

f.run_outs,

f.stumpings

FROM player_fielding_stats f

JOIN players p

ON p.player_id=f.player_id

ORDER BY catches DESC;

""",



"Question 16 - Player Career Summary":

"""

SELECT

p.player_name,

SUM(b.matches) AS TotalMatches,

SUM(b.runs_scored) AS TotalRuns,

AVG(b.batting_average) AS AvgBattingAverage

FROM players p

JOIN player_batting_stats b

ON p.player_id=b.player_id

GROUP BY p.player_name;

""",



"Question 17 - Toss Win Analysis":

"""

SELECT

decision,

COUNT(*) AS Total_Tosses

FROM toss_details

GROUP BY decision;

""",



"Question 18 - Most Economical Bowlers":

"""

SELECT

p.player_name,

bw.format,

bw.economy_rate,

bw.wickets_taken

FROM player_bowling_stats bw

JOIN players p

ON p.player_id=bw.player_id

ORDER BY bw.economy_rate ASC;

""",



"Question 19 - Most Consistent Batsmen":

"""

SELECT

p.player_name,

AVG(b.runs_scored) AS AverageRuns,

AVG(b.batting_average) AS BattingAverage

FROM player_batting_stats b

JOIN players p

ON p.player_id=b.player_id

GROUP BY p.player_name

ORDER BY AverageRuns DESC;

""",



"Question 20 - Matches Played by Format":

"""

SELECT

p.player_name,

b.format,

b.matches,

b.batting_average

FROM player_batting_stats b

JOIN players p

ON p.player_id=b.player_id

ORDER BY p.player_name,b.format;

""",



"Question 21 - Overall Player Ranking":

"""

SELECT

p.player_name,

(

(b.runs_scored*0.01)+

(b.batting_average*0.5)+

(b.strike_rate*0.3)+

(COALESCE(bw.wickets_taken,0)*2)+

(COALESCE(f.catches,0)*3)

) AS RankingScore

FROM player_batting_stats b

JOIN players p

ON p.player_id=b.player_id

LEFT JOIN player_bowling_stats bw

ON bw.player_id=p.player_id

LEFT JOIN player_fielding_stats f

ON f.player_id=p.player_id

ORDER BY RankingScore DESC;

""",



"Question 22 - Team Win Percentage":

"""

SELECT

t.team_name,

COUNT(*) AS Wins

FROM match_results mr

JOIN teams t

ON mr.winner_team_id=t.team_id

GROUP BY t.team_name

ORDER BY Wins DESC;

""",



"Question 23 - Recent Batting Form":

"""

SELECT

p.player_name,

b.format,

b.runs_scored,

b.strike_rate,

CASE

WHEN b.runs_scored>5000 THEN 'Excellent'

WHEN b.runs_scored>3000 THEN 'Good'

ELSE 'Average'

END AS CurrentForm

FROM player_batting_stats b

JOIN players p

ON p.player_id=b.player_id;

""",



"Question 24 - Best Batting Partnerships":

"""

SELECT

p1.player_name AS Player1,

p2.player_name AS Player2,

partnership_runs

FROM partnerships pt

JOIN players p1

ON pt.batsman1_id=p1.player_id

JOIN players p2

ON pt.batsman2_id=p2.player_id

ORDER BY partnership_runs DESC;

""",



"Question 25 - Player Performance Ranking":

"""

SELECT

player_name,

SUM(runs_scored) AS TotalRuns,

RANK() OVER(

ORDER BY SUM(runs_scored) DESC

) AS PlayerRank

FROM

player_batting_stats b

JOIN players p

ON p.player_id=b.player_id

GROUP BY player_name;

"""
}

# -------------------- QUERY SELECTION --------------------

selected_query = st.selectbox(
    "Select SQL Query",
    list(queries.keys())
)

# -------------------- RUN QUERY --------------------

if st.button("▶ Run Query", use_container_width=True):

    result = execute_query(queries[selected_query])

    if result:

        df = pd.DataFrame(result)

        st.success(f"✅ Rows Returned : {len(df)}")

        st.subheader("📄 Query Result")

        st.dataframe(
            df,
            use_container_width=True
        )

        # -------------------- DOWNLOAD CSV --------------------

        st.download_button(
            label="📥 Download Result as CSV",
            data=df.to_csv(index=False),
            file_name="query_result.csv",
            mime="text/csv"
        )

        # -------------------- AUTO CHART --------------------

        numeric_columns = df.select_dtypes(include="number").columns

        if len(numeric_columns) > 0 and len(df.columns) > 1:

            st.markdown("---")
            st.subheader("📊 Data Visualization")

            category_column = df.columns[0]
            numeric_column = numeric_columns[0]

            chart_df = df.set_index(category_column)[numeric_column]

            st.bar_chart(chart_df)

    else:

        st.warning("⚠ No data found for this query.")

# -------------------- FOOTER --------------------

st.markdown("---")

st.caption("🏏 Cricbuzz LiveStats Dashboard | SQL Analytics | Python • Streamlit • MySQL")