bits 32 
bits 32 
global start       

extern exit               
import exit msvcrt.dll   

; Se dau octetii A si B. Sa se obtina dublucuvantul C:
; bitii 16-31 ai lui C sunt 1
; bitii 0-3 ai lui C coincid cu bitii 3-6 ai lui B
; bitii 4-7 ai lui C au valoarea 0
; bitii 8-10 ai lui C au valoarea 110
; bitii 11-15 ai lui C coincid cu bitii 0-4 ai lui A
segment data use32 class=data
    a db 01011110b
    b db 00111001b
    cd dd 0

; our code starts here
segment code use32 class=code
    ;vom calcula rezultatul in ebx
    start:
    mov ebx, 0 
    
    ;bitii 16-31 ai lui C sunt 1
    ;fortam 1 pe bitii 16-31 din C
    or ebx, 11111111111111110000000000000000b
    
    ;bitii 11-15 ai lui C coincid cu bitii 0-4 ai lui A
    mov ax, [a] ;izolam bitii 0-4 ai lui A
    cwd 
    and eax, 00000000000000000000000000011111b
    mov cl, 11
    rol eax, cl ;deplasam bitii 11 pozitii in rezultat 
    or ebx, eax 
    
    ;bitii 8-10 ai lui C au valoarea 110
    ;bitii 8-9 au valoarea 11 
    ;fortam 1 pe bitii 8-9
    or ebx, 00000000000000000000011000000000b

    ;bitii 4-7 ai lui C au valoarea 0
    ;fortam 0 pe bitii 4-7
    or ebx, 00000000000000000000000000000000b
    
    ;bitii 0-3 ai lui C coincid cu bitii 3-6 ai lui B
    mov ax, [b] ;izolam bitii 3-6 ai lui b 
    cwd 
    and eax, 00000000000000000000000001111000b
    mov cl, 3
    ror eax, cl ;rotim spre dreapta cu 3 pozitii
    or ebx, eax 
    
    mov [cd], ebx 
    
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
