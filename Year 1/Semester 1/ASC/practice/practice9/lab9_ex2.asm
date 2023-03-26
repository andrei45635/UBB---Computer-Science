bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    
    
; Cititi de la tastatura si afisati un sir de numere intregi.
; (citirea se termina atunci cand utilizatorul introduce numarul ZERO)
segment code use32 class=code
    start:
        
    
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
