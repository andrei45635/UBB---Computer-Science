bits 32 
global start        

extern minim 
extern exit, fopen, fclose, scanf, fprintf, printf        
import exit msvcrt.dll  
import fopen msvcrt.dll
import fclose msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll

;Se citeste de la tastatura un sir de numere in baza 10, cu semn. 
;Sa se determine valoarea minima din sir si sa se afiseze 
;in fisierul min.txt (fisierul va fi creat) valoarea minima, in baza 16.
segment data use32 class=data
    n dd 0
    x dd 0
    sir times 100 dd 0
    format_citire db 'Introduceti numarul elementelor= ', 0
    citire db '%d', 0
    format_sir db 'Introduceti elementul= ', 0
    string db '%s', 0
    format_hexa db 'Cel mai mic element in baza 16 este: ', 0
    rezultat db '%x', 0
    descriptor dd -1 
    nume_fisier db 'min.txt', 0
    mod_acces db 'w', 0
    
segment code use32 class=code
    start:
        ;create file 
        ;eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        
        mov [descriptor], eax 
        
        cmp eax, 0
        je final
        
        ;printf(string, format_citire)
        push dword format_citire
        push dword string 
        call [printf]
        add esp, 4*2
        
        ;scanf(citire, n)
        push dword n
        push dword citire 
        call [scanf]
        add esp, 4*2
        
        ;citim de la tastatura
        mov edi, sir 
        mov ebx, [n] 
    repeta: 
        ;printf(string, format_sir)
        push dword format_sir
        push dword string
        call [printf]
        add esp, 4*2
        
        ;scanf(citire, n)
        push dword x
        push dword citire 
        call [scanf]
        add esp, 4*2
        
        mov eax, [x]
        stosd
        dec ebx
        cmp ebx, 0
    ja repeta 
        
        ;eax = minim(sir, n, rezultat)
        push dword 0          ;ESP = ESP + 12
        push dword [n]        ;ESP = ESP + 8
        push dword sir        ;ESP = ESP + 4
        call minim 
        pop dword [x]
        
        ;fprintf(descriptor, format_hexa)
        push dword format_hexa
        push dword [descriptor]
        call [fprintf]
        add esp, 4*2 
        
        ;fprintf(descriptor, rezultat, x)
        push dword [x]
        push dword rezultat
        push dword [descriptor]
        call [fprintf]
        add esp, 4*3
        
        ;close file 
        ;fclose(descriptor)
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
    final:
        push    dword 0      
        call    [exit]       
