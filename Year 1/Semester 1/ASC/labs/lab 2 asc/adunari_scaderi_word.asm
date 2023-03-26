bits 32 
global start   
     
extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    a dw 3
    b dw 4
    c dw 8
    d dw 5
    
    ;(a+c)-(b+b+d)
segment code use32 class=code
    start:
    
    ;(a+c)
    MOV AX, [a]
    ADD AX, [c]
    
    ;b+b+d
    MOV BX, [b]
    ADD BX, [b]
    ADD BX, [d]
    
    SUB AX, BX
    
        push    dword 0     
        call    [exit]      
