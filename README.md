# polyShellGen
Linux/x64 - execve(/bin/sh) + Custom Encoded XOR + Polymorphic Shellcode (Generator) (Size: <60 bytes)

## Overview
A minimized and polymorphic version of the x64 execve(/bin/sh) shellcode generator. 

This is an updated and optimized version of the original script by **0x4ndr3** (Exploit-DB 43955), refactored to achieve a smaller footprint (<60 bytes) with custom XOR encoding.

* Original script: [Exploit-DB 43955](https://www.exploit-db.com/shellcodes/43955)
* Created with the assistance of AI.

---

## Usage
Run the script to generate the shellcode:
```bash
python3 polyshellgen.py
