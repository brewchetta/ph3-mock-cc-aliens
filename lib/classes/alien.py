from lib import CONN, CURSOR

class Alien:

    # CALL THIS METHOD TO CREATE YOUR TABLE #
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS aliens (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        planet_id PRIMARY KEY
        )"""
        CURSOR.execute(sql)

    # WRITE YOUR CODE BELOW #
