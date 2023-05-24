import sqlite3
import time

class RecordDAO:
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name
        self._create_table()

    def _create_table(self):
        with self.connect() as conn:
            conn.execute(
                f"CREATE TABLE IF NOT EXISTS {self.table_name} (name TEXT NOT NULL, status TEXT NOT NULL, time INT, PRIMARY KEY(name))"
            )

    def connect(self):
        return sqlite3.connect(self.db_path)

    def get_all_cfer(self):
        with self.connect() as conn:
            r = conn.execute(
                f"SELECT name, status, time FROM {self.table_name}",
            ).fetchall()
        return r

    def get_cfer(self, name):
        with self.connect() as conn:
            r = conn.execute(
                f"SELECT name, status, time FROM {self.table_name} WHERE name='{name}'",
            ).fetchone()
        return r

    def insert_cfer(self, name, msg):
        now = time.time() // 1
        with self.connect() as conn:
            r = conn.execute(
                f"REPLACE INTO {self.table_name}(name, status, time) VALUES('{name}', '{msg}', {now})",
            ).fetchall()
        return r

    def update_cfer(self, name, msg):
        now = time.time() // 1
        with self.connect() as conn:
            r = conn.execute(
                f"UPDATE {self.table_name} SET status='{msg}', time={now} WHERE name='{name}'",
            ).fetchall()
        return r
