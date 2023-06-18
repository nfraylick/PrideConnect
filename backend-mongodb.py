from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/prideconnect'
mongo = PyMongo(app)

# Route to get all mentors
@app.route('/mentors', methods=['GET'])
def get_mentors():
    mentors = mongo.db.mentors.find()
    return jsonify({'mentors': mentors}), 200

# Route to add a new mentor
@app.route('/mentors', methods=['POST'])
def add_mentor():
    mentor_data = request.get_json()
    mongo.db.mentors.insert_one(mentor_data)
    return jsonify({'message': 'Mentor added successfully'}), 201

# Route to get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = mongo.db.events.find()
    return jsonify({'events': events}), 200

# Route to add a new event
@app.route('/events', methods=['POST'])
def add_event():
    event_data = request.get_json()
    mongo.db.events.insert_one(event_data)
    return jsonify({'message': 'Event added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
