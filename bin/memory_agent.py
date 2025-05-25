# agents/memory_agent.py
import os

class MemoryAgent:
    def run(self):
        with open("/proc/meminfo", "r") as f:
            lines = f.readlines()
        return "".join(lines[:5])  # Return the top 5 lines for summary
