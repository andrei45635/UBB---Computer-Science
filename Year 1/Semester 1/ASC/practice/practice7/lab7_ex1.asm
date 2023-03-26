bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s db 'abcdef'
    len equ $-s 
    d times len db 0 
; Se da un sir de caractere s.
; Se cere sirul de caractere d obtinut prin copierea sirului s, folosind instructiuni pe siruri.
segment code use32 class=code
    start:
    mov ecx, len 
    jecxz sfarsit
    cld ;DF = 0
    mov esi, s ;offset ul primului element in esi
    mov edi, d ;offset ul primului element din destinatie
    repeta:
        ;lodsb 
        ;stosb
        movsb 
    loop repeta
    ;rep movsb (inlocuieste loop-ul, doar daca incarcam in ecx, esi, edi ce trebuie)
    
    sfarsit:    
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
