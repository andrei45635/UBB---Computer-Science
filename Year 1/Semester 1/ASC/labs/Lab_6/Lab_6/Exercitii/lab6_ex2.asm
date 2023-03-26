bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s db 'abcdef' ;abcdcba
    len equ $-s
    d times len db 0
    
; Se da un sir de caractere s.
; Se cere sirul de caractere d obtinut prin inversarea sirului s.
segment code use32 class=code
    start:
        mov ecx, len        
        mov esi, 0 
        mov edi, len-1
        jecxz sfarsit
    repeta: 
        mov al, [s+esi]
        inc esi 
        mov [d+edi], al
        dec edi 
    loop repeta
    sfarsit:
        
        
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
