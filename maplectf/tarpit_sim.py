from tarpit_data import code 
from pwn import * 
do_check = False 
regs = [0, 0]
pc = 0
pc_regbig = None 
pc_regsmall = None 
reg_index = None 
store_type = None
counter = 0
reg0_neq_0 = None
inp=b'maple{'+b'a'*(16-7)+b'}'
while True:
    while True:
        while True:
            counter += 1
            if do_check:
                print('check', regs[1], 0x1f)
                exit(0)
            ins = u32(code[pc*5:pc*5+4])
            print('pc=',pc, 'ins=',hex(ins), 'regs=',regs)
            pc_regbig = (ins >> 8)&0xffff
            pc_regsmall = (ins >> 0x18) + (code[pc*5+4] << 8)
            store_type = (ins&0xff)>>2 
            reg_index = ((ins&0xff)>>1)&1 
            if store_type != 2: break 
            print('reg[',reg_index,']=','input[', regs[ins&0x1], ']')
            regs[reg_index] = inp[regs[ins&0x1]]
            #if counter==1:reg0_neq_0=True
            #else:reg0_neq_0=False
            pc = pc_regsmall 
            print('pc=',pc)
        if store_type < 3: break 
        do_check = True 
    if store_type == 0:
        print('reg[',reg_index,']+=1')
        regs[reg_index]+=1
        pc = pc_regsmall
    else:
        if store_type != 1: 
            print('docheck=true')
            do_check = True 
        else:
            #print(f'if regs[{reg_index}]==0')
            #print('    pc=',pc_regbig)
            #print('else')
            #print(f'    regs[{reg_index}]-=1')
            #print('    pc=',pc_regsmall)
            #if reg0_neq_0:
            if regs[0] == 0:
                print('pc=',pc_regbig)
                pc = pc_regbig 
            else:
                print(f'regs[{reg_index}]-=1')
                print('pc=',pc_regsmall)
                regs[reg_index]-=1
                pc = pc_regsmall
            

