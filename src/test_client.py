import requests

BASE = "http://127.0.0.1:5000"

print("Testing home...")
r = requests.get(f"{BASE}/")
print(" ", r.status_code, r.json())

print("Testing fleet...")
r = requests.get(f"{BASE}/api/fleet")
print(" ", r.status_code, r.json())

print("Testing cold chain...")
r = requests.get(f"{BASE}/api/cold-chain")
print(" ", r.status_code, r.json())

print("Testing disruption (POST)...")
r = requests.post(f"{BASE}/api/disruption", json={"disruption_event": "Port Strike in Rotterdam"})
print(" ", r.status_code, r.json())