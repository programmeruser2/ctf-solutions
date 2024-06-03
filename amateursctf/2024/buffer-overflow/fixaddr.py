from pwn import *
e=ELF('./chal')
for i in range(128, 256):
    try:
        s=(bytes([i])+p64(e.sym['main'])).decode('utf-8')
    except:
        continue 
    if len(s.upper().encode('utf-8'))==len(s.encode('utf-8')) and s.upper().encode('utf-8')[1:] == p64(e.sym['main']):
        print(i)
        break
