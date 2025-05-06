# EcoMonitor - Indian Pollution Data API

A comprehensive API providing real pollution data for Indian cities, with metrics on water, soil, and plastic pollution.

## API Overview

This project provides a REST API for accessing real pollution data from authoritative Indian sources:

- **Water Pollution**: Data from Central Pollution Control Board (CPCB) and National Water Monitoring Programme
- **Soil Pollution**: Data from Indian Council of Agricultural Research (ICAR) and National Bureau of Soil Survey
- **Plastic Pollution**: Data from CPCB, Centre for Science and Environment (CSE), and TERI

## API Endpoints

### Get Pollution Data
```
GET /api/pollution
```

Optional query parameters:
- `city`: Filter by city name (e.g., "Mumbai", "Delhi")
- `type`: Filter by pollution type (e.g., "water", "soil", "plastic")

### Get Available Cities
```
GET /api/cities
```

### Get Available Pollution Types
```
GET /api/pollution-types
```

### Health Check
```
GET /api/health
```

## Deployment Instructions

### Backend (API Server)

The backend is a Flask-based REST API that serves pollution data from the `data/pollution_data.json` file.

1. Make sure you have Python 3.x installed
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python api_server.py`
4. API will be available at `http://localhost:5000/api/`

Environment variables:
- `PORT`: Port number (default: 5000)

### Frontend

The frontend is a vanilla JavaScript application that visualizes the pollution data using Chart.js.

1. Update the API endpoint in the frontend code if necessary (current default: `/api/`)
2. Deploy the frontend static files to any web server or CDN
3. The frontend will fetch data from the API endpoints

## Data Sources

The application uses real pollution data from:

1. **Water Pollution**:
   - Central Pollution Control Board (CPCB): https://cpcb.nic.in/water-quality/
   - National Water Monitoring Programme data from 4000+ stations

2. **Soil Pollution**:
   - Indian Council of Agricultural Research (ICAR): https://icar.gov.in/
   - National Bureau of Soil Survey & Land Use Planning: https://www.nbsslup.in/
   - Ministry of Environment, Forest and Climate Change: https://moef.gov.in/

3. **Plastic Pollution**:
   - CPCB Plastic Waste Management: https://cpcb.nic.in/plastic-waste-management/
   - Centre for Science and Environment (CSE): https://www.cseindia.org/
   - The Energy and Resources Institute (TERI): https://www.teriin.org/
   - UN Environment Programme: https://www.unep.org/explore-topics/plastic-pollution

## License

MIT