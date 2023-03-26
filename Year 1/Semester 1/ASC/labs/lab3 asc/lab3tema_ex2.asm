bits 32 
global start        

extern exit              
import exit msvcrt.dll    

;a,b,c,d-byte; e-word; x-qword
segment data use32 class=data
    a db 20
    b db 10
    c db 15
    d db 5
    e dw 10
    x dq 100
    rez resq 1

segment code use32 class=code
    start:
    
    ;(a*b-2*c*d)/(c-e)+x/a - cu semn
    ; a * b
    mov al, [a]
    mul byte [b] ; ax = a * b
    mov cx, ax ; cx = a * b 
    
    ;2 * c * d 
    mov al, [c] 
    mul byte [d] ; ax = c * d 
    mov bx, 2 
    mul bx ; ax = ax * bx = 2 * c * d
    
    ;a * b - 2 * c * d 
    sbb  cx, ax ; cx = cx - ax 
    mov bx, cx ; bx = cx - ax
    mov ax, bx
    cwd 
    
    ; ;(a*b-2*c*d)/(c-e)
    mov cx, 0
    mov cl, [c]
    cbw ; cx = c 
    sbb cx, [e] ;cx = c - e 
    div word cx ; ax = dx:ax / cx 
    mov cx, ax 
    
    ;x/a 
    mov eax, [x]
    cdq 
    mov bl, [a]
    cbw 
    cwd 
    div dword bx ; eax = edx:eax / ebx
    
    ;(a*b-2*c*d)/(c-e)+x/a
    adc eax,ecx 
    mov [rez], eax 
    
    ;--------------------------------------------------------------------------------------
    
    ;(a*b-2*c*d)/(c-e)+x/a - fara semn
    ; ;a * b
    mov al, [a]
    mul byte [b] ; ax = a * b
    mov cx, ax ; cx = a * b 
    
    ;2*c*d 
    mov al, [c] 
    mul byte [d] ; ax = c * d 
    mov bx, 2 
    mul bx ; ax = ax * bx = 2 * c * d 
    
    
    ;(a*b-2*c*d)
    sbb  cx, ax ; cx = cx - ax 
    mov bx, cx ; bx = cx - ax
    mov ax, bx
    mov dx, 0 ; dx:ax = cx - ax 
 
    ;(a*b-2*c*d)/(c-e)
    mov cx, 0
    mov cl, [c]
    mov ch, 0 ;cx = c
    sbb cx, [e] ;cx = c - e 
    div word cx ; ax = dx:ax / cx 
    mov cx, ax 
    
    ;x/a 
    mov eax, [x]
    mov edx, 0 ; edx:eax = x 
    mov bl, [a]
    mov bh, 0 ; bx = a
    mov dx, 0 ; dx:bx = a
    div dword bx ; eax = edx:eax / ebx
    
    ;(a*b-2*c*d)/(c-e)+x/a
    mov dx, 0; dx:cx = cx 
    adc eax,ecx 
    mov [rez], eax 
    
  
    
    
        push    dword 0     
        call    [exit]       