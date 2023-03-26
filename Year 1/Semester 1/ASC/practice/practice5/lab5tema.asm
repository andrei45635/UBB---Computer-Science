bits 32 
global start        

extern exit               
import exit msvcrt.dll    

; Se dau doua siruri de caractere S1 si S2. 
; Sa se construiasca sirul D prin concatenarea elementelor sirului S2 
; in ordine inversa cu elementele de pe pozitiile pare din sirul S1.
segment data use32 class=data
    s1 db '+', '2', '2', 'b', '8', '6', 'X', '8'
    len1 equ $-s1
    s2 db 'a', '4', '5'
    len2 equ $-s2
    d times len2+len1/2 db 0 
; Exemplu:  
; S1: '+', '2', '2', 'b', '8', '6', 'X', '8'
; S2: 'a', '4', '5'
; D: '5', '4', 'a', '2','b', '6', '8'
segment code use32 class=code
    start:
        mov ecx, len2
        mov edi, d
        mov ebx, s2
        jecxz ending
    
    repeta1:
        mov al, [ebx+ecx-1] 
        mov [edi], al 
        inc edi 
        loop repeta1 
    
        mov ecx, len1
        mov ebx, s1
        mov eax, 1
        mov esi, 1
        jecxz ending 
    
    repeta2:
        cmp ecx, 1
        jz ending
        mov dl, [ebx+esi]
        add esi, 2
        mov [edi], dl 
        inc edi
        dec ecx 
        loop repeta2
    
    ending:
        push    dword 0      
        call    [exit]       
