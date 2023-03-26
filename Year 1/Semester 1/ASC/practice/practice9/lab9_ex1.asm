bits 32
global start

extern exit, scanf, printf, gets
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import gets msvcrt.dll

segment data use32 class=data
    max_len equ 50
    sir times max_len + 1 db 0 ;max_len adauga un bit care va fi mereu 0 ca sa incheiem sirul
    message db "Introduceti propozitia: ", 0
    ;format_citire db "%s", 0
    format_citire db "%50[0-9a-zA-Z \.?]", 0 
    ;expresia %50[0-9a-zA-Z \.?] reprezinta: vreau sa citesc max_len de caractere (50 adica), si vreau sa citesc cifre, litere mici/mari, spatii si punct(.), dar trb sa sa punem \. ca sa nu fie conflict  
    format_afisare db "sirul citit este: %s", 0
    
    
; Cititi de la tastatura si afisati o propozitie
; (mai multe siruri de caractere separate prin SPATII si care se termina cu caracterul '.')
segment code use32 class=code
    start:
        ;facem printf(message)
        push dword message ;pe stiva punem adresa string-ului message
        call [printf] ;apelam functia printf 
        add esp, 4 ;eliberam parametrii de pe stiva

        
        ; ;apelam gets(sir)
        ; push dword sir 
        ; call [gets]
        ; add esp, 4
        
        ;apelam scanf(format, sir)
        push dword sir
        push dword format_citire
        call [scanf]
        add esp, 4*2
        
        ;apelam printf(format_afisare, sir)
        push dword sir 
        push dword format_afisare
        call [printf]
        add esp, 4*2
        
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
