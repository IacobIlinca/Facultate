bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start      
global invers_transformare  

; declare external functions needed by our program
extern exit,printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
import printf msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; numar db 23
    ; format db "%s", 0
    zece db 10
    
    
; our code starts here
segment code use32 class=code
    invers_transformare:
    ; esp-adresa de revenire
    ; esp+4-adresa numarului de transformat
    ;numarul transformat e returnat in eax
    
    
    mov eax, [esp+4]          ;eax=numarul
    mov ecx, 0
    mov edi,0
    cld
        
    repeta3:
        push eax
        pop ax
        pop dx
        
        div byte [zece]
        mov edx, 0
        mov dl,al
        mov al, ah
        add al, "0"
        stosb
        mov eax, 0
        mov eax, edx
        inc ecx
        
        cmp eax, 0
        je afara
        
        jmp repeta3
        
    afara:
        mov eax, edi
    ret

    ; start:
        ; push dword numar
        ; call invers_transformare
        ; add esp, 4
            
        ; push dword edi
        ; push dword format
        ; call [printf]
        ; add esp ,4*2
        
    
        ; ; exit(0)
        ; push    dword 0      ; push the parameter for exit onto the stack
        ; call    [exit]       ; call exit to terminate the program
