import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS   # ← NEW
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)   # ← Allow ALL cross-origin requests (fixes "Failed to fetch")

# ---------------- Mock Data ----------------
MOCK_SHIPMENTS = [
    {"id": "SHIP-001", "route": "Shanghai -> LA", "status": "In Transit", "cargo": "Electronics", "value": 200000},
    {"id": "SHIP-002", "route": "Mumbai -> Rotterdam", "status": "Delayed", "cargo": "Vaccines", "value": 500000, "temp_sensor": "T-998"},
    {"id": "SHIP-003", "route": "NY -> London", "status": "In Transit", "cargo": "Perishables", "value": 50000, "temp_sensor": "T-112"}
]

MOCK_FLEET = [
    {"id": "TRUCK-01", "location": "LA Port", "status": "Idle", "capacity": "Refrigerated"},
    {"id": "TRUCK-02", "location": "Rotterdam", "status": "Idle", "capacity": "Standard"},
    {"id": "VESSEL-09", "location": "Shanghai", "status": "Maintenance", "capacity": "Cold Storage"}
]

# ---------------- Bob AI (Simulated) ----------------
def call_bob_ai(prompt):
    p = prompt.lower()
    if "disruption" in p or "port strike" in p:
        return json.dumps({
            "affected_shipments": ["SHIP-002"],
            "reason": "Port strike in Rotterdam",
            "recommendation": "Reroute to Antwerp or use TRUCK-02"
        })
    if "cold chain" in p or "temperature" in p or "sensor" in p:
        return json.dumps({
            "shipment_id": "SHIP-002",
            "risk_level": "CRITICAL",
            "action": "Immediate inspection required. Temp excursion detected at 08:00 AM."
        })
    if "fleet" in p:
        return json.dumps({
            "idle_assets": ["TRUCK-01", "TRUCK-02"],
            "redeployment_plan": "Assign TRUCK-01 to SHIP-003 for cold chain backup."
        })
    return json.dumps({"status": "ok"})

# ---------------- Routes ----------------
@app.route('/')
def home():
    return send_from_directory('.', 'dashboard.html')

@app.route('/api/disruption', methods=['GET', 'POST'])
def analyze_disruption():
    if request.is_json:
        data = request.json
    else:
        data = {"disruption_event": request.args.get('event', 'Unknown disruption')}
    prompt = f"Disruption: {data.get('disruption_event')}. Shipments: {json.dumps(MOCK_SHIPMENTS)}"
    return jsonify({"analysis": call_bob_ai(prompt)})

@app.route('/api/fleet', methods=['GET', 'POST'])
def optimize_fleet():
    prompt = f"Fleet optimization. Assets: {json.dumps(MOCK_FLEET)}"
    return jsonify({"optimization": call_bob_ai(prompt)})

@app.route('/api/cold-chain', methods=['GET', 'POST'])
def monitor_cold_chain():
    prompt = "Cold chain temperature sensor IoT breach check."
    return jsonify({"cold_chain_status": call_bob_ai(prompt)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)