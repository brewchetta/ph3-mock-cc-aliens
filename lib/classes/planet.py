from lib import CONN, CURSOR

class Planet:

    # CALL THIS METHOD TO CREATE YOUR TABLE #
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS planets (
        id INTEGER PRIMARY KEY,
        name TEXT
        )"""
        CURSOR.execute(sql)

    # WRITE YOUR CODE BELOW #
