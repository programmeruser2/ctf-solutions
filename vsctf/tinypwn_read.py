import sys
elf = open(sys.argv[1], 'rb').read()

i = 0

sizes = (16, 2, 2, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2)
for x in sizes:
    print(elf[i:i+x])
    i+=x
