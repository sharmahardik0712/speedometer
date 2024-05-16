import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify 

app = Flask(__name__)

### API to Insert Data into DB
@app.route('/data_insert', methods=['POST'])
def data_insert():
    conn = sqlite3.connect('speed_data.db')
    c = conn.cursor()
    data = request.json
    speed = data.get('speed')

    if not speed:
        return 'Speed data is missing', 400

    timestamp = datetime.now()
    c.execute("INSERT INTO speed_data (timestamp, speed) VALUES (?, ?)", (timestamp, speed))
    conn.commit()

    # Close the connection
    conn.close()

    return 'Data inserted successfully', 201

### API to Clear DB 
@app.route('/clear_data', methods=['GET'])
def clear_data():
    conn = sqlite3.connect('speed_data.db')
    c = conn.cursor()

    # Delete all data from the table
    c.execute("DELETE FROM speed_data")
    conn.commit()

    # Close the connection
    conn.close()

    return 'All data cleared successfully', 200


# API endpoint to return the latest entry in JSON format
@app.route('/latest_entry', methods=['GET'])
def latest_entry():
    conn = sqlite3.connect('speed_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM speed_data ORDER BY timestamp DESC LIMIT 1")
    latest_entry = c.fetchone()
    conn.close()
 
    if latest_entry:
        return jsonify({
            'timestamp': latest_entry[0],
            'speed': latest_entry[1]
        })
    else:
        return jsonify({'message': 'No data available'}), 404
    
@app.route('/')
def latest_entry_page():
    return render_template('index.html')    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
