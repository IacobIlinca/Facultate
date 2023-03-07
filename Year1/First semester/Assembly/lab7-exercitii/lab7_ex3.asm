bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s1 dw 1234h, 67abh, 89cdh
    len1 equ $-s1
    s2 dw 2345h, 5678h, 4567h
    len2 equ $-s2
    d times len1 db 0
    
; Se dau doua siruri de cuvinte s1 si s2.
; Se cere sirul de cuvinte d obtinut in interpretarea cu semn, astfel:
; - d[i] = s1[i], daca s1[i] > s2[i]
; - d[i] = s2[i], altfel.
segment code use32 class=code
    start:
        mov ecx, len1 ; nr de elemente din sir
        mov esi, s1 ; incarcare offset s in esi
        mov ebx, s2 ; incarcare offset s in ebx
        mov edi, d ; incarcare offset d in edi
        
        
    
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
