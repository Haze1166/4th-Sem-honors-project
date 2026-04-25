from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# In-memory storage (for batch processing demo)
data_store = []

# Home route
@app.route('/')
def home():
    return "Server is running 🚀"

# API to receive data (Client → Server)
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    data_store.append(data)
    return jsonify({
        "message": "Data received successfully",
        "received": data
    })

# Batch processing endpoint
@app.route('/process', methods=['GET'])
def process_data():
    return jsonify({
        "total_records": len(data_store),
        "data": data_store
    })

# Run server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))