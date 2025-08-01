import shutil
import yaml
import os

def discover_tools(config_path="config.yaml"):
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
    except Exception as e:
        print(f"Error reading config: {e}")
        config = {}

    exclude = config.get("discovery", {}).get("exclude", [])
    cache_path = config.get("discovery", {}).get("cache_path", "cache/tools.yaml")

    tools_to_check = [
        "curl", "wget", "nmap", "git", "python3", "sqlite3", "mitmproxy", "openssl", "ping"
    ]

    available_tools = {}
    for tool in tools_to_check:
        if tool in exclude:
            continue
        path = shutil.which(tool)
        available_tools[tool] = path if path else "Not found"

    # Ensure cache directory exists
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)

    with open(cache_path, "w") as f:
        yaml.dump(available_tools, f)

    return available_tools
