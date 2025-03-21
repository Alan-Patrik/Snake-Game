import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS dados(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER NOT NULL,
            date TEXT NOT NULL)
        ''')

    def get_top_scores(self):
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 5').fetchall()

    def get_last_score(self):
        # Retorta o último score adicionado no banco baseado na data inserida
        return self.connection.execute('SELECT * FROM dados WHERE date = (SELECT MAX(date) FROM dados)').fetchall()

    def save(self, dict_score: dict):
        self.connection.execute('INSERT INTO dados (score, date) VALUES (:score, :date)', dict_score)
        self.connection.commit()

    def close(self):
        self.connection.close()
