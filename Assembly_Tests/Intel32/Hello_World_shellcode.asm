; Author: Pepitoex123
; Purpose: Writing a Hello World shellcode using JMP-POP-CALL technique, and avoiding NULL problems in the machine language interpreter
global _start

section .text

_start:
	jmp short call_shellcode
shellcode:
	xor eax, eax
    mov al, 0x4
    xor ebx, ebx
    mov bl, 0x1
    pop ecx
    xor edx, edx
    mov dl, 13
    int 0x80

	xor eax, eax
    mov al, 0x1
    xor ebx, ebx
    mov bl, 0x5
    int 0x80
call_shellcode:
	call shellcode
    message: db "Hello World!", 0xA
