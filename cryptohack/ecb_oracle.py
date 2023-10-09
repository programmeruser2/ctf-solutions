import requests 
from string import printable
BLOCK_SIZE = 16
from tqdm import tqdm
def encrypt(pt):
    while True:
        try:
            r = requests.get('https://aes.cryptohack.org/ecb_oracle/encrypt/'+pt.hex()+'/')
            return bytes.fromhex(r.json()['ciphertext'])
        except BaseException as e:
            if type(e) == KeyboardInterrupt: exit(0)
            print(e, r.text)

known = b'crypto{p3n6u1n5_'
block_n = 1
while not b'}' in known:
    # leak each block individually and pray there's not too much trash at the end
    tmp = b''
    for i in tqdm(range(0, 16)):
        payload = b'\x00'*(16-i-1)
        if block_n > 0:
            #payload += known[:i+1]
            pass
        if len(payload) == 0:
            payload = b'\x00'*16
            block_n += 1
        #print(payload, len(payload))
        ct = encrypt(payload)
        #print(block_n, ct)
        block = ct[16*block_n:16*(block_n+1)]
        # block = 00 (16-i-1 times) + tmp + unknown byte
        #print(block)
        for b in tqdm(printable.encode(), leave=False):
            if len(known) == 0:
                new_block = payload
                new_block += tmp
            else:
                #new_block = payload
                new_block = known[i+1:16*block_n] + tmp
            new_block += bytes([b])
            #print(new_block, new_block[16*block_n:16*(block_n+1)])
            new_ct = encrypt(new_block)
            #print(new_block,payload)
            #print(new_ct,block)
            #print(new_block, new_ct, block)
            if new_ct[0:16] == block:
                tmp += bytes([b])
                break
        if b'}' in tmp:
            break
    known += tmp
    print(known) 
print(known)
