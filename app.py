import os
import json
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS

# Create the Flask app - pure API server with no static file serving
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.secret_key = os.environ.get("SESSION_SECRET", "default_secret_key")

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load pollution data
def load_pollution_data():
    try:
        with open("data/pollution_data.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error loading pollution data: {e}")
        return {"cities": [], "pollution_types": [], "data": []}

# API Routes
@app.route("/api/pollution")
def get_pollution_data():
    data = load_pollution_data()
    
    # Filter by city if specified
    city = request.args.get('city')
    if city:
        data['data'] = [item for item in data['data'] if item['city'] == city]
    
    # Filter by pollution type if specified
    pollution_type = request.args.get('type')
    if pollution_type:
        data['data'] = [item for item in data['data'] if item['type'] == pollution_type]
    
    logger.debug(f"Returning pollution data with {len(data['data'])} records")
    return jsonify(data)

# Endpoint to get available cities
@app.route("/api/cities")
def get_cities():
    data = load_pollution_data()
    return jsonify(data.get('cities', []))

# Endpoint to get available pollution types
@app.route("/api/pollution-types")
def get_pollution_types():
    data = load_pollution_data()
    return jsonify(data.get('pollution_types', []))

# Root endpoint for API documentation
@app.route("/")
def root():
    return jsonify({
        "name": "EcoMonitor API",
        "version": "1.0.0",
        "description": "Pure API for pollution data in Indian cities",
        "endpoints": [
            {"path": "/api/pollution", "description": "Get all pollution data with optional filters"},
            {"path": "/api/cities", "description": "Get list of all cities"},
            {"path": "/api/pollution-types", "description": "Get list of all pollution types"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
