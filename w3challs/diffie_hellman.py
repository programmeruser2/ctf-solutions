import requests
import re

s = requests.Session()

r = s.get('https://diffie-hellman.crypto.w3challs.com/challenge_diffie_hellman.php')
match = re.search(r'p =\n(\d+)\n\ng = (\d+)', r.text)
p = int(match.group(1))
g = int(match.group(2))
print(f'{p = }')
print(f'{g = }')

a = 3
A = pow(g,a,p)
print(f'{a = }')
print(f'{A = }')

r = s.post('https://diffie-hellman.crypto.w3challs.com/dhkey.php?type=alice_send_key', data={
    'alice_send_key': f'''[ --------- w3challs-Sniffer 1.4.7 --------- ]

Message from Alice to Bob on 2023/09/03 22:19:07

"Hey Bob, if I don't receive your B in about thirty seconds maximum, I'll consider this channel unsafe

A = {A}"'''
})
B = int(re.search(r"B = (\d+)", r.text).group(1))

secret = pow(B,a,p)
print(f'{B = }')
print(f'{secret = }')

r = s.post('https://diffie-hellman.crypto.w3challs.com/dhkey.php?type=bob_send_key', data={
    'bob_send_key': f'''[ --------- w3challs-Sniffer 1.4.7 --------- ]

Message from Bob to Alice on 2023/09/03 22:24:15

"Hey Alice, here is my B :

B = {B}"'''
})
ct = int(re.search(r"(\d+)\"", r.text).group(1))
print(f'{ct = }')
msg = ct ^ secret
print(f'{msg = }')

r = s.get('https://diffie-hellman.crypto.w3challs.com/solution_diffie_hellman.php?password=' + str(msg))
print(r.text)


