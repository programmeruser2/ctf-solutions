from tarpit_data import code 
from pwn import * 
def parse(pc):
    ins = u32(code[pc*5:pc*5+4])
    pc_retbig = (ins >> 8)&0xffff
    pc_retsmall = (ins >> 0x18) + (code[pc*5+4] << 8)
    store_type = (ins&0xff)>>2 
    reg_index = ((ins&0xff)>>1)&1 
    return dict(ins=ins, pc_retbig=pc_retbig, pc_retsmall=pc_retsmall, store_type=store_type, reg_index=reg_index)
pc = 0 
flag = b''
for i in range(0x1f):
    ins = parse(pc)
    assert ins['store_type'] == 2 
    pc = ins['pc_retsmall']
    fail_ret = parse(pc)['pc_retbig']
    c = 0
    while True:
        ins = parse(pc)
        if ins['pc_retbig'] != fail_ret: 
            flag += bytes([c])
            pc = ins['pc_retbig']
            ins = parse(pc)
            while ins['store_type'] != 2:
                if ins['store_type'] != 1:
                    pc = ins['pc_retsmall']
                    ins = parse(pc)
                else:
                    pc = ins['pc_retbig']
                    ins = parse(pc)
            break
        pc = ins['pc_retsmall']
        c += 1
print(flag)


