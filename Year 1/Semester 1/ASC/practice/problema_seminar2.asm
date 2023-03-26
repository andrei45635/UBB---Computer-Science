bits 32 
global start        

extern exit               
import exit msvcrt.dll   

;sir de octeti 
;sa se construiasca in d sirul oglindit
segment data use32 class=data
    s db 1,2,3,4,5
    len equ $-s 
    d times len db 0
    
segment code use32 class=code
    start:
        mov ecx, len 
        jecxz final
        mov esi, s
        mov edi, d 
        std ;DF = 1, adica incepem de la final  
        add esi, len-1 ;incepem de la offset 9 ca sa parcurgem sirul invers 
    repeta:
        std ;DF = 1, le luam iar de la final 
        lodsb
        cld ;DF = 0, ca sa restartam directia 
        stosb 
    loop repeta 
    
    final:
        push    dword 0      
        call    [exit]       
