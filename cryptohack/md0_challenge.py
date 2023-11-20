from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
#from utils import listener


FLAG = "crypto{???????????????}"


def log(e):
    with open('/tmp/err.txt', 'a') as f:
        f.write(str(e)+'\n')
def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def hash(data):
    data = pad(data, 16)
    out = b"\x00" * 16
    log('-----start-----')
    for i in range(0, len(data), 16):
        blk = data[i:i+16] 
        log(str(blk)+' '+str(out))
        out = bxor(AES.new(blk, AES.MODE_ECB).encrypt(out), out)
    log('result '+str(out))
    return out


class Challenge():
    def __init__(self):
        self.before_input = "You'll never forge my signatures!\n"
        #self.key = os.urandom(16)
        self.key = b'.'*16

    def challenge(self, msg):
        if "option" not in msg:
            return {"error": "You must send an option to this server."}

        elif msg["option"] == "sign":
            data = bytes.fromhex(msg["message"])
            if b"admin=True" in data:
                return {"error": "Unauthorized to sign message"}
            sig = hash(self.key + data)

            return {"signature": sig.hex()}

        elif msg["option"] == "get_flag":
            sent_sig = bytes.fromhex(msg["signature"])
            data = bytes.fromhex(msg["message"])
            real_sig = hash(self.key + data)
            log('real_sig '+str(real_sig))
            if real_sig != sent_sig:
                return {"error": "Invalid signature"}

            if b"admin=True" in data:
                return {"flag": FLAG}
            else:
                return {"error": "Unauthorized to get flag"}

        else:
            return {"error": "Invalid option"}


"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""
#listener.start_server(port=13388)
import sys 
#sys.stderr = sys.stdout
c = Challenge()
print(c.before_input, end='')
from json import loads, dumps
while True:
    try:
        x = loads(input())
        print(dumps(c.challenge(x)))
    except Exception as e:
        log(e) 
        print('error, appended to /tmp/err.txt')
        exit(1)

