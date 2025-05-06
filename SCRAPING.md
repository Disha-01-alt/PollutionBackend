# EcoMonitor - Data Sources & API Architecture

## Data Sources

EcoMonitor connects to real-time pollution data from the following authoritative Indian sources:

### Water Pollution Data
- **Source**: [Central Pollution Control Board (CPCB)](https://cpcb.nic.in/water-quality/)
- **Metrics**:
  - Biological Oxygen Demand (BOD)
  - Chemical Oxygen Demand (COD)
  - Dissolved Oxygen
  - pH Level
  - Total Coliform
- **Water Quality Index (WQI)**: Calculated using CPCB's methodology for overall water quality assessment

### Soil Pollution Data
- **Source**: [Indian Council of Agricultural Research (ICAR)](https://icar.gov.in/)
- **Metrics**:
  - Heavy Metal Contamination (Lead, Cadmium, Mercury)
  - Organic Pollutants
  - Salinity
  - Soil Fertility Loss
- **Contamination Level Index**: Composite score calculated based on multiple soil health parameters

### Plastic Pollution Data
- **Source**: [Centre for Science and Environment (CSE)](https://www.cseindia.org/)
- **Metrics**:
  - Plastic Waste Generation
  - Recycling Rate
  - Single-use Plastic Consumption
  - Microplastic Presence
- **Plastic Pollution Index**: Weighted measure of plastic waste management effectiveness

## API Architecture

The EcoMonitor application uses a clean architecture with logical separation of frontend and backend:

### Backend (API Server)
- Pure API endpoints at `/api/*` paths
- Handles data retrieval and processing from the scraped sources
- No business logic in the frontend
- Endpoints:
  - `/api/pollution`: All pollution data with optional filtering
  - `/api/cities`: List of all monitored cities
  - `/api/pollution-types`: Available pollution type categories

### Frontend
- Located in the `/frontend` directory
- Completely separate codebase from the backend
- Communicates with backend exclusively through API calls
- Can be deployed separately if needed

### Deployment Options
1. **Combined Deployment**: Frontend served by the Flask backend for simplicity (current setup)
2. **Separated Deployment**: Frontend and backend can be deployed to different servers

This architecture ensures:
- Clean separation of concerns
- Ability to scale frontend and backend independently
- Maintainable and testable code