bits 32 
     
global _changebase 

;Se citeste de la tastatura un sir de mai multe numere in baza 2. 
;Sa se afiseze aceste numere in baza 16.
;Am incercat sa implementez algoritmul de schimbare de baza, dar nu imi afiseaza nimic

segment data use32 class=data
     mem_power db 0 
     suma dd 0

segment code use32 class=code
    ;void changebase(char sir1[], int len)
    _changebase:
    ;crearea unui cadru de stiva (stackframe) pentru programul apelat 
        push ebp
        mov ebp, esp
        pushad  ;pusham valorile initiale are registrilor si le restauram la final
        
        ;[ebp]    -> valoarea ebp pentru apelant
        ;[ebp+4]  -> adresa de revenire
        ;[ebp+8]  -> sir1
        ;[ebp+12] -> len
        
        mov esi, [ebp+8]    ;in ESI o sa avem sir1[i]  
        mov ecx, [ebp+12]   ;in ECX o sa avem len(sir1)
        mov ebx, ecx ;luam de la final elementul sir1[i]
        dec ebx ;pt sirul 10101010, in ebx o sa avem EBX = 7 pt 1 * 2^7
        repeta:
            lodsb ;punem caracterul in al
            sub al, 30h ;convertim din ascii in cifre 
            mov byte [mem_power], al ;elementul curent il mutam in memorie  
            mov eax, 1 ;punem 1 in EAX ca sa inmultim puterile 
            push ecx 
            mov  ecx, ebx ;punem in ECX valoarea lungimii elementului 
            push ebx            
            mov  ebx, 2 ;mutam 2 in EBX pentru ca o sa facem EAX = EAX * EBX 
            power:
                mul ebx     ;eax = ebx * 2
                loop power ;o sa avem eax = 2 ^ 7 pt primul element, eax = 2 ^ 6 pt al doilea etc 
            mov edx, eax ;in EDX mutam puterile 
            mov al, byte [mem_power] ;in AL mutam iar elementul din memorie 
            cmp al, 1 ;daca in AL o sa fie caracterul 1, atunci adunam in suma, ce e in EDX 
            jne continue 
            add [suma], edx ;adunam puterile de la 1 
            continue:
                pop ebx 
                pop ecx 
                ;dec ebx ;decrementam EBX ca sa trecem la cealalta putere 
                loop repeta 
        ;refacem cadrul de stiva pentru programul apelant
        popad   ;restauram valorile initiale ale registrilor
        mov eax, [suma]
        mov esp, ebp
        pop ebp
        ;intoarcem rezultatul din EAX 
        ret  