bits 32 
global start   
     
extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    b db 5
    c db 4
    e dw 10
    g dw 4
    
    ;(e+g-2*b)/c
segment code use32 class=code
    start:
    ;e+g
    MOV BX, [e]
    ADD BX, [g]
    MOV CX, BX
    
    ;2*b
    MOV AL, [b]
    MOV BL, 2
    MUL BL   ;AX=AL*BL = AL*2
    
    ;(e+g-2*b)/c
    SUB CX, AX
    MOV AX, CX 
    DIV BYTE [c] ;AX = EAX / c and DX = EAX % c
    
        push    dword 0     
        call    [exit]      
