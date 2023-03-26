bits 32 
global start        

extern exit               
import exit msvcrt.dll  

segment data use32 class=data
    s db 'a', 'b', 'c', 'm', 'n';sir initial
    ; sau s db 'abcmn'
    len equ $-s ;$= contor de locatii, noi facem lungimea sirului initial 
    d times len db 0  ;aloca o variabila d in care de len ori sa aloci cate un octet pe care il initializezi cu 0  
    
;Se da un sir de caractere format din litere mici.
;Sa se transforme acest sir in sirul literelor mari corespunzator.    
segment code use32 class=code
    start:
        mov ecx, 5
        jecxz sfarsit 
        mov esi, 0 ;index sursa, un fel de i = 0
        mov edi, 0 ; j = 0
        
    repeta:
        mov al, [s+esi] ; AL = 61 (<=> 'a'=61h), AL = s[i]
        
        mov bl, 'a' - 'A'
        ; sau instructiunile astea 
        ; mov bl, al 
        ; sub bl, 'A' ;BL = 'A' - 'a'  
        sub al, bl
        
        mov [d+edi], al ;d[j]
        
        inc esi    ;i++
        inc edi    ;j++
    loop repeta
    
    sfarsit:
        push    dword 0      
        call    [exit]       