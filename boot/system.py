# system.py
# Loads the full kernel and hands off control to syscall interface

def start_kernel():
    print("System: Handing control to SysCall Interface...")
    from kernel.syscall_interface import handle_prompt
    handle_prompt("Hello, LifeOS")
