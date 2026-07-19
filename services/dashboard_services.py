from database.db_connection import get_connection


def get_dashboard_counts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM teams")
    teams = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM venues")
    venues = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM matches")
    matches = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM match_scores")
    scores = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return teams, venues, matches, scores