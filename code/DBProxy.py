import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        try:
            self.connection = sqlite3.connect(db_name)
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS dados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                date TEXT NOT NULL)
            ''')
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def get_top_scores(self):
        try:
            return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 5').fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao obter scores: {e}")
            return []

    def get_last_score(self):
        try:
            # Returns the last score added to the bank based on the date entered
            return self.connection.execute('SELECT * FROM dados WHERE date = (SELECT MAX(date) FROM dados)').fetchall()
        except sqlite3.Error as e:
            print(f"Error getting score from database: {e}")
            return []

    def save(self, dict_score: dict):
        try:
            self.connection.execute('INSERT INTO dados (score, date) VALUES (:score, :date)', dict_score)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error saving score to database: {e}")
            return []

    def close(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")
