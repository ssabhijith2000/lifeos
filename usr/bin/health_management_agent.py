# agents/health_management_agent.py

import os
from datetime import datetime

class HealthManagementAgent:
    def __init__(self, health_dir="health"):
        self.health_dir = health_dir
        os.makedirs(self.health_dir, exist_ok=True)

    def start(self):
        print("[HealthAgent] Monitoring started.")

    def log_metric(self, category: str, value: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = os.path.join(self.health_dir, f"{category}.log")
        with open(filename, "a") as f:
            f.write(f"{timestamp} - {value}\n")
        return f"[HealthAgent] Logged {category}: {value}"

    def show_history(self, category: str, count: int = 5):
        filename = os.path.join(self.health_dir, f"{category}.log")
        if not os.path.exists(filename):
            return f"[HealthAgent] No data for '{category}' yet."
        with open(filename, "r") as f:
            lines = f.readlines()
        return "".join(lines[-count:])

    def shutdown(self):
        print("[HealthAgent] Monitoring stopped.")
