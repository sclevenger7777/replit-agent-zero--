import yaml

class Agent:
    def __init__(self, name, role, description):
        self.name = name
        self.role = role
        self.description = description

    def run(self, input_text):
        return f"[{self.name} ({self.role})]: {input_text}"

def load_agents(config_path="config.yaml"):
    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)
            agents_data = config.get("agents", [])
            agents = [
                Agent(agent["name"], agent["role"], agent.get("description", ""))
                for agent in agents_data
            ]
            return agents
    except Exception as e:
        print(f"Error loading agents: {e}")
        return []
