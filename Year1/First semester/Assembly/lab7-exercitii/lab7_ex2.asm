bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s db 'abcdef'
    len equ $-s
    d times len db 0
    
; Se da un sir de caractere s
; Se cere sirul de caractere d obtinut prin copierea sirului s, folosind instructiuni pe siruri.
segment code use32 class=code
    start:
        mov ECX, len ; nr de elemente din sir
        mov ESI, s ; incarcare offset s in ESI
        mov EDI, d ; incarcare offset d in EDI
        jecxz sfarsit
        std
        Again:
            LODSW
            STOSW
        LOOP Again
        
        sfarsit:
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
