SUB 2018-2019

1) shell cmd that displays lines that contain words starting with capital letters

	grep -E "\<[A-Z].*\>" a.txt
	
2) shell cmd that inverts all pairs of neighbouring digits
	
	sed -E "s/([0-9])([0-9])/\2\1/gi" b.txt

3) shell cmd that displays for each line the sum of its numbers
	
	awk -F' ' 'BEGIN{sum = 0;} {for (i=0; i < NF; i++) {sum += i;}} END{print sum}'
	
4) display lines of a text file d.txt that appear only once

	cat d.txt | sort | uniq -u
	
5) write a shell script that displays the name of each .txt file in the current directory that contains "cat"
	#!/bin/bash

	for file in $(find -type f -name "*.txt"); do
		if [ ! -z "$(grep -E "cat" $file )" ]; then
			echo $file
		fi
	done
	
6) In the program fragment bellow, mark which process executes each line: the Parent, the Child, or both.
	P k = fork();
	P C if (k == 0){
	C printf("A\n");
	  }
	P else {
	P printf("B\n");
	  }
	P C printf(C\n");
	
7) how many processes will be created, excluding the parent process? 
 
	fork(); wait(0); fork(); wait(0); fork();
	
	fork();
	wait(0);
	
	fork();
	wait(0);
	
	fork();
	
	//pe partea stanga sunt copiii parintelui, pe partea dreapta a copilului
					 C
				 C1      C2 
			   C3  C4  C5  C6
	  7 procese 
	  
8) all possible output of the next lines of code

	printf("A\n");
	execl(..);
	printf("B\n");
	
	it will output A and whatever output execl has or A and B if execl isn't executed
	
9) what does "read" do when the pipe is empty?
	
	it waits for data to be sent, so it will block until there are writers 
	
10) what does "open" do before returning from opening fifo?
	
	waits for fifo to be open for complementary operation before returning

11) give a reason for choosing threads over processes
  
	creating threads is simpler than creating processes, it's quicker to switch between threads, threads share data more easily
	 
12) Consider that functions "fa" and "fb" are run in concurrent threads, what will the value of "n" be after the threads are finished? Why?
	
	pthread_mutex_t a, b;
	int n = 0;
	
	void* fa(void* p){
		pthread_mutex_lock(&a);
		n++;
		pthread_mutex_unlock(&a);
	}

	void* fb(void* p){
		pthread_mutex_lock(&b);
		n++;
		pthread_mutex_unlock(&b);
	}

	n = number of threads 
	
13) Schedule the following jobs so that they all meet their deadlines: A/5/9, B/7/13, C/1/10

	A,C,B no delay (or C,A,B)

14) one advantage and one disadvantage of segmented allocation over paged allocation 

	ADVANTAGES:
		- Segment tables use less memory than paging
		- The segment table is of less size compared with the page table in paging
		- Does not offer internal fragmentation, while paged allocation does
		- Simple to relocate segments than the entire address space

	DISADVANTAGES:
		- Un-equal size of segments is not good in the case of swapping.
		- It demands programmer intervention.
		- It is hard to allocate contagious memory to partition as it is of its variable size.
		- This is costly memory management algorithm. 

15) when would you load into memory the pages of a program that just started?

	load it only when it's necessary to avoid allocating pages that will not be used 

16) when does a process change its state from RUN to READY?

	when it hasn't finished executing after its small time quant is over, it gets sent back to ready and lets another process run its course during its own time quant, and when that finishes, the process which got sent to ready will now run again
	
17) Given a unix file system configured with a block size of B bytes that can contain A addresses, and i-nodes having S direct link, one simple indirection link, and one triple indirection link, give the formula for the maximum file size possible.
 
	N^2 + N^3
	
18) Give a method from preventing deadlocks
	
	Eliminate circular wait: pick an order to lock resources and stick to it
	
19) What is a binary semaphore and what is the effect of its P method, when called by multiple concurrent processes/threads?
	  
	  A binary semaphore is also known as mutex lock. It can have only two values – 0 and 1. Its value is initialized to 1. It is used to implement the solution of critical section problems with multiple processes.
	
	  Method P: If the semaphore is unlocked, it becomes locked and the call returns, allowing the thread to continue. If the semaphore is locked, the thread is blocked and placed in a queue Q of waiting threads.
	  




SUBIECT 24 iun 2019

1) shell cmd that contain at least 1 timestamp hh:mm:ss:sss (08:04:14:893)

	grep -E "0+[0-9]:0+[0-9]:[0-9][0-9]:[0-9][0-9][0-9]" a.txt
	
2) shell cmd that swaps pairs (vowel, odd digit) (a52b7 -> 5a2b7)

	sed -E "s/([aeiouAEIOU])([13579])/\2\1/gi" b.txt
	
3) display all unique appearances of pi with 2 or more decimals

	grep -E "(3\.14)\d*" a.txt
	
4) shell script that calculates the avg nr of lines of code with the extension ".sh" in the current dir ignoring comment lines, lines with only spaces/tabs

	#!/bin/bash

	count=0
	files=0

	for file in $(find -type f -name "*.sh"); do
        files=$(find -type f -name "*.sh" | wc -l)
        count=$(cat $file | wc -l)
	done
	
	echo "avg = $(($count/$files))"
	
5) if(fork() || fork()) fork(); how many processes? 
		8 procs
		
             P
          P       C1
	    P  C2   C1  C3
	            C1
	          C1  C4
	          
6) consumer-producer with buffer N -> semaphores and their values
	
	we will use N semaphores with the value set to 0
	









































