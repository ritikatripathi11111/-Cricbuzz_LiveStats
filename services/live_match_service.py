from database.db_connection import get_connection


def get_live_matches():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        m.match_desc,
        m.match_format,
        m.status,
        m.state,

        t1.team_name AS team1,
        t2.team_name AS team2,

        v.ground,
        v.city

    FROM matches m

    JOIN teams t1
        ON m.team1_id = t1.team_id

    JOIN teams t2
        ON m.team2_id = t2.team_id

    JOIN venues v
        ON m.venue_id = v.venue_id
    """

    cursor.execute(query)

    matches = cursor.fetchall()
    
    print(matches)

    cursor.close()
    conn.close()

    return matches