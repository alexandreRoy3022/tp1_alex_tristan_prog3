import sqlite3

from action.init import Partie


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('ma_base.db')
        self.cursor = self.conn.cursor()

    def ajouter_partie(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS partie(
             id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
             name TEXT,
             age INTERGER
        )
        """)
        self.conn.commit()
        self.conn.close()

    def ajouter_informations_partie(self, partie : Partie):
        self.cursor.execute("""
        INSERT INTO partie(name, age) VALUES(?, ?)""", ("olivier", 30))
        self.conn.commit()
        self.conn.close()

    def modifier_partie(self):
        self.cursor.execute("""UPDATE users SET age = ? WHERE id = 2""", (31,))
        self.conn.commit()
        self.conn.close()

    def supprimer_partie(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        DROP TABLE users
        """)
        self.conn.commit()
        self.conn.close()