# agents/uptime_agent.py
import os

class UptimeAgent:
    def run(self):
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
        hours = uptime_seconds // 3600
        minutes = (uptime_seconds % 3600) // 60
        return f"System Uptime: {int(hours)}h {int(minutes)}m"
