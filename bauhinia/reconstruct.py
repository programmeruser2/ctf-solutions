info = [
    (2,10),
    (3,27),
    (4,6),
    (6,16),
    (7,22),
    (8,19),
    (9,5),
    (10,2),
    (11,26),
]
slen = max([i[0] for i in info])+1
slist = ['?']*slen
for i in info:
    slist[i[0]] = chr(ord('A') + i[1] - 2)
flag = f'b6actf{{{"".join(slist)}}}'
print(flag)
# b6actf{??IZE?OURDAY}
# -> b6actf{SEIZEYOURDAY}
