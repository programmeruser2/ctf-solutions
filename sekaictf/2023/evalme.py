from pwn import *
import re

def solve_challenge(challenge):
    match = re.match(r'(\d+) ([+\-*\/]) (\d+)', challenge)
    if not match:
        return None 
    #print(match.groups())
    num1, operation, num2 = match.groups()
    num1 = int(num1)
    num2 = int(num2)
    #num1, num2 = int(numbers[0]), int(numbers[2])
    
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2  # Integer division
    
    return None

# Establish a connection to the server
conn = remote('chals.sekai.team', 9000)
conn.recvline()
conn.recvline()
conn.recvline()
conn.recvline()

# Loop through 100 challenges
for _ in range(100):
    challenge = conn.recvline().decode().strip()
    if not challenge:
        print("Challenge reception timed out.")
        break
    
    print("Challenge:", challenge)

    # Calculate the answer
    answer = solve_challenge(challenge)
    if answer is None:
        print("Invalid challenge format.")
        break

    # Send the answer
    conn.sendline(str(answer).encode())
    print("Answer sent:", answer)
    conn.recvline()

flag = conn.recvline(timeout=2).decode().strip()
if flag:
    print("Flag:", flag)
else:
    print("Flag reception timed out.")
conn.close()

