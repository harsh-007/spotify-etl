import sqlite3
import unittest
import pandas as pd

db_conn = sqlite3.connect("spotify_data.db")
df = pd.read_sql_query("SELECT * FROM albums", db_conn)
db_conn.close()

class TestSpotifyDataProcessing(unittest.TestCase):

    def test_radio_mix_column(self):
        self.assertTrue(all(df[df["duration_ms"] <= 180000]["radio_mix"] == True))
        self.assertTrue(all(df[df["duration_ms"] > 180000]["radio_mix"] == False))

    def test_non_explicit_filter(self):
        self.assertTrue(all(df["explicit"] == False))

    def test_popularity_filter(self):
        self.assertTrue(all(df["track_popularity"] > 50))

    def test_sqlite_table_exists(self):
        conn = sqlite3.connect("spotify_data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='albums';")
        table_exists = cursor.fetchone() is not None
        conn.close()
        self.assertTrue(table_exists)


if __name__ == "__main__":
    unittest.main()