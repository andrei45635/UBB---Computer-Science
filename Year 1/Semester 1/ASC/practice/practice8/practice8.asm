bits 32 
global start        

extern exit, fopen, fclose, fwrite, fread, fprintf                
import exit msvcrt.dll   
import fopen msvcrt.dll 
import fclose msvcrt.dll 
import fwrite msvcrt.dll 
import fread msvcrt.dll 
import fprintf msvcrt.dll

;litere mic -> ascii
segment data use32 class=data

      nume_fisier_1 db 'practice8.txt', 0
      mod_acces_1 db 'r', 0
      descriptor_1 dd -1 
      nume_fisier_2 db 'output.txt', 0
      mod_acces_2 db 'w', 0
      descriptor_2 dd -1
      len_text equ 100
      text resb len_text ;asta e buffer ul practic 
      nr_car_citite db 0
      result_text times (len_text + len_text) db 0
      format_mic db '%d', 0
      format_mare db '%s', 0
      
  
segment code use32 class=code
    start:
    
        ;eax = fopen(nume_fisier_1, mod_acces_1)
        push dword mod_acces_1
        push dword nume_fisier_1
        call [fopen]
        add esp, 4*2 
        
        mov [descriptor_1], eax 
        
        cmp eax, 0
        je final 
        
        ;eax = fopen(nume_fisier_2, mod_acces_2)
        push dword mod_acces_2
        push dword nume_fisier_2
        call [fopen]
        add esp, 4*2 
        
        mov [descriptor_2], eax 
        
        cmp eax, 0
        je final 
        
    repeta:
    
        ;eax = fread(text, 1, len_text, descriptor_1)
        push dword [descriptor_1]
        push dword len_text
        push dword 1 
        push dword text
        call [fread]
        add esp, 4*4 ;in EAX o sa fie numarul de caractere citite 
        
        ;mov [nr_car_citite], eax 
        
        cmp eax, 0
        je cleanup 
        
        mov ecx, eax
        jecxz final 
        cld 
        mov esi, text ;ESI = AncaT 
        mov edi, result_text
        
     repeating:
     
        lodsb ;in AL o sa fie primul caracter samd, in AL o sa fie 'A'
        cmp al, 'A'
        ja check1
        
     check1:
     
        cmp al, 'Z'
        jb good_char 
        ;in AL avem o litera mica daca a trecut de toate check-urile
        jmp bad_char
        
     good_char:
     
        mov [edi], al 
        push eax
        push ecx
        ;fprintf(descriptor_2, format_mare, result_text)
        push dword result_text
        push dword format_mare
        push dword [descriptor_2]
        call [fprintf]
        add esp, 4*3
        pop ecx 
        pop eax 
        jmp looping
        
     bad_char:
     
        mov [edi], al  
        push eax 
        push ecx        
        ;fprintf(descriptor_2, format_mic, result_text)
        push dword result_text
        push dword format_mic
        push dword [descriptor_2]
        call [fprintf]
        add esp, 4*3
        pop ecx 
        pop eax 
        
     looping:
     
        loop repeating
     
     jmp repeta
      
     cleanup: 
        
        ;eax = fclose(descriptor_1)
        push dword [descriptor_1]
        call [fclose]
        add esp, 4
        
        ;eax = fclose(descriptor_2)
        push dword [descriptor_2]
        call [fclose]
        add esp, 4
    
    final:
    
        push    dword 0      
        call    [exit]      
