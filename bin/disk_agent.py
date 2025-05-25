# agents/disk_agent.py
import shutil

class DiskAgent:
    def run(self):
        total, used, free = shutil.disk_usage("/")
        return (
            f"Disk Usage:\n"
            f"Total: {total // (2**30)} GB\n"
            f"Used: {used // (2**30)} GB\n"
            f"Free: {free // (2**30)} GB"
        )
