bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s1 dw 1234h, 67abh, 89cdh
    len1 equ ($-s1)/2 
    s2 dw 2345h, 5678h, 4567h
    len2 equ ($-s2)/2
    d times len1 dw 0 
; Se dau doua siruri de cuvinte s1 si s2.
; Se cere sirul de cuvinte d obtinut in interpretarea cu semn, astfel:
; - d[i] = s1[i], daca s1[i] > s2[i]
; - d[i] = s2[i], altfel.
segment code use32 class=code
    start:
        mov ecx, len1
        jecxz ending
        cld 
        mov esi, s1 
        mov edi, s2 
        mov ebx, 0 ;index pt sirul destinatie d 
        
    repeta:
        lodsw ;incarca primul cuvant din s1, esi = esi + 2
        scasw ;cmp ax, <es:edi>, practic compari primul din s1 cu primul din s2, edi = edi + 2
        jle mai_mic
        
        mov [d+ebx], ax ; d[i] <- s1[i]
        jmp continue 
    
    mai_mic:
        mov ax, [s2+ebx] ; ax = s2[i]
        mov [d+ebx], ax ; d[i] < s2[i]
    
    continue:
        add ebx, 2

    loop repeta
    
    ending:
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
