bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s1 db 7, 3, 9, 1, 5
    s2 db 2, 4, 6, 8, 10
    len equ $-s1
    len equ $-s1
    d times len db 0
    
; Se dau 2 siruri de numere intregi s1 si s2 de lungimi egale.
; Se cere sirul de numere intregi d obtinut astfel:
; - d[i] = s1[i] - s2[i], daca s1[i] > s2[i]
; - d[i] = s2[i] - s1[i], altfel.
segment code use32 class=code
    start:
        mov ecx, len    ;punem in ecx lungimea sirului s pentru a realiza ciclarea de atatea ori
        jecxz sfarsit
        mov esi, 0
        mov edi, 0
        mov ebx, 0
  
    repeta:
        mov al, [s1+esi]
        mov cl, [s2+ebx]
        inc esi
        inc ebx
        ja mare
        
        sub cl, al
        mov [d+edi], cl
        inc edi
        jmp final_altfel
        
  
        
        
    start:
        mov ecx, len
        jecxz final
        mov esi,0
        mov edi, 0
    repeta:
        mov al, [s1+esi]
        mov ah, [s2+esi]
        cmp al, ah
        ja mare
        
        sub ah, al
        mov [d+edi], ah
        jmp mai_departe
        
    mare:
        sub al, ah
        mov [d+esi], 
        
        
    mai_departe:
        inc edi
    
        
    loop repeta
    
    sfarsit ;terminarea programului
        
        
        
        
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
