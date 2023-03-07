bits 32 
global start        

extern exit, printf, scanf       
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll
;25: Sa se citeasca de la tastatura doua numere a si b (in baza 10) şi să se determine relaţia de ordine dintre ele (a < b, a = b sau a > b). Afisati rezultatul în următorul format: "<a> < <b>, <a> = <b> sau <a> > <b>".
segment data use32 class=data
    x dd 0
    y dd 0
    mesaj_initial db "Introduceti cele doua numere: " , 0
    format db "%d %d",0
    mesaj_mai_mic db "%d < %d", 0
    mesaj_mai_mare db "%d > %d", 0
    mesaj_egale db "%d = %d", 0
    
    
segment code use32 class=code
    start:
        ;mesaj initial: "Introduceti cele doua numere: "
        push dword mesaj_initial
        call [printf]
        add esp, 4*1
        
        ;citirea celor doua numere de la tastatura
        push dword y
        push dword x
        push dword format
        call [scanf]
        add esp, 4*3
        
        mov eax, [x]
        mov ebx, [y]
        cmp eax, ebx
        jg mai_mare
        jl mai_mic
        
        ;daca x=y => se va afisa "<x> = <y>"
        push dword [y]
        push dword [x]
        push dword mesaj_egale
        call [printf]
        add esp, 4*3
        jmp sfarsit
        
        ;daca x>y => se va afisa "<x> > <y>"
        mai_mare:
            push dword [y]
            push dword [x]
            push dword mesaj_mai_mare 
            call [printf]
            add esp, 4*3
            jmp sfarsit
            
        ;daca x<y => se va afisa "<x> < <y>"
        mai_mic:
            push dword [y]
            push dword [x]
            push dword mesaj_mai_mic 
            call [printf]
            add esp, 4*3
            jmp sfarsit
            
        sfarsit:
        push    dword 0    
        call    [exit]     

        