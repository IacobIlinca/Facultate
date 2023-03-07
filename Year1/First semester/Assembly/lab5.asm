bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s1 db 'a', 'b', 'c', 'd', 'e', 'f'
    s2 db '1', '2', '3', '4', '5'
    len1 equ $-s1
    len2 equ $-s2
    d times len1+len2 db 0
    
    
;Se dau doua siruri de caractere S1 si S2. 
;Sa se construiasca sirul D prin concatenarea elementelor de pe pozitiile pare din S2 cu elementele de pe pozitiile impare din S1.
segment code use32 class=code
    start:
        mov ecx, len2    ;punem in ecx lungimea sirului s2 pentru a realiza ciclarea de atatea ori
        jecxz sfarsit2
        mov esi, 0
        mov edi, 0
  
    repeta:
        mov al, [s2+esi]
        inc esi
        test esi, 01h       ;ZF=1 daca nr e par          ZF=0 daca nr e impar
        jz par
        
        jmp final_impar
        
    par:
        mov [d+edi], al
        inc edi
        
    final_impar
    
    loop repeta
    sfarsit2
    
    
    mov ecx, len1    ;punem in ecx lungimea sirului s1 pentru a realiza ciclarea de atatea ori
        jecxz sfarsit
        mov esi, 0
        mov edi, 0
  
    repeta:
        mov al, [s1+esi]
        inc esi
        test esi, 01h       ;ZF=1 daca nr e par          ZF=0 daca nr e impar
        jz impar
        
        jmp final_par
        
    impar:
        mov [d+edii], al
        inc edi
        jmp final_impar
        
    final_par
  
        
    loop repeta
    
    
    
    
    
    
    sfarsit ;terminarea programului
        
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
