bits 32 
global start        

extern exit              
import exit msvcrt.dll 

;sir de nr intregi pe doubleword
;construiti un sir corespunzator al octetilor strict negativi 
;din reprezentarea in memorie a doublewords

segment data use32 class=data

   s dd 12345678h, 1AC2A65Ah, 87654321h
   len equ $-s ;retinem numarul de octeti
   d times len db 0
   
segment code use32 class=code

    start:
        mov ecx, len 
        jecxz final
        mov esi , s
        mov edi , d 
        cld 
        
        repeta:
            lodsb ;punem in AL bitul low din s 
            cmp al, 0 ;testam daca octetul este negativ in reprezentarea din memorie
            jge not_add
            stosb ;daca e negativ il adaugam in d 
        not_add:
            loop repeta ;daca nu e atunci loop 
    final:
        push    dword 0      
        call    [exit]      
