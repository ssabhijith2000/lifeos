# agents/cpu_agent.py
import os

class CPUAgent:
    def run(self):
        with open("/proc/cpuinfo", "r") as f:
            lines = f.readlines()
        info = [line for line in lines if "model name" in line or "cpu cores" in line]
        return "\n".join(info[:2])
