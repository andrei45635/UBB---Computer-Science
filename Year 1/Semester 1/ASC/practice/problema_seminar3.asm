bits 32 
global start        

extern exit               
import exit msvcrt.dll   

;se dau 2 siruri de cuvinte
;sa se concateneze sirul octetilor inferiori ai cuvantului din primul sir
;cu sirul octetilor superiori ai cuv din al doilea sir
;sirul rezultat este sortat crescator in interpretarea cu semn

segment data use32 class=data

   s1 dw 1234h, 2345h, 3456h, 4567h
   len1 equ ($-s1)/2 ;retinem numarul de dublucuvinte
   s2 dw 9876h, 8765h, 7654h, 6543h
   len2 equ ($-s2)/2 ;retinem numarul de dublucuvinte
   len equ len1+len2 
   d times len db 0 
   
segment code use32 class=code

    start:
        ;punem in d octetii low din sirul s1
        mov ecx, len1 
        jecxz final1
        cld
        mov esi, s1
        mov edi, d
       
        repeta1:
            lodsw ;punem word-ul din s1 in AX
            stosb ;punem octetul low din AL in d
        loop repeta1
        
        final1:
        
        ;punem in d octetii high din sirul s2 
        mov ecx, len2 
        jecxz final2 
        mov esi, s2 
        
        repeta2:
            lodsw
            lodsw ;am pus octetul high din word 
            mov al, ah ;mutam octetul high in AL ca sa il punem in d  
            stosb 
        loop repeta2
        
        final2:
        
        ;sortare 
        mov ecx,1 ;ecx actioneaza pe post de ok boolean, aici ok = 1
        
        executa:
            cmp ecx,1 ;if (ok == 1)
            jnz afara ;daca ok != 1 atunci iesi din program
            xor ecx, 0 ;ok = 0
            xor edx, 0 ;cu edx introducem in d octetii 
            
            forloop:
                mov al, [d+edx] ;punem in AL octetul low din d 
                mov bl, [d+edx+1] ;punem in BL octetul high din d 
                cmp al,bl ;le comparam <=> if(s1[i]<s2[j])
                jl continua 
                mov [d+edx], bl ;daca octetul din AL e mai mare decat cel din BL, atunci le interschimbam
                mov [d+edx+1], al 
                mov ecx, 1 ;ok = 1
                
            continua:
                inc edx ;incrementam EDX ca sa continuam sa adaugam in d
                cmp edx, len-1 ;daca EDX < len-1 atunci se repeta forloop  
                jl forloop
                jmp executa ;sare la inceputul sortarii 
                
            afara:
                push    dword 0      
                call    [exit]