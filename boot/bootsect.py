# bootsect.py
# Simulates BIOS loading the bootloader (LLM runtime boot entry point)

def load_bootloader():
    print("BIOS: Initializing LLM runtime...")
    # Proceed to setup stage
    from setup import configure_environment
    configure_environment()
