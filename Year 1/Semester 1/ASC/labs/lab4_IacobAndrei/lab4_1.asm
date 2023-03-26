bits 32 
global start  
      
extern exit               
import exit msvcrt.dll    

; Se dau octetii A si B. Sa se obtina dublucuvantul C
; bitii 8-15 ai lui C sunt 0
; bitii 16-23 ai lui C coincid cu bitii lui B
; bitii 24-31 ai lui C coincid cu bitii lui A
; bitii 0-7 ai lui C sunt 1
segment data use32 class=data
    a db 01011110b
    b db 00111001b
    c dd 0

segment code use32 class=code
    start:
    mov ebx, 0 ;in ebx calculam rezultatul
    
    ;bitii 8-15 ai lui C sunt 0 
    ;fortam 0 pe pozitiile 8-15 din C
    or ebx, 11111111111111111000000001111111b
    
    ;bitii 16-23 ai lui C coincid cu bitii lui B
    mov dx, 0
    mov ax, [b] ;eax = b 
    rol eax, 8 ;rotim 8 pozitii spre stanga
    or ebx, eax  ;punem in rezultat
    
    ; bitii 24-31 ai lui C coincid cu bitii lui A
    mov dx, 0
    mov cx, [a] ;ecx = a 
    rol ecx, 8
    or ebx, ecx ;idem mai sus
    
    ; bitii 0-7 ai lui C sunt 1
    and ebx, 1111111111111111111111110000000b
    
    mov [c], ebx 
    

        push    dword 0      
        call    [exit]       
