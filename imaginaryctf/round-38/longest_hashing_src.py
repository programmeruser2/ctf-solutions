#!/usr/bin/env python3

from hashlib import sha256
from Crypto.Util.number import long_to_bytes, isPrime
from random import getrandbits

flag = open("flag.txt").read()

def sign(m):
    return sha256(m).hexdigest()

def next():
    return getrandbits(1024)

def auth(sig, msg, p):
    if isPrime(msg):
        return "No no no, composites only."
    msg = long_to_bytes(p)
    print(sig, msg, p)
    print(sig, sign(msg))
    print(msg, long_to_bytes(p))
    if sig != sign(msg):
        return "Authentication Failed."
    if msg.startswith(long_to_bytes(p)):
        return f"Welcome admin! Flag is {flag}"
    return "Authentication Successful!"

def menu():
    global p
    print("1. Authenticate")
    print("2. Get p")
    print("3. Show source")
    print("4. Quit")
    x = int(input(">>> "))
    if x == 1:
        m = int(input("Enter message as long: "))
        sig = str(input("Enter string as hexstr: "))
        print(auth(sig,m,p))
    elif x == 2:
        print("Your prime is", p % 2**512)
        print("The signature is", sha256(long_to_bytes(p)).hexdigest())
        p = next()
    elif x == 3:
        print("="*80)
        print(open(__file__).read())
        print("="*80)
    elif x == 4:
        exit()

if __name__ == "__main__":
    p = next()
    while True:
        menu()
