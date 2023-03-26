bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s db 'abcdef'
    len equ $-s
    d times len db 0 
    
; Se da un sir de caractere s.
; Se cere sirul de caractere d obtinut prin copierea sirului s.
segment code use32 class=code
    start:
    ; cu op pe siruri
        mov ecx, len 
        jecxz sfarsit
        cld ;clear direction flag <=> DF = 0 
        mov esi, s ;offset-ul primului element din s 
        mov edi, d ;offset-ul primului element din d
        
    repeta:
        ;movsb  ;movsb face ceea ce fac lodsb si stosb 
        
        lodsb ;al = <DS:ESI> + inc ESI
        ;lodsw ;ax = <DS:ESI> + ESI+2        
        ;mov al, [s+esi]   ;al =s[i]
        ;inc esi ;trecem la urm element 
        
        stosb ; <ES:EDI> = al + inc EDI (daca DF = 0)
        ;mov [d+edi], al
        ;inc edi 
    
    loop repeta
        ; mov ecx, len
        ; jecxz sfarsit        
        ; mov esi, 0 
        ; mov edi, 0
    ; repeta: 
        ; mov al, [s+esi]
        ; inc esi 
        ; mov [d+edi], al
        ; inc edi 
    ; loop repeta
    
    sfarsit:
        
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
