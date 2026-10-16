# Section 7: Compiler Design

*Total Questions in this section: 4*

---

### [GATE 2024 (CS2), Q.21]

Q.21 
Consider the following two sets: 
             Set X                                                                Set Y 
P. Lexical Analyzer                                         1. Abstract Syntax Tree 
Q. Syntax Analyzer                                         2. Token 
R. Intermediate Code Generator                     3. Parse Tree 
S. Code Optimizer                                          4. Constant Folding                   
Which one of the following options is the CORRECT match from Set X to Set Y ? 

(A) 
P – 4; Q – 1; R – 3; S – 2 
(B) 
P – 2; Q – 3; R – 1; S – 4 
(C) 
P – 2; Q – 1; R – 3; S – 4 
(D) 
P – 4; Q – 3; R – 2; S – 1

---

### [GATE 2024 (CS2), Q.29]

Q.29 
Which of the following statements is/are FALSE? 

(A) 
An attribute grammar is a syntax-directed definition (SDD) in which the functions 
in the semantic rules have no side effects 
(B) 
The attributes in a L-attributed definition cannot always be evaluated in a depth-
first order 
(C) 
Synthesized attributes can be evaluated by a bottom-up parser as the input is parsed 
(D) 
All L-attributed definitions based on LR(1) grammar can be evaluated using a 
bottom-up parsing strategy

---

### [GATE 2024 (CS2), Q.40]

Q.40 
Consider the following context-free grammar where the start symbol is 𝑆 and the 
set of terminals is {𝑎,𝑏,𝑐,𝑑}. 
𝑆→𝐴𝑎𝐴𝑏⁡|⁡𝐵𝑏𝐵𝑎 
𝐴→𝑐𝑆⁡|⁡𝜖 
𝐵→𝑑𝑆⁡|⁡𝜖 
The following is a partially-filled LL(1) parsing table. 

𝑎 
𝑏 
𝑐 
𝑑 
$ 
𝑆 
𝑆→𝐴𝑎𝐴𝑏 
𝑆→𝐵𝑏𝐵𝑎 
(1) 
(2) 

𝐴 
𝐴→𝜖 
(3) 
𝐴→𝑐𝑆 

𝐵 
(4) 
𝐵→𝜖 

𝐵→𝑑𝑆 

Which one of the following options represents the CORRECT combination for the 
numbered cells in the parsing table? 
Note: In the options, “blank” denotes that the corresponding cell is empty.   

(A) 
(1) 𝑆→𝐴𝑎𝐴𝑏  (2) 𝑆→𝐵𝑏𝐵𝑎  (3) 𝐴→𝜖  (4) 𝐵→𝜖 
(B) 
(1) 𝑆→𝐵𝑏𝐵𝑎  (2) 𝑆→𝐴𝑎𝐴𝑏  (3) 𝐴→𝜖  (4) 𝐵→𝜖 
(C) 
(1) 𝑆→𝐴𝑎𝐴𝑏  (2) 𝑆→𝐵𝑏𝐵𝑎  (3) blank   (4) blank 
(D) 
(1) 𝑆→𝐵𝑏𝐵𝑎  (2) 𝑆→𝐴𝑎𝐴𝑏  (3) blank  (4) blank

---

### [GATE 2024 (CS2), Q.65]

Q.65 
Consider the following augmented grammar, which is to be parsed with a SLR 
parser. The set of terminals is {𝑎,𝑏,𝑐,𝑑,#,@}  
𝑆′ →𝑆 
𝑆→𝑆𝑆⁡|⁡𝐴𝑎⁡|⁡𝑏𝐴𝑐⁡|⁡𝐵𝑐⁡|⁡𝑏𝐵𝑎 
𝐴→𝑑# 
𝐵→@ 
Let 𝐼0 = 𝐶𝐿𝑂𝑆𝑈𝑅𝐸({𝑆′ →⁡• 𝑆}). The number of items in the set 𝐺𝑂𝑇𝑂(𝐼0, 𝑆)  
is ___________
