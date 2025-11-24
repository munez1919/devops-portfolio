import os
import psycopg2
from flask import jsonify

def test_db_connection():
    db_url = os.getenv("DATABASE_URL")
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("SELECT 123;")
        result = cur.fetchone()
        conn.close()
        return jsonify({"db_status": "ok", "value": result[0]})
    except Exception as e:
        return jsonify({"db_status": "error", "error": str(e)})
