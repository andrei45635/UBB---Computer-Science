bits 32 
global start   
     
extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    a db 3
    b db 4
    c db 8
    d dw 5
    
    ;d+[(a+b)*5-(c+c)*5]
segment code use32 class=code
    start:
    
    ;(a+b)*5
    MOV AL, [a]
    ADD AL, [b]
    MOV BL, 5
    MUL BL    ;AX = AL * BL 
    MOV BX, AX
    
    
    ;(c+c)*5
    MOV AL, [c]
    ADD AL, AL
    MOV DL, 5
    MUL DL      ;AX = AL * DL
    
    
    ;d+[(a+b)*5 - (c+c)*5]
    SUB BX, AX
    ADD BX, [d]
    
        push    dword 0     
        call    [exit]      
