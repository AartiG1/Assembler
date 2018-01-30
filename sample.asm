section .data
	a dd 5,19
	b dd 10,20
	c dd 10
	d dd 20
	e dw 10
	msg db 'sagar'

section .bss
	s1 resb 1
	
section .text
	global main
	extern printf
main:
	mov eax,12
	add ebx,12
	mov eax,ebx
	add ecx,edx
	mov eax,a
	mov ebx,b
	mov ebx,ecx
	add eax,a
	add ebx,b
	mov eax,dword[a]
	mov dword[b],ecx
	mov eax,dword[e]
	mov ecx,12
	mov eax,14
	mov edx,12
	mov eax,13
	mov al,'z'
	mov byte[s1],al
	
	
