# Module 09 — Advanced Programming with SCL (Structured Text)

> **Level:** Advanced | **Duration:** ~5 Hours | **Prerequisites:** Module 05, 06

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Write programs using SCL (Structured Control Language)
- Use all control flow statements (IF, CASE, FOR, WHILE, REPEAT)
- Work with arrays and structures in SCL
- Implement mathematical algorithms and state machines
- Create reusable FCs and FBs in SCL
- Understand indirect addressing and pointers

---

## 📖 Lesson 9.1 — Introduction to SCL

### What is SCL?
**SCL (Structured Control Language)** is Siemens' implementation of **IEC 61131-3 Structured Text (ST)**.

- Text-based language (like Pascal/C)
- Best for: **complex calculations, algorithms, loops, arrays**
- Runs identically to LAD/FBD — just different notation
- Can call other blocks (FC, FB) in SCL
- Can be mixed with LAD/FBD in same project

### SCL vs LAD

| Aspect | LAD | SCL |
|---|---|---|
| Type | Graphical | Text |
| Best for | Relay logic, simple bit ops | Math, loops, arrays, algorithms |
| Readability (bit logic) | Better | Harder |
| Readability (calculations) | Harder | Better |
| Debugging | Visual | Textual |

---

## 📖 Lesson 9.2 — SCL Syntax Basics

### Comments
```pascal
// Single line comment

(* 
   Multi-line
   comment
*)
```

### Variable Declaration (in block interface)
```pascal
// In FC/FB interface (same as other languages, defined in TIA Portal interface table)
// Variables are declared in the interface, not in code body

// In SCL body, use # prefix for local variables:
#MyVariable := 10;

// Global DB access:
"Production_DB".Part_Count := 0;

// I/O:
%I0.0        // Input bit
%Q0.0        // Output bit
%MW10        // Memory word
```

### Assignment
```pascal
#Result := #Value1 + #Value2;
"DB1".Temperature := 25.5;
%Q0.0 := TRUE;
```

### Arithmetic Operators

| Operator | Description | Example |
|---|---|---|
| `+` | Addition | `A + B` |
| `-` | Subtraction | `A - B` |
| `*` | Multiplication | `A * B` |
| `/` | Division | `A / B` |
| `MOD` | Modulo (remainder) | `A MOD B` |
| `**` | Power | `A ** 2` |
| `-` | Unary minus | `-A` |

### Comparison Operators

| Operator | Meaning |
|---|---|
| `=` | Equal |
| `<>` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater or equal |
| `<=` | Less or equal |

### Logical Operators

| Operator | Meaning |
|---|---|
| `AND` or `&` | Logical AND |
| `OR` | Logical OR |
| `NOT` | Logical NOT |
| `XOR` | Exclusive OR |

---

## 📖 Lesson 9.3 — IF Statement

### Basic IF

```pascal
IF #Temperature > 80.0 THEN
    #High_Temp_Alarm := TRUE;
END_IF;
```

### IF-ELSE

```pascal
IF #Start_Button AND NOT #Stop_Button THEN
    #Motor_Output := TRUE;
ELSE
    #Motor_Output := FALSE;
END_IF;
```

### IF-ELSIF-ELSE

```pascal
IF #Temp > 100.0 THEN
    #Alarm_Level := 3;     // Critical
ELSIF #Temp > 80.0 THEN
    #Alarm_Level := 2;     // Warning
ELSIF #Temp > 60.0 THEN
    #Alarm_Level := 1;     // Caution
ELSE
    #Alarm_Level := 0;     // Normal
END_IF;
```

### Nested IF

```pascal
IF #System_Running THEN
    IF #Motor_Fault THEN
        #Motor_Output := FALSE;
        #Fault_Light := TRUE;
    ELSIF #Start_Cmd THEN
        #Motor_Output := TRUE;
        #Fault_Light := FALSE;
    END_IF;
END_IF;
```

---

## 📖 Lesson 9.4 — CASE Statement

### CASE for Enumerated States

```pascal
CASE #Machine_State OF
    0:  // IDLE
        #Motor_Output := FALSE;
        #Conveyor := FALSE;
        #Status_Light := FALSE;
        
    1:  // STARTING
        #Motor_Output := TRUE;
        #Status_Light := TRUE;
        
    2:  // RUNNING
        #Motor_Output := TRUE;
        #Conveyor := TRUE;
        #Status_Light := TRUE;
        
    3:  // STOPPING
        #Conveyor := FALSE;
        #Motor_Output := TRUE;  // Wait for conveyor to empty
        
    4:  // FAULTED
        #Motor_Output := FALSE;
        #Conveyor := FALSE;
        #Fault_Light := TRUE;
        
    ELSE:   // Unknown state
        #Machine_State := 0;   // Reset to IDLE
END_CASE;
```

### CASE with Multiple Values

```pascal
CASE #Day_Of_Week OF
    1, 7:   // Weekend
        #Shift_Active := FALSE;
    2, 3, 4, 5, 6:  // Weekday
        #Shift_Active := TRUE;
END_CASE;
```

---

## 📖 Lesson 9.5 — FOR Loop

### Basic FOR Loop

```pascal
// Count from 1 to 10
FOR #i := 1 TO 10 DO
    #Sum := #Sum + #i;
END_FOR;
```

### FOR with Step

```pascal
// Count from 0 to 100 in steps of 10
FOR #i := 0 TO 100 BY 10 DO
    // Do something every 10 steps
    #Array_Values[#i / 10] := #i;
END_FOR;

// Count backwards
FOR #i := 10 TO 0 BY -1 DO
    #Countdown[#i] := #i;
END_FOR;
```

### FOR with Array Processing

```pascal
// Find maximum value in sensor array
#Max_Value := #Sensor_Array[0];
FOR #i := 1 TO 9 DO
    IF #Sensor_Array[#i] > #Max_Value THEN
        #Max_Value := #Sensor_Array[#i];
        #Max_Index := #i;
    END_IF;
END_FOR;
```

### Calculate Array Average

```pascal
#Total := 0.0;
FOR #i := 0 TO 9 DO
    #Total := #Total + #Sensor_Array[#i];
END_FOR;
#Average := #Total / 10.0;
```

---

## 📖 Lesson 9.6 — WHILE and REPEAT Loops

### WHILE Loop (condition checked before)

```pascal
// WHILE condition is true, execute loop
#Index := 0;
WHILE #Index < 10 AND #Array[#Index] <> 0 DO
    #Sum := #Sum + #Array[#Index];
    #Index := #Index + 1;
END_WHILE;
```

### REPEAT-UNTIL Loop (condition checked after)

```pascal
// Execute at least once, then check condition
#Attempt := 0;
REPEAT
    #Attempt := #Attempt + 1;
    #Result := FC_Try_Connect();
UNTIL #Result = TRUE OR #Attempt >= 5
END_REPEAT;
```

### EXIT — Break out of loop

```pascal
FOR #i := 0 TO 99 DO
    IF #Data_Array[#i] = 0 THEN
        EXIT;   // Stop searching when empty slot found
    END_IF;
    #Count := #Count + 1;
END_FOR;
```

### CONTINUE — Skip iteration

```pascal
FOR #i := 0 TO 9 DO
    IF #Sensor_Array[#i] < 0.0 THEN
        CONTINUE;   // Skip invalid readings
    END_IF;
    #Valid_Sum := #Valid_Sum + #Sensor_Array[#i];
    #Valid_Count := #Valid_Count + 1;
END_FOR;
```

> ⚠️ **Caution:** Avoid infinite loops in PLCs! Always ensure exit condition is reachable.

---

## 📖 Lesson 9.7 — Working with Arrays in SCL

### Declaring Array in DB

```pascal
// In DB interface or UDT:
Temperatures    : ARRAY[0..9] OF REAL;
Recipe_Steps    : ARRAY[1..10] OF INT;
History_Buffer  : ARRAY[0..99] OF REAL;
```

### Accessing Array Elements

```pascal
"MyDB".Temperatures[0] := 25.5;    // Set first element
#Temp_Value := "MyDB".Temperatures[5]; // Get 6th element

// Dynamic index (variable as index)
"MyDB".Temperatures[#Index] := #New_Value;
```

### Shift Array (FIFO Buffer)

```pascal
// Shift all values right (oldest at index 9, newest at index 0)
FOR #i := 9 TO 1 BY -1 DO
    "History_DB".Buffer[#i] := "History_DB".Buffer[#i - 1];
END_FOR;
"History_DB".Buffer[0] := #New_Value;   // Insert new value at front
```

### Multi-Dimensional Arrays

```pascal
// 2D array: 5 recipes × 8 parameters each
Recipe_Matrix : ARRAY[0..4, 0..7] OF REAL;

// Access:
"Recipe_DB".Recipe_Matrix[2, 3] := 75.0;  // Recipe 3, Parameter 4
```

---

## 📖 Lesson 9.8 — State Machine in SCL

### State Machine Concept

```pascal
// States defined as constants
CONST
    STATE_IDLE      : INT := 0;
    STATE_STARTING  : INT := 1;
    STATE_RUNNING   : INT := 2;
    STATE_STOPPING  : INT := 3;
    STATE_FAULTED   : INT := 4;
END_CONST;
```

### Complete State Machine FB (SCL)

```pascal
FUNCTION_BLOCK FB_StateMachine
VAR_INPUT
    Start_Cmd       : BOOL;
    Stop_Cmd        : BOOL;
    Fault_Input     : BOOL;
    Fault_Reset     : BOOL;
END_VAR

VAR_OUTPUT
    Motor_Output    : BOOL;
    Running_FB      : BOOL;
    Faulted_FB      : BOOL;
    State_Out       : INT;
END_VAR

VAR
    State           : INT;
    Start_Timer     : TON;
    Stop_Timer      : TON;
END_VAR

// ─── State Machine Logic ───
CASE #State OF

    0: // IDLE
        #Motor_Output := FALSE;
        #Running_FB := FALSE;
        IF #Start_Cmd AND NOT #Fault_Input THEN
            #State := 1;
        END_IF;
        
    1: // STARTING (wait 2 seconds)
        #Motor_Output := TRUE;
        #Start_Timer(IN := TRUE, PT := T#2S);
        IF #Start_Timer.Q THEN
            #Start_Timer(IN := FALSE);
            #State := 2;
        END_IF;
        IF #Fault_Input THEN
            #Start_Timer(IN := FALSE);
            #State := 4;
        END_IF;
        
    2: // RUNNING
        #Motor_Output := TRUE;
        #Running_FB := TRUE;
        IF #Stop_Cmd THEN
            #State := 3;
        END_IF;
        IF #Fault_Input THEN
            #State := 4;
        END_IF;
        
    3: // STOPPING (wait 1 second)
        #Running_FB := FALSE;
        #Stop_Timer(IN := TRUE, PT := T#1S);
        IF #Stop_Timer.Q THEN
            #Stop_Timer(IN := FALSE);
            #Motor_Output := FALSE;
            #State := 0;
        END_IF;
        
    4: // FAULTED
        #Motor_Output := FALSE;
        #Running_FB := FALSE;
        #Faulted_FB := TRUE;
        IF #Fault_Reset AND NOT #Fault_Input THEN
            #Faulted_FB := FALSE;
            #State := 0;
        END_IF;
        
    ELSE:
        #State := 0;    // Safe default
        
END_CASE;

#State_Out := #State;
```

---

## 📖 Lesson 9.9 — Mathematical Functions

### Built-in Math Functions

| Function | Description | Example |
|---|---|---|
| `ABS(x)` | Absolute value | `ABS(-5.0)` → 5.0 |
| `SQRT(x)` | Square root | `SQRT(16.0)` → 4.0 |
| `SQR(x)` | Square (x²) | `SQR(4.0)` → 16.0 |
| `EXP(x)` | e^x | `EXP(1.0)` → 2.718 |
| `LN(x)` | Natural log | `LN(2.718)` → 1.0 |
| `LOG(x)` | Base-10 log | `LOG(100.0)` → 2.0 |
| `SIN(x)` | Sine (radians) | `SIN(3.14159/2)` → 1.0 |
| `COS(x)` | Cosine | `COS(0.0)` → 1.0 |
| `TAN(x)` | Tangent | `TAN(3.14159/4)` → 1.0 |
| `ASIN(x)` | Arc sine | `ASIN(1.0)` → 1.571 |
| `ACOS(x)` | Arc cosine | — |
| `ATAN(x)` | Arc tangent | — |
| `TRUNC(x)` | Truncate to integer | `TRUNC(3.7)` → 3 |
| `ROUND(x)` | Round to nearest | `ROUND(3.5)` → 4 |
| `CEIL(x)` | Round up | `CEIL(3.1)` → 4 |
| `FLOOR(x)` | Round down | `FLOOR(3.9)` → 3 |

### Engineering Calculations Example

```pascal
// Flow calculation (using Bernoulli)
// Q = Cd × A × SQRT(2 × ΔP / ρ)
#Flow_Rate := #Cd * #Pipe_Area * SQRT(2.0 * #Delta_Pressure / #Density);

// Temperature conversion
#Temp_F := (#Temp_C * 9.0 / 5.0) + 32.0;
#Temp_K := #Temp_C + 273.15;

// Moving average (last 10 samples)
#Sum := 0.0;
FOR #i := 0 TO 9 DO
    #Sum := #Sum + #Sample_Buffer[#i];
END_FOR;
#Moving_Average := #Sum / 10.0;
```

---

## 📖 Lesson 9.10 — Type Conversions in SCL

### Explicit Conversion Functions

```pascal
// Integer to Real
#Real_Value := INT_TO_REAL(#Int_Value);
#Real_Value := DINT_TO_REAL(#DInt_Value);

// Real to Integer (rounds)
#Int_Value := REAL_TO_INT(#Real_Value);
#DInt_Value := REAL_TO_DINT(#Real_Value);

// Using CONVERT/TRUNC
#Int_Value := TRUNC(#Real_Value);    // Truncate decimal
#Int_Value := ROUND(#Real_Value);    // Round to nearest

// Word <-> Int
#Int_Value := WORD_TO_INT(#Word_Value);
#Word_Value := INT_TO_WORD(#Int_Value);
```

### Implicit Conversion
SCL can sometimes auto-convert compatible types:
```pascal
// INT + DINT → DINT (auto-widened)
#DINT_result := #INT_val + #DINT_val;  // OK

// REAL + INT → NOT allowed automatically — must convert
#REAL_result := #REAL_val + INT_TO_REAL(#INT_val);  // Must convert
```

---

## 📖 Lesson 9.11 — Recipe Management System (Complete Example)

```pascal
FUNCTION FC_Load_Recipe : BOOL
VAR_INPUT
    Recipe_Number : INT;
END_VAR
VAR_OUTPUT
    Loaded : BOOL;
END_VAR
VAR_TEMP
    i : INT;
END_VAR

// Validate recipe number
IF #Recipe_Number < 1 OR #Recipe_Number > 5 THEN
    #Loaded := FALSE;
    RETURN;
END_IF;

// Load recipe parameters from recipe DB into active settings
FOR #i := 0 TO 7 DO
    "Active_Recipe_DB".Parameters[#i] := 
        "Recipe_DB".Recipes[#Recipe_Number - 1, #i];
END_FOR;

"Active_Recipe_DB".Recipe_Number := #Recipe_Number;
"Active_Recipe_DB".Load_Time := TIME_OF_DAY();
#Loaded := TRUE;
```

---

## ✅ Module 9 — Review Questions

1. What is SCL and when should you use it instead of LAD?
2. What is the difference between WHILE and REPEAT-UNTIL?
3. How do you access element 5 of an array `Data_Array` in SCL?
4. Write an IF-ELSIF statement for 4 temperature alarm levels.
5. What does EXIT do inside a FOR loop?
6. Write a FOR loop that calculates the sum of array elements 0–9.
7. What is a state machine and what are its advantages?
8. What function gives you the square root in SCL?
9. Why must you use INT_TO_REAL() when adding INT to REAL?
10. What does the CASE ELSE block do?

---

## 🔬 Practical Exercise 9.1 — Batch Recipe Controller

**Task:** Implement a batch recipe controller in SCL:
1. Create DB with 5 recipes × 6 parameters (Temperature_SP, Speed_SP, Mix_Time, Dose_Volume, Pressure_SP, Cool_Time)
2. Create FC_Load_Recipe to copy recipe to active DB
3. Create FB_Batch_Machine with state machine:
   - States: IDLE, HEATING, DOSING, MIXING, COOLING, COMPLETE
   - Each state uses correct recipe parameter
   - Timers for each phase
4. Implement in OB1 with HMI-connected recipe number input

---

*Previous: [Module 08](../Module_08_HMI_Communication/README.md) | Next: [Module 10](../Module_10_Safety_Diagnostics/README.md)*
