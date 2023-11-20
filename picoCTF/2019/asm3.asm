section .text
extern printf
extern exit
global _start
; nasm -f elf32 -o asm3.o asm3.asm
; ld -m elf_i386 -dynamic-linker /lib/ld-linux.so.2 -o asm3 -lc asm3.o
_start:
    push 0xe54409d5
    push 0xe6cf51f0
    push 0xd2c26416 
    call asm3
    add esp, 12
    push eax
    push fmt
    call printf
    add esp, 8
    push 0x00
    call exit
asm3:
    push   ebp
    mov    ebp,esp
    xor    eax,eax
    mov    ah,BYTE [ebp+0x9]
    shl    ax,0x10
    sub    al,BYTE [ebp+0xe]
    add    ah,BYTE [ebp+0xf]
    xor    ax,WORD [ebp+0x12]
    nop
    pop    ebp
    ret

section .data
    fmt: db "0x%x", 0xa, 0x00

