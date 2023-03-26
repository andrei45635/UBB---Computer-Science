bits 32 
global start        


extern exit, fopen,fclose, fprintf               
import exit msvcrt.dll   
import fopen msvcrt.dll 
import fclose msvcrt.dll
import fprintf msvcrt.dll   


;Se dau un nume de fisier si un text (definite in segmentul de date). 
;Textul contine litere mici, litere mari, cifre si caractere speciale. 
;Sa se transforme toate literele mari din textul dat in litere mici. 
;Sa se creeze un fisier cu numele dat si sa se scrie textul obtinut in fisier.
segment data use32 class=data
   
   nume_fisier db 'practice4.txt', 0 
   mod_acces db 'w', 0
   descriptor dd -1 
   text db 'AnUnTa', 0
   len equ $ - text 
   text_final times len db 0    
   
segment code use32 class=code
    start:
        ;opening file practice4.txt 
        ;eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fisier
        call [fopen] 
        add esp, 4*2 
        
        mov [descriptor], eax 
        
        cmp eax, 0
        je final 
        
        mov ecx, len 
        mov esi, text
        mov edi, text_final 
    repeta: 
        lodsb
        cmp al, 'a' ;comparam codurile ascii ale lui al cu 'a', iar daca
                    ;este mai mare (adica e litera mica) atunci sare la eticheta 
                    ;nope, unde continutul lui al va fi pus in text_final si se va face loop
        ja nope   
        cmp al, 'A' ;comparam codurile ascii ale lui al cu 'A', iar daca este mai mare (adica e litera mare)
                    ;atunci sare la check_again_Z, unde se va compara cu 'Z', iar daca este mai mic (adica e tot litera mare)
                    ;atunci sare la check_again, unde se va face schimbarea uppercase to lowercase 
        ja check_again_Z
    check_again_Z:
        cmp al, 'Z'
        jb check_again
        cmp al, 'z'
        jb nope 
    check_again:
        xor al, 32
    nope:
        stosb
        loop repeta
        
        ;scriem in practice4.txt textul rezultat 
        ;eax = fprintf(descriptor, text) 
        push dword text_final  
        push dword [descriptor] 
        call [fprintf] 
        add esp, 4*2 
        
        ;closing file practice4.txt 
        ;eax = fclose(descriptor)
        push dword [descriptor]
        call [fclose]
        add esp, 4
        
    final:
        push    dword 0      
        call    [exit]       
