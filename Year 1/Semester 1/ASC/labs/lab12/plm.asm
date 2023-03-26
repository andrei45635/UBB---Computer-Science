bits 32 
global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
   a1 dd -255, a5 
   a5 dd -1<<1Fh, 11h>>11b
   a6 dd '0abcdefgh', -127<<1
   a3 db ~((-1)^0cch), 1^0cch
   dece equ 2
segment code use32 class=code
    start: 
        mov al, 6
        mov bl, 4
        add al, bl 
        push    dword 0      
        call    [exit]       
