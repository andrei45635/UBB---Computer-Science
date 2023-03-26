bits 32 
global start        


extern exit, fopen, fprintf, printf, scanf, fclose, fread                
import exit msvcrt.dll    
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll 
import scanf msvcrt.dll
import fread msvcrt.dll 

;Se da un fisier text. Sa se citeasca continutul fisierului, 
;sa se contorizeze numarul de cifre pare si sa se afiseze aceasta valoare
;Numele fisierului text este definit in segmentul de date.
segment data use32 class=data

    nume_fisier db 'practice3.txt', 0 
    mod_acces db 'r', 0
    descriptor dd -1 
    format_pare db 'Numarul de cifre pare este %d',0
    len_fisier equ 100 
    text_fisier times (len_fisier+1) db 0 
    cifra dd 0
    buffer resb len_fisier
    nr_car_citite dd 0 
    
segment code use32 class=code
    start:
    
        ;opening fisierul practice3.txt 
        ;eax = fopen(nume_fisier, mod_acces)
        ;functia va returna 0 daca nu a mers operatia de opening 
        push dword mod_acces
        push dword nume_fisier
        call [fopen] 
        add esp, 4*2
        
        
        ;punem in eax descriptorul 
        mov [descriptor], eax 
        
        cmp eax, 0 
        je final
    
        ;refacem citirea folosind bucla 
        ; echivalentul in pseudocod al urmatoarei secvente de cod este:
        ;repeta
        ;   nr_car_citite = fread(buffer, 1, len, descriptor_fis)
        ;   daca nr_car_citite > 0
        ;       ; instructiuni pentru procesarea caracterelor citite in aceasta etapa
        ;pana cand nr_car_citite == 0
        ; bucla:
            ; push dword [descriptor]
            ; push dword len_fisier
            ; push dword 1 
            ; push dword buffer 
            ; call [fread]
            ; add esp, 4*4 ;in EAX avem numarul de caractere citite
            
            ; cmp eax, 0
            ; je cleanup
            
            ; mov [nr_car_citite], eax 
            
                ; mov ecx, len_fisier 
                ; mov esi, text_fisier
            ; repeta:
                ; lodsb ;punem in eax fiecare element 
                ; test al, 1b ;verificam daca numarul din eax este par 
                ; jnz look_again
                ; inc ebx 
            ; look_again:
                ; loop repeta 
            ; mov [cifra], ebx 
            
            ; jmp bucla 
        
        
        ;citim textul folosind functia fread
        ;eax = fread(text_fisier, 1, len_fisier, descriptor)
        push dword [descriptor]
        push dword len_fisier
        push dword 1
        push dword text_fisier
        call [fread]
        add esp, 4*4 ;in EAX avem numarul de caractere citite 
        
        
         mov ecx, eax
         mov esi, text_fisier
      repeta:
         lodsb ;punem in eax fiecare element 
         test al, 1b ;verificam daca numarul din eax este par 
         jnz look_again
         inc ebx 
      look_again:
          loop repeta 
          
          mov [cifra], bl 
        
        ;printf(format_pare, cifra)
        push dword [cifra]
        push dword format_pare
        call [printf]
        add esp, 4*2
        
    ;cleanup:
        ;inchidem fisierul folosind fclose 
        ;eax = fclose(descriptor)
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
    final:
        push    dword 0      
        call    [exit]       
