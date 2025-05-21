import sqlite3
from datetime import datetime

DB_NAME = "sent_messages.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sent
                 (listing_id TEXT PRIMARY KEY, timestamp TEXT)''')
    conn.commit()
    conn.close()

def has_sent(listing_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT 1 FROM sent WHERE listing_id=?", (listing_id,))
    result = c.fetchone()
    conn.close()
    return result is not None

def log_sent(listing_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO sent (listing_id, timestamp) VALUES (?, ?)", 
              (listing_id, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
