bits 32 
global start   
extern exit, fopen, fread, fprintf, printf, fclose             ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import fopen msvcrt.dll
import fread msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

;6: Se da un fisier text. Sa se citeasca continutul fisierului, sa se determine cifra cu cea mai mare frecventa si sa se afiseze acea cifra impreuna cu frecventa acesteia. Numele fisierului text este definit in segmentul de date.

segment data use32 class=data
    nume_fis db "input.txt", 0   ; numele fisierului care va fi deschis
    mod_acces db "r", 0          ; modul de deschidere a fisierului - 
                                 ; r - pentru scriere. fisierul trebuie sa existe 
    descriptor_fis dd -1         ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
    len equ 100                  ; numarul maxim de elemente citite din fisier.                            
    text times len db 0          ; sirul in care se va citi textul din fisier 
    nr_citite dd 0               ;cate caractere s-au citit din fisier
    frecventa times 10 dd 0       ;vectorul de frecventa pe cifre
    max dd 0                     ;numarul maxim de aparitii al unei cifre citite
    cifra dd 0                   ;cifra cu numarul maxim de aparitii
    format_afisare dd "Cifra cu cea mai mare frecventa este %c, frecventa acesteia este %d.", 0

segment code use32 class=code
    start:    
        ; apelam fopen pentru a deschide fisierul
        ; functia va returna in EAX descriptorul fisierului sau 0 in caz de eroare
        ; eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fis
        call [fopen]
        add esp, 4*2                ;eliberam parametrii de pe stiva
        
        mov [descriptor_fis], eax   ; salvam valoarea returnata de fopen in variabila descriptor_fis
        
        ; verificam daca functia fopen a creat cu succes fisierul (daca EAX != 0)
        cmp eax, 0                      
        je final                        ; daca citirea din fisier nu are succes
        
        ; citim textul in fisierul deschis folosind functia fread
        ; eax = fread(text, 1, len, descriptor_fis)
        push dword [descriptor_fis]
        push dword len
        push dword 1
        push dword text        
        call [fread]
        add esp, 4*4                 ; dupa apelul functiei fread EAX contine numarul de caractere citite din fisier
        
        
        
        ;//////
        mov [nr_citite],eax          ;pt ca in eax e numarul de caractere citite din fisier
        mov ecx,[nr_citite]
        mov esi, text
         
        cld
        
        ;determinarea vectorului de frecventa = "frecventa" 
        repeta_1:
            xor eax,eax
            lodsb                   ;in al avem caract pe care il vf daca e cifra
            
            cmp al, '0'              ;48 este codul ascii al primei cifre din tabel-0
            jb nu_e_cifra
            
            cmp al, '9'
            ja nu_e_cifra
           
            sub al, '0' 
            
            ;mov edi, eax            ;edi-cifra
            inc dword [frecventa + 4*eax] 
            nu_e_cifra:
        loop repeta_1
        
        mov ecx, 9                  ; lungimea vectorului de frceventa=numarul de cifre
        mov edi ,0
        
        
        ;determinam cifra cu frecventa maxima
        repeta_2:
            mov ebx, [max]
            cmp ebx, [frecventa+edi]
            jb nu_e_mai_mare
            ;inc edi
            mov al,[frecventa+edi]
            mov [max], al
            mov edx, edi
            add edx, 48
            mov [cifra], edx   ;cifra=cifra cu nr maxim de aparitii
            inc edi
            nu_e_mai_mare:
            loop repeta_2
            
         mov ecx, 9                  ; lungimea vectorului de frceventa=numarul de cifre
         mov ebx , 0                 ; initializam numarul de aparitii al cifrei cu frecventa maxima cu 0
         mov edi, 0
        ;determinam numarul de aparitii al cifrei cu frecventa maxima
        repeta_3:
            mov edx, [max]
            cmp edx, [frecventa+edi]
            inc edi
            jne nu_sunt_egale
            add ebx, 1
        
            nu_sunt_egale:
            loop repeta_3
            
        ;//////
        
        ;afiseaza cifra cu frecvenat maxima si numarul de aparitii ale acesteia
        push dword [max]
        push dword [cifra]
        push dword format_afisare
        call [printf]
        add esi, 4*3
        
        ; apelam functia fclose pentru a inchide fisierul
        ; fclose(descriptor_fis)
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
        
        
        final:
        
        ; exit(0)
        push    dword 0      
        call    [exit]     