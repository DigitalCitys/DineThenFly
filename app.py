from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

def connect_db(db, sqlcommand):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(sqlcommand)
    table = c.fetchall()
    conn.close()
    return jsonify([dict(r) for r in table])

@app.route('/api/restaurants')
def get_flight_data():
    try:
        rows = connect_db('restaurants.db', 'SELECT * FROM restaurants')
        return rows
    except Exception as e:
        return jsonify({'error': 'Could not retrieve restaurants', 'details': str(e)}), 500
