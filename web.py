from flask import Flask, jsonify
import yaml
import os
from tool_discovery import discover_tools

app = Flask(__name__)

CONFIG_PATH = "config.yaml"
TOOL_CACHE_PATH = "cache/tools.yaml"

@app.route("/")
def index():
    return jsonify({"status": "Agent Zero is online 🧠"})

@app.route("/discover")
def discover():
    tools = discover_tools(CONFIG_PATH)
    return jsonify({"discovered_tools": tools})

@app.route("/tools")
def tools():
    if os.path.exists(TOOL_CACHE_PATH):
        with open(TOOL_CACHE_PATH, "r") as f:
            tools = yaml.safe_load(f)
        return jsonify({"cached_tools": tools})
    else:
        return jsonify({"error": "No tools found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
