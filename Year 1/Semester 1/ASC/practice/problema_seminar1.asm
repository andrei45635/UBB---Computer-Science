bits 32 
global start        

extern exit               
import exit msvcrt.dll    

;sir de caractere cu litere mari 
;sa se construiasca un sir nou cu litere mici 
segment data use32 class=data
    s db 'A', 'B', 'C', 'D'
    len equ $-s 
    d times len db 0 
    
segment code use32 class=code
    start:
        mov ecx, len 
        mov esi, s 
        mov edi, d
        cld 
        jecxz final
    repeta:
        lodsb ;primul element din s va fi introdus in AL
        sub AL, 'A' - 'a' ;transformam din litera mare in litera mica 
        stosb ;punem in d 
    loop repeta 
        
    final:
        push    dword 0      
        call    [exit]       