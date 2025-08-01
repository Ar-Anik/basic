"""
General computer memory types :

1. Register Memory
Location: Inside the CPU.
Speed: Fastest memory in a computer system.
Purpose: Temporarily holds data being operated on by the CPU (e.g., arithmetic).
Size: Very small (a few bytes or words).
Example Use: When adding two numbers, the operands are first loaded into CPU registers.
Accessed By: CPU instruction set, not by Python directly.

2. Cache Memory
Location: Between CPU and RAM.
Levels:
    * L1: Closest to the core, smallest but fastest.
    * L2: Larger than L1, this memory resource is accessible by multiple CPU cores at the same time. Slower than L1 but faster than L3
    * L3: Largest, shared among all CPU cores. Slower than L1 and L2 but faster than RAM.
Purpose: Stores frequently accessed data to reduce access time from RAM.
Managed By: Hardware (CPU), not manually controlled by OS or Python.
Effect on Python: Improves performance indirectly by caching Python bytecode execution and data access.

3. Main Memory (RAM->Random Access Memory)
Location: System memory (outside CPU).
Purpose: Stores running programs and their working data.
Volatile: Data is lost when the system is powered off.
Python Usage: Python objects (variables, functions, modules) are stored here while running.

4. Virtual Memory
Concept: Maps disk space to RAM to give the illusion of more memory than physically available.
Managed By: Operating System (OS).
Components: Includes swap space or pagefile on disk.
Effect: Slower than RAM, but allows large Python programs to run even when RAM is full.
Python View: Transparent — Python just sees it as more memory, though with performance impact.

5. Persistent Memory (Storage)
Location: HDD, SSD, NVMe.
Non-Volatile: Stores data even after shutdown.
Purpose: Stores Python files (.py, .pyc), modules, packages, databases, and logs.
Not Used For: Active object memory during program execution.

6. Static Memory
Purpose: Holds fixed-size data allocated before runtime.
Examples in Python:
    * Built-in constants like None, True, False.
    * Interned small integers [-5 to 256] and some strings.
Location: Global/static segments in memory layout.
Behavior: These objects are never deleted, exist throughout interpreter lifetime.

7. Buffer Memory
Purpose: Temporarily holds binary or stream data.
Used in Python for:
    * io.BytesIO, file.read(), memoryview, bytearray.
    * Used internally for efficient I/O and network operations.
Benefit: Reduces memory copying for large binary data.

8. ROM (Read-Only Memory)
Location: Hardware-level storage.
Used For: BIOS, firmware, bootloader.
Not Directly Used by Python: But involved during interpreter loading in embedded systems.
"""
