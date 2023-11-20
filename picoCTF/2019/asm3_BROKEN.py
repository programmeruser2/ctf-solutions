from pwn import p32
# Broken, use asm3.asm instead
a1 = 0xd2c26416 
a2 = 0xe6cf51f0 
a3 = 0xe54409d5 
mem = p32(a1)+p32(a2)+p32(a3)
print(mem.hex())
ax = 0 
print(hex(ax))
ax = mem[0x9-0x8]<<8
print(hex(ax))
ax <<= 0x10 
print(hex(ax))
ax = ax-(ax&0xff)+(((ax&0xff)-mem[0xe-0x8])%256)
print(hex(ax))
ax = ax-((ax>>8)&0xff)+(((ax>>8)&0xff)+mem[0xf-0x8])%256
print(hex(ax))
ax ^= mem[0x12-0x8]+mem[0x12-0x8+1]<<8
print('final', hex(ax))


