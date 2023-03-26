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

int main(){
	int p2c;
	int c2p;
	mkfifo("./p2cfifo",0600);
	mkfifo("./c2pfifo",0600);
	if(fork()==0){
		p2c = open("p2cfifo",O_RDONLY);
		if(-1==p2c){
			printf("p2c B epic fail!\n");
			exit(1);
		}
		c2p = open("c2pfifo",O_WRONLY);
		if(-1==c2p){
			printf("c2p B epic fail!\n");
            exit(1);
		}
		int nr;
		char sign;
		srandom(time(NULL));
		nr = random()%9001+1000;
		write(c2p,&nr,sizeof(int));
		while(1){
			read(p2c,&sign,sizeof(char));
			if(sign=='='){
				printf("Am ghicit!\n");
				close(p2c);
				close(c2p);
				exit(0);
			}
			else if(sign=='>'){
				nr=nr-random()%1000;
				printf("nr este %d... m-am dus mai jos...\n",nr);
				write(c2p,&nr,sizeof(int));
			}
			else{
				nr=nr+random()%1000;
				printf("nr este %d... m-am dus mai sus...\n",nr);
				write(c2p,&nr,sizeof(int));
			}
		}
	}
	p2c = open("p2cfifo",O_WRONLY);
    if(-1==p2c){
        printf("p2c A epic fail!\n");
		unlink("./p2cfifo");
		unlink("./c2pfifo");
        exit(1);
    }
    c2p = open("c2pfifo",O_RDONLY);
    if(-1==c2p){
        printf("c2p A epic fail!\n");
		unlink("./p2cfifo");
        unlink("./c2pfifo");
        exit(1);
    }
	int x,nr;
	srandom(time(NULL));
	x=10000-random()%9001;
	printf("X este %d\n",x);
	while(1){
		char sign;
		read(c2p,&nr,sizeof(int));
		if(nr==x){
			sign='=';
			write(p2c,&sign,sizeof(char));
			close(p2c);
			close(c2p);
			break;
		}
		else if(nr>x){
			sign='>';
			write(p2c,&sign,sizeof(char));
		}
		else{
			sign='<';
			write(p2c,&sign,sizeof(char));
		}
	}
	unlink("./p2cfifo");
    unlink("./c2pfifo");
	return 0;
}
