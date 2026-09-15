import os
import requests
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# IBM Bob Configuration
BOB_API_KEY = os.getenv("BOB_API_KEY")
BOB_API_URL = "https://api.bob.ibm.com/v1/chat/completions"

# Mock Data
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


def call_bob_ai(prompt):
    """Helper to call IBM Bob API (with simulated fallback)."""
    # --- SIMULATED BOB LOGIC FOR DEMO ---
    if "disruption" in prompt.lower():
        return json.dumps({
            "affected_shipments": ["SHIP-002"],
            "reason": "Port strike in Rotterdam",
            "recommendation": "Reroute to Antwerp or use TRUCK-02"
        })
    if "cold chain" in prompt.lower() or "temperature" in prompt.lower():
        return json.dumps({
            "shipment_id": "SHIP-002",
            "risk_level": "CRITICAL",
            "action": "Immediate inspection required. Temp excursion detected at 08:00 AM."
        })
    if "fleet" in prompt.lower():
        return json.dumps({
            "idle_assets": ["TRUCK-01", "TRUCK-02"],
            "redeployment_plan": "Assign TRUCK-01 to SHIP-003 for cold chain backup."
        })
    return json.dumps({"error": "Unknown prompt type"})


@app.route('/')
def home():
    return jsonify({
        "status": "Online ✅",
        "project": "Supply Chain Disruption Assistant & Fleet Utilisation Optimizer",
        "powered_by": "IBM Bob AI",
        "endpoints": {
            "1_disruption": "GET/POST /api/disruption?event=Port Strike in Rotterdam",
            "2_fleet": "GET/POST /api/fleet",
            "3_cold_chain": "GET/POST /api/cold-chain"
        }
    })


@app.route('/api/disruption', methods=['GET', 'POST'])
def analyze_disruption():
    if request.is_json:
        data = request.json
    else:
        data = {"disruption_event": request.args.get('event', 'Unknown disruption')}

    prompt = f"""
    Current Shipments: {json.dumps(MOCK_SHIPMENTS)}
    Active Disruption: {data.get('disruption_event')}
    Task: Identify which shipments are affected and recommend re-routing alternatives.
    """
    result = call_bob_ai(prompt)
    return jsonify({"analysis": result})


@app.route('/api/fleet', methods=['GET', 'POST'])
def optimize_fleet():
    prompt = f"""
    Fleet Assets: {json.dumps(MOCK_FLEET)}
    Current Shipment Needs: {json.dumps(MOCK_SHIPMENTS)}
    Task: Identify idle fleet assets and suggest redeployment for overloaded routes.
    """
    result = call_bob_ai(prompt)
    return jsonify({"optimization": result})


@app.route('/api/cold-chain', methods=['GET', 'POST'])
def monitor_cold_chain():
    iot_log = "Sensor T-998: Temp 8C (Threshold 2-8C). Duration: 2 hours."
    target_shipment = [s for s in MOCK_SHIPMENTS if s['id'] == 'SHIP-002']
    prompt = f"""
    IoT Sensor Log: {iot_log}
    Shipment Context: {json.dumps(target_shipment)}
    Task: Detect temperature excursions and classify regulatory severity before delivery.
    """
    result = call_bob_ai(prompt)
    return jsonify({"cold_chain_status": result})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)