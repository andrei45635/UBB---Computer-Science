#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

typedef struct{
     int nr;
     int cnt;
}package;

int boltz(int x){
     if(x % 7 == 0) return 1;
     else return 0;
} 

int main(int argc, char** argv){
    int a2b[2], b2c[2], c2d[2], d2a[2];
    if(pipe(a2b) == -1){
       printf("Error when creating pipe a2b\n");
       return 1;
    }
    if(pipe(b2c) == -1){
       printf("Error when creating pipe b2c\n");
       return 1;
    }
    if(pipe(c2d) == -1){
       printf("Error when creating pipe c2d\n");
       return 1;
    }
    if(pipe(d2a) == -1){
       printf("Error when creating pipe d2a\n");
       return 1;
    }
    package pkg;
    pkg.cnt = 0;
    if(fork() == 0) {
       if(fork() == 0) {
	   if(fork() == 0){
	       //proc D
	       close(a2b[0]); 
	       close(a2b[1]);
	       close(b2c[0]);
	       close(b2c[1]);
	       close(c2d[1]);
	       close(d2a[0]);
	       while(1){
               	if(read(c2d[0], &pkg, sizeof(pkg)) == -1){
	          printf("Error when reading from C in D\n");
		  return 1;
	       	}
	       	printf("D read from C: number = %d, count = %d\n", pkg.nr, pkg.cnt);
	       	if(boltz(pkg.nr) == 1){
		  printf("Boltz!\n");
		  pkg.cnt++;
		  if(pkg.cnt == 6){
		    break;
		  }
		}
		pkg.nr++;
		printf("D wrote to A: number = %d, count = %d\n", pkg.nr, pkg.cnt);
		if(write(d2a[1], &pkg, sizeof(pkg)) == -1){
		   printf("Error writing from D to A\n");
		   return 1;
		}
	       }
	       close(c2d[0]);
	       close(d2a[1]);
	       exit(0);
	   }
	   // proc C
           close(a2b[0]);
	   close(a2b[1]);
	   close(b2c[1]);
	   close(c2d[0]);
	   close(d2a[0]);
	   close(d2a[1]);
           while(1){
	     if(read(b2c[0], &pkg, sizeof(pkg)) == -1){
		 printf("Error when reading from B in C\n");
		 return 1;
	     }
	     printf("C read from B: number = %d, count = %d\n", pkg.nr, pkg.cnt);
             if(boltz(pkg.nr) == 1){
	        printf("Boltz!\n");
		pkg.cnt++;	     
	        if(pkg.cnt == 6){
	           break;
	       }
	     }
             pkg.nr++;
	     printf("C wrote to D: number = %d, count = %d\n", pkg.nr, pkg.cnt);
	     if(write(c2d[1], &pkg, sizeof(pkg)) == -1){
	        printf("Error when writing to D from C\n");
		return 1;
	     }
	   }
	   close(b2c[0]);
	   close(c2d[1]);
	   wait(0);
	   exit(0);
       }
      //proc B
      close(a2b[1]);
      close(b2c[0]);
      close(c2d[0]);
      close(c2d[1]);
      close(d2a[0]);
      close(d2a[1]);
      while(1){
         if(read(a2b[0], &pkg, sizeof(pkg)) == -1){
	    printf("Error when reading from A in B\n");
	    return 1;
	 }
	 printf("B read from A: number = %d, count = %d\n", pkg.nr, pkg.cnt);
	 if(boltz(pkg.nr) == 1){
	    printf("Boltz\n");
	    pkg.cnt++;
	    if(pkg.cnt == 6){
	       break;
	    }
	 }
	 pkg.nr++;
	 printf("B wrote to C: number = %d, count = %d\n", pkg.nr, pkg.cnt);
	 if(write(b2c[1], &pkg, sizeof(pkg)) == -1){
	    printf("Error when writing from B to C\n");
	    return 1;
	 }
      }
      close(a2b[0]);
      close(b2c[1]);
      wait(0);
      exit(0);
    } else {
           close(a2b[0]);
	   close(b2c[0]);
	   close(b2c[1]);
	   close(c2d[0]);
	   close(c2d[1]);
	   close(d2a[1]);
	   pkg.nr = atoi(argv[1]);
	   printf("The number is: %d\n", pkg.nr);
	   if(write(a2b[1], &pkg, sizeof(pkg)) == -1){
	      printf("Error when writing to B from A for the first time\n");
	      return 1;
	   }
	   while(1){
           	if(read(d2a[0], &pkg, sizeof(pkg)) == -1){
	     	  printf("Error reading from D\n");
	     	  return 1;
	   	}
                printf("A read from D: number = %d, count = %d\n", pkg.nr, pkg.cnt);		
           	if(boltz(pkg.nr) == 1){
			printf("Boltz!\n");
	      		pkg.cnt++;
	   	     if(pkg.cnt == 6){
			  break;
	   	   }
		}
		pkg.nr++;
		printf("A wrote to B: number = %d, count = %d\n", pkg.nr, pkg.cnt);
		if(write(a2b[1], &pkg, sizeof(pkg)) == -1){
		   printf("Error when writing from A to B\n");
		   return 1;
		}
           }
	   close(d2a[0]);
	   close(a2b[1]);
	   wait(0);
	}
    return 0;
}
