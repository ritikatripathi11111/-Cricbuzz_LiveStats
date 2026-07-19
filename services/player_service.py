from database.db_connection import get_connection


def get_players():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM players ORDER BY player_id")

    players = cursor.fetchall()

    cursor.close()
    conn.close()

    return players


def add_player(name, team, matches, runs):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO players(player_name, team_name, matches, runs)
    VALUES(%s,%s,%s,%s)
    """

    cursor.execute(query, (name, team, matches, runs))

    conn.commit()

    cursor.close()
    conn.close()


def update_player(player_id, name, team, matches, runs):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE players
    SET player_name=%s,
        team_name=%s,
        matches=%s,
        runs=%s
    WHERE player_id=%s
    """

    cursor.execute(query, (name, team, matches, runs, player_id))

    conn.commit()

    cursor.close()
    conn.close()


def delete_player(player_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM players WHERE player_id=%s",
        (player_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()