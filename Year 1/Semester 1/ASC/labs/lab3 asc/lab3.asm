bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a db 240 
    b db 20
    c db 10
    rez resb 1

    ;a+b/c
segment code use32 class=code
    start:
        
        ;1. nu tinem cont de transport
        ; -----------------------------
        ;b/c
        ; MOV AL, [b]
        ; MOV AH, 0                   ; AX = b (am extins b pe 16 biti fara semn)
        ; DIV BYTE [c]                ; AL = AX / c
        
        ; ;a +b/c
        ; ADD AL, [a]                 ;AL = AL + a <=> AL = a + b/c
        ; MOV [rez], AL
        
        ;2. tinem cont de transport
        ; b/c
        MOV AL, [b]
        MOV AH, 0                   ; AX = b (am extins b pe 16 biti fara semn)
        DIV BYTE [c]                ; AL = AX / c
        
        ; a+b/c
        ADD AL, [a]
        MOV AH, 0 
        ADC AX, 0                   ;AX = a+ b/c + CarryFlag
        MOV [rez], AX
        
        push    dword 0      
        call    [exit]       
