# Module 01 — Introduction to PLC & S7-1200 Hardware

> **Level:** Basic | **Duration:** ~3 Hours | **Prerequisites:** None

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Explain what a PLC is and where it is used
- Identify S7-1200 CPU variants and their specifications
- Understand the hardware components of an S7-1200 system
- Wire digital inputs and outputs correctly
- Identify signal board and expansion module options

---

## 📖 Lesson 1.1 — What is a PLC?

### Definition
A **Programmable Logic Controller (PLC)** is an industrial digital computer designed to control manufacturing processes, machinery, and automation systems.

### Key Characteristics
- **Rugged** — designed for harsh industrial environments
- **Real-time** — executes scan cycles deterministically
- **Reliable** — built for 24/7 continuous operation
- **Flexible** — reprogrammable without hardware changes

### PLC vs Relay Logic vs Microcontroller

| Feature | Relay Panel | Microcontroller | PLC |
|---|---|---|---|
| Reprogrammable | ❌ No | ✅ Yes | ✅ Yes |
| Industrial Rated | ✅ Yes | ❌ No | ✅ Yes |
| Easy to Troubleshoot | ❌ Hard | ❌ Hard | ✅ Easy |
| Real-time Deterministic | ✅ Yes | ⚠️ Limited | ✅ Yes |
| Cost | Low | Very Low | Medium-High |

### PLC Applications
- **Manufacturing:** Assembly lines, conveyor systems
- **Process Control:** Water treatment, chemical plants
- **Building Automation:** HVAC, elevators, lighting
- **Energy:** Power distribution, renewable energy
- **Food & Beverage:** Filling, packaging, mixing

---

## 📖 Lesson 1.2 — S7-1200 PLC Family Overview

### What is S7-1200?
The **Siemens SIMATIC S7-1200** is a compact, modular PLC designed for small to medium automation tasks. It is programmed using **TIA Portal** software.

### S7-1200 CPU Variants

| CPU Model | DI | DQ | AI | Work Memory | Notes |
|---|---|---|---|---|---|
| **CPU 1211C** | 6 | 4 | 2 | 50 KB | Entry-level, smallest |
| **CPU 1212C** | 8 | 6 | 2 | 75 KB | Small applications |
| **CPU 1214C** | 14 | 10 | 2 | 100 KB | Most popular, mid-range |
| **CPU 1215C** | 14 | 10 | 2 | 125 KB | 2x PROFINET ports |
| **CPU 1217C** | 14 | 10 | 2 | 150 KB | High-speed motion |

> **DI** = Digital Inputs | **DQ** = Digital Outputs | **AI** = Analog Inputs

### CPU Naming Convention

```
CPU 1214C  DC/DC/DC
│    │  │   │  │  └─ Output type: DC (Transistor) or RLY (Relay)
│    │  │   │  └──── Output type (redundant in naming)
│    │  │   └─────── Input supply: DC or AC
│    │  └─────────── C = Compact (integrated I/O)
│    └────────────── Series number (14 = mid-range)
└─────────────────── Product family (S7-1200)
```

### Power Supply Options
- **DC/DC/DC** — 24V DC supply, 24V DC inputs, 24V DC transistor outputs
- **AC/DC/RLY** — 85-264V AC supply, 24V DC inputs, Relay outputs
- **DC/DC/RLY** — 24V DC supply, 24V DC inputs, Relay outputs

---

## 📖 Lesson 1.3 — Hardware Architecture

### Front Panel Layout

```
┌─────────────────────────────────────────┐
│  SIMATIC S7-1200  CPU 1214C DC/DC/DC    │
│                                         │
│  [RUN/STOP LED]  [ERROR LED]  [MAINT]  │
│                                         │
│  ┌────────────┐    ┌─────────────────┐  │
│  │ PROFINET   │    │  Signal Board   │  │
│  │  Port(s)   │    │   Slot (SB)     │  │
│  └────────────┘    └─────────────────┘  │
│                                         │
│  ┌──────────────────────────────────┐   │
│  │  Digital Inputs  (I0.0 – I1.5)  │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │  Digital Outputs (Q0.0 – Q1.1)  │   │
│  └──────────────────────────────────┘   │
│  ┌──────────────────────────────────┐   │
│  │  Analog Inputs  (AI0, AI1)       │   │
│  └──────────────────────────────────┘   │
│                                         │
│  [SD Card Slot]  [24VDC Power]          │
└─────────────────────────────────────────┘
```

### Key Hardware Components

#### 1. CPU (Central Processing Unit)
- Executes the user program
- Contains integrated I/O
- Manages communication
- Stores program and data

#### 2. Signal Modules (SM) — Expansion I/O
Plug to the RIGHT of the CPU (up to 8 modules on 1214C/1215C/1217C)

| Module Type | Example Models |
|---|---|
| Digital Input | SM 1221 — 8DI, 16DI |
| Digital Output | SM 1222 — 8DQ, 16DQ |
| Digital Combo | SM 1223 — 8DI/8DQ |
| Analog Input | SM 1231 — 4AI, 8AI |
| Analog Output | SM 1232 — 2AQ, 4AQ |
| Analog Combo | SM 1234 — 4AI/2AQ |
| RTD/TC Input | SM 1231 AI 4xRTD |

#### 3. Signal Board (SB) — Onboard Expansion
Plugs directly into the **front** of the CPU. Only ONE per CPU.

| SB Type | Channels |
|---|---|
| SB 1221 | 4x DI |
| SB 1222 | 4x DQ |
| SB 1223 | 2x DI / 2x DQ |
| SB 1231 | 1x AI (±10V or 0-20mA) |
| SB 1232 | 1x AQ |
| SB 1241 | RS485 / RS232 |

#### 4. Communication Modules (CM) — Left Side
Plug to the LEFT of the CPU (up to 3 modules)

| CM Type | Protocol |
|---|---|
| CM 1241 | RS232 / RS485 (Modbus RTU, ASCII) |
| CM 1242-5 | PROFIBUS DP Slave |
| CM 1243-5 | PROFIBUS DP Master |
| CP 1242-7 | GPRS |

---

## 📖 Lesson 1.4 — I/O Wiring

### Digital Input Wiring (Sourcing / Sinking)

#### Sinking Input (NPN Sensor)
```
+24V ──────────────────── 1M (Common)
                              │
NPN Sensor ──── Signal ──── I0.0
                              │
0V ─────────────────────── 0V
```

#### Sourcing Input (PNP Sensor)
```
+24V ──── PNP Sensor ──── Signal ──── I0.0
                                          │
0V ──────────────────────────────── 1M (Common)
```

### Digital Output Wiring

#### Transistor Output (DC Load)
```
+24V ──── Load (+) ──── Q0.0 (Transistor)
                              │
0V ──────────────────── 1L (Common)
```

#### Relay Output (AC or DC Load)
```
L (Line) ──── Load ──── Q0.0 (Relay NO)
                              │
N (Neutral) ─────────── 1L (Common)
```

### Wiring Best Practices
- Always use **shielded cable** for analog signals
- Keep **24V DC and 120/240V AC** wiring separated
- Use **ferrules/end sleeves** on stranded wire ends
- Add **fuses** on each output circuit
- Label all terminals clearly
- Use **proper wire gauge**: 0.5–1.5mm² for I/O, 2.5mm² for power

---

## 📖 Lesson 1.5 — PLC Scan Cycle

### Understanding the Scan Cycle

```
┌─────────────────────────────────────────────────┐
│                  SCAN CYCLE                     │
│                                                 │
│   1. Read Inputs ──────► Process Image Input    │
│                                    │            │
│   2. Execute Program ◄─────────────┘            │
│                │                               │
│   3. Write Outputs ────► Process Image Output   │
│                                    │            │
│   4. Communications ◄──────────────┘            │
│                │                               │
│   5. Self-Diagnostics                          │
│                │                               │
│   └──────── Repeat ─────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

### Scan Cycle Times
- **Typical S7-1200 scan time:** 1–10 ms
- Depends on program size and complexity
- Can be monitored in TIA Portal diagnostics

### Process Image vs Direct I/O Access
| Method | When Used |
|---|---|
| **Process Image (default)** | Standard I/O — consistent snapshot per scan |
| **Direct Access (:P suffix)** | Time-critical applications, need immediate value |

---

## 📖 Lesson 1.6 — CPU Status LEDs

| LED | Color | State | Meaning |
|---|---|---|---|
| RUN/STOP | Green | Solid | CPU in RUN mode |
| RUN/STOP | Yellow | Solid | CPU in STOP mode |
| ERROR | Red | Flashing | Error present |
| MAINT | Yellow | Solid | Maintenance needed |
| LINK | Green | Solid | PROFINET link active |
| Rx/Tx | Yellow | Flashing | Data being exchanged |

---

## ✅ Module 1 — Review Questions

1. What does PLC stand for and what is its main purpose?
2. What is the difference between CPU 1211C and CPU 1214C?
3. How many Signal Modules can be attached to a CPU 1214C?
4. What is the difference between a Signal Module (SM) and a Signal Board (SB)?
5. Explain the difference between sinking and sourcing input wiring.
6. What happens during a PLC scan cycle? List the steps.
7. What does a solid RED ERROR LED indicate?
8. What is the naming convention for `CPU 1214C DC/DC/RLY`?

---

## 🔬 Practical Exercise 1.1

**Task:** Hardware Identification
1. Open TIA Portal and create a new project
2. Add a CPU 1214C DC/DC/DC to the hardware configuration
3. Identify all onboard I/O addresses (input/output byte addresses)
4. Add one SM 1223 (8DI/8DQ) expansion module
5. Verify the automatically assigned I/O addresses for the expansion module
6. Document the complete I/O address table

---

## 📚 Additional Resources

- [Siemens S7-1200 System Manual](https://support.industry.siemens.com)
- S7-1200 Hardware Installation Manual
- TIA Portal Getting Started Guide
- SIMATIC S7-1200 Product Catalog

---

*Next Module: [Module 02 — TIA Portal Software & Project Setup](../Module_02_TIA_Portal_Setup/README.md)*
