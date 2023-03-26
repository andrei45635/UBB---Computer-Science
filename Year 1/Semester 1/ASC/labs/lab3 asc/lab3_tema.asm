bits 32 
global start        
extern exit              
import exit msvcrt.dll    
                          
    ;a - byte, b - word, c - double word, d - qword                     
segment data use32 class=data
    a db 10
    b dw 15
    c dd 25
    d dq 40
    
    ; ;((a + a) + (b + b) + (c + c)) - d - fara semn
segment code use32 class=code
    start:
    ; a+a
    mov al, [a] 
    mov ah,0    ;ax = a
    add ax, ax 
    mov dx, 0 
    adc dx, 0
    
    
    ;b+b
    mov bx, [b] ;bx = b
    add bx, ax 
    mov cx, 0 
    adc cx, dx 
    
    ;c + c
    mov ecx, [c]
    adc ecx, [c]
    
    ;(a + a) + (b + b)
    adc ax, bx ;ax = ax+bx+cf (daca avem cf)
    
    ;(a + a) + (b + b) + (c + c) - d
    mov dx, 0   ; ax = dx:ax
    adc eax, ecx ; eax = eax + ecx 
    sbb eax, [d] ; eax = eax - d
    
    ; -------------------------------------------------
    
    ; a + b + c + d - (a + b) - cu semn 
    ; a + b 
    mov al, [a]
    cbw ;ax = a
    mov bx, [b]
    adc ax, bx ; ax = a + b 
    cwde ; eax = a + b 
    
    ; c + d 
    mov cx, [c]
    cwde ;ecx = c 
    mov edx, [d]
    adc ecx, edx ; ecx = ecx + edx 
    
    ;a + b + c + d - (a + b)
    adc eax, ecx ; eax = eax + ecx 
    mov edx, eax 
    sbb edx, eax ; edx = edx - eax = eax + ecx - eax = ecx 
    
    ; ((a + a) + (b + b) + (c + c)) - d - cu semn 
    ; ; a + a
    ; mov al, [a]
    ; cbw  ; ax = a
    ; adc ax, ax
    
    ; ; b + b
    ; mov bx, [b]
    ; adc bx, bx
    
    ; ; c + c
    ; mov ecx, [c]
    ; adc ecx, [c]
    
    ; ; (a + a) + (b + b) + (c + c)) - d
    ; adc ax, bx ;ax = ax + bx = a + a + b + b
    ; cwde ; ax -> eax, astfel eax = a + a + b + b 
    ; adc eax, ecx ; eax = a + a + b + b + c + c
    ; sbb eax, [d] ; eax = (a + a) + (b + b) + (c + c)) - d
    
        push    dword 0      
        call    [exit]       
