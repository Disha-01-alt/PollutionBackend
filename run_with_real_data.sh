#!/bin/bash

# EcoMonitor Startup Script with Real-time Data Scraping
# This script runs the data scraper to fetch the latest pollution data
# from authoritative Indian sources and then starts the API server

echo "=== EcoMonitor with Real-time Pollution Data ==="
echo "Starting data scraping process..."

# Run the scraper to get real-time pollution data
python data_scraper.py

# Check if scraping was successful
if [ $? -eq 0 ]; then
    echo "Successfully scraped real-time pollution data from authoritative sources:"
    echo "- Central Pollution Control Board (CPCB) for water quality"
    echo "- Indian Council of Agricultural Research (ICAR) for soil data"
    echo "- Centre for Science and Environment (CSE) for plastic pollution"
    echo ""
    echo "Data saved to data/pollution_data.json"
else
    echo "Warning: Data scraping encountered issues. Using existing data."
fi

echo ""
echo "Starting API server with real pollution data..."
echo "API will be available at: http://localhost:5000/api"
echo ""
echo "Available endpoints:"
echo "- /api/pollution - Get all pollution data with optional filters"
echo "- /api/cities - Get list of all cities"
echo "- /api/pollution-types - Get list of all pollution types"
echo ""
echo "Press Ctrl+C to stop the server"

# Start the API server
if [ -n "$PORT" ]; then
    gunicorn --bind 0.0.0.0:$PORT api_server:app
else
    gunicorn --bind 0.0.0.0:5000 api_server:app
fi