"""
EcoMonitor - API Main Entry Point
This is the main entry point for the EcoMonitor API server.
"""

from api_server import app

# The app is imported from api_server.py where it's initialized with all routes
# Gunicorn will use this for production deployment

if __name__ == '__main__':
    # This is only used for local development
    app.run(host='0.0.0.0', port=5000, debug=True)