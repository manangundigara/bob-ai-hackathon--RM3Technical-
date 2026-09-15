from flask import Flask, render_template_string
import json

app = Flask(__name__)

# Mock Data: Simulating your supply chain database
fleet_data = [
    {"asset_id": "TRK-101", "status": "Idle", "location": "Ahmedabad Hub", "type": "Reefer (Cold)"},
    {"asset_id": "TRK-102", "status": "Active", "location": "Route 47", "type": "Dry Van"}
]

shipment_data = [
    {"shipment_id": "SC-809", "status": "At Risk", "temp_current": "9°C", "temp_limit": "8°C"},
    {"shipment_id": "SC-810", "status": "On Track", "temp_current": "4°C", "temp_limit": "8°C"}
]

# Simple Dashboard UI
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ChainPulse | RM3Technical</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; padding: 20px; }
        h1 { color: #0f62fe; }
        .card { background: white; padding: 15px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .alert { color: #da1e28; font-weight: bold; }
    </style>
</head>
<body>
    <h1>ChainPulse Logistics & Fleet Monitor</h1>
    
    <div class="card">
        <h2>Active Shipments (Cold-Chain)</h2>
        <ul>
            {% for shipment in shipments %}
                <li>
                    <strong>{{ shipment.shipment_id }}</strong> - 
                    <span class="{% if shipment.status == 'At Risk' %}alert{% endif %}">
                        {{ shipment.status }}
                    </span> 
                    (Current Temp: {{ shipment.temp_current }} | Limit: {{ shipment.temp_limit }})
                </li>
            {% endfor %}
        </ul>
    </div>

    <div class="card">
        <h2>Fleet Availability</h2>
        <ul>
            {% for asset in fleet %}
                <li><strong>{{ asset.asset_id }}</strong> - {{ asset.status }} ({{ asset.location }}) - {{ asset.type }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def dashboard():
    return render_template_string(HTML_TEMPLATE, fleet=fleet_data, shipments=shipment_data)

if __name__ == '__main__':
    # Run the server on port 5000
    print("Starting ChainPulse UI on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)