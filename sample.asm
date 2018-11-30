section .data
	a dd 5
	b dd 10
	c dd 10,50
	d dd 20
	msg db 'Nihal'

section .bss
	s1 resd 3
	s2 resb 1
	s3 resd 3
section .text
	global main
	extern printf
main:
	mov eax,a
	mov ebx,eax
	mov ecx,12
	mov eax,14
	mov edx,12
	mov eax,13
	add edi,dword[msg]
	mov eax,d
	mov eax,ecx
	mov ebp,esi
	mov edx,eax
	mov eax,dword[a]
