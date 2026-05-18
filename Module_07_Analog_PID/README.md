# Module 07 — Analog I/O & PID Control

> **Level:** Advanced | **Duration:** ~5 Hours | **Prerequisites:** Module 05, 06

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Configure analog input and output modules
- Scale raw analog values to engineering units
- Understand PID control theory
- Configure and use PID_Compact instruction
- Auto-tune a PID loop
- Implement temperature and flow control loops

---

## 📖 Lesson 7.1 — Analog I/O Overview

### Analog vs Digital

| Feature | Digital | Analog |
|---|---|---|
| Signal Type | ON/OFF (0 or 1) | Continuous value |
| Range | 0 or 1 | 0–10V, 4–20mA, etc. |
| Resolution | 1 bit | 12–16 bit |
| Use for | Buttons, sensors, relays | Temperature, pressure, speed |

### S7-1200 Analog Capabilities

| Location | Type | Range |
|---|---|---|
| CPU Onboard | 2x Analog Input | 0–10V DC |
| SB 1231 | 1x Analog Input | ±10V or 0–20mA |
| SB 1232 | 1x Analog Output | ±10V or 0–20mA |
| SM 1231 | 4x or 8x Analog Input | ±10V, ±5V, ±2.5V, 0–20mA |
| SM 1232 | 2x or 4x Analog Output | ±10V, 0–20mA |
| SM 1234 | 4xAI / 2xAQ | Combined module |
| SM 1231 RTD | 4x RTD | PT100, PT1000, Ni100 |
| SM 1231 TC | 4x Thermocouple | J, K, T, E, R, S, B type |

---

## 📖 Lesson 7.2 — Analog Signal Types

### Voltage Signals
```
0–10V   → Most common, simple wiring
±10V    → Bidirectional (drives, servo)
0–5V    → Less common
1–5V    → With wire-break detection (below 1V = broken wire)
```

### Current Signals (4–20mA)
```
4mA  = 0% (minimum signal)
20mA = 100% (maximum signal)
0mA  = WIRE BREAK (fault condition!)

Advantages:
✅ Immune to cable resistance (long distances)
✅ Wire break detection (0mA = fault)
✅ Industry standard for process control
```

### 2-Wire vs 4-Wire Transmitters

```
2-Wire (Loop powered):
    +24V ─── Transmitter+ ─── AI+ ─── AI─ ─── 0V
    (transmitter draws power from the current loop)

4-Wire (Self powered):
    +24V ─── Transmitter VCC
    0V   ─── Transmitter GND
    AI+  ─── Transmitter Output+
    AI─  ─── Transmitter Output─
```

---

## 📖 Lesson 7.3 — Analog Raw Values

### Raw ADC Values (S7-1200)

| Signal Range | 0% (Min Raw) | 100% (Max Raw) | Notes |
|---|---|---|---|
| 0–10V | 0 | 27648 | Most common |
| ±10V | -27648 | +27648 | Signed |
| 0–20mA | 0 | 27648 | Current |
| 4–20mA | 5530 | 27648 | 4mA=5530 |
| 0–5V | 0 | 27648 | |

> **Key number:** `27648` = 100% of analog range in S7-1200

### Why 27648?
```
12-bit ADC = 4096 levels (0 to 4095)
But S7-1200 uses 27648 for historical compatibility
with Siemens standard scaling formula
```

---

## 📖 Lesson 7.4 — Analog Scaling

### Manual Scaling Formula

```
Engineering Value = ((Raw - Raw_Min) / (Raw_Max - Raw_Min)) × (EU_Max - EU_Min) + EU_Min

Where:
  Raw      = Current raw ADC value (from IW64 etc.)
  Raw_Min  = Raw value at 0% (e.g., 0 for 0-10V)
  Raw_Max  = Raw value at 100% (e.g., 27648)
  EU_Min   = Engineering unit minimum (e.g., 0.0°C)
  EU_Max   = Engineering unit maximum (e.g., 100.0°C)
```

### Example: 4–20mA Pressure Sensor (0–10 bar)

```
Sensor: 4mA = 0 bar, 20mA = 10 bar
Raw at 4mA  = 5530
Raw at 20mA = 27648

Formula: Pressure = ((Raw - 5530) / (27648 - 5530)) × (10.0 - 0.0) + 0.0
         Pressure = ((Raw - 5530) / 22118) × 10.0
```

### Using NORM_X and SCALE_X Instructions (Recommended)

**NORM_X — Normalize to 0.0–1.0**
```
NETWORK 1 — Normalize raw analog to 0.0–1.0 range
    NORM_X (INT)
    EN    ENO
    MIN: 0
    VALUE: IW64    → OUT: MD100 (0.0 to 1.0, REAL)
    MAX: 27648
```

**SCALE_X — Scale normalized to engineering units**
```
NETWORK 2 — Scale to 0.0–100.0°C
    SCALE_X (REAL)
    EN    ENO
    MIN: 0.0
    VALUE: MD100   → OUT: MD104 (Temperature in °C)
    MAX: 100.0
```

### Complete 4–20mA Example in SCL (cleaner)

```pascal
// Scale 4-20mA temperature sensor (0–150°C)
"Temperature_C" := ((REAL#1.0 * "AI_Raw" - 5530.0) / 22118.0) * 150.0;

// Clamp to valid range
IF "Temperature_C" < 0.0 THEN "Temperature_C" := 0.0; END_IF;
IF "Temperature_C" > 150.0 THEN "Temperature_C" := 150.0; END_IF;
```

---

## 📖 Lesson 7.5 — Analog Output Scaling

### Setting Analog Output (e.g., 0–10V speed reference)

```
Engineering Value → Raw Count → Analog Output

Raw = ((EU_Value - EU_Min) / (EU_Max - EU_Min)) × 27648

Example: Set 75% speed (0–100% → 0–10V)
Raw = (75.0 / 100.0) × 27648 = 20736
QW80 = 20736
```

### In TIA Portal (LAD)

```
NETWORK 1 — Convert speed % to analog output
    SCALE_X (REAL)
    EN    ENO
    MIN: 0
    VALUE: MD200 (speed%)  → OUT: MD204 (temp real)
    MAX: 27648

NETWORK 2 — Write to analog output
    MOVE
    EN    ENO
    IN: REAL_TO_INT(MD204) → OUT: QW80
```

---

## 📖 Lesson 7.6 — PID Control Theory

### What is PID?
**PID = Proportional + Integral + Derivative** control

A feedback control algorithm that:
1. Measures the **process variable (PV)** — actual value
2. Compares to **setpoint (SP)** — desired value
3. Calculates **error** = SP - PV
4. Outputs a **control signal (CV)** to minimize error

### PID Block Diagram

```
                    ┌─────────────────────────────┐
  SP ─────────────►│    ERROR CALCULATION         │
                   │    Error = SP - PV           │
  PV ─────────────►│                             │
                   └──────────────┬──────────────┘
                                  │
                   ┌──────────────▼──────────────┐
                   │         PID ALGORITHM        │
                   │                             │
                   │  P: Kp × Error              │
                   │  I: Ki × ∫Error dt          │
                   │  D: Kd × dError/dt          │
                   │                             │
                   │  Output = P + I + D         │
                   └──────────────┬──────────────┘
                                  │ Control Variable (CV)
                                  ▼
                   ┌──────────────────────────────┐
                   │     PROCESS / ACTUATOR       │
                   │  (Heater, Valve, VFD, etc.)  │
                   └──────────────┬───────────────┘
                                  │ Measured Output
                                  ▼ (feeds back to PV)
```

### PID Terms Explained

| Term | Symbol | Effect | Too High | Too Low |
|---|---|---|---|---|
| **Proportional** | Kp | Reduces error quickly | Oscillation | Slow response |
| **Integral** | Ki | Eliminates steady-state error | Overshoot | Slow correction |
| **Derivative** | Kd | Dampens oscillation | Noise sensitive | No damping |

### PID Tuning Rules of Thumb

```
Start with:
  Kp = 1.0   (moderate gain)
  Ki = 0.1   (slow integral)
  Kd = 0.0   (no derivative initially)

Then:
1. Increase Kp until oscillation appears, then halve it
2. Increase Ki until steady-state error is gone
3. Add Kd only if needed to dampen overshoot
```

---

## 📖 Lesson 7.7 — PID_Compact Instruction

### What is PID_Compact?
Siemens' built-in PID function block for S7-1200:
- Closed-loop PID control
- Integrated auto-tuning
- Anti-windup
- Output limiting
- Ramp function

### Adding PID_Compact

1. In TIA Portal instructions: **Technology → PID Control → PID_Compact**
2. Drag into **OB30** (cyclic interrupt, e.g., 100ms)
3. Assign an instance DB automatically

### PID_Compact Parameters

```
FB "PID_Compact" [Instance DB: PID_DB_1]
─────────────────────────────────────────────────────────────
INPUT PIN       | Description                 | Data Type
─────────────────────────────────────────────────────────────
Setpoint        | Desired value               | REAL
Input           | Process variable (feedback) | REAL
Input_PER       | Analog input (raw)          | INT (optional)
ManualEnable    | Enable manual mode          | BOOL
ManualValue     | Manual output value         | REAL
Reset           | Reset PID                   | BOOL
ModeActivate    | Activate mode change        | BOOL
─────────────────────────────────────────────────────────────
OUTPUT PIN      |                             |
─────────────────────────────────────────────────────────────
Output          | PID output (0.0–100.0%)     | REAL
Output_PER      | Analog output (raw)         | INT
Output_PWM      | PWM output                  | BOOL
SetpointLimit_H | High setpoint limit         | BOOL
SetpointLimit_L | Low setpoint limit          | BOOL
InputWarning_H  | High input warning          | BOOL
InputWarning_L  | Low input warning           | BOOL
State           | PID state (0–4)             | INT
Error           | Error active                | BOOL
ErrorBits       | Error code                  | DWORD
─────────────────────────────────────────────────────────────
```

### PID States

| State | Value | Description |
|---|---|---|
| Inactive | 0 | PID not running |
| Pre-tuning | 1 | Startup tuning active |
| Fine-tuning | 2 | Fine tuning active |
| Automatic | 3 | Normal closed-loop control |
| Manual | 4 | Manual output mode |

---

## 📖 Lesson 7.8 — PID_Compact Configuration

### Step 1: Configure in OB30

```
OB30 [100ms Cyclic Interrupt]
─────────────────────────────────────────────────────────────
NETWORK 1 — Temperature PID
    PID_Compact [DB: "Temp_PID_DB"]
    EN             ENO
    Setpoint:  "TempSP"         → Output:     "HeaterOutput"
    Input:     "Temperature_C"  → Output_PER: QW80
    Reset:     M2.0
─────────────────────────────────────────────────────────────
```

### Step 2: Configure PID Parameters in TIA Portal

Double-click **PID_Compact instance DB** → "Configuration" tab:

```
Basic settings:
  Controller type:    Temperature
  Input/Output:       Input (scaled), Output (scaled)
  
Setpoint limits:
  Upper: 200.0°C
  Lower: 0.0°C

Process value monitoring:
  Upper warning limit: 180.0°C
  Lower warning limit: 5.0°C
  
Output value limits:
  Upper: 100.0%
  Lower: 0.0%
  
PID parameters (manual or after auto-tune):
  Proportional gain (Kp): 2.5
  Integral time (Ti):     30.0s
  Derivative time (Td):   5.0s
```

### Step 3: Auto-Tune PID

1. Go online → Open PID_Compact commissioning panel
2. Set `Mode = 1` (Pre-tuning) or `Mode = 2` (Fine-tuning)
3. Set `ModeActivate = 1` (pulse)
4. PID controller performs step response analysis
5. After completion, parameters are automatically loaded
6. Switch to `Mode = 3` (Automatic) for normal operation

---

## 📖 Lesson 7.9 — Temperature Control Example

### Complete Temperature Controller

```
Hardware:
  AI: SM 1231 RTD — PT100 sensor → temperature feedback
  AQ: SM 1232     — 0–10V → SSR (Solid State Relay) → Heater

Tags:
  Temperature_Raw:  IW96  (raw RTD value)
  Temperature_C:    MD100 (scaled °C, REAL)
  Temp_Setpoint:    MD104 (desired temperature, REAL)
  Heater_Output:    QW80  (0–27648 → 0–10V)
```

**OB30 — 100ms Cyclic Interrupt:**

```
NETWORK 1 — Scale temperature input
    NORM_X → SCALE_X
    Raw(IW96) → Normalized → Temperature_C(MD100)
    Range: 0–27648 → 0°C–300°C

NETWORK 2 — PID Control
    PID_Compact [DB1]
    Setpoint:  MD104 (Temp_Setpoint)
    Input:     MD100 (Temperature_C)
    → Output_PER: QW80 (Heater output)
```

---

## 📖 Lesson 7.10 — Analog Wiring Best Practices

### Do's ✅
- Use **shielded twisted pair** cable for all analog signals
- Connect shield at **ONE end only** (usually panel side)
- Keep analog cables away from **power cables** (min 150mm)
- Use **differential inputs** where available
- Add **surge protection** for field instruments
- Use **4–20mA** over 0–10V for long cable runs

### Don'ts ❌
- Don't run analog and power cables in the **same conduit**
- Don't loop **multiple grounds** on analog shields
- Don't leave unused analog **inputs floating** — connect to GND
- Don't use **cheap unshielded** cable for analog signals

### Wiring Diagram (4–20mA, 2-wire)

```
                    SM 1231
+24V ─────────────── AI+
Transmitter ─────── AI+  (signal return)
             ─────── AI─
0V ──────────────── M (module common)
Shield ──────────── PE (chassis ground, panel end only)
```

---

## ✅ Module 7 — Review Questions

1. What is the raw value range for S7-1200 analog inputs?
2. What raw value corresponds to 4mA in a 4–20mA input?
3. What are NORM_X and SCALE_X used for?
4. Explain the three terms of PID control.
5. What OB should PID_Compact be placed in and why?
6. What is the difference between PID auto-tune mode 1 and mode 2?
7. Why is 4–20mA preferred over 0–10V for long cable runs?
8. What does a 0mA signal on a 4–20mA loop indicate?
9. What PID parameter eliminates steady-state error?
10. What is the Output pin range of PID_Compact?

---

## 🔬 Practical Exercise 7.1 — Temperature PID

**Task:** Build a complete oven temperature controller:
- Input: SM 1231 RTD at IW96 (0–300°C)
- Output: AQ at QW80 (0–100% heater)
- Setpoint stored in DB: `"Oven_DB".Temp_SP`
- OB30 at 200ms for PID execution
- Include high-temp alarm at 280°C → Q0.7
- Implement manual override mode

---

*Previous: [Module 06](../Module_06_Functions_FBs_OBs/README.md) | Next: [Module 08](../Module_08_HMI_Communication/README.md)*
