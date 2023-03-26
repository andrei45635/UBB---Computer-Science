bits 32 
global start        

extern exit, printf, scanf      
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll

;Se da un numar natural a (a: dword, definit in segmentul de date). 
;Sa se citeasca un numar natural b si sa se calculeze: a + a/b. 
;Sa se afiseze rezultatul operatiei. Valorile vor fi afisate in format decimal (baza 10) cu semn.
segment data use32 class=data

   a dd 12
   b dd 0
   rez dd 0
   format_citire db 'Introduceti numarul natural b: ', 0
   citire_b db '%d', 0
   format_rezultat db 'Rezultatul operatiei a + a/b este: %d', 0
   ;rezultat db '%d', 0
   
segment code use32 class=code
    start:
      ;printf(format_citire)
      push dword format_citire
      call [printf]
      add esp, 4
      
      ;scanf(citire_b, b)
      push dword b
      push dword citire_b
      call [scanf]
      add esp, 4*2
      
      mov eax, [a] ;am pus in EDX, valoarea lui a
      cdq
      ;mov edx, 0 ;in EDX:EAX avem a 
      mov ebx, [b] ;in EBX avem b 
      idiv dword [b] ; in EAX o sa avem valoarea impartirii lui a la b
      mov ecx, [a] 
      add eax, ecx ;in eax avem rezultatul final 
      mov [rez], eax 
      
      ;printf(format_rezultat, rez)
      push dword [rez]
      push dword format_rezultat
      call [printf]
      add esp, 4*2

      
      push    dword 0      
      call    [exit]       
