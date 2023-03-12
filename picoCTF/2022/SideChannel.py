import os
import time
def find_digit(prefix):
	maxtime = -1 # small value that will never be achieved
	maxtimedigit = None
	for i in range(0, 9+1):
		start = time.time()
		os.system(f'echo {prefix + str(i) + ("0" * (8-len(prefix)-1))} | /tmp/pin_checker')
		elapsed = time.time() - start
		if elapsed > maxtime:
			maxtime = elapsed
			maxtimedigit = i
	return maxtimedigit
pin = ''
for i in range(8):
	pin += str(find_digit(pin))
	print("pin=",pin)
print(pin)
