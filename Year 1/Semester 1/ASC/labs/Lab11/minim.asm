bits 32 
global minim       
segment code use32 public code 
    minim:
        mov esi, [esp+4] ;esi = sir[0]
        mov ecx, [esp+8] ;ecx = n 
        
        mov ebx, 0
        mov ebx, [esi] ;initializam minim cu ebx 
        repetat:
            lodsd
            cmp eax, ebx 
            jge looping
            mov ebx, eax 
        looping:
            loop repetat 
        mov [esp+12], ebx 
        
        ret 4*2 