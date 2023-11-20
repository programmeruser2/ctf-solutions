from z3 import * 
def solve(llen, plen):
	login = [BitVec(f'l{i}', 8) for i in range(llen)]
	password = [BitVec(f'p{i}', 8) for i in range(plen)]
	s = Solver()
	las = ZeroExt(24, login[0])
	pas = ZeroExt(24, password[0])
	ls = BitVecVal(0, 32)
	ps = BitVecVal(0, 32)
	f = 1
	for i in range(llen):
		s.add(login[i] >= 97, login[i] <= 122)
		ze = ZeroExt(24, login[i])
		if i >= 1: 
			if f == 1:
				las += ze
			else:
				las -= ze			
			f *= -1
		ls += ze
	f = -1
	for i in range(plen):
		s.add(password[i] >= 97, password[i] <= 122)
		ze = ZeroExt(24, password[i])
		if i >= 1: 
			if f == 1:
				pas += ze 
			else:
				pas -= ze 
			f *= -1
		ps += ze
	#print(las,'|||',pas)
	#print(ls,'|||',ps)
	s.add(las == pas)
	for i in range(llen):
		for j in range(plen):
			s.add(login[i] != password[j])
	for i in range(llen):
		for j in range(llen):
			if i != j: s.add(login[i] != login[j])
	for i in range(plen):
		for j in range(plen):
			if i != j: s.add(password[i] != password[j])
	s.add(ls == ps)
	for i in range(1, plen-2):
		if i % 2 == 1:
			s.add(password[i] >= password[i+2])
		else:
			s.add(password[i] <= password[i+2])
	#s.add(password[0] < password[plen-1])
	s.add(password[0] >= password[plen-1])
	if s.check() != sat:
		return None 
	else:
		login_b = b''
		password_b = b''
		for i in range(plen):
			password_b += bytes([s.model()[password[i]].as_long()])
		for i in range(llen):
			login_b += bytes([s.model()[login[i]].as_long()])
		return (login_b, password_b)
for a in range(5, 8+1):
	for b in range(5, 8+1):
		print(a,b,solve(a,b))

