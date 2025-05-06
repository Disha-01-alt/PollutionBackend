import json
import logging
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('api_server')

# Create Flask app - pure API server without static file serving
app = Flask(__name__)

# Enable CORS for all routes with Access-Control-Allow-Origin: *
CORS(app)

# Global variable to store pollution data
pollution_data = None

@app.route('/')
def root():
    """API root endpoint - documentation"""
    return jsonify({
        "name": "EcoMonitor API",
        "version": "1.0.0",
        "description": "Pure API for pollution data in Indian cities",
        "note": "Frontend must be run separately",
        "endpoints": [
            {"path": "/api/pollution", "description": "Get all pollution data with optional filters"},
            {"path": "/api/cities", "description": "Get list of all cities"},
            {"path": "/api/pollution-types", "description": "Get list of all pollution types"}
        ]
    })

@app.route('/api')
def api_doc():
    """API documentation endpoint"""
    return jsonify({
        "name": "EcoMonitor API",
        "version": "1.0.0",
        "description": "API for pollution data in Indian cities",
        "endpoints": [
            {"path": "/api/pollution", "description": "Get all pollution data with optional filters"},
            {"path": "/api/cities", "description": "Get list of all cities"},
            {"path": "/api/pollution-types", "description": "Get list of all pollution types"}
        ]
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({"status": "ok", "message": "API is operational"})

def load_pollution_data():
    """Load pollution data from JSON file"""
    global pollution_data
    try:
        data_file = os.path.join('data', 'pollution_data.json')
        with open(data_file, 'r') as file:
            pollution_data = json.load(file)
        logger.debug(f"Loaded pollution data with {len(pollution_data['data'])} records")
    except Exception as e:
        logger.error(f"Error loading pollution data: {str(e)}")
        pollution_data = {"data": [], "cities": [], "pollution_types": []}

@app.route('/api/pollution')
def get_pollution_data():
    """
    Get pollution data with optional filtering
    Query parameters:
    - city: Filter by city name
    - type: Filter by pollution type (water, soil, plastic)
    """
    # Load data if not already loaded
    if pollution_data is None:
        load_pollution_data()
    
    # Get filter parameters
    city = request.args.get('city')
    pollution_type = request.args.get('type')
    
    # Apply filters if specified
    filtered_data = pollution_data['data']
    
    if city:
        filtered_data = [item for item in filtered_data if item['city'] == city]
    
    if pollution_type:
        filtered_data = [item for item in filtered_data if item['type'] == pollution_type]
    
    # Return filtered data
    result = {
        "data": filtered_data,
        "cities": pollution_data['cities'],
        "pollution_types": pollution_data['pollution_types']
    }
    
    logger.debug(f"Returning pollution data with {len(filtered_data)} records")
    return jsonify(result)

@app.route('/api/cities')
def get_cities():
    """Get list of all cities"""
    # Load data if not already loaded
    if pollution_data is None:
        load_pollution_data()
    
    return jsonify(pollution_data['cities'])

@app.route('/api/pollution-types')
def get_pollution_types():
    """Get list of all pollution types"""
    # Load data if not already loaded
    if pollution_data is None:
        load_pollution_data()
    
    return jsonify(pollution_data['pollution_types'])

# Load data at startup
load_pollution_data()

if __name__ == '__main__':
    # Set host to 0.0.0.0 to make the server publicly available
    app.run(host='0.0.0.0', port=5000, debug=True)