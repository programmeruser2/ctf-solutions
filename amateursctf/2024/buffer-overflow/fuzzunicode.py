for i in range(0, 0x10FFFF+1):
    if len(chr(i).upper().encode('utf-8')) > len(chr(i).encode('utf-8')):
        print(i)
        break

