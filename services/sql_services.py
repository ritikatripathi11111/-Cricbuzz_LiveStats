from database.db_connection import get_connection


def execute_query(query):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result