import sqlite3

DB_PATH = 'database.db'  # Make sure this matches the path in your utils/database.py in my case


def check_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # Check if the table exists
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='analysis_results'")
        if c.fetchone():
            print("Table 'analysis_results' exists.")

            # Check if there's any data
            c.execute("SELECT COUNT(*) FROM analysis_results")
            count = c.fetchone()[0]
            print(f"Number of rows in 'analysis_results': {count}")
        else:
            print("Table 'analysis_results' does not exist.")

        conn.close()
    except Exception as e:
        print(f"Error checking database: {e}")


if __name__ == "__main__":
    check_db()