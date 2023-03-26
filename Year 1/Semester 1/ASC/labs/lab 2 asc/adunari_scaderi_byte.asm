bits 32 
global start   
     
extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    a db 3
    b db 4
    c db 8
    d db 5
    
    ;(a+a)-(b+b)-c
segment code use32 class=code
    start:
    
    ; a+a 
    MOV AL, [a]
    ADD AL, [a]  
    
    ; b+b
    MOV BL, [b]
    ADD BL, [b]
    
    ; (a+a) - (b+b)
    SUB AL, BL 
    MOV AH, AL 
    
    ;(a+a) - (b+b) - c
    SUB AH, [c]
    
        push    dword 0     
        call    [exit]      
