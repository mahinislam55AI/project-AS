# 🏭 Siemens S7-200 PLC Programming Course
### Using STEP 7-Micro/WIN Software

---

> **Course Level:** Beginner to Advanced  
> **Software:** STEP 7-Micro/WIN (SIMATIC LAD)  
> **Hardware:** Siemens S7-200 CPU 224XP  
> **Programming Language:** Ladder Diagram (LAD)

---

## 📋 Table of Contents

| Module | Topic | Level |
|--------|-------|-------|
| Module 01 | PLC Basic Concept & Introduction | 🟢 Beginner |
| Module 02 | STEP 7-Micro/WIN Software Overview | 🟢 Beginner |
| Module 03 | Bit Logic Instructions | 🟢 Beginner |
| Module 04 | Timer Instructions | 🟡 Intermediate |
| Module 05 | Counter Instructions | 🟡 Intermediate |
| Module 06 | Compare Instructions | 🟡 Intermediate |
| Module 07 | Move Instructions | 🟡 Intermediate |
| Module 08 | Integer Math Instructions | 🟠 Upper-Intermediate |
| Module 09 | Floating-Point Math Instructions | 🟠 Upper-Intermediate |
| Module 10 | Convert Instructions | 🟠 Upper-Intermediate |
| Module 11 | Logical Operations | 🟠 Upper-Intermediate |
| Module 12 | Shift / Rotate Instructions | 🟠 Upper-Intermediate |
| Module 13 | String Instructions | 🔴 Advanced |
| Module 14 | Table Instructions | 🔴 Advanced |
| Module 15 | Program Control Instructions | 🔴 Advanced |
| Module 16 | Interrupt Instructions | 🔴 Advanced |
| Module 17 | Communications | 🔴 Advanced |
| Module 18 | Subroutines & Real-World Projects | 🔴 Advanced |

---

## 🟢 MODULE 01 — PLC Basic Concept & Introduction
> **"শেখার আগে জানা দরকার — PLC কী এবং কেন?"**

### 📚 Course Content:
- **1.1** — PLC কী? (What is a PLC?)
- **1.2** — PLC vs Relay Logic পার্থক্য
- **1.3** — PLC এর সুবিধা ও ব্যবহার ক্ষেত্র (Industry Applications)
- **1.4** — PLC এর মূল অংশসমূহ (CPU, Power Supply, I/O Modules)
- **1.5** — Siemens S7-200 Series পরিচিতি
- **1.6** — CPU 224XP এর Hardware পরিচয় ও Specifications
- **1.7** — Input / Output Wiring (Sourcing & Sinking)
- **1.8** — PLC Scan Cycle (Input → Process → Output)
- **1.9** — S7-200 Memory Organization (I, Q, M, V, T, C, AI, AQ)

---

## 🟢 MODULE 02 — STEP 7-Micro/WIN Software Overview
> **"Software চেনা — প্রোগ্রামিং শুরুর আগের ধাপ"**

### 📚 Course Content:
- **2.1** — STEP 7-Micro/WIN ইন্সটলেশন ও সেটআপ
- **2.2** — Software Interface পরিচয় (Toolbar, Project Tree, Editor)
- **2.3** — নতুন Project তৈরি করা
- **2.4** — Program Block, Symbol Table, Status Chart, Data Block পরিচয়
- **2.5** — System Block — CPU Configuration
- **2.6** — Communications Setup (PC → PLC সংযোগ)
- **2.7** — Set PG/PC Interface সেটআপ
- **2.8** — Program Download ও Upload
- **2.9** — LAD / FBD / STL Editor পরিচয়
- **2.10** — MAIN, SBR_0, INT_0 — Program Structure বোঝা
- **2.11** — Network তৈরি ও Comment যোগ করা
- **2.12** — Program Run, Stop ও Monitor করা

---

## 🟢 MODULE 03 — Bit Logic Instructions
> **"Ladder Programming এর ভিত্তি"**

### 📚 Course Content:
- **3.1** — Normally Open Contact `—| |—` (LD, A, O)
- **3.2** — Normally Closed Contact `—|/|—` (LDN, AN, ON)
- **3.3** — Positive Transition Contact `—|P|—` (Rising Edge)
- **3.4** — Negative Transition Contact `—|N|—` (Falling Edge)
- **3.5** — NOT Instruction `—|NOT|—`
- **3.6** — Output Coil `—( )—` (=)
- **3.7** — Set Coil `—(S)—` ও Reset Coil `—(R)—`
- **3.8** — Immediate Input `—|I|—` ও Immediate Output `—(I)—`
- **3.9** — Set Immediate `—(SI)—` ও Reset Immediate `—(RI)—`
- **3.10** — SR (Set Dominant) ও RS (Reset Dominant) Flip-Flop
- **3.11** — NOP Instruction
- **3.12** — Series ও Parallel Circuit তৈরি
- **3.13** — **Practical Project:** Start-Stop Motor Control Circuit

---

## 🟡 MODULE 04 — Timer Instructions
> **"সময় নিয়ন্ত্রণ শেখা"**

### 📚 Course Content:
- **4.1** — Timer কী এবং কীভাবে কাজ করে?
- **4.2** — Timer Memory Area (T0 ~ T255)
- **4.3** — **TON** — Timer On-Delay (সবচেয়ে বেশি ব্যবহৃত)
- **4.4** — **TONR** — Timer On-Delay Retentive (Accumulated Timer)
- **4.5** — **TOF** — Timer Off-Delay
- **4.6** — Timer Resolution — 1ms, 10ms, 100ms পার্থক্য
- **4.7** — Timer Preset Value (PT) ও Accumulated Value (AT)
- **4.8** — **BGN_ITIME** ও **CAL_ITIME** — Interval Timer Instructions
- **4.9** — Timer Reset করার পদ্ধতি
- **4.10** — **Practical Project:** Automatic Light ON/OFF with Delay

---

## 🟡 MODULE 05 — Counter Instructions
> **"গণনা করা শেখা"**

### 📚 Course Content:
- **5.1** — Counter কী এবং কখন ব্যবহার হয়?
- **5.2** — Counter Memory Area (C0 ~ C255)
- **5.3** — **CTU** — Count Up Counter
- **5.4** — **CTD** — Count Down Counter
- **5.5** — **CTUD** — Count Up/Down Counter
- **5.6** — **HDEF** — High Speed Counter Definition
- **5.7** — **HSC** — High Speed Counter (উচ্চগতির গণনা)
- **5.8** — **PLS** — Pulse Output Instruction
- **5.9** — Counter Preset Value (PV) ও Current Value (CV)
- **5.10** — Counter Reset করার পদ্ধতি
- **5.11** — **Practical Project:** Bottle Counting System on Conveyor Belt

---

## 🟡 MODULE 06 — Compare Instructions
> **"মান তুলনা করা শেখা"**

### 📚 Course Content:
- **6.1** — Compare Instruction কী এবং কেন দরকার?
- **6.2** — Byte (B) Compare:
  - `==B` Equal | `<>B` Not Equal | `>=B` Greater or Equal
  - `<=B` Less or Equal | `>B` Greater | `<B` Less
- **6.3** — Integer (I) Compare:
  - `==I`, `<>I`, `>=I`, `<=I`, `>I`, `<I`
- **6.4** — Double Integer (DI) Compare:
  - `==DI`, `<>DI`, `>=DI`, `<=DI`, `>DI`, `<DI`
- **6.5** — Real (R) / Floating-Point Compare:
  - `==R`, `<>R`, `>=R`, `<=R`, `>R`, `<R`
- **6.6** — String (S) Compare:
  - `==S`, `<>S`
- **6.7** — **Practical Project:** Temperature Range Alarm System

---

## 🟡 MODULE 07 — Move Instructions
> **"Data এক জায়গা থেকে অন্য জায়গায় নেওয়া"**

### 📚 Course Content:
- **7.1** — Move Instruction কী?
- **7.2** — **MOV_B** — Move Byte
- **7.3** — **MOV_W** — Move Word
- **7.4** — **MOV_DW** — Move Double Word
- **7.5** — **MOV_R** — Move Real (Floating-Point)
- **7.6** — **BLKMOV_B** — Block Move Byte
- **7.7** — **BLKMOV_W** — Block Move Word
- **7.8** — **BLKMOV_D** — Block Move Double Word
- **7.9** — **SWAP** — Swap Bytes in a Word
- **7.10** — **MOV_BIR** — Move Byte Immediate Read
- **7.11** — **MOV_BIW** — Move Byte Immediate Write
- **7.12** — **Practical Project:** Recipe Data Transfer System

---

## 🟠 MODULE 08 — Integer Math Instructions
> **"পূর্ণসংখ্যার গণিত"**

### 📚 Course Content:
- **8.1** — Integer Math কেন দরকার?
- **8.2** — **ADD_I** — Add Integer | **ADD_DI** — Add Double Integer
- **8.3** — **SUB_I** — Subtract Integer | **SUB_DI** — Subtract Double Integer
- **8.4** — **MUL** — Multiply (16×16=32) | **MUL_I** — Multiply Integer | **MUL_DI** — Multiply Double Integer
- **8.5** — **DIV** — Divide (32÷16) | **DIV_I** — Divide Integer | **DIV_DI** — Divide Double Integer
- **8.6** — **INC_B** — Increment Byte | **INC_W** — Increment Word | **INC_DW** — Increment DWord
- **8.7** — **DEC_B** — Decrement Byte | **DEC_W** — Decrement Word | **DEC_DW** — Decrement DWord
- **8.8** — Overflow ও Error Flag (SM1.0, SM1.1)
- **8.9** — **Practical Project:** Production Rate Calculator

---

## 🟠 MODULE 09 — Floating-Point Math Instructions
> **"দশমিক সংখ্যার গণিত ও PID Control"**

### 📚 Course Content:
- **9.1** — Floating-Point Number কী? (IEEE 754 Format)
- **9.2** — **ADD_R** — Add Real | **SUB_R** — Subtract Real
- **9.3** — **MUL_R** — Multiply Real | **DIV_R** — Divide Real
- **9.4** — **SQRT** — Square Root
- **9.5** — **SIN** — Sine | **COS** — Cosine | **TAN** — Tangent
- **9.6** — **LN** — Natural Logarithm | **EXP** — Exponential
- **9.7** — **PID** — PID Controller Instruction (অত্যন্ত গুরুত্বপূর্ণ!)
  - PID Loop Table
  - Proportional, Integral, Derivative Gain
  - PID Tuning পদ্ধতি
- **9.8** — **Practical Project:** PID Temperature Control System

---

## 🟠 MODULE 10 — Convert Instructions
> **"Data Type পরিবর্তন করা"**

### 📚 Course Content:
- **10.1** — Convert Instruction কেন দরকার?
- **10.2** — **B_I** — Byte to Integer | **I_B** — Integer to Byte
- **10.3** — **I_DI** — Integer to Double Integer | **DI_I** — Double Integer to Integer
- **10.4** — **I_S** — Integer to Real (Floating) | **DI_R** — Double Integer to Real
- **10.5** — **DI_S** — Double Integer to String
- **10.6** — **BCD_I** — BCD to Integer | **I_BCD** — Integer to BCD
- **10.7** — **ROUND** — Round Real to Double Integer
- **10.8** — **TRUNC** — Truncate Real to Double Integer
- **10.9** — **R_S** — Real to String
- **10.10** — **ITA** — Integer to ASCII | **DTA** — Double Integer to ASCII
- **10.11** — **RTA** — Real to ASCII | **ATH** — ASCII to Hex | **HTA** — Hex to ASCII
- **10.12** — **S_I** — String to Integer | **S_DI** — String to Double Integer | **S_R** — String to Real
- **10.13** — **DECO** — Decode | **ENCO** — Encode
- **10.14** — **SEG** — Seven Segment Decode
- **10.15** — **Practical Project:** 7-Segment Display Controller

---

## 🟠 MODULE 11 — Logical Operations
> **"Bit-wise Logic"**

### 📚 Course Content:
- **11.1** — Logical Operation কী?
- **11.2** — **AND** — Byte/Word/DWord AND
- **11.3** — **OR** — Byte/Word/DWord OR
- **11.4** — **XOR** — Byte/Word/DWord XOR
- **11.5** — **INV** — Invert (1's Complement)
- **11.6** — Masking Technique (Bit Masking দিয়ে নির্দিষ্ট Bit নিয়ন্ত্রণ)
- **11.7** — **Practical Project:** Status Byte Masking in Process Control

---

## 🟠 MODULE 12 — Shift / Rotate Instructions
> **"Data কে বাম বা ডানে সরানো"**

### 📚 Course Content:
- **12.1** — Shift ও Rotate এর পার্থক্য
- **12.2** — **SHL_B/W/DW** — Shift Left Byte/Word/DWord
- **12.3** — **SHR_B/W/DW** — Shift Right Byte/Word/DWord
- **12.4** — **ROL_B/W/DW** — Rotate Left Byte/Word/DWord
- **12.5** — **ROR_B/W/DW** — Rotate Right Byte/Word/DWord
- **12.6** — **SHRB** — Shift Register Bit (Sequencer হিসেবে ব্যবহার)
- **12.7** — **Practical Project:** Running Light / Knight Rider Effect

---

## 🔴 MODULE 13 — String Instructions
> **"Text ও Message নিয়ে কাজ"**

### 📚 Course Content:
- **13.1** — String Memory Format (S Data Type)
- **13.2** — **SLEN** — String Length
- **13.3** — **SCAT** — String Concatenate
- **13.4** — **SCPY** — String Copy
- **13.5** — **SSCPY** — Substring Copy
- **13.6** — **SFND** — String Find
- **13.7** — **CFND** — Character Find
- **13.8** — **Practical Project:** HMI Message Display System

---

## 🔴 MODULE 14 — Table Instructions
> **"Array / List আকারে Data সংরক্ষণ"**

### 📚 Course Content:
- **14.1** — Table (TBL) কী এবং Structure
- **14.2** — **ATT** — Add to Table
- **14.3** — **LIFO** — Last In First Out (Stack)
- **14.4** — **FIFO** — First In First Out (Queue)
- **14.5** — **FND=, FND<>, FND<, FND>** — Table Find Operations
- **14.6** — **FILL** — Fill Memory with Value
- **14.7** — **Practical Project:** Data Logging System

---

## 🔴 MODULE 15 — Program Control Instructions
> **"Program এর Flow নিয়ন্ত্রণ"**

### 📚 Course Content:
- **15.1** — **END** — Conditional End of Program
- **15.2** — **STOP** — Stop CPU
- **15.3** — **WDR** — Watchdog Reset
- **15.4** — **JMP** — Jump to Label | **LBL** — Label
- **15.5** — **CALL** — Call Subroutine | **RET** — Return from Subroutine
- **15.6** — **FOR** — For Loop | **NEXT** — Next Loop
- **15.7** — **DLED** — Diagnostic LED
- **15.8** — **Practical Project:** Multi-Step Sequential Process Control

---

## 🔴 MODULE 16 — Interrupt Instructions
> **"জরুরি ঘটনায় সাথে সাথে সাড়া দেওয়া"**

### 📚 Course Content:
- **16.1** — Interrupt কী এবং কখন ব্যবহার হয়?
- **16.2** — Interrupt Priority ও Types (I/O, Timer, Communication)
- **16.3** — **ATCH** — Attach Interrupt Routine
- **16.4** — **DTCH** — Detach Interrupt Routine
- **16.5** — **ENI** — Enable Interrupt | **DISI** — Disable Interrupt
- **16.6** — **CRETI** — Conditional Return from Interrupt
- **16.7** — Interrupt Event Table (Event 0 ~ 33)
- **16.8** — **Practical Project:** Emergency Stop with Interrupt

---

## 🔴 MODULE 17 — Communications
> **"PLC থেকে PLC বা HMI সংযোগ"**

### 📚 Course Content:
- **17.1** — S7-200 Communication Ports (Port 0, Port 1)
- **17.2** — PPI Protocol (Point-to-Point Interface)
- **17.3** — **NETR** — Network Read | **NETW** — Network Write
- **17.4** — Freeport Communication Mode
- **17.5** — **XMT** — Transmit | **RCV** — Receive
- **17.6** — USS Protocol (Variable Speed Drive Control)
- **17.7** — Modbus RTU Protocol
- **17.8** — S7-200 ও HMI (TD400C) সংযোগ
- **17.9** — **Practical Project:** Two PLC Communication System

---

## 🔴 MODULE 18 — Subroutines & Real-World Projects
> **"সব কিছু একসাথে ব্যবহার করে বড় প্রজেক্ট তৈরি"**

### 📚 Course Content:
- **18.1** — Subroutine (SBR) তৈরি ও ব্যবহার
- **18.2** — Local Variable ও Parameter Passing
- **18.3** — Structured Programming পদ্ধতি
- **18.4** — Cross Reference ব্যবহার
- **18.5** — Status Chart দিয়ে Debug করা
- **18.6** — Data Block এ Initial Value দেওয়া

### 🏗️ Real-World Projects:
| # | Project Name | ব্যবহৃত Instructions |
|---|-------------|---------------------|
| P1 | 🚦 Traffic Light Control System | Bit Logic, Timer |
| P2 | 🏭 Conveyor Belt with Sorting | Counter, Compare, Move |
| P3 | 💧 Water Level Control System | Compare, Timer, Bit Logic |
| P4 | 🌡️ PID Temperature Controller | FP Math, PID, Analog I/O |
| P5 | 🔢 Batch Process with Recipe | Move, Math, Table |
| P6 | 🚀 Multi-Station Assembly Line | All Instructions Combined |

---

## 📊 Learning Path Summary

```
START
  │
  ▼
🟢 PLC Basics (Module 1-2)         ← সবার আগে এটা জানা দরকার
  │
  ▼
🟢 Bit Logic (Module 3)            ← Ladder Programming এর ভিত্তি
  │
  ▼
🟡 Timer + Counter (Module 4-5)    ← সময় ও গণনা নিয়ন্ত্রণ
  │
  ▼
🟡 Compare + Move (Module 6-7)     ← Data নিয়ে কাজ শুরু
  │
  ▼
🟠 Math Operations (Module 8-9)    ← গণিত ও PID
  │
  ▼
🟠 Convert + Logic + Shift (10-12) ← উন্নত Data Processing
  │
  ▼
🔴 String + Table + Control (13-15)← Program কাঠামো
  │
  ▼
🔴 Interrupt + Comms (16-17)       ← Professional Level
  │
  ▼
🔴 Real Projects (Module 18)       ← শিল্প প্রকল্প
  │
  ▼
✅ COMPLETE — Industry-Ready PLC Programmer!
```

---

## 🛠️ Required Tools & Resources

| Item | Details |
|------|---------|
| **Software** | STEP 7-Micro/WIN V4.0 SP9 |
| **Hardware** | Siemens S7-200 CPU 224XP |
| **Cable** | PC/PPI Cable বা USB-PPI Adapter |
| **Simulator** | S7-200 Simulator (Software-based) |
| **Reference** | S7-200 System Manual (Siemens) |

---

## 📝 Notes

> 💡 **টিপস:** প্রতিটি Module শেষে Practical Project অবশ্যই করবেন। Theory পড়ার চেয়ে হাতে-কলমে করলে ৫ গুণ দ্রুত শেখা যায়।

> ⚠️ **সতর্কতা:** Real Hardware এ Program লোড করার আগে Simulator এ Test করুন।

> 📖 **Reference Manual:** Siemens S7-200 Programmable Controller System Manual (6ES7298-8FA24-8DH0)

---

*Course Outline prepared for S7-200 PLC Programming using STEP 7-Micro/WIN*  
*Siemens SIMATIC S7-200 Series — CPU 224XP REL 02.01*
