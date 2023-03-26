bits 32 
global start        

extern exit, printf, scanf        
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll

;Sa se citeasca de la tastatura in baza 16 doua numere a si b de tip dword si sa se afiseze suma partilor low si diferenta partilor high. 
;Exemplu:
;a = 00101A35h, b = 00023219h
;suma = 4C4Eh
;diferenta = Eh
segment data use32 class=data
    
    format_citire_a db 'Introduceti a: ', 0
    citire_a db '%x', 0
    format_citire_b db 'Introduceti b: ', 0
    citire_b db '%x', 0
    a dd 0 
    b dd 0
    dif1 dd 0
    dif2 dd 0
    suma dd 0 
    format_rezultat db 'Suma partilor low este: %x, iar ', 0
    diferenta dd 0 
    format_diferenta db 'diferenta partilor high este: %x', 0
    
segment code use32 class=code
    start:
        ;printf(format_citire_a)
        push dword format_citire_a
        call [printf]
        add esp, 4
        
        ;scanf(citire_a, a)
        push dword a 
        push dword citire_a
        call [scanf]
        add esp, 4*2
        
        ;printf(format_citire_b)
        push dword format_citire_b
        call [printf]
        add esp, 4
        
        ;scanf(citire_b, b)
        push dword b 
        push dword citire_b
        call [scanf]
        add esp, 4*2
        
        mov eax, [a] 
        mov ebx, [b]
        add ax, bx ;in AX va fi suma partilor low 
        mov [suma], ax 
        
        mov cx, [a+2]
        mov dx, [b+2]
        sub cx, dx 
        mov [diferenta], cx 
        
        ;printf(format_rezultat, suma)
        push dword [suma] 
        push dword format_rezultat
        call [printf] 
        add esp, 4*2
        
        ;printf(format_diferenta, diferenta)
        push dword [diferenta]
        push dword format_diferenta
        call [printf]
        add esp, 4*2
        
        push    dword 0      
        call    [exit]       
