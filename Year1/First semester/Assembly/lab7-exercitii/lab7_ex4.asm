bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s dd 11234456h, 22345567h, 33456678h
    
    d times len db 0

segment code use32 class=code
    start:
        
        
        
        
        jecxz final
        salt daca e 0
        
         
        final:
        
        
        
        
    
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
