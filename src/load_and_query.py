import sqlite3
import pandas as pd

def main():
    df = pd.read_csv("data/cleaned_data.csv")
    conn = sqlite3.connect('spotify_data.db')
    df.to_sql('albums', conn, if_exists='replace', index=False)
    query1 = """
    SELECT label, COUNT(track_id) AS total_tracks
    FROM albums
    GROUP BY label
    ORDER BY total_tracks DESC
    LIMIT 20;
    """
    top_labels = pd.read_sql(query1, conn)
    print("Top 20 Labels by Total Tracks:")
    print(top_labels)

    query2 = """
    SELECT track_name
    FROM albums
    WHERE release_date BETWEEN '2020-01-01' AND '2023-12-31'
    ORDER BY track_popularity DESC
    LIMIT 25;
    """
    top_tracks = pd.read_sql(query2, conn)
    print("\nTop 25 Popular Tracks (2020-2023):")
    print(top_tracks)

    conn.close()




if __name__ == "__main__":
    main()