#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <time.h>
#include <sys/stat.h>
#include <fcntl.h>

typedef struct{
	int count;
	int nr;
}pack;

int hd6(int nr){
	if(nr%6==0)
		return 1;
	while(nr){
		if(nr%10==6)
			return 1;
		nr=nr/10;
	}
	return 0;
}

int main(){
	int p2a[2],a2b[2],b2p[2];
	pack pckg;
	pckg.count=0;
	pipe(p2a);
	pipe(a2b);
	pipe(b2p);
	if(fork()==0){
		if(fork()==0){
			//proc B
			close(p2a[0]);
			close(p2a[1]);
			close(a2b[1]);
			close(b2p[0]);
			while(1){
	            if(1>read(a2b[0],&pckg,sizeof(pack)))
					break;
				printf("B's number is %d\n",pckg.nr);
            	if(hd6(pckg.nr)==1){
        	        pckg.count++;
    	            printf("B said bazinga!\n");
					if(pckg.count==6)
						break;
	            }
            	pckg.nr++;
        	    write(b2p[1],&pckg,sizeof(pack));
    	    }
			close(a2b[0]);
            close(b2p[1]);
	        exit(0);
		}
		//proc A
		close(b2p[0]);
		close(b2p[1]);
		close(a2b[0]);
		close(p2a[1]);
		while(1){
			if(1>read(p2a[0],&pckg,sizeof(pack)))
				break;
			printf("A's number is %d\n",pckg.nr);
    	    if(hd6(pckg.nr)==1){
	            pckg.count++;
            	printf("A said bazinga!\n");
				if(pckg.count==6)
					break;
        	}
    	    pckg.nr++;
	        write(a2b[1],&pckg,sizeof(pack));
		}
		close(a2b[1]);
        close(p2a[0]);
		wait(0);
		exit(0);
	}
	//proc P
	close(a2b[0]);
	close(a2b[1]);
	close(p2a[0]);
	close(b2p[1]);
	srand(time(NULL));
	pckg.nr=rand()%100;
	printf("Initial number is %d\n",pckg.nr);
	if(hd6(pckg.nr)==1){
		printf("P said bazinga!\n");
		pckg.count++;
	}
	pckg.nr++;
	write(p2a[1],&pckg,sizeof(pack));
	while(1){
		if(1>read(b2p[0],&pckg,sizeof(pack)))
			break;
		printf("P's number is %d\n",pckg.nr);
		if(hd6(pckg.nr)==1){
			pckg.count++;
			printf("P said bazinga!\n");
			if(pckg.count==6)
				break;
		}
		pckg.nr++;
		write(p2a[1],&pckg,sizeof(pack));
	}
	close(p2a[1]);
    close(b2p[0]);
	wait(0);
	return 0;
}
