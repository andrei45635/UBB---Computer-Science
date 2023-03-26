bits 32 
global start        

extern exit, printf, scanf, fopen, fclose, fprintf               
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll

;Sa se citeasca de la tastatura un nume de fisier si un text (definite in segmentul de date). 
;Textul contine litere mici, litere mari, cifre si caractere speciale. Sa se inlocuiasca toate spatiile din textul dat cu caracterul 'S'. 
;Sa se creeze un fisier cu numele dat si sa se scrie textul obtinut prin inlocuire in fisier.
segment data use32 class=data
   
   create_fisier_nume db 'Introduceti numele fisierului= ', 0
   read_text db 'Introduceti textul= ', 0
   format_read_text db '%s', 0
   format_create_fisier db '%s', 0
   nume_fisier db 0
   mod_acces db 'w', 0
   descriptor dd -1
   text db 0
   len_text equ $-text 
   result_text times len_text db 0
   msg_err db 'Eroare la deschiderea fisierului wai boule', 0
   
segment code use32 class=code
    start:
        ;printf(create_fisier_nume)
        push dword create_fisier_nume
        call [printf]
        add esp, 4
        
        ;scanf(format_create_fisier, nume_fisier)
        push dword nume_fisier
        push dword format_create_fisier
        call [scanf]
        add esp, 4*2
        
        ;eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4*2 
        
        mov [descriptor], eax 
        cmp eax, 0
        je err_ 
        
    repeta:
        
        ;printf(read_text)
        push dword read_text
        call [printf]
        add esp, 4
        
        ;scanf(format_read_text, text)
        push dword text 
        push dword format_read_text
        call [scanf]
        add esp, 4*2
        
        mov ecx, eax 
        jecxz final  
        mov esi, text 
        mov edi, result_text
        repeating:
            lodsb ;in AL avem primul caracter samd 
            cmp al, 20h ;comparam daca ce e in AL e spatiu 
            jne again
            mov al, 20h
        again:
            loop repeating 
            
        ;eax = fprintf(descriptor, result_text)
        push dword result_text
        push dword [descriptor]
        call [fprintf]
        add esp, 4*2
        
    cleanup:
        ;eax = fclose(descriptor)
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
    err_:
        ;eax = printf(msg_err)
        push dword msg_err
        call [printf]
        add ESP, 4*1
        
    final:
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
