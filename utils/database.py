import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS analysis_results
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  image_path TEXT,
                  damage_probability REAL,
                  damage_area REAL,
                  calculated_force REAL,
                  device_adjustment TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()
    print("Database initialized successfully")

def insert_result(image_path, damage_probability, damage_area, calculated_force, device_adjustment):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Store only the filename, not the full path
    filename = os.path.basename(image_path)
    c.execute('''INSERT INTO analysis_results 
                 (image_path, damage_probability, damage_area, calculated_force, device_adjustment)
                 VALUES (?, ?, ?, ?, ?)''',
              (filename, damage_probability, damage_area, calculated_force, device_adjustment))
    conn.commit()
    conn.close()

def get_all_results():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM analysis_results where image_path is NOT NULL AND image_path != "" ORDER BY timestamp DESC')
    results = c.fetchall()
    conn.close()
    return results