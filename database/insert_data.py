from database.db_connection import get_connection


# teams data
def insert_team(team):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO teams(team_id, team_name, short_name, image_id)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        team["teamId"],
        team["teamName"],
        team["teamSName"],
        team["imageId"]
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    
    # Venue
    
def insert_venue(venue):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO venues
    (venue_id, ground, city, timezone, latitude, longitude)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        venue["id"],
        venue["ground"],
        venue["city"],
        venue["timezone"],
        venue["latitude"],
        venue["longitude"]
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
    
    
    # matches
def insert_match(info):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT IGNORE INTO matches
    (
        match_id,
        series_id,
        series_name,
        match_desc,
        match_format,
        start_date,
        end_date,
        state,
        status,
        team1_id,
        team2_id,
        venue_id
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        info["matchId"],
        info["seriesId"],
        info["seriesName"],
        info["matchDesc"],
        info["matchFormat"],
        info["startDate"],
        info["endDate"],
        info["state"],
        info["status"],
        info["team1"]["teamId"],
        info["team2"]["teamId"],
        info["venueInfo"]["id"]
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()
    
def insert_score(match_id, team_id, score):
        
        print(score)
        
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO match_scores
        (match_id, team_id, innings, runs, wickets, overs)
        VALUES (%s,%s,%s,%s,%s,%s)
        """
    
        values = (
        match_id,
        team_id,
        score.get("inningsId"),
        score.get("runs", 0),
        score.get("wickets", 0),
        score.get("overs", 0)
        )


        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()
    