# Module 05 — Data Types, Memory Areas & Addressing

> **Level:** Intermediate | **Duration:** ~3.5 Hours | **Prerequisites:** Module 03, 04

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Understand all S7-1200 data types
- Use all memory areas (I, Q, M, DB, L, T, C)
- Apply correct addressing syntax
- Create and use Global Data Blocks
- Understand data block structure and access
- Use indirect addressing and pointers basics

---

## 📖 Lesson 5.1 — S7-1200 Data Types

### Elementary Data Types

| Data Type | Size | Range | Example Value |
|---|---|---|---|
| **BOOL** | 1 bit | TRUE / FALSE | TRUE |
| **BYTE** | 8 bits | 0 to 255 | 16#FF |
| **WORD** | 16 bits | 0 to 65535 | 16#00FF |
| **DWORD** | 32 bits | 0 to 4,294,967,295 | 16#FFFF0000 |
| **LWORD** | 64 bits | 0 to 2^64-1 | — |
| **SINT** | 8 bits signed | -128 to +127 | -50 |
| **INT** | 16 bits signed | -32,768 to +32,767 | 1000 |
| **DINT** | 32 bits signed | -2,147,483,648 to +2,147,483,647 | 100000 |
| **LINT** | 64 bits signed | Very large | — |
| **USINT** | 8 bits unsigned | 0 to 255 | 200 |
| **UINT** | 16 bits unsigned | 0 to 65535 | 50000 |
| **UDINT** | 32 bits unsigned | 0 to 4,294,967,295 | — |
| **REAL** | 32 bits float | ±1.18e-38 to ±3.40e+38 | 3.14 |
| **LREAL** | 64 bits float | Higher precision | 3.141592653 |
| **TIME** | 32 bits | T#-24d to T#+24d | T#10s |
| **LTIME** | 64 bits | High resolution | — |
| **DATE** | 16 bits | D#1990-01-01 to D#2168-12-31 | D#2024-01-15 |
| **TOD** | 32 bits | TOD#0:0:0 to TOD#23:59:59.999 | TOD#14:30:00 |
| **CHAR** | 8 bits | Single ASCII character | 'A' |
| **STRING** | Variable | Up to 254 characters | 'Hello World' |
| **WCHAR** | 16 bits | Unicode character | — |
| **WSTRING** | Variable | Unicode string | — |

### Data Type Sizes (Memory)

```
BOOL  ─── 1 bit   (8 BOOLs = 1 BYTE)
BYTE  ─── 1 byte
WORD  ─── 2 bytes
DWORD ─── 4 bytes
INT   ─── 2 bytes
DINT  ─── 4 bytes
REAL  ─── 4 bytes
LREAL ─── 8 bytes
```

---

## 📖 Lesson 5.2 — Number Systems

### Decimal, Hexadecimal, Binary

| Decimal | Binary | Hexadecimal | BCD |
|---|---|---|---|
| 0 | 0000 0000 | 16#00 | — |
| 10 | 0000 1010 | 16#0A | — |
| 15 | 0000 1111 | 16#0F | — |
| 16 | 0001 0000 | 16#10 | — |
| 255 | 1111 1111 | 16#FF | — |

### Literal Formats in TIA Portal

| Format | Example | Type |
|---|---|---|
| Decimal | `100` | INT/DINT |
| Hexadecimal | `16#64` | HEX |
| Binary | `2#01100100` | BIN |
| Float | `3.14` | REAL |
| Boolean | `TRUE` or `FALSE` | BOOL |
| Time | `T#5s` | TIME |
| String | `'Hello'` | STRING |

---

## 📖 Lesson 5.3 — Memory Areas

### S7-1200 Memory Architecture

```
┌─────────────────────────────────────────────────────────┐
│                 S7-1200 MEMORY MAP                      │
│                                                         │
│  ┌──────────────┐   ┌──────────────┐                   │
│  │  LOAD MEMORY │   │  WORK MEMORY │                   │
│  │  (Flash/MMC) │   │   (SRAM)     │                   │
│  │  - Program   │   │  - OBs/FBs   │                   │
│  │  - DB Data   │   │  - FCs/DBs   │                   │
│  └──────────────┘   │  - I/Q/M/L   │                   │
│                     └──────────────┘                   │
│  ┌──────────────────────────────────┐                   │
│  │         RETENTIVE MEMORY        │                   │
│  │  (Retains values through        │                   │
│  │   power loss — configurable)    │                   │
│  └──────────────────────────────────┘                   │
└─────────────────────────────────────────────────────────┘
```

### Memory Areas Summary

| Area | Identifier | Description | Access |
|---|---|---|---|
| **Process Image Input** | I | Physical input state (read at scan start) | R |
| **Process Image Output** | Q | Physical output state (written at scan end) | R/W |
| **Bit Memory (Merker)** | M | Internal flags/variables | R/W |
| **Data Block** | DB | Structured data storage | R/W |
| **Local/Temp** | L | Local variables in block | R/W |
| **Physical Input** | I:P | Direct hardware input | R |
| **Physical Output** | Q:P | Direct hardware output | R/W |

---

## 📖 Lesson 5.4 — Addressing Syntax

### Address Format

```
% [Area] [Size] [Byte_Number] . [Bit_Number]
│  │      │      │               └─ Bit position (0-7), only for BOOL
│  │      │      └─ Byte address (0, 1, 2...)
│  │      └─ Data size: X(bit), B(byte), W(word), D(dword)
│  └─ Memory area: I, Q, M, DB, L
└─ Siemens prefix (% can be omitted in TIA Portal)
```

### Examples

```
%I0.0    → Input  Bit,  Byte 0, Bit 0   (BOOL)
%I0.1    → Input  Bit,  Byte 0, Bit 1   (BOOL)
%IB0     → Input  Byte, Byte 0          (BYTE = bits 0-7)
%IW0     → Input  Word, starts Byte 0   (WORD = bits 0-15)
%ID0     → Input  DWord,starts Byte 0   (DWORD = bits 0-31)

%Q0.0    → Output Bit,  Byte 0, Bit 0
%QB0     → Output Byte, Byte 0
%QW0     → Output Word, Byte 0+1

%M0.0    → Memory Bit,  Byte 0, Bit 0
%MB0     → Memory Byte, Byte 0
%MW10    → Memory Word, Byte 10+11
%MD20    → Memory DWord,Byte 20-23

%DB1.DBX0.0  → Data Block 1, Bit, Byte 0, Bit 0
%DB1.DBB0    → Data Block 1, Byte 0
%DB1.DBW2    → Data Block 1, Word, Byte 2+3
%DB1.DBD4    → Data Block 1, DWord, Byte 4-7
```

### Byte-Bit Addressing

```
Byte 0:   Bit7  Bit6  Bit5  Bit4  Bit3  Bit2  Bit1  Bit0
          I0.7  I0.6  I0.5  I0.4  I0.3  I0.2  I0.1  I0.0

Byte 1:   Bit7  Bit6  Bit5  Bit4  Bit3  Bit2  Bit1  Bit0
          I1.7  I1.6  I1.5  I1.4  I1.3  I1.2  I1.1  I1.0
```

### Word Addressing (Byte Overlap!)

```
⚠️ IMPORTANT: Bytes OVERLAP in Word/DWord addressing!

MW0  = Byte MB0 (high) + MB1 (low)
MW2  = Byte MB2 (high) + MB3 (low)
MW4  = Byte MB4 (high) + MB5 (low)

MW0 and MB0 SHARE the same memory!
```

**Safe addressing practice:**
```
Use ONLY WORD addresses:    MW0, MW2, MW4, MW6...
Use ONLY BYTE addresses:    MB0, MB1, MB2, MB3...
NEVER mix overlapping addresses in the same area!
```

---

## 📖 Lesson 5.5 — Bit Memory (M Area)

### Usage
- Internal flags (motor running, fault active, etc.)
- Timer/counter auxiliary bits
- Intermediate calculation results
- Communication flags between blocks

### Retentive M Memory
Some M bits can be configured as **retentive** (retain value through power cycle):

TIA Portal → PLC_1 → Properties → General → Retentive Memory
```
Retentive bit memory:  From M0 to MB99  (configurable)
```

### Special Memory Bits (Clock Bits)

| Address | Frequency | Period |
|---|---|---|
| %M0.0 | 10 Hz | 100ms cycle |
| %M0.1 | 5 Hz | 200ms cycle |
| %M0.2 | 2.5 Hz | 400ms cycle |
| %M0.3 | 2 Hz | 500ms cycle |
| %M0.4 | 1.25 Hz | 800ms cycle |
| %M0.5 | 1 Hz | 1s cycle |
| %M0.6 | 0.625 Hz | 1.6s cycle |
| %M0.7 | 0.5 Hz | 2s cycle |

> Enable: TIA Portal → PLC properties → System and clock memory → Enable clock memory byte → Set byte address (e.g., MB0)

### System Memory Bits

| Address | Function |
|---|---|
| %M1.0 | First scan bit (ON for first scan only) |
| %M1.1 | Diagnostic status changed |
| %M1.2 | Always HIGH (=1) |
| %M1.3 | Always LOW (=0) |

> Enable: TIA Portal → PLC properties → System and clock memory → Enable system memory byte → Set byte address (e.g., MB1)

---

## 📖 Lesson 5.6 — Global Data Blocks (Global DB)

### What is a Data Block?
A **Data Block (DB)** is a structured memory area for storing variables permanently accessible from any program block.

### Creating a Global DB

1. Project Tree → **PLC_1 → Program blocks → Add new block**
2. Select **Data block (DB)**
3. Type: **Global DB**
4. Name: `Production_Data`
5. Number: DB1 (auto-assigned)

### Global DB Structure Example

```
DB1 "Production_Data"
─────────────────────────────────────────────────────────────
Name              | Data Type | Offset | Initial Value | Comment
─────────────────────────────────────────────────────────────
Part_Count        | INT       | 0.0    | 0             | Total parts made
Batch_Count       | INT       | 2.0    | 0             | Batches completed
Motor_Hours       | REAL      | 4.0    | 0.0           | Running hours
System_Running    | BOOL      | 8.0    | FALSE         | System active
Recipe_Number     | INT       | 10.0   | 1             | Active recipe
Temperature_SP    | REAL      | 12.0   | 25.0          | Temperature setpoint
Alarm_Code        | INT       | 16.0   | 0             | Active alarm code
Last_Start_Time   | TOD       | 18.0   | TOD#0:0:0     | Last start timestamp
```

### Accessing DB Variables

**Method 1: Symbolic (preferred)**
```
"Production_Data".Part_Count        ← tag name access
"Production_Data".System_Running    ← bool access
```

**Method 2: Absolute**
```
%DB1.DBW0    ← INT at offset 0
%DB1.DBX8.0  ← BOOL at byte 8, bit 0
%DB1.DBD4    ← REAL at offset 4
```

---

## 📖 Lesson 5.7 — DB Optimized vs Standard Access

### Optimized DB (Default in S7-1200)
- No fixed addresses — Siemens assigns memory automatically
- More efficient memory use
- Only symbolic access (`"DB1".Variable`)
- **Cannot** use absolute addressing

### Standard/Classic DB (Legacy)
- Fixed byte offsets (like classic S7-300/400)
- Supports absolute addressing
- Needed for PUT/GET communication or legacy systems

### Changing DB Access Type
Double-click DB → Properties → **Uncheck "Optimized block access"**

> ⚠️ Leave optimized ON for new projects unless you specifically need absolute addressing.

---

## 📖 Lesson 5.8 — MOVE and Data Operations

### MOVE Instruction

```
Copies value from IN to OUT

NETWORK 1
─────────────────────────────────────────────────────────────
    I0.0                MOVE
───┤────────────── EN     ENO
                  IN: MW10 ──── OUT: MW20
─────────────────────────────────────────────────────────────
```

### MOVE_BLK (Block Move)
Copies a block of elements:
```
MOVE_BLK
  IN:    Source array start
  COUNT: Number of elements
  OUT:   Destination start
```

### Data Type Conversion

| Instruction | From | To |
|---|---|---|
| `INT_TO_REAL` | INT | REAL |
| `REAL_TO_INT` | REAL | INT |
| `INT_TO_DINT` | INT | DINT |
| `DINT_TO_INT` | DINT | INT |
| `WORD_TO_INT` | WORD | INT |
| `INT_TO_WORD` | INT | WORD |
| `BCD_TO_INT` | BCD | INT |
| `INT_TO_BCD` | INT | BCD |

### Conversion Example

```
NETWORK 1 — Convert analog raw value to REAL for calculation
    I0.0                  INT_TO_REAL
───┤────── EN  ENO
           IN: IW64 ───── OUT: MD100  (now a REAL value)
```

---

## 📖 Lesson 5.9 — Arrays and Structures (UDTs)

### Arrays
An array is a collection of elements of the **same data type**.

**Define in DB:**
```
Sensor_Values    Array[0..9] of REAL    ← 10 REAL values
Recipe_Steps     Array[0..4] of INT     ← 5 INT values
```

**Access:**
```
"MyDB".Sensor_Values[0]    ← first element
"MyDB".Sensor_Values[5]    ← sixth element
```

### Structures (STRUCT)
A structure groups variables of **different types** together.

**Define in DB or UDT:**
```
STRUCT "Motor_Type"
   Running      : BOOL
   Speed_RPM    : INT
   Current_A    : REAL
   Fault_Code   : INT
   Run_Hours    : REAL
END_STRUCT
```

### User-Defined Types (UDT)
Create reusable custom data types:

Project Tree → **PLC data types → Add new data type**

```
UDT "Motor_Data"
   Running      : BOOL
   Speed_RPM    : INT
   Current_A    : REAL
   Fault_Code   : INT
```

Then use in DB:
```
DB3 "Machine_Motors"
   Motor_1      : "Motor_Data"
   Motor_2      : "Motor_Data"
   Motor_3      : "Motor_Data"
```

---

## ✅ Module 5 — Review Questions

1. What is the size in bytes of: BOOL, INT, DINT, REAL?
2. What is the range of an INT data type?
3. What does `%MW10` mean? What bytes does it occupy?
4. Why must you be careful about overlapping addresses?
5. What is the difference between a Global DB and an Instance DB?
6. What are clock memory bits and how do you enable them?
7. What is the difference between optimized and standard DB access?
8. How do you convert an INT to REAL in TIA Portal?
9. What is an Array and how do you access element 3 of array `Temp_Values`?
10. What does the first-scan bit (M1.0) do and when is it used?

---

## 🔬 Practical Exercise 5.1 — Data Block Design

**Task:** Create a production management DB:
1. Create Global DB `"Production_DB"`
2. Add variables: Part_Count (INT), Batch_Size (INT), Batch_Done (BOOL), Temperature (REAL), Speed_RPM (INT), Last_Recipe (INT)
3. Create a UDT `"Alarm_Type"` with: Active (BOOL), Code (INT), Time (TOD)
4. Add array `Alarms[0..4]` of `"Alarm_Type"` to Production_DB
5. Write a short LAD program to increment Part_Count on sensor pulse

---

*Previous: [Module 04](../Module_04_Timers_Counters/README.md) | Next: [Module 06](../Module_06_Functions_FBs_OBs/README.md)*
