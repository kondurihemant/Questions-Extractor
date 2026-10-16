# Section 8: Operating Systems

*Total Questions in this section: 5*

---

### [GATE 2024 (CS2), Q.24]

Q.24 
Which of the following tasks is/are the responsibility/responsibilities of the memory 
management unit (MMU) in a system with paging-based memory management? 

(A) 
Allocate a new page table for a newly created process 
(B) 
Translate a virtual address to a physical address using the page table 
(C) 
Raise a trap when a virtual address is not found in the page table 
(D) 
Raise a trap when a process tries to write to a page marked with read-only 
permission in the page table

---

### [GATE 2024 (CS2), Q.25]

Q.25 
Consider a process P running on a CPU. Which one or more of the following events 
will always trigger a context switch by the OS that results in process P moving to a 
non-running state (e.g., ready, blocked)? 

(A) 
P makes a blocking system call to read a block of data from the disk 
(B) 
P tries to access a page that is in the swap space, triggering a page fault 
(C) 
An interrupt is raised by the disk to deliver data requested by some other process 
(D) 
A timer interrupt is raised by the hardware

---

### [GATE 2024 (CS2), Q.37]

Q.37 
Consider a single processor system with four processes A, B, C, and D, represented 
as given below, where for each process the first value is its arrival time, and the 
second value is its CPU burst time. 
A (0, 10), B (2, 6), C (4, 3), and D (6, 7). 
Which one of the following options gives the average waiting times when 
preemptive Shortest Remaining Time First (SRTF) and Non-Preemptive Shortest 
Job First (NP-SJF) CPU scheduling algorithms are applied to the processes? 

(A) 
SRTF = 6, NP-SJF = 7 
(B) 
SRTF = 6, NP-SJF = 7.5 
(C) 
SRTF = 7, NP-SJF = 7.5 
(D) 
SRTF = 7, NP-SJF = 8.5

---

### [GATE 2024 (CS2), Q.46]

Q.46 
Consider a multi-threaded program with two threads T1 and T2. The threads share 
two semaphores: s1 (initialized to 1) and s2 (initialized to 0). The threads also 
share a global variable x (initialized to 0). The threads execute the code shown 
below. 

// code of T1 
wait(s1);  
x = x+1;  
print(x);  
wait(s2);  
signal(s1); 
  // code of T2  
  wait(s1);  
  x = x+1;  
  print(x); 
  signal(s2);  
  signal(s1); 

Which of the following outcomes is/are possible when threads T1 and T2 execute 
concurrently? 

(A) 
T1 runs first and prints 1, T2 runs next and prints 2 
(B) 
T2 runs first and prints 1, T1 runs next and prints 2 
(C) 
T1 runs first and prints 1, T2 does not print anything (deadlock) 
(D) 
T2 runs first and prints 1, T1 does not print anything (deadlock)

---

### [GATE 2024 (CS2), Q.64]

Q.64 
Consider a 32-bit system with 4 KB page size and page table entries of size 4 bytes 
each. Assume 1 KB = 210 bytes. The OS uses a 2-level page table for memory 
management, with the page table containing an outer page directory and an inner 
page table. The OS allocates a page for the outer page directory upon process 
creation. The OS uses demand paging when allocating memory for the inner page 
table, i.e., a page of the inner page table is allocated only if it contains at least one 
valid page table entry.  
An active process in this system accesses 2000 unique pages during its execution, 
and none of the pages are swapped out to disk. After it completes the page accesses, 
let X denote the minimum and Y denote the maximum number of pages across the 
two levels of the page table of the process.  
The value of X+Y is ________
