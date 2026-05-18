# Module 04 — Timers, Counters & Comparators

> **Level:** Intermediate | **Duration:** ~4 Hours | **Prerequisites:** Module 03

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Use TON, TOF, TONR, TP timer instructions
- Use CTU, CTD, CTUD counter instructions
- Use comparison instructions (CMP)
- Implement timed sequences and delays
- Build counters for production counting
- Combine timers and counters in real applications

---

## 📖 Lesson 4.1 — IEC Timers Overview

### Timer Types in S7-1200

| Timer | Name | Function |
|---|---|---|
| **TON** | Timer On-Delay | Output ON after delay |
| **TOF** | Timer Off-Delay | Output stays ON after input goes OFF |
| **TONR** | Timer On-Delay Retentive | Accumulates time, reset separately |
| **TP** | Timer Pulse | Fixed-width output pulse |

### Timer Data Types
S7-1200 uses **IEC timers** stored in **DB blocks** or as **multi-instance** in FB.

Time format: `T#[d]d_[h]h_[m]m_[s]s_[ms]ms`
```
T#5s       = 5 seconds
T#2m30s    = 2 minutes 30 seconds
T#1h       = 1 hour
T#500ms    = 500 milliseconds
T#0d_1h_30m_0s_0ms = 1 hour 30 minutes
```

---

## 📖 Lesson 4.2 — TON (On-Delay Timer)

### How TON Works

```
Input (IN):   _____|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|_______
                   ←── PT time ──→
Output (Q):   ________________|‾‾‾‾‾|_______
              (Q goes ON after IN has been ON for PT duration)
ET (Elapsed): 0 → counts up to PT → resets when IN goes OFF
```

### TON in LAD

```
NETWORK 1
─────────────────────────────────────────────────────────────
    I0.0             TON
───┤ IN ├──────── IN      Q ──────( Q0.0 )───
                   PT: T#5S
                   ET ──── MW100 (optional)
─────────────────────────────────────────────────────────────
```

### TON Parameters

| Pin | Type | Description |
|---|---|---|
| **IN** | Bool | Timer enable input |
| **PT** | Time | Preset time (how long to wait) |
| **Q** | Bool | Output (TRUE when ET >= PT) |
| **ET** | Time | Elapsed time (current count) |

### TON Example — Motor Start Delay

```
Requirement: Motor starts 5 seconds after start button press

NETWORK 1 — Start Timer
    I0.0 (Start)    [TON "Start_Delay"]
───┤────────────── IN        Q ──────────── M0.0 (Timer_Done)
                   PT: T#5S
                   ET ──── MW10

NETWORK 2 — Motor Output
    M0.0 (Timer_Done)    I0.1 (Stop)    Q0.0 (Motor)
───┤──────────────────┤/──────────────( )───
```

---

## 📖 Lesson 4.3 — TOF (Off-Delay Timer)

### How TOF Works

```
Input (IN):   _____|‾‾‾‾‾‾‾|_____________________
Output (Q):   _____|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|____________
                             ←── PT ──→
              (Q stays ON for PT duration after IN goes OFF)
```

### TOF in LAD

```
NETWORK 1
─────────────────────────────────────────────────────────────
    I0.0             TOF
───┤ IN ├──────── IN      Q ──────( Q0.0 )───
                   PT: T#3S
─────────────────────────────────────────────────────────────
```

### TOF Example — Cooling Fan Delay

```
Requirement: Cooling fan runs for 30 seconds after motor stops

    Q0.0 (Motor)     [TOF "Fan_Delay"]
───┤──────────────── IN        Q ──────── Q0.1 (Fan)
                     PT: T#30S
```

---

## 📖 Lesson 4.4 — TONR (Retentive On-Delay Timer)

### How TONR Works
- Accumulates time whenever IN = TRUE
- **Retains** elapsed time when IN goes FALSE
- Must be **manually reset** using R input

```
Input (IN):   ___|‾‾‾|___|‾‾‾‾‾‾‾‾|___
                  3s      7s (total = 10s)
Output (Q):   __________________|‾‾‾‾‾|
                    (PT = 10s, Q fires when total = 10s)
Reset (R):                            |___ resets ET to 0
```

### TONR in LAD

```
NETWORK 1
─────────────────────────────────────────────────────────────
    I0.0             TONR
───┤ IN ├──────── IN        Q ──────( M0.0 )───
                   R ◄──────── I0.2 (Reset)
                   PT: T#10S
                   ET ──── MD10
─────────────────────────────────────────────────────────────
```

### TONR Use Case — Machine Running Hours

```
Purpose: Track total machine running time

    Q0.0 (Motor)     [TONR "Run_Hours"]
───┤──────────────── IN        Q ──────── M1.0 (Hours_Exceeded)
    I0.5 (Reset)  ── R
                     PT: T#8h     (alert after 8 hours running)
                     ET ──── MD100 (store elapsed time)
```

---

## 📖 Lesson 4.5 — TP (Pulse Timer)

### How TP Works
- Generates a fixed-width pulse output
- Input trigger (0→1) starts the pulse
- Output stays ON for exactly PT duration
- Ignores further inputs while pulse active

```
Input (IN):   _|‾‾|___|‾|______________
Output (Q):   _|‾‾‾‾‾‾‾‾‾|_|‾‾‾‾‾‾‾‾‾|__
                   ←PT→       ←PT→
```

### TP Example — Valve Pulse

```
Requirement: Open solenoid valve for exactly 2 seconds on trigger

    I0.0 (Trigger)     [TP "Valve_Pulse"]
───┤──────────────── IN        Q ──────── Q0.3 (Solenoid)
                     PT: T#2S
```

---

## 📖 Lesson 4.6 — Timer Comparison Summary

| Feature | TON | TOF | TONR | TP |
|---|---|---|---|---|
| Output ON when | After IN=1 for PT | Immediately on IN=1 | After total IN=1 ≥ PT | On IN rising edge |
| Output OFF when | IN goes OFF | After IN=0 for PT | When R=1 | After PT elapses |
| Retentive | No | No | Yes | No |
| Reset needed | No (auto) | No (auto) | Yes (R input) | No (auto) |

---

## 📖 Lesson 4.7 — Counters Overview

### Counter Types

| Counter | Name | Function |
|---|---|---|
| **CTU** | Count Up | Counts up from 0 to preset |
| **CTD** | Count Down | Counts down from preset to 0 |
| **CTUD** | Count Up/Down | Counts both directions |

### Counter Data Types
Counters in S7-1200 use **IEC standard** — stored in DB or multi-instance.

---

## 📖 Lesson 4.8 — CTU (Count Up)

### How CTU Works

```
CU input:   _|‾|_|‾|_|‾|_|‾|_|‾|___
            ↑  ↑  ↑  ↑  ↑
CV:         0  1  2  3  4  (counts each rising edge)
PV = 4
Q output:   _________________|‾‾‾‾‾|  (Q=1 when CV >= PV)
```

### CTU Parameters

| Pin | Type | Description |
|---|---|---|
| **CU** | Bool | Count Up pulse input |
| **R** | Bool | Reset (CV = 0) |
| **PV** | Int | Preset value |
| **Q** | Bool | Output (TRUE when CV >= PV) |
| **CV** | Int | Current value |

### CTU in LAD

```
NETWORK 1
─────────────────────────────────────────────────────────────
    I0.0 (Pulse)     CTU
───┤ P ├─────────── CU        Q ──────( Q0.0 )───
    I0.1 (Reset) ── R
                    PV: 10
                    CV ──── MW20
─────────────────────────────────────────────────────────────
```

### CTU Example — Production Counter

```
Count 100 parts, then trigger end-of-batch alarm

NETWORK 1 — Count parts
    I0.0 (Part sensor)    [CTU "Part_Counter"]
───┤ P ├──────────────── CU        Q ──────── Q0.5 (Batch_Done)
    I0.1 (Reset batch) ── R
                          PV: 100
                          CV ──── MW50 (current count)

NETWORK 2 — Display count (optional via HMI)
    MW50 = current part count
```

---

## 📖 Lesson 4.9 — CTD (Count Down)

### How CTD Works

```
CD input:   _|‾|_|‾|_|‾|___
            ↑  ↑  ↑
CV:         5  4  3  (loaded with PV, counts down)
PV = 5
Q output:   ____when CV=0─────|‾‾‾‾|
```

### CTD Parameters

| Pin | Type | Description |
|---|---|---|
| **CD** | Bool | Count Down pulse input |
| **LD** | Bool | Load preset (CV = PV) |
| **PV** | Int | Preset value (starting count) |
| **Q** | Bool | Output (TRUE when CV <= 0) |
| **CV** | Int | Current value |

### CTD Example — Batch Dispenser

```
Requirement: Dispense exactly 50 items, output when done

NETWORK 1 — Count down dispensed items
    I0.0 (Item sensor)    [CTD "Dispense_Counter"]
───┤ P ├──────────────── CD        Q ──────── Q0.2 (Batch_Complete)
    I0.1 (Load) ───────── LD
                          PV: 50
                          CV ──── MW60
```

---

## 📖 Lesson 4.10 — CTUD (Count Up/Down)

### How CTUD Works

```
CU:  _|‾|_|‾|_________
CD:  ___________|‾|_|‾|
CV:  0  1  2  1  0  (increments on CU, decrements on CD)
```

### CTUD Parameters

| Pin | Type | Description |
|---|---|---|
| **CU** | Bool | Count Up input |
| **CD** | Bool | Count Down input |
| **R** | Bool | Reset (CV = 0) |
| **LD** | Bool | Load (CV = PV) |
| **PV** | Int | Preset value |
| **QU** | Bool | Up output (CV >= PV) |
| **QD** | Bool | Down output (CV <= 0) |
| **CV** | Int | Current value |

---

## 📖 Lesson 4.11 — Comparison Instructions (CMP)

### Available Comparators

| Instruction | Symbol | Condition |
|---|---|---|
| Equal | `==` | IN1 = IN2 |
| Not Equal | `<>` | IN1 ≠ IN2 |
| Greater Than | `>` | IN1 > IN2 |
| Less Than | `<` | IN1 < IN2 |
| Greater or Equal | `>=` | IN1 >= IN2 |
| Less or Equal | `<=` | IN1 <= IN2 |
| In Range | `IN_RANGE` | MIN <= VAL <= MAX |
| Out of Range | `OUT_RANGE` | VAL < MIN or VAL > MAX |

### Comparator in LAD

```
NETWORK 1 — High Temperature Alarm
─────────────────────────────────────────────────────────────
                    CMP >=
    ────────────── IN1: MW100 (Temp_Value)
                   IN2: 85        ──────── Q0.5 (High_Temp_Alarm)
─────────────────────────────────────────────────────────────
If Temp_Value >= 85 → Alarm ON
```

### IN_RANGE Example

```
NETWORK 1 — Check if temperature is in safe range
─────────────────────────────────────────────────────────────
                    IN_RANGE
    ────────────── MIN: 20
                   VAL: MW100  ──────── M2.0 (Temp_Normal)
                   MAX: 80
─────────────────────────────────────────────────────────────
If 20 <= MW100 <= 80 → Temp_Normal = TRUE
```

---

## 📖 Lesson 4.12 — Combined Timer/Counter Application

### Flashing Light (Using Timers)

```
NETWORK 1 — Flash ON timer
    M0.1 (Flash_OFF_done)     [TON "Flash_ON"]
───┤──────────────────────── IN        Q ──── M0.0
                              PT: T#500ms

NETWORK 2 — Flash OFF timer
    M0.0 (Flash_ON_done)     [TON "Flash_OFF"]
───┤──────────────────────── IN        Q ──── M0.1
                              PT: T#500ms

NETWORK 3 — Output (driven by Flash_ON)
    M0.0
───┤────┤──────────────────── Q0.7 (Flash_Light)
```

### Conveyor with Part Counter

```
NETWORK 1 — Conveyor runs while counting
    I0.0 (Start)     I0.1 (Stop)     M1.0 (Batch_done)     Q0.0 (Conveyor)
───┤──────────────┤/──────────────┤/─────────────────────( Seal-in )───
    Q0.0 ──────────┤

NETWORK 2 — Count parts
    I0.5 (Sensor)     [CTU "Parts"]
───┤ P ├──────────── CU        Q ──── M1.0 (Batch_done)
    I0.6 (Reset) ──── R
                      PV: 100

NETWORK 3 — Stop alarm after batch
    M1.0
───┤────┤──────────────────── Q0.3 (Batch_Alarm)
```

---

## ✅ Module 4 — Review Questions

1. What is the difference between TON and TOF?
2. When would you use TONR instead of TON?
3. What does TP do differently from TON?
4. What is the difference between CTU and CTD?
5. How do you reset a CTU counter?
6. What data type are IEC timers stored in?
7. Write the time format for 2 hours 30 minutes 15 seconds.
8. What does `IN_RANGE` do and what are its parameters?
9. At what value does CTU output Q go TRUE?
10. Explain the seal-in circuit in the conveyor example.

---

## 🔬 Practical Exercise 4.1 — Traffic Light Controller

**Task:** Implement a traffic light using timers:
- Green: 10 seconds (TON)
- Yellow: 3 seconds (TON)
- Red: 10 seconds (TON)
- Automatic cycling
- I0.0 = System Enable
- Q0.0 = Green, Q0.1 = Yellow, Q0.2 = Red

## 🔬 Practical Exercise 4.2 — Production Counter

**Task:** Build a production line counter:
- I0.0 = Product sensor (pulse per part)
- I0.1 = Shift reset
- Q0.0 = Batch complete (every 50 parts)
- Q0.1 = Warning light (45–49 parts)
- MW20 = Current count (display on HMI later)

---

*Previous: [Module 03](../Module_03_Basic_Programming/README.md) | Next: [Module 05](../Module_05_Data_Types_Memory/README.md)*
