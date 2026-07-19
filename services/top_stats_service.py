from database.db_connection import get_connection


def get_top_scores():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        t.team_name,
        ms.runs,
        ms.wickets,
        ms.overs
    FROM match_scores ms
    JOIN teams t
        ON ms.team_id = t.team_id
    ORDER BY ms.runs DESC
    LIMIT 10;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data