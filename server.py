from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample events, each with an 'id' and a 'title'
events = [
    {"id": 1, "title": "Tech Meetup"},
    {"id": 2, "title": "Python Workshop"},
]

# GET / : welcome message
@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Event Catalog API!"})

# GET /events : all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events)

# POST /events : add a new event
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(silent=True)

    # 400 if no JSON or no title
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    new_id = max((e["id"] for e in events), default=0) + 1
    new_event = {"id": new_id, "title": data["title"]}
    events.append(new_event)
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)