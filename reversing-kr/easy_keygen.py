from pwn import xor
serial = bytes.fromhex('5B134977135E7D13')
xor_key = b'\x10 0'
print(xor(serial, xor_key).decode())
