# setup.py
# Sets up environment, memory, identity, I/O config before handing off to kernel

def configure_environment():
    print("Setup: Loading personality config, initializing memory map...")
    # Proceed to kernel
    from system import start_kernel
    start_kernel()
