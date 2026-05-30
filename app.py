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
def get_restaurant_data():
    try:
        rows = connect_db('restaurants.db', 'SELECT * FROM restaurants')
        return rows
    except Exception as e:
        return jsonify({'error': 'Could not retrieve restaurants', 'details': str(e)}), 500

@app.route('/')
def index():
    return render_template('restaurants.html')

@app.route('/api/ontherocsmenu')
def get_menu_data():
    try:
        rows = connect_db('ontherocsmenu.db', 'SELECT * FROM menu ORDER BY category')
        return rows
    except Exception as e:
        return jsonify({'error': 'Could not retrieve menu items', 'details': str(e)}), 500

@app.route('/ontherocs')
def ontherocs():
    return render_template('ontherocs.html')

if __name__ == '__main__':
    app.run(debug=True)