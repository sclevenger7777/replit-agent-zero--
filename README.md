# replit-agent-zero--
"Agent Zero CLI+ Web interface for Replit"
# 🧠 Agent Zero: Replit Edition

**Agent Zero** is a modular, multi-agent privacy guardian and tool orchestrator designed to run fully inside **Replit** or any standard **Windows/Linux environment** — no Termux, root access, or mobile setup required.

This version is adapted from the original Android+Termux-based Agent Zero project and is simplified for ease of use, learning, and future expansion.

---

## 🚀 Features

- ✅ Modular agent system defined in `config.yaml`
- ✅ Flask-based web API (`web.py`) for agent interaction
- ✅ CLI entrypoint (`main.py`) for local use
- ✅ Dynamic tool discovery with caching (`tool_discovery.py`)
- ✅ Persistent memory using SQLite (`agent_zero_memory.db`)
- ✅ Fully self-contained – ready to run on Replit, GitHub Codespaces, or locally

---

## 🛠️ Setup (One-Click on Replit)

> Click **"Run"** on Replit or follow these steps locally:

```bash
# 1. Clone the repo
git clone https://github.com/sclevenger7777/replit-agent-zero--
cd replit-agent-zero--

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the CLI
python main.py

# or run the Flask API
python web.py
