# Architecture

## Overview
The system uses a 3-tier architecture:
1. **Data Ingestion Layer:** Simulates IoT sensors, Fleet GPS, and Shipment Manifests.
2. **AI Processing Layer (IBM Bob):** The core engine. It takes structured data, prompts Bob with specific supply chain logic, and returns JSON actions.
3. **Presentation Layer:** A React/Streamlit dashboard (or API endpoints) that displays alerts and recommendations.

## Data Flow
1. External Event (e.g., Port Strike) triggers webhook.
2. Backend sends Shipment list + Event to Bob API.
3. Bob identifies affected shipments (e.g., those passing through the strike zone).
4. Bob checks Fleet DB for idle trucks in nearby locations.
5. Bob outputs a "Reroute Plan".
6. System updates status and alerts the operator.