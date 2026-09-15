# ChainPulse — AI Fleet Optimizer & Cold-Chain Sentinel

> **Bob AI Hackathon 2026 Submission** | **Track:** Open (Problem Statement L2)[cite: 2, 3]

---

## 📌 Problem Statement
Supply chain disruptions from severe weather and transit bottlenecks cascade across active freight routes, leaving operators with blind spots[cite: 3]. Fleet capacity sits idle in adjacent hubs while high-priority corridors face massive delays[cite: 3]. Simultaneously, sensitive cold-chain shipments (such as vaccines and biologics) experience undetected temperature excursions, leading to catastrophic product loss discovered only at the delivery dock[cite: 3].

## 💡 Solution Overview
ChainPulse is an intelligent supply chain copilot powered by **IBM Bob**. It continuously:
1. Cross-references live route disruptions with active shipments[cite: 3].
2. Identifies idle fleet containers and trucks to orchestrate dynamic re-routing[cite: 3].
3. Analyzes streaming cold-chain IoT telemetry to detect thermal excursions and grade regulatory severity prior to delivery[cite: 3].

## 🚀 Key Features
* **Active Disruption Mapping:** Automatically flags at-risk shipments intersecting severe route hazards[cite: 3].
* **Fleet Utilization Optimizer:** Scans underutilized assets to suggest carrier swaps and redeployment routes[cite: 3].
* **Cold-Chain Excursion Sentinel:** Audits IoT sensor time-series to catch temperature breaches early[cite: 3].
* **IBM Bob MCP Architecture:** Uses Model Context Protocol (MCP) tools to empower Bob to inspect telemetry and dispatch plans[cite: 1].

## 🛠️ Tech Stack
* **AI Agent:** IBM Bob (Rules, MCP Tools, Subagent Execution)[cite: 1]
* **Backend:** Python (FastAPI / FastMCP)
* **Frontend:** Interactive Web Dashboard (HTML5, TailwindCSS, JavaScript)
* **Data Layer:** Mock IoT time-series telemetry (JSON/CSV), OpenWeather/Hazard feeds[cite: 3]

## 🏃 Quick Start
Refer to [`docs/setup-guide.md`](docs/setup-guide.md) for full reproduction instructions.

```bash
# 1. Clone repo
git clone https://github.com/manangundigara/bob-ai-hackathon--RM3Technical-.git
cd bob-ai-hackathon--RM3Technical-

# 2. Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies & run
pip install -r src/requirements.txt
python src/app.py