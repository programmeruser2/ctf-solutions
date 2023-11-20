length = 9
sol = bytearray(length)
s1 = b'W3challs Protection system\x00'
s2 = b'Please enter your password :\x00'

sol[0] = s1[13]-3
sol[1] = s2[14]-6
sol[2] = s1[0]-12
sol[3] = s2[1]+5 
sol[4] = s1[13] - length + 3 
sol[5] = s2[14] - length + 6 
sol[6] = s1[1] + length - 8 
sol[7] = s2[1] - length + 4
sol[8] = s1[4] + length + length + 7 

print(sol)
