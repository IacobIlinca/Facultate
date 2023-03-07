bits 32 
global _citire
extern _scanf

segment data use32 class=data
    format db "%s",0
segment code public use32 class=code 
    _citire:
        ;functia citeste cele 3 siruri de la tastatura
        ;_citire(sir1,sir2,sir3)
        ;ebp-adresa revenire
        ;ebp+4-adresa sir3
        ;ebp+8-adresa sir2
        ;ebp+12-adresa sir1

        push ebp
        mov ebp,esp
        
        mov eax, [ebp+12]
        mov ebx, [ebp+8]
        mov ecx, [ebp+4]
        
        push dword eax
        push dword format
        call _scanf
        add esp, 4*2
        
        push dword ebx
        push dword format
        call _scanf
        add esp, 4*2
        
        push dword ecx
        push dword format
        call _scanf
        add esp, 4*2
        
        mov esp, ebp
        pop ebp
        ret
 