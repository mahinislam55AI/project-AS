# Module 06 — Functions, Function Blocks & Organization Blocks

> **Level:** Intermediate | **Duration:** ~4.5 Hours | **Prerequisites:** Module 05

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Understand the difference between FC, FB, and OB
- Create and call Functions (FC) with parameters
- Create Function Blocks (FB) with instance data blocks
- Use multi-instance FBs for reusable components
- Implement startup, cyclic interrupt, and error OBs
- Structure a program using modular programming techniques

---

## 📖 Lesson 6.1 — Program Block Types Review

### Block Hierarchy

```
┌──────────────────────────────────────────────────────────┐
│                   OPERATING SYSTEM (OS)                  │
│  (Controls scan cycle, interrupt handling, diagnostics)  │
└───────────────────────┬──────────────────────────────────┘
                        │ calls
                ┌───────▼────────┐
                │   OB1 (Main)   │  ← Called every scan cycle
                └───────┬────────┘
                        │ calls
          ┌─────────────┼─────────────┐
          │             │             │
    ┌─────▼──────┐ ┌────▼─────┐ ┌────▼─────┐
    │  FC Block  │ │ FB Block │ │ FC Block │
    │(No memory) │ │(Has inst)│ │          │
    └────────────┘ └────┬─────┘ └──────────┘
                        │
                ┌───────▼────────┐
                │  Instance DB   │
                │  (FB memory)   │
                └────────────────┘
```

### Block Type Summary

| Block | Memory | Parameters | Use Case |
|---|---|---|---|
| **OB** | No | Limited | OS entry points (main, startup, interrupt) |
| **FC** | No (only temp) | Yes (IN/OUT/IN_OUT/Return) | Reusable routines, calculations |
| **FB** | Yes (Instance DB) | Yes + STAT | Reusable components with state |
| **DB** | Yes | N/A | Data storage only |

---

## 📖 Lesson 6.2 — Functions (FC)

### What is an FC?
- **No static memory** — variables exist only during execution
- Has **input, output, in/out, return, temp** parameters
- Called like a subroutine
- Best for: calculations, conversions, utility routines

### Creating an FC

1. Project Tree → **Add new block → Function (FC)**
2. Name: `FC_MotorControl`
3. Language: LAD (or SCL)
4. Click OK

### FC Interface Table

```
FC "FC_Motor_Control"
─────────────────────────────────────────────────────────────
Section    | Name          | Data Type | Comment
─────────────────────────────────────────────────────────────
IN         | Start_Cmd     | Bool      | Start command
IN         | Stop_Cmd      | Bool      | Stop command
IN         | Fault_Active  | Bool      | Fault input
OUT        | Motor_Output  | Bool      | Motor contactor
OUT        | Fault_Output  | Bool      | Fault indicator
IN_OUT     | (none)        |           |
RETURN     | (void)        |           |
TEMP       | Temp_Bit      | Bool      | Temporary calc bit
CONSTANT   | (none)        |           |
─────────────────────────────────────────────────────────────
```

### FC Body (LAD)

```
NETWORK 1 — Motor Logic
─────────────────────────────────────────────────────────────
    #Start_Cmd     #Stop_Cmd     #Fault_Active    #Motor_Output
───┤─────────┬───┤/──────────┤/───────────────( )───────────
             │
  #Motor_Out │
───┤─────────┘
─────────────────────────────────────────────────────────────

NETWORK 2 — Fault Output
─────────────────────────────────────────────────────────────
    #Fault_Active
───┤─────────────────────────────────────────( #Fault_Output )
─────────────────────────────────────────────────────────────
```

### Calling an FC in OB1

```
NETWORK 1 — Call Motor FC
─────────────────────────────────────────────────────────────
    FC_Motor_Control
    EN          ENO
    Start_Cmd:  I0.0
    Stop_Cmd:   I0.1
    Fault_Active: I0.2
    Motor_Output: Q0.0
    Fault_Output: Q0.5
─────────────────────────────────────────────────────────────
```

> ⚠️ **FC Rule:** You MUST connect all IN/OUT/IN_OUT parameters when calling an FC.

---

## 📖 Lesson 6.3 — Function Blocks (FB)

### What is an FB?
- Has **static memory** stored in an **Instance Data Block (IDB)**
- Variables persist between scan cycles (STAT section)
- Best for: motors, valves, PIDs, sequences — anything with state
- Each "instance" of an FB has its OWN copy of data

### FC vs FB — Key Difference

```
FC:  Each call runs with new temp data, no memory between calls
FB:  Each instance has own DB — values remembered between scans

Use FC when:     Use FB when:
- No state needed    - State needed (running, fault, timer)
- Calculations       - Equipment control (motor, valve)
- Conversions        - PID controllers
- Utility functions  - Sequential processes
```

### Creating an FB

1. Project Tree → **Add new block → Function Block (FB)**
2. Name: `FB_Motor`
3. Language: LAD

### FB Interface Table

```
FB "FB_Motor"
─────────────────────────────────────────────────────────────
Section | Name           | Data Type | Default | Comment
─────────────────────────────────────────────────────────────
IN      | Start_Cmd      | Bool      | FALSE   | Start command
IN      | Stop_Cmd       | Bool      | FALSE   | Stop command
IN      | Fault_Input    | Bool      | FALSE   | Hardware fault
IN      | Speed_SP       | INT       | 0       | Speed setpoint
OUT     | Running        | Bool      | FALSE   | Motor is running
OUT     | Faulted        | Bool      | FALSE   | Fault indicator
OUT     | Current_Speed  | INT       | 0       | Current speed
STAT    | Run_Latch      | Bool      | FALSE   | Internal latch ← STATIC
STAT    | Fault_Latch    | Bool      | FALSE   | Fault latch    ← STATIC
TEMP    | Temp_Calc      | INT       | 0       | Temp variable
─────────────────────────────────────────────────────────────
```

### FB Body (LAD)

```
NETWORK 1 — Start Logic
─────────────────────────────────────────────────────────────
    #Start_Cmd  #Stop_Cmd   #Fault_Latch   #Running
───┤──────────┬─┤/──────┤─┤/─────────────( )────────
              │
   #Running   │
───┤──────────┘
─────────────────────────────────────────────────────────────

NETWORK 2 — Fault Latch
─────────────────────────────────────────────────────────────
    #Fault_Input
───┤───────────────────────────────────(S #Fault_Latch)───

    #Stop_Cmd
───┤───────────────────────────────────(R #Fault_Latch)───
─────────────────────────────────────────────────────────────

NETWORK 3 — Fault Output
─────────────────────────────────────────────────────────────
    #Fault_Latch
───┤─────────────────────────────────────( #Faulted )────
─────────────────────────────────────────────────────────────
```

### Calling an FB — Creating Instance DB

**Method 1: Single Instance**
When you call FB in OB1, TIA Portal asks for an Instance DB name:

```
NETWORK 1 — Call FB_Motor for Motor 1
─────────────────────────────────────────────────────────────
    FB_Motor [DB1 "Motor1_IDB"]
    EN             ENO
    Start_Cmd:     I0.0       → Running:       Q0.0
    Stop_Cmd:      I0.1       → Faulted:       Q0.5
    Fault_Input:   I0.2
    Speed_SP:      MW10
─────────────────────────────────────────────────────────────

NETWORK 2 — Call FB_Motor for Motor 2 (same FB, different IDB!)
─────────────────────────────────────────────────────────────
    FB_Motor [DB2 "Motor2_IDB"]
    EN             ENO
    Start_Cmd:     I1.0       → Running:       Q1.0
    Stop_Cmd:      I1.1       → Faulted:       Q1.5
    Fault_Input:   I1.2
    Speed_SP:      MW12
─────────────────────────────────────────────────────────────
```

> **Key benefit:** Same FB code controls BOTH motors — only data (IDB) differs!

---

## 📖 Lesson 6.4 — Multi-Instance FBs

### What is Multi-Instance?
Instead of creating a separate IDB for each FB call, the **parent FB** stores instance data internally.

```
Parent FB "FB_Machine"
├── Motor_1 : FB_Motor (multi-instance)
├── Motor_2 : FB_Motor (multi-instance)
└── Valve_1 : FB_Valve (multi-instance)
```

All data stored in ONE instance DB for the parent FB.

### Creating Multi-Instance

In parent FB interface, STAT section:
```
STAT  | Motor_Drive_1  | FB_Motor   |   | Drive 1 instance
STAT  | Motor_Drive_2  | FB_Motor   |   | Drive 2 instance
STAT  | Inlet_Valve    | FB_Valve   |   | Valve instance
```

Calling in parent FB body:
```
NETWORK 1
    #Motor_Drive_1.Start_Cmd := #Start_1_Input;
    // or via LAD call box — selects multi-instance automatically
```

---

## 📖 Lesson 6.5 — Organization Blocks (OB)

### OB Types and Triggers

| OB | Number | Trigger | Use Case |
|---|---|---|---|
| **Program cycle (Main)** | OB1 | Every scan cycle | Main program |
| **Startup** | OB100 | Once on warm restart | Initialization |
| **Time delay interrupt** | OB20-23 | After SRT_DINT delay | Delayed actions |
| **Cyclic interrupt** | OB30-38 | Fixed interval (1ms–60s) | Periodic tasks |
| **Hardware interrupt** | OB40-47 | I/O edge detected | Fast response |
| **Time-of-day interrupt** | OB10-17 | Specific time | Scheduled tasks |
| **Status** | OB55 | Status change | Monitoring |
| **Update** | OB56 | Process update | — |
| **Profile** | OB57 | Profile change | — |
| **Diagnostic error** | OB82 | Hardware fault | Fault handling |
| **Pull/plug of modules** | OB83 | Module change | Hot swap |
| **CPU hardware fault** | OB84 | CPU fault | Fault handling |
| **Program cycle error** | OB85 | OS cycle error | Fault handling |
| **Rack/station failure** | OB86 | DP slave/PN fault | Fault handling |
| **Programming error** | OB121 | Code error | Fault handling |
| **I/O access error** | OB122 | I/O fault | Fault handling |

### OB1 — Main Program Cycle

```
OB1 [Main]
─────────────────────────────────────────────────────────────
NETWORK 1 — Call Motor Control
    FC_Safety_Check
    EN    ENO

NETWORK 2 — Motor 1
    FB_Motor [DB1]
    ...

NETWORK 3 — Conveyor
    FB_Conveyor [DB10]
    ...

NETWORK 4 — Alarm handling
    FC_Alarm_Manager
    EN    ENO
─────────────────────────────────────────────────────────────
```

### OB100 — Startup

```
OB100 [Startup]
─────────────────────────────────────────────────────────────
NETWORK 1 — Initialize outputs to safe state
    MOVE
    EN    ENO
    IN: 0 ─── OUT: QB0   (clear all outputs)

NETWORK 2 — Load default recipe
    MOVE
    EN    ENO
    IN: 1 ─── OUT: "Production_DB".Recipe_Number

NETWORK 3 — Reset fault latches
    M0.0 (always TRUE) ─── (R) Q0.5 (Fault_Light)
─────────────────────────────────────────────────────────────
```

### OB30 — Cyclic Interrupt

```
OB30 [Cyclic interrupt — every 100ms]
─────────────────────────────────────────────────────────────
Used for:
- PID calculations
- Data logging
- Watchdog checks
- Communication tasks

Configuration:
    Properties → Cyclic interrupt → 100ms interval
─────────────────────────────────────────────────────────────
```

### OB40 — Hardware Interrupt

```
OB40 [Hardware interrupt — triggered by I0.0 rising edge]
─────────────────────────────────────────────────────────────
Configuration:
    TIA Portal → PLC Properties → Hardware interrupts
    → Assign I0.0 rising edge to OB40

Use for:
- Emergency stop immediate response
- High-speed counting trigger
- Fast position capture
─────────────────────────────────────────────────────────────
```

---

## 📖 Lesson 6.6 — Modular Program Structure

### Recommended Program Architecture

```
OB1 [Main]
│
├── FC_Safety [Safety checks before anything runs]
│
├── FB_Machine_1 [DB10] [Complete machine 1 logic]
│   ├── FB_Motor_Main [multi-instance]
│   ├── FB_Motor_Feed [multi-instance]
│   ├── FB_Valve_Inlet [multi-instance]
│   └── FB_Conveyor [multi-instance]
│
├── FB_Machine_2 [DB20]
│   └── ...
│
├── FC_Alarms [Alarm collection and management]
│
└── FC_HMI_Handler [HMI data preparation]

OB100 [Startup]
│
└── FC_Initialize [Set safe defaults]

OB30 [100ms Cyclic]
│
└── FC_PID_Tasks [PID and periodic calculations]

OB82 [Diagnostic Error]
│
└── FC_Fault_Log [Log hardware faults]
```

### Programming Principles

| Principle | Description |
|---|---|
| **Single Responsibility** | Each block does ONE thing |
| **Reusability** | Use FB for repeating equipment |
| **Top-down** | OB1 → high level → detail |
| **No global variables** | Pass data through parameters when possible |
| **Named tags** | Never use raw addresses in block code |

---

## 📖 Lesson 6.7 — EN/ENO Mechanism

### What is EN/ENO?

```
EN  = Enable Input  — block executes when EN = TRUE
ENO = Enable Output — passes the EN status (if no error inside)

Chaining blocks with ENO:
    I0.0 ─── EN [FC_1] ENO ─── EN [FC_2] ENO ─── Q0.0
    
    If FC_1 has an error inside, ENO goes FALSE → FC_2 is skipped
```

### ENO Error Handling

```
NETWORK 1
─────────────────────────────────────────────────────────────
    I0.0       MOVE              MOVE
───┤────────── EN  ENO ────── EN   ENO ─── Q0.0 (Success)
               IN:MW10        IN:MW20
               OUT:MW20       OUT:MW30
─────────────────────────────────────────────────────────────
If first MOVE errors → second MOVE blocked → Q0.0 OFF
```

---

## ✅ Module 6 — Review Questions

1. What is the key difference between FC and FB?
2. Why does an FB need an Instance Data Block?
3. What happens to TEMP variables in an FB between scan cycles?
4. What is multi-instance and what is its advantage?
5. List 5 types of OBs and their triggers.
6. When would you use OB100 instead of OB1?
7. What does EN/ENO do and why is chaining useful?
8. When should you use FC vs FB? Give an example of each.
9. What is the recommended modular structure for a machine program?
10. What are STAT variables and how are they different from TEMP?

---

## 🔬 Practical Exercise 6.1 — Reusable Motor FB

**Task:** Create a complete motor control FB:
1. Create `FB_Motor_Control` with full interface:
   - IN: Start, Stop, E_Stop, Overload (all BOOL)
   - IN: Fault_Reset (BOOL)
   - OUT: Running, Faulted (BOOL)
   - STAT: Run_Latch, Fault_Latch (BOOL), Fault_Count (INT)
2. Implement logic: start/stop, fault latch, fault count increment
3. Call the FB twice in OB1 for Motor_1 and Motor_2 with different I/O
4. Add to OB100: reset fault counts and outputs

---

*Previous: [Module 05](../Module_05_Data_Types_Memory/README.md) | Next: [Module 07](../Module_07_Analog_PID/README.md)*
