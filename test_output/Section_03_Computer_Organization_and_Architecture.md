# Section 3: Computer Organization and Architecture

*Total Questions in this section: 11*

---

### [GATE 2024 (CS2), Q.4]

Q.4 
For positive non-zero real variables 𝑥 and 𝑦, if  
ln (𝑥+ 𝑦
2
) = 1
2 [ln⁡(𝑥) + ln⁡(𝑦)] 
 then, the value of  
𝑥
𝑦+
𝑦
𝑥  is 

(A) 
1 
(B) 
(C) 
2 
(D) 
4

---

### [GATE 2024 (CS2), Q.5]

Q.5 
In the sequence 6, 9, 14, x, 30, 41, a possible value of 𝑥 is 

(A) 
25 
(B) 
21 
(C) 
18 
(D) 
20

---

### [GATE 2024 (CS2), Q.11]

Q.11 
Consider a computer with a 4 MHz processor. Its DMA controller can transfer  
8 bytes in 1 cycle from a device to main memory through cycle stealing at regular 
intervals. Which one of the following is the data transfer rate (in bits per second) of 
the DMA controller if 1% of the processor cycles are used for DMA? 

(A) 
2,56,000 
(B) 
3,200 
(C) 
25,60,000  
(D) 
32,000

---

### [GATE 2024 (CS2), Q.16]

Q.16 
Let 𝑓(𝑥) be a continuous function from ℝ to ℝ such that  

 𝑓(𝑥) = 1 −𝑓(2 −𝑥)   

Which one of the following options is the CORRECT value of ∫𝑓(𝑥)𝑑𝑥
2
0
 ? 

(A) 
0  
(B) 
1  
(C) 
2  
(D) 
−1

---

### [GATE 2024 (CS2), Q.31]

Q.31 
An instruction format has the following structure:  
Instruction Number: Opcode destination reg, source reg-1, source reg-2 
Consider the following sequence of instructions to be executed in a pipelined 
processor:  
     I1: DIV R3, R1, R2 
     I2: SUB R5, R3, R4 
     I3: ADD R3, R5, R6 
     I4: MUL R7, R3, R8 
Which of the following statements is/are TRUE? 

(A) 
There is a RAW dependency on R3 between I1 and I2 
(B) 
There is a WAR dependency on R3 between I1 and I3 
(C) 
There is a RAW dependency on R3 between I2 and I3 
(D) 
There is a WAW dependency on R3 between I3 and I4

---

### [GATE 2024 (CS2), Q.33]

Q.33 
Consider the following C function definition. 
int fX(char *a){ 
    char *b = a; 
    while(*b) 
        b++; 
    return b - a;} 
Which of the following statements is/are TRUE? 
(A) 
The function call fX(”abcd”) will always return a value  
(B) 
Assuming a character array c is declared as char c[] = ”abcd” in main(), 
the function call fX(c)will always return a value 
(C)  
The code of the function will not compile 
(D) 
Assuming a character pointer c is declared as char *c = ”abcd” in main(), 
the function call fX(c)will always return a value

---

### [GATE 2024 (CS2), Q.35]

Q.35 
Let 𝐴⁡be an array containing integer values. The distance of 𝐴 is defined as the 
minimum number of elements in 𝐴 that must be replaced with another integer so 
that the resulting array is sorted in non-decreasing order. The distance of the array 
[2, 5, 3, 1, 4, 2, 6] is ___________

---

### [GATE 2024 (CS2), Q.42]

Q.42 

Consider an array X that contains n positive integers. A subarray of X is defined to 
be a sequence of array locations with consecutive indices.  
The C code snippet given below has been written to compute the length of the 
longest subarray of X that contains at most two distinct integers. The code has two 
missing expressions labelled (𝑃)⁡and (𝑄).  
int first=0, second=0, len1=0, len2=0, maxlen=0; 
for (int i=0; i < n; i++) { 
  if (X[i] == first) {  
    len2++; len1++;  
  } else if (X[i] == second) { 
    len2++; 
    len1 = ⁡⁡⁡⁡⁡(𝑃)⁡⁡⁡⁡⁡⁡⁡;  
    second = first; 
  } else { 
    len2 = ⁡⁡⁡⁡⁡(𝑄)⁡⁡⁡⁡⁡⁡; 
    len1 = 1; second = first; 
  } 
  if (len2 > maxlen) {  
    maxlen = len2;  
  } 
  first = X[i]; 
} 
Which one of the following options gives the CORRECT missing expressions? 
(Hint: At the end of the i-th iteration, the value of len1 is the length of the longest 
subarray ending with X[i] that contains all equal values, and len2 is the length 
of the longest subarray ending with X[i] that contains at most two distinct values.) 

(A) 
 (𝑃) len1+1    (𝑄)  len2+1   
(B) 
 (𝑃) 1         (𝑄)  len1+1    
(C) 
 (𝑃) 1         (𝑄)  len2+1 
(D) 
 (𝑃) len2+1    (𝑄)  len1+1

---

### [GATE 2024 (CS2), Q.57]

Q.57 
A processor with 16 general purpose registers uses a 32-bit instruction format. The 
instruction format consists of an opcode field, an addressing mode field, two register 
operand fields, and a 16-bit scalar field. If 8 addressing modes are to be supported, 
the maximum number of unique opcodes possible for every addressing mode  
is _________

---

### [GATE 2024 (CS2), Q.58]

Q.58 
A non-pipelined instruction execution unit operating at 2 GHz takes an average of 
6 cycles to execute an instruction of a program P. The unit is then redesigned to 
operate on a 5-stage pipeline at 2 GHz. Assume that the ideal throughput of the 
pipelined unit is 1 instruction per cycle. In the execution of program P,  
20% instructions incur an average of 2 cycles stall due to data hazards and  
20% instructions incur an average of 3 cycles stall due to control hazards. The 
speedup (rounded off to one decimal place) obtained by the pipelined design over 
the non-pipelined design is _________

---

### [GATE 2024 (CS2), Q.61]

Q.61 
A processor uses a 32-bit instruction format and supports byte-addressable memory 
access. The ISA of the processor has 150 distinct instructions. The instructions are 
equally divided into two types, namely R-type and I-type, whose formats are shown 
below. 
R-type Instruction Format: 
OPCODE UNUSED DST Register 
SRC Register1 
SRC Register 2 
I-type Instruction Format: 
OPCODE DST Register SRC Register # Immediate value/address 
In the OPCODE, 1 bit is used to distinguish between I-type and R-type instructions 
and the remaining bits indicate the operation. The processor has 50 architectural 
registers, and all register fields in the instructions are of equal size. 
Let 𝑋 be the number of bits used to encode the UNUSED field, 𝑌 be the number 
of bits used to encode the OPCODE field, and 𝑍 be the number of bits used to 
encode the immediate value/address field. The value of 𝑋+ 2𝑌+ 𝑍 is ________
