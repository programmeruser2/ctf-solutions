from pwn import *
import json
import base64
import codecs
r = remote('socket.cryptohack.org', 13377)
def respond(data):
    r.sendline(json.dumps({'decoded':data}).encode('ascii'))
for i in range(100):
    data = json.loads(r.recvline().decode('ascii'))
    if data['type'] == 'base64':
        respond(base64.b64decode(data['encoded']).decode('ascii'))
    elif data['type'] == 'hex':
        respond(bytes.fromhex(data['encoded']).decode('ascii'))
    elif data['type'] == 'rot13':
        respond(codecs.encode(data['encoded'], 'rot_13'))
    elif data['type'] == 'bigint':
        respond(bytes.fromhex(data['encoded'][2:]).decode('ascii'))
    elif data['type'] == 'utf-8':
        respond(''.join([chr(i) for i in data['encoded']]))
print(r.recvall())
