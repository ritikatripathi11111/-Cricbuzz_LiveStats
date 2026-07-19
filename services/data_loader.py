from api.cricket_api import fetch_live_matches
from database.insert_data import (
    insert_team,
    insert_venue,
    insert_match,
    insert_score
)


def load_data():
    data = fetch_live_matches()

    if not data:
        print("❌ No data received from API")
        return

    print("✅ Fetching Live Match Data...")

    for match_type in data.get("typeMatches", []):

        for series in match_type.get("seriesMatches", []):

            if "seriesAdWrapper" not in series:
                continue

            wrapper = series["seriesAdWrapper"]

            for match in wrapper.get("matches", []):

                info = match["matchInfo"]

                # -----------------------------
                # TEAM
                # -----------------------------
                team1 = info["team1"]
                team2 = info["team2"]

                insert_team(team1)
                insert_team(team2)

                # -----------------------------
                # VENUE
                # -----------------------------
                venue = info["venueInfo"]

                insert_venue(venue)

                # -----------------------------
                # MATCH
                # -----------------------------
                insert_match(info)

                # -----------------------------
                # MATCH SCORE
                # -----------------------------
                if "matchScore" in match:

                    score = match["matchScore"]

                    if "team1Score" in score:

                        innings = score["team1Score"].get("inngs1")

                        if innings:

                            insert_score(
                                info["matchId"],
                                team1["teamId"],
                                innings
                            )

                    if "team2Score" in score:

                        innings = score["team2Score"].get("inngs1")

                        if innings:

                            insert_score(
                                info["matchId"],
                                team2["teamId"],
                                innings
                            )

    print("✅ All Data Loaded Successfully!")