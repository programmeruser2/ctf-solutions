[bits 64]
file_load_va: equ 0x400000
db 0x7f, 'E', 'L', 'F' 
db 2 
db 1 
db 1
db 0
dq 0
dw 2
dw 0x3e
dd 1
dq 0x0 ; entry point 
dq program_headers_start
; Section header offset. We don't have any sections, so set it to 0 for now.
dq 0
dd 0
dw 64
dw 0x38
dw 1
; Size of a section header entry.
dw 0x40
; Number of section header entries. Now 0, since we don't have them.
dw 0
; The section containing section names. Not used anymore, so set to 0.
dw 0

program_headers_start:
dd 0x3 
dd 0x4 
dq interp 
dq interp + file_load_va ; p_vaddr 
dq interp + file_load_va ; p_paddr 
dq 0x9 
dq 0x9 
dq 0x8 
interp: db "./python", 0

file_end:

