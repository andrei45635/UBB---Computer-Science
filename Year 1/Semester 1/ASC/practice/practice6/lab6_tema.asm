bits 32 
global start        

extern exit               
import exit msvcrt.dll    

;Dandu-se un sir de dublucuvinte,
;sa se obtina un alt sir de dublucuvinte 
;in care se vor pastra doar dublucuvintele din primul sir
;care au un numar par de biti cu valoare 1.

segment data use32 class=data

   s dd 11101010001101000101011001110000b, 11010010001011000011110000011100b, 11000000111111001101110001110110b
   len equ ($-s)/4
   d times len dw 0 
   
segment code use32 class=code

    start:
    
       mov ecx, len 
       jecxz sfarsit 
       cld ;DF = 0
       mov esi, s  ; la adresa <DS:ESI> incarcam adresa primului element din s
       mov edi, d   ;idem doar ca la adresa <ES:EDI>
       xor ebx, ebx ;cu ajutorul lui ebx testam 
       
    repeta:
    
        lodsd ;incarcam primul element din sirul s de la adresa <DS:ESI> in EAX, 
;               iar daca DF=0 atunci ESI:=ESI+4, altfel ESI:=ESI-4
        mov edx, eax
        shr edx, 1;shiftam la dreapta in CF bitul cel mai din dreapta
        xor bl, bl; resetam bl-ul de fiecare data cand ne reintoarcem pentru un dublucuvant
        
    numarare_bit:
    
        adc bl, 0
        shr edx, 1
        jnz numarare_bit
        
        adc bl, 0 ;numaram ultimul bit
        
        test bl, 1b ;daca numarul de biti e par atunci se adauga in d
        jnz skip ;daca nu e par, atunci skip 
        
        stosd ;incarcam in d 
        
    skip:
    
        xor edx, edx 
        loop repeta
      
    sfarsit:
        push    dword 0      
        call    [exit]       
