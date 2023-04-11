from lib import CONN, CURSOR

class Alien:

    def __init__(self, first_name, last_name, age, id = None):
        if type(first_name) == str:
            self.first_name = first_name
        if type(last_name) == str: 
            self.last_name = last_name
        if type(age) == int and age >= 0:
            # self._age = age
            self.age = age
        self.id = id

    def __repr__(self):
        return f"Alien first_name={self.first_name} last_name={self.last_name} age={self.age}"

    def get_age(self):
        if hasattr(self, "_age"):
            return self._age

    def set_age(self,age):
        if isinstance(age, int) and age >= 0:
            self._age = age
        else:
            print("Age must be a number greater or equal to 0")

    age = property(get_age, set_age)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def save(self):
        if self.id:
            self._update()
        else:
            self._create()

    def _create(self):
        sql = """INSERT INTO aliens (first_name, last_name, age)
        VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, [self.first_name, self.last_name, self.age])
        CONN.commit()

        self.id = CURSOR.execute("SELECT * FROM aliens ORDER BY id DESC").fetchone()[0]

    def _update(self):
        sql = """UPDATE aliens
        SET first_name = ?, last_name = ?, age = ?
        WHERE id = ?
        """
        CURSOR.execute(sql, [self.first_name, self.last_name, self.age, self.id])
        CONN.commit()

    @classmethod
    def query_all(cls):
        sql = "SELECT * FROM aliens"
        all_aliens = CURSOR.execute(sql).fetchall()
        aliens_list = []
        for data in all_aliens:
            alien = Alien(data[1], data[2], data[3], data[0])
            # alien.id = data[0]
            aliens_list.append(alien)
        return aliens_list

    @classmethod
    def query_one(cls, id):
        all = cls.query_all()
        for alien in all:
            if alien.id == id:
                return alien

    @classmethod
    def average_age(cls):
        all = cls.query_all()
        sum = 0
        for alien in all:
            sum += alien.age
        return sum / len(all)

    @classmethod
    def query_oldest(cls):
        # sql = """SELECT * FROM aliens ORDER BY age DESC
        # """
        sql = """SELECT * FROM aliens 
        WHERE age = (SELECT MAX(age) FROM aliens)
        """
        oldest = CURSOR.execute(sql).fetchone()
        return Alien(oldest[1], oldest[2], oldest[3], oldest[0])