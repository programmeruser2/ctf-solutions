code = open('password_checker.smol', 'rb').read()
if code[:4] != b'SMOL':
    print('invalid format')
    exit(1)
code = code[4:]
for i in range(0, len(code), 4):
    op = code[i]
    addr1 = hex(code[i+1])
    addr2 = hex(code[i+2])
    imm = hex(code[i+3])
    print(hex(code[i]), addr1, addr2, imm, ': ', end='')
    if op == 0:
        print(f'*{addr1} = *{addr2}')
    elif op == 1 or op == 2:
        print(f'*{addr1} += *{addr2} + {imm}')
    elif op == 3:
        print(f'print *{addr1}')
    elif op == 4:
        print(f'*{addr1} = {imm}')
    elif op == 5:
        print(f'*((long)(*0x18) + 8) = *{addr2}')
    elif op == 6:
        print(f'*{addr1} = *(*0x18)', end=', ')
        print(f'*0x18 -= 8')
    elif op == 7:
        print(f'*0x10 = *{addr1} - *{addr2}')
    elif op == 8:
        print(f'if *0x10 == 0: pc += (*{addr2} * 0x100) + {imm}')
    elif op == 9:
        print(f'print_bytes 0x18, count={imm}')
    elif op == 10:
        print(f'*{addr1} = (*{addr1} * *{addr2}) + {imm}')
    elif op == 0xb:
        print(f'*{addr1} += {imm}')
    elif op == 0xc:
        print(f'exit 0')
    elif op == 0xd:
        print(f'input *{addr1}')
    else:
        print('invalid')

