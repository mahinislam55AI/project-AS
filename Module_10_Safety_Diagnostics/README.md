# Module 10 — Safety, Diagnostics & Best Practices

> **Level:** Advanced | **Duration:** ~4 Hours | **Prerequisites:** All previous modules

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Understand functional safety concepts (IEC 62061 / ISO 13849)
- Implement hardware and software safety measures
- Use diagnostic OBs and error handling
- Read and interpret PLC diagnostic buffers
- Apply industrial programming best practices
- Perform PLC system maintenance and backup

---

## 📖 Lesson 10.1 — Functional Safety Overview

### Safety Standards

| Standard | Scope | Level |
|---|---|---|
| **IEC 62061** | Safety of machinery — electrical | SIL 1/2/3 |
| **ISO 13849** | Safety-related parts of control | PL a/b/c/d/e |
| **IEC 61508** | Functional safety (general) | SIL 1/2/3/4 |
| **IEC 61511** | Process industry safety | SIL 1/2/3 |

### Safety Integrity Levels (SIL)

| SIL | PFH (per hour) | Risk Reduction | Example |
|---|---|---|---|
| SIL 1 | 10⁻⁵ to 10⁻⁶ | 10x–100x | Low-risk conveyor |
| SIL 2 | 10⁻⁶ to 10⁻⁷ | 100x–1000x | Industrial press |
| SIL 3 | 10⁻⁷ to 10⁻⁸ | 1000x–10000x | Chemical reactor |
| SIL 4 | 10⁻⁸ to 10⁻⁹ | Very high | Nuclear/aerospace |

### Performance Levels (PL)

| PL | MTTFd | DC | CCF | Typical Application |
|---|---|---|---|---|
| a | Low | None | Not required | Indicator lights |
| b | Low | Low | Not required | Simple guard |
| c | Medium | Low | Required | Interlocked guard |
| d | High | Medium | Required | Safety light curtain |
| e | High | High | Required | Two-hand control |

---

## 📖 Lesson 10.2 — Safety Hardware

### Safety Relays vs Safety PLC

| Feature | Safety Relay | Safety PLC (F-CPU) |
|---|---|---|
| Complexity | Simple circuits | Complex systems |
| Flexibility | Fixed logic | Programmable |
| SIL capability | Up to SIL 3 | Up to SIL 3 |
| Cost | Lower | Higher |
| Diagnostics | Limited | Extensive |
| Example | Pilz PNOZ | S7-1200F CPU |

### Common Safety Devices

| Device | Function | Wiring |
|---|---|---|
| **E-Stop button** | Manual emergency stop | NC contact, Category 3/4 |
| **Safety light curtain** | Area protection | OSSD outputs |
| **Safety door switch** | Guard monitoring | Coded, dual channel |
| **Safety mat** | Floor area detection | Dual channel |
| **Two-hand control** | Operator presence | Simultaneous operation |
| **Safety relay** | Monitor and switch | Dual channel, timed |

### Two-Channel Safety Circuit

```
Category 3 / PL d E-Stop Circuit:

CH1: +24V ─── E-Stop NC ─── Safety Relay IN1
CH2: +24V ─── E-Stop NC ─── Safety Relay IN2
                                      │
                              Safety Relay Monitoring:
                              - Both channels must be consistent
                              - Detects single failures
                              - NC output to machine power
```

### Safety Wiring Rules
- **Redundant (dual-channel)** circuits for SIL 2+
- **Physically separated** cable routing for redundant channels
- **Cross-fault detection** at safety controller
- **Monitored** manual reset (anti-restart)
- **Regular testing** of safety functions (proof test interval)

---

## 📖 Lesson 10.3 — S7-1200F (Fail-Safe CPU)

### What is S7-1200F?
The **F variants** of S7-1200 CPUs support **STEP 7 Safety** programming for SIL 2 / PL d/e.

| F-CPU | Notes |
|---|---|
| CPU 1214FC | Fail-safe, 14DI/10DQ/2AI |
| CPU 1215FC | Fail-safe, 2x PROFINET |
| CPU 1217FC | Fail-safe, high-speed motion |

### Standard vs Safety Program

```
S7-1200F CPU runs TWO programs:

┌─────────────────────────────────────────┐
│         STANDARD PROGRAM                │
│  (Normal automation, OB1, FBs, etc.)   │
│  Runs at normal scan cycle              │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│          SAFETY PROGRAM (F-Program)     │
│  (Safety functions — E-Stop, guards)   │
│  Runs with higher priority             │
│  Self-checks, cross-validation         │
│  Compiled separately, CRC protected    │
└─────────────────────────────────────────┘
```

### F-I/O Modules
- **F-DI** modules for safety inputs (E-Stop, light curtains)
- **F-DQ** modules for safety outputs (contactors, valves)
- Automatically perform signal self-tests and cross-checks

---

## 📖 Lesson 10.4 — Software Safety Measures

### ⚠️ Software-Only Safety IS NOT Sufficient for SIL

> The PLC program alone CANNOT replace hardware safety devices for SIL-rated functions. Always use:
> - Hardware safety relays or F-CPU for actual safety functions
> - PLC software only for operational control

### Defensive Programming Practices

#### 1. Output Watchdog

```pascal
// Reset all outputs if scan time exceeds limit
// (Usually handled by CPU watchdog, but can add software too)
IF "ScanTime" > T#100ms THEN
    %QB0 := 0;      // Clear all outputs
    %QB1 := 0;
    "Watchdog_Fault" := TRUE;
END_IF;
```

#### 2. Sensor Plausibility Check

```pascal
// Check sensor value is in valid range
IF "Temperature_C" < -10.0 OR "Temperature_C" > 350.0 THEN
    "Sensor_Fault" := TRUE;
    "Temperature_C" := "Last_Valid_Temp";   // Use last known good
ELSE
    "Last_Valid_Temp" := "Temperature_C";
    "Sensor_Fault" := FALSE;
END_IF;
```

#### 3. Output Feedback Check

```pascal
// Verify motor actually started after command
// (Compare command with feedback after startup delay)
IF "Motor_Command" = TRUE AND "Motor_Run_Feedback" = FALSE 
   AND "Start_Timer".ET > T#3S THEN
    "Motor_Fault" := TRUE;
    "Motor_Command" := FALSE;
END_IF;
```

#### 4. Counter Overflow Protection

```pascal
// Prevent counter overflow
IF "Part_Count" >= 32767 THEN
    "Part_Count" := 0;
    "Overflow_Detected" := TRUE;
END_IF;
```

#### 5. Division by Zero Protection

```pascal
// Always check before dividing
IF #Denominator <> 0 THEN
    #Result := #Numerator / #Denominator;
ELSE
    #Result := 0.0;
    #Math_Error := TRUE;
END_IF;
```

---

## 📖 Lesson 10.5 — Diagnostics and Error Handling

### Diagnostic Buffer

The S7-1200 keeps a **diagnostic buffer** of system events:
1. TIA Portal → Go online → **PLC_1 → Online & Diagnostics**
2. Open **Diagnostics buffer**
3. Events shown with timestamp, event ID, description

### OB82 — Diagnostic Error OB

Triggered when hardware faults occur (module failure, I/O error):

```pascal
OB82 [Diagnostic Error Interrupt]

// OB82 input parameters (available in block):
// IO_STATE     : WORD   — I/O state info
// LADDR        : HW_IO  — Logical hardware address of faulty device
// CHANNEL      : UINT   — Channel number
// MULTI_ERROR  : BOOL   — Multiple errors present

// Log fault to DB
"Fault_Log_DB".Last_Fault_LADDR := #LADDR;
"Fault_Log_DB".Last_Fault_Time := "SYS_TIME"();
"Fault_Log_DB".Fault_Count := "Fault_Log_DB".Fault_Count + 1;
"Fault_Log_DB".Fault_Active := TRUE;
```

### OB121 — Programming Error

Triggered by software errors (type mismatch, access error):

```pascal
OB121 [Programming Error]
// Called when program error occurs
// Best practice: log error, go to safe state

"System_DB".Program_Error := TRUE;
"System_DB".Error_OB := #OB_NUM;
%QB0 := 0;   // Safe state — all outputs off
```

### OB122 — I/O Access Error

Triggered when accessing non-existent or failed I/O:

```pascal
OB122 [I/O Access Error]
// Called when I/O address cannot be accessed

"System_DB".IO_Error := TRUE;
"System_DB".IO_Error_LADDR := #LADDR;
```

### GET_DIAG Instruction

Read diagnostics programmatically:

```pascal
GET_DIAG(
    REQ    := #Req_Diag,
    LADDR  := 16#0000,   // Hardware component address
    MODE   := 0,
    DONE   := #Diag_Done,
    BUSY   := #Diag_Busy,
    ERROR  := #Diag_Error,
    WBUF   := "Diag_Buffer_DB".Data
);
```

---

## 📖 Lesson 10.6 — CPU Operating Modes

### Mode Transitions

```
POWER ON
    │
    ▼
STARTUP (OB100 runs)
    │
    ▼
RUN (OB1 repeating)
    │
    ├──[STOP command / Error]──► STOP
    │                              │
    │                              ▼
    │                         PROGRAM STOPPED
    │                         I/O state: maintained
    │                              │
    └──────────────────────────────┘
                [RUN command]
```

### CPU Memory Reset (MRES)
Clears all memory:
1. Switch CPU to STOP
2. Hold MRES button for 3+ seconds
3. LED flashes — memory cleared
4. CPU returns to factory defaults

> ⚠️ **MRES deletes the entire program!** Always backup first.

---

## 📖 Lesson 10.7 — Project Backup and Restore

### Backup Methods

#### Method 1: TIA Portal Archive

```
File → Archive...
→ Select project folder
→ .zap18 file created (compressed project)
```

#### Method 2: Memory Card (MMC)

```
S7-1200 uses Siemens SIMATIC Memory Card (SD format)
Functions:
  - Program backup
  - Program transfer (card → CPU)
  - Firmware update
  - Data logging

Insert card → TIA Portal → PLC_1 → Copy RAM to ROM
```

#### Method 3: Upload from CPU

```
TIA Portal → Project → New
→ Add new device → Unspecified CPU
→ Go online → Upload from device
→ Retrieves program from CPU
```

### Backup Schedule Recommendation

| When | What |
|---|---|
| Before ANY change | Archive full project |
| After commissioning | Archive + Memory card |
| After modifications | Archive with version comment |
| Monthly | Backup memory card |

---

## 📖 Lesson 10.8 — PLC Programming Best Practices

### Code Organization ✅

```
1. Consistent naming convention:
   FB_MotorControl         (Function Blocks: FB_)
   FC_AlarmManager         (Functions: FC_)
   DB_ProductionData       (Data Blocks: DB_)
   OB1_Main               (OBs: OB_)
   
2. Tag naming:
   Motor1_Start_PB         (physical input)
   Motor1_Run_Contactor    (physical output)
   Motor1_Running_FB       (feedback/status)
   Motor1_Speed_RPM        (process value)
   
3. Comment every network
4. Use symbolic tags — never raw addresses in code
5. Group related code in FBs
6. Use OB100 for all initialization
```

### Version Control

```
Comment each software revision in PLC properties:
Version 1.0 — Initial commissioning
Version 1.1 — Added overload alarm
Version 1.2 — Fixed timer reset issue
Version 2.0 — Added recipe management

Store in:
PLC_1 → Properties → General → Comment/Author/Version
```

### Documentation Standards

Every project should include:

```
1. Electrical drawings (E-Plan, AutoCAD)
2. I/O list (input/output register)
3. PLC tag table (exported from TIA Portal)
4. Functional description
5. Software version history
6. Network/IP address list
7. HMI screen descriptions
8. Alarm list
```

---

## 📖 Lesson 10.9 — Common PLC Faults and Troubleshooting

### Troubleshooting Guide

| Symptom | Possible Cause | Solution |
|---|---|---|
| CPU in STOP, red LED | Program error or hardware fault | Check diagnostic buffer |
| Output not working | Wrong address, wiring fault, FB error | Check tag address, wiring, force output |
| PLC not going online | Wrong IP, firewall blocking | Check IP, disable PC firewall temporarily |
| Timer not working | Timer in wrong OB or DB issue | Check OB context, verify timer DB |
| Analog value wrong | Wrong scaling, wiring type mismatch | Verify raw value, recalculate scaling |
| HMI not connecting | IP mismatch, wrong connection type | Check HMI/PLC IP, verify connection |
| Program runs wrong | Scan order issue, double coil | Review network order, check coil usage |
| Counter not counting | Edge detection missing | Add P-contact on count input |

### Forcing I/O (for testing)

1. Go online → PLC_1 → Watch and force tables
2. **Watch table:** Observe current values
3. **Force table:** Override hardware I/O values

> ⚠️ **DANGER:** Forcing outputs can cause physical movement! Ensure area is clear.

### Online Monitoring Tips
- Use **Breakpoints** in SCL for step debugging
- Use **Watch tables** for multi-variable monitoring
- Use **Cross-reference** to find all uses of a tag
- Check **Call hierarchy** to trace execution path

---

## 📖 Lesson 10.10 — Industry 4.0 & IIoT Considerations

### S7-1200 Industry 4.0 Features

| Feature | Description |
|---|---|
| **OPC UA** | Open standard connectivity to cloud/SCADA |
| **PROFINET** | Real-time industrial Ethernet |
| **Web Server** | Built-in web server for remote monitoring |
| **Data Logging** | Log data to SD card |
| **Email** | Send alerts via SMTP (with CP module) |
| **REST API** | JSON-based data exchange (newer FW) |

### Data Logging to SD Card

```pascal
// DataLogCreate — create log file
// DataLogWrite  — write record
// DataLogClear  — clear log

DataLogWrite(
    REQ   := #Log_Trigger,
    ID    := 1,
    DONE  := #Log_Done,
    ERROR := #Log_Error
);
```

### OPC UA for Cloud Connectivity

```
S7-1200 OPC UA Server
        │
        │ opc.tcp://192.168.1.10:4840
        │
    ┌───▼────────────────────────────────┐
    │  OPC UA Client Options:           │
    │  - SCADA (Ignition, WinCC OA)     │
    │  - MES/ERP systems                │
    │  - Azure IoT Hub                  │
    │  - AWS IoT Core                   │
    │  - Python/Node.js client          │
    └────────────────────────────────────┘
```

---

## ✅ Module 10 — Review Questions

1. What is the difference between SIL and PL safety levels?
2. Why can PLC software alone NOT guarantee a safety function?
3. When is OB82 triggered?
4. What does MRES do and when must you be careful using it?
5. What are 3 methods to backup an S7-1200 program?
6. What naming convention should you use for Function Blocks?
7. How do you force an output in TIA Portal?
8. What is OPC UA used for in Industry 4.0?
9. List 5 items that should be in every PLC project documentation.
10. What OB handles I/O access errors?

---

## 🔬 Practical Exercise 10.1 — Error Handling System

**Task:** Implement complete fault management:
1. Create `DB_Fault_Log` with array of 20 fault records (Code, Time, Description)
2. Implement OB82 to log hardware faults to DB
3. Create FC_Fault_Manager to:
   - Manage fault queue (FIFO)
   - Set fault outputs
   - Support fault reset with interlock
4. Add fault count display to HMI
5. Implement watchdog timer using OB30

---

*Previous: [Module 09](../Module_09_SCL_Advanced/README.md) | Next: [Practical Projects](../Practical_Projects/README.md)*
