bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s1 db 7, 3, 9, 1, 5
    s2 db 2, 4, 6, 8, 10
    len equ $-s1
    d times len db 0 
    
; Se dau 2 siruri de numere intregi s1 si s2 de lungimi egale.
; Se cere sirul de numere intregi d obtinut astfel:
; - d[i] = s1[i] - s2[i], daca s1[i] > s2[i]
; - d[i] = s2[i] - s1[i], altfel.
segment code use32 class=code
    start:
        mov ecx, len
        mov esi, 0
        mov edi, 0 
        jecxz sfarsit
        
    repeta:
        mov al, [s1+esi]
        mov bl, [s2+esi]
        cmp al,bl ;ZF = 1 (s1 > s2)
        inc esi
        ja mai_mare
        
        sub bl, al
        mov [d+edi], bl 
        jmp mai_departe
        
    mai_mare: 
        sub al, bl 
        mov [d+edi], al 
        inc edi
     
    mai_departe:
        inc edi 
        loop repeta
    
    sfarsit:
        push dword 0        
        call [exit]        
