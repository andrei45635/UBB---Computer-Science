bits 32 
global start        

extern exit, fopen, fclose, fread, printf, fwrite, scanf, fprintf               
import exit msvcrt.dll    
import fopen msvcrt.dll 
import fclose msvcrt.dll 
import fread msvcrt.dll
import printf msvcrt.dll
import fwrite msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll  

; write a program that will read from keyboard a filename input.txt and a character c.
; the input file input.txt contains words separated by space. write in the file output.txt 
; only the words that contain the character c
segment data use32 class=data

    nume_fisier_input db 'practice6.txt', 0
    mod_acces_input db 'r', 0
    descriptor_input dd -1
    c dd 0
    caracter db '%c', 0
    format_citire db 'Introduceti caracterul c= ', 0
    nume_fisier_output db 'output.txt', 0
    mod_acces_output db 'w', 0
    descriptor_output dd -1
    text db 0
    len_text equ 100 
    buffer resb len_text 
    result_text times len_text db 0
    nr_car_citite dd 0 
   
segment code use32 class=code
    start:
       ;opening the first file 
       ;eax = fopen(nume_fisier_input, mod_acces_input)
       push dword mod_acces_input
       push dword nume_fisier_input
       call [fopen]
       add esp, 4*2
       
       mov [descriptor_input], eax
       
       cmp eax, 0
       je final 
       
       ;opening the second file 
       ;eax = fopen(nume_fisier_output, mod_acces_output)
       push dword mod_acces_output
       push dword nume_fisier_output 
       call [fopen]
       add esp, 4*2
       
       mov [descriptor_output], eax 
       
       cmp eax, 0
       je final 
       
       ;printf(format_citire)
       push dword format_citire
       call [printf]
       add esp, 4
       
       ;scanf(caracter, c)
       push dword c 
       push dword caracter
       call [scanf]
       add esp, 4*2
       
       
    repeta:
        ;reading the elements of the string from the input file 
        ;fread(buffer, 1, len_text, descriptor_input)
        push dword [descriptor_input] 
        push dword len_text
        push dword 1 
        push dword buffer 
        call [fread]
        add esp, 4*4
        
        mov [nr_car_citite], eax
        
        cmp word [nr_car_citite], 0
        je error  
        
        mov ecx, eax
        mov esi, text 
        mov edi, result_text
        repeta2:
            lodsb
            cmp al, [c]
            jne repeating
            stosb
            repetat_spatiu:
                lodsb ;eu m-am gandit ca dupa ce verificam daca in al este caracterul cautat,
                      ;atunci o sa tot punem caracterele pana la spatiu
                      ;cand ajungem la spatiu, sarim 
                cmp al, 20h ;verificam daca e spatiu 
                je out_spatiu
                stosb
                jmp repetat_spatiu
        out_spatiu:           
            stosb
        repeating:
            loop repeta2
            
            ;fwrite(buffer, 1, len_text, descriptor_output)
            push dword [descriptor_output]
            push dword len_text
            push dword 1 
            push dword result_text 
            call [fwrite]
            add esp, 4*4 
            
            cmp eax, 0 
            je error
            
            jmp repeta 
            error:
                ;closing practice6.txt 
                ;fclose(descriptor_input)
                push dword [descriptor_input]
                
                ;closing output.txt 
                ;fclose(descriptor_output)
                push dword [descriptor_output]

    final:   
       push    dword 0      
       call    [exit]       
