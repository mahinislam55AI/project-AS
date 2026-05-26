# Module 03 — Basic PLC Programming (LAD / FBD / STL)

> **Level:** Basic | **Duration:** ~4 Hours | **Prerequisites:** Module 01, 02

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Write programs using Ladder Diagram (LAD)
- Write programs using Function Block Diagram (FBD)
- Understand Statement List (STL/IL) basics
- Use NO/NC contacts, coils, SET/RESET instructions
- Implement basic motor control logic
- Use positive/negative edge detection
- Understand bit logic and Boolean operations

---

## 📖 Lesson 3.1 — Programming Languages in TIA Portal

### IEC 61131-3 Standard Languages

| Language | Type | Best For |
|---|---|---|
| **LAD** (Ladder Diagram) | Graphical | Relay logic, beginners |
| **FBD** (Function Block Diagram) | Graphical | Signal flow, process control |
| **STL** (Statement List) | Textual | Low-level, compact code |
| **SCL** (Structured Control Language) | Textual | Complex algorithms, math |
| **GRAPH** (Sequential Function Chart) | Graphical | Sequential processes |

> **Recommended for beginners:** LAD → FBD → SCL

---

## 📖 Lesson 3.2 — Ladder Diagram (LAD)

### LAD Concept
LAD resembles electrical relay ladder diagrams:
- **Left rail** = Power (24V/L)
- **Right rail** = Neutral/Ground
- **Rungs** = Logic paths from left to right
- **Contacts** = Conditions (inputs, memory bits)
- **Coils** = Actions (outputs, memory bits)

### Basic LAD Symbols

#### Contacts (Inputs / Conditions)

```
Normally Open (NO) Contact — Examine if Closed (XIC)
    ─────┤ ├─────
    Passes power when tag = TRUE (1)

Normally Closed (NC) Contact — Examine if Open (XIO)
    ─────┤/├─────
    Passes power when tag = FALSE (0)

Positive Edge (P-contact) — detects 0→1 transition
    ─────┤P├─────
    Passes ONE scan when tag goes from 0 to 1

Negative Edge (N-contact) — detects 1→0 transition
    ─────┤N├─────
    Passes ONE scan when tag goes from 1 to 0
```

#### Coils (Outputs / Actions)

```
Output Coil
    ─────( )─────
    Sets tag = TRUE when rung is powered

Negated Coil
    ─────(//)─────
    Sets tag = FALSE when rung is powered (inverted)

SET Coil (Latch)
    ─────(S)─────
    Sets tag = TRUE, STAYS true even if rung loses power

RESET Coil (Unlatch)
    ─────(R)─────
    Sets tag = FALSE, STAYS false even if rung gains power

Positive Edge Coil
    ─────(P)─────
    Tag = TRUE for ONE scan on rising edge

Negative Edge Coil
    ─────(N)─────
    Tag = TRUE for ONE scan on falling edge
```

---

## 📖 Lesson 3.3 — Basic LAD Examples

### Example 1: Simple Motor Start/Stop

**Requirements:**
- I0.0 = Start button (momentary, NO)
- I0.1 = Stop button (momentary, NC)
- Q0.0 = Motor contactor

```
NETWORK 1 — Motor Start/Stop with Seal-In
─────────────────────────────────────────────────
    I0.0          I0.1          Q0.0
───┤Start├──┬───┤/Stop/├──────( Motor )───
            │
    Q0.0    │
───┤Motor├──┘
─────────────────────────────────────────────────
```

**Logic Explanation:**
1. Press Start (I0.0 = 1) → Power flows through Stop NC → Q0.0 energizes
2. Q0.0 seals itself in (parallel contact)
3. Release Start → Q0.0 stays ON via seal-in
4. Press Stop (I0.1 = 0 through NC contact) → circuit breaks → Q0.0 OFF

### Example 2: AND Logic

```
NETWORK 1 — Both conditions must be TRUE
─────────────────────────────────────────
    I0.0      I0.1      Q0.0
───┤ A ├────┤ B ├────( Output )───
─────────────────────────────────────────
Q0.0 = I0.0 AND I0.1
```

### Example 3: OR Logic

```
NETWORK 1 — Either condition can be TRUE
─────────────────────────────────────────
    I0.0             Q0.0
───┤ A ├──────────( Output )───
    I0.1
───┤ B ├──────────┘
─────────────────────────────────────────
Q0.0 = I0.0 OR I0.1
```

### Example 4: NOT Logic

```
NETWORK 1 — Output ON when input OFF
─────────────────────────────────────────
    I0.0          Q0.0
───┤/ A /├──────( Output )───
─────────────────────────────────────────
Q0.0 = NOT I0.0
```

### Example 5: SET / RESET (Latch)

```
NETWORK 1 — Set Motor ON
─────────────────────────────
    I0.0         Q0.0
───┤Start├──────(S Motor)───

NETWORK 2 — Reset Motor OFF
─────────────────────────────
    I0.1         Q0.0
───┤Stop ├──────(R Motor)───
```

### Example 6: Edge Detection

```
NETWORK 1 — Detect start button press (rising edge only)
─────────────────────────────────────────────────────────
    I0.0         M0.0          Q0.0
───┤ P ├────────( Edge_Mem)──( Output)───
  (P-contact    (edge memory  (one scan
   detects       bit)          pulse)
   0→1 edge)
─────────────────────────────────────────────────────────
```

---

## 📖 Lesson 3.4 — Function Block Diagram (FBD)

### FBD Concept
FBD uses **function blocks connected by signal lines** — similar to electronic logic gates.

### Basic FBD Symbols

```
AND Gate:
     I0.0 ──┐
            ├──[AND]── Q0.0
     I0.1 ──┘

OR Gate:
     I0.0 ──┐
            ├──[OR]─── Q0.0
     I0.1 ──┘

NOT Gate:
     I0.0 ──[NOT]──── Q0.0

AND with Negated Input:
     I0.0 ──┐
            ├──[AND]── Q0.0
    /I0.1 ──┘  (circle on input = negated)
```

### FBD Motor Control Example

```
     Start(I0.0) ──┐
                   ├──[OR]──┐
     Motor(Q0.0)──┘         ├──[AND]── Motor(Q0.0)
     Stop(I0.1) ────[NOT]───┘
```

### FBD vs LAD — Same Logic, Different View

| Aspect | LAD | FBD |
|---|---|---|
| Origin | Relay diagrams | Electronic schematics |
| Read direction | Left to right (rungs) | Left to right (signal flow) |
| Best for | Relay replacements | Process/signal flow |
| Complexity | Simple logic easy | Complex signal chains |

---

## 📖 Lesson 3.5 — Statement List (STL)

### STL Concept
STL is a low-level textual language. Each instruction operates on the **status bit (RLO)**.

### STL Basic Instructions

| Instruction | Full Name | Meaning |
|---|---|---|
| `A` | AND | AND condition |
| `AN` | AND NOT | AND inverted |
| `O` | OR | OR condition |
| `ON` | OR NOT | OR inverted |
| `=` | Assign | Write result to address |
| `S` | Set | Set bit unconditionally |
| `R` | Reset | Reset bit unconditionally |
| `NOT` | Invert | Invert RLO |

### STL Motor Control Example

```stl
NETWORK 1: Motor Start/Stop with Seal-In
      A     I0.0        // AND Start button
      O     Q0.0        // OR Motor already running (seal-in)
      AN    I0.1        // AND NOT Stop button
      =     Q0.0        // Output = Motor contactor
```

### STL Equivalent of SET/RESET

```stl
NETWORK 1: Set Motor
      A     I0.0        // Start button pressed
      S     Q0.0        // Set motor output

NETWORK 2: Reset Motor
      A     I0.1        // Stop button pressed
      R     Q0.0        // Reset motor output
```

> **Note:** STL is less common in modern programming — LAD/FBD/SCL are preferred in TIA Portal.

---

## 📖 Lesson 3.6 — Practical Control Circuits

### Forward / Reverse Motor Control (with Interlock)

```
NETWORK 1 — Forward Direction
─────────────────────────────────────────────────────────
    I0.0          I0.2          Q0.1         Q0.0
───┤FWD_Start├──┬─┤/Stop/├───┤/REV_Run/├──(FWD_Run)───
                │
    Q0.0        │
───┤FWD_Run ├──┘
─────────────────────────────────────────────────────────

NETWORK 2 — Reverse Direction
─────────────────────────────────────────────────────────
    I0.1          I0.2          Q0.0         Q0.1
───┤REV_Start├──┬─┤/Stop/├───┤/FWD_Run/├──(REV_Run)───
                │
    Q0.1        │
───┤REV_Run ├──┘
─────────────────────────────────────────────────────────
```

**Interlock:** `Q0.0` NC contact in reverse rung prevents both from energizing simultaneously.

### Traffic Light Sequence (Simple)

```
Variables:
  M0.0 = Green phase    M0.1 = Yellow phase    M0.2 = Red phase
  Q0.0 = Green lamp     Q0.1 = Yellow lamp     Q0.2 = Red lamp

NETWORK 1 — Green Lamp
    M0.0
───┤Green_Phase├──(Green_Lamp Q0.0)───

NETWORK 2 — Yellow Lamp
    M0.1
───┤Yellow_Phase├──(Yellow_Lamp Q0.1)───

NETWORK 3 — Red Lamp
    M0.2
───┤Red_Phase├──(Red_Lamp Q0.2)───
```

### Emergency Stop Implementation

```
NETWORK 1 — E-Stop Safety Relay
─────────────────────────────────────────────────────
    I0.7
───┤/E_STOP/├──── [Connect in series with ALL outputs]
─────────────────────────────────────────────────────
```

> ⚠️ **Safety Note:** In real applications, E-Stop must use **hardware safety relays** — never rely on PLC software alone for emergency stops.

---

## 📖 Lesson 3.7 — Bit Logic Instructions Reference

### Complete Bit Logic Reference Table

| Instruction | LAD Symbol | FBD | STL | Description |
|---|---|---|---|---|
| NO Contact | ┤ ├ | AND in | A | Passes if bit = 1 |
| NC Contact | ┤/├ | AND NOT | AN | Passes if bit = 0 |
| P-Contact | ┤P├ | rising | FP | Passes on 0→1 |
| N-Contact | ┤N├ | falling | FN | Passes on 1→0 |
| Output Coil | ( ) | = | = | Sets bit when true |
| /Coil | (//) | /= | NOT = | Sets bit when false |
| SET Coil | (S) | S | S | Latches bit ON |
| RESET Coil | (R) | R | R | Latches bit OFF |
| P-Coil | (P) | -- | -- | 1 scan on rising |
| N-Coil | (N) | -- | -- | 1 scan on falling |

---

## 📖 Lesson 3.8 — Programming Best Practices

### DO's ✅
- Use **meaningful tag names** (e.g., `Motor_Start_PB` not `I0.0`)
- Add **network comments** explaining the purpose
- Use **SET/RESET pairs** for latching logic
- Keep rungs **short and readable** — split complex logic
- Use **NC stop buttons** in hardware (fail-safe)
- **Compile and test** each network before adding more

### DON'Ts ❌
- Don't use the **same output coil** in more than one rung (double coil issue)
- Don't leave **unused contacts** in rungs
- Don't rely on PLC software for **safety-critical functions**
- Don't use absolute addresses (I0.0) — always create **named tags**
- Don't skip **comments** — future you will thank past you

---

## ✅ Module 3 — Review Questions

1. What is the difference between a NO and NC contact in LAD?
2. Explain the seal-in circuit and why it's needed for motor start/stop.
3. What is the difference between an Output Coil `( )` and a SET Coil `(S)`?
4. What does edge detection do and when would you use it?
5. Convert this LAD to FBD: `I0.0 AND (NOT I0.1) → Q0.0`
6. What is a double-coil problem and how do you avoid it?
7. What does the following STL do? `A I0.0 / AN I0.1 / = Q0.0`
8. Why should you use NC contacts for Stop/E-Stop buttons?

---

## 🔬 Practical Exercise 3.1 — Motor Control

**Task:** Implement the following motor control system in LAD:
- **I0.0** = Start (NO momentary)
- **I0.1** = Stop (NC momentary)
- **I0.2** = Overload (NC thermal protection)
- **I0.3** = Emergency Stop (NC mushroom button)
- **Q0.0** = Motor Contactor
- **Q0.1** = Run Indicator Light
- **Q0.2** = Fault Indicator (ON when E-Stop or Overload active)

Requirements:
1. Seal-in start circuit
2. Motor runs only when no faults
3. Fault light activates on E-Stop or Overload
4. Test in PLCSIM

## 🔬 Practical Exercise 3.2 — Traffic Light

**Task:** Implement a 3-phase traffic light in LAD:
- Use timers (from Module 04) for timed phases
- Green: 10 seconds, Yellow: 3 seconds, Red: 10 seconds
- Use SET/RESET to switch phases

---

*Previous: [Module 02](../Module_02_TIA_Portal_Setup/README.md) | Next: [Module 04](../Module_04_Timers_Counters/README.md)*
