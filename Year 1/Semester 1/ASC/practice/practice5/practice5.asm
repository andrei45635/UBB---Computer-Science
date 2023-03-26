bits 32 
global start        


extern exit, fopen, fclose, fprintf               
import exit msvcrt.dll    
import fopen msvcrt.dll 
import fclose msvcrt.dll
import fprintf msvcrt.dll 

;Se dau un nume de fisier si un text (definite in segmentul de date). Textul contine litere mici, cifre si spatii. 
;Sa se inlocuiasca toate cifrele de pe pozitii pare cu caracterul ‘X’. 
;Sa se creeze un fisier cu numele dat si sa se scrie textul obtinut in fisier.

segment data use32 class=data
    
    nume_fisier db 'practice5.txt', 0
    mod_acces db 'w', 0
    descriptor dd -1 
    text db 'andr3i ar3 573 note la mat3', 0
    len equ $ - text 
    text_final times len db 0 
    
segment code use32 class=code
    start:
        ;opening file practice5.txt 
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
        mov ebx, 1
    repeta:
        lodsb ;incarcam in AL elementul din text 
        inc bl ;incrementam ca sa ii aflam pozitia
        test bl, 1b
        jnz iesire_repeta
        cmp al, '0'
        jb iesire_repeta
        cmp al, '9'
        jb change_digit
        cmp al, '9'
        ja iesire_repeta
    change_digit:
        mov al, 'X'
    ; ;literally the worst solution that I could have ever thought of 
    ; ;I hate myself for doing this
    ; change_digit:
        ; cmp al, 0
        ; je add_digit1
        ; cmp al, 1
        ; je add_digit2
        ; cmp al, 2
        ; je add_digit3
        ; cmp al, 3
        ; je add_digit4
        ; cmp al, 4
        ; je add_digit5
        ; cmp al, 5
        ; je add_digit6
        ; cmp al, 6
        ; je add_digit7
        ; cmp al, 7
        ; je add_digit8
        ; cmp al, 8
        ; je add_digit9
        ; cmp al, 9
        ; je add_digit10
    ; add_digit1:
        ; add al, 40
    ; add_digit2:
        ; add al, 39
    ; add_digit3:
        ; add al, 38
    ; add_digit4:
        ; add al, 37
    ; add_digit5:
        ; add al, 36
    ; add_digit6:
        ; add al, 35
    ; add_digit7:
        ; add al, 34
    ; add_digit8:
        ; add al, 33
    ; add_digit9:
        ; add al, 32
    ; add_digit10:
        ; add al, 31
        
    iesire_repeta:
        stosb 
        loop repeta 
        
        ;print the resulting text in the file
        ;eax = fprintf(descriptor, text_final)
        push dword text_final
        push dword [descriptor]
        call [fprintf]
        add esp, 4*2 
    
        ;closing file
        ;eax = fclose(descriptor)
        push dword [descriptor]
        call [fclose]
        add esp, 4
    
    final:
        push    dword 0      
        call    [exit]       
