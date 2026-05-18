# Practical Projects & Capstone Exercises

> **Level:** All Levels | Consolidate knowledge from all modules

---

## 📋 Overview

These projects are designed to integrate multiple concepts from across the course. Each project builds on the previous, gradually increasing in complexity.

| Project | Level | Modules Used | Duration |
|---|---|---|---|
| P1 — Traffic Light Controller | Basic | M03, M04 | 2–3 hrs |
| P2 — Conveyor Sorting System | Basic-Intermediate | M03, M04, M05 | 3–4 hrs |
| P3 — Water Tank Level Control | Intermediate | M04, M05, M07 | 4–5 hrs |
| P4 — Multi-Motor Drive System | Intermediate | M06, M07, M08 | 5–6 hrs |
| P5 — Batch Process Controller | Advanced | M06, M07, M08, M09 | 6–8 hrs |
| P6 — Complete Packaging Line | Advanced | All modules | 8–12 hrs |

---

## 🟢 Project 1 — Traffic Light Controller

### Difficulty: Basic

### System Description
Automate a 4-way intersection traffic light system with pedestrian crossing.

### Hardware I/O

| Tag | Address | Type | Description |
|---|---|---|---|
| System_Enable | I0.0 | DI | System ON/OFF switch |
| Ped_Button_NS | I0.1 | DI | Pedestrian button (North-South) |
| Ped_Button_EW | I0.2 | DI | Pedestrian button (East-West) |
| NS_Green | Q0.0 | DQ | North-South green light |
| NS_Yellow | Q0.1 | DQ | North-South yellow light |
| NS_Red | Q0.2 | DQ | North-South red light |
| EW_Green | Q0.3 | DQ | East-West green light |
| EW_Yellow | Q0.4 | DQ | East-West yellow light |
| EW_Red | Q0.5 | DQ | East-West red light |
| Ped_Walk_NS | Q0.6 | DQ | Walk signal North-South |
| Ped_Walk_EW | Q0.7 | DQ | Walk signal East-West |

### Timing Requirements

| Phase | Duration |
|---|---|
| NS Green | 15 seconds |
| NS Yellow | 4 seconds |
| EW Green | 15 seconds |
| EW Yellow | 4 seconds |
| Pedestrian walk | 8 seconds (during Red phase) |
| All red (transition) | 2 seconds |

### Requirements
1. Implement full 4-phase sequence using TON timers
2. NS and EW must NEVER be green simultaneously (interlock)
3. Pedestrian buttons queue a walk phase request
4. Walk signal only activates during red phase for that direction
5. System stops (all red) when System_Enable = FALSE
6. Use SCL state machine for phase management (CASE statement)

### Bonus
- Add flashing yellow mode for night operation (M0.5 clock bit)
- Add fault mode if E-Stop pressed

---

## 🟢 Project 2 — Conveyor Sorting System

### Difficulty: Basic-Intermediate

### System Description
Three-lane product sorting conveyor — sorts products by size (small, medium, large) using proximity sensors.

### Hardware I/O

| Tag | Address | Description |
|---|---|---|
| Start_PB | I0.0 | Start pushbutton |
| Stop_PB | I0.1 | Stop pushbutton (NC) |
| E_Stop | I0.2 | Emergency stop (NC) |
| Product_Sensor | I0.3 | Optical sensor — product detected |
| Size_Small | I0.4 | Small product size sensor |
| Size_Large | I0.5 | Large product size sensor |
| Main_Conveyor | Q0.0 | Main belt motor |
| Diverter_Small | Q0.1 | Small product diverter solenoid |
| Diverter_Large | Q0.2 | Large product diverter solenoid |
| Run_Light | Q0.3 | Green run indicator |
| Fault_Light | Q0.4 | Red fault indicator |

### Sorting Logic
```
Size_Small = ON  → Small → Diverter_Small activates
Size_Large = ON  → Large → Diverter_Large activates
Both = OFF       → Medium → passes through
```

### Requirements
1. Seal-in start/stop with E-Stop
2. Count products per category (Small/Medium/Large) in DB
3. Diverter activates for exactly 500ms after detection (TP timer)
4. Jam detection: If Product_Sensor stays ON > 5 seconds → fault
5. Display counts on HMI screen
6. Reset counters button on HMI

### Data Block Structure

```
DB "Sorter_DB"
  Small_Count    : INT
  Medium_Count   : INT
  Large_Count    : INT
  Total_Count    : INT
  Jam_Fault      : BOOL
  System_Running : BOOL
```

---

## 🟡 Project 3 — Water Tank Level Control

### Difficulty: Intermediate

### System Description
Automatic water tank fill and drain system with analog level control.

### Hardware I/O

| Tag | Address | Description |
|---|---|---|
| Level_Raw | IW64 | Analog input — level sensor (0–27648 = 0–100%) |
| Inlet_Valve_AQ | QW80 | Analog output — inlet valve (0–27648 = 0–100% open) |
| High_Level_SW | I0.0 | High level float switch (NC) |
| Low_Level_SW | I0.1 | Low level float switch (NO) |
| Drain_Valve | I0.2 | Manual drain valve open feedback |
| Fill_Mode | I0.3 | Auto-fill mode switch |
| Pump_Enable | Q0.0 | Inlet pump (runs when valve opens) |
| Drain_Pump | Q0.1 | Drain pump |
| High_Alarm_Light | Q0.2 | High level alarm light |
| Low_Alarm_Light | Q0.3 | Low level alarm light |

### Control Requirements

**Level Setpoints:**
```
High alarm:     90% → close inlet, alarm light
High limit:     85% → close inlet valve
Normal high:    75% → reduce fill rate
Setpoint:       60% → maintain target
Normal low:     45% → increase fill rate
Low limit:      20% → open inlet fully
Low alarm:      15% → alarm light
```

**Control Modes:**
1. **Manual:** Operator sets valve position from HMI
2. **Auto:** PID_Compact controls level automatically
3. **Drain:** Drain pump runs until low level switch

### Requirements
1. Scale analog input: IW64 → Level_Percent (0.0–100.0%)
2. Implement PID_Compact in OB30 (500ms) for valve control
3. Switch between Manual/Auto/Drain modes via HMI
4. High and low hardware alarm interlocks (independent of PLC)
5. Alarm logging with timestamps in DB
6. HMI screen showing tank graphic with level, alarms, mode selector

### Data Block Structure

```
DB "Tank_DB"
  Level_Percent   : REAL
  Level_SP        : REAL      // Setpoint (default 60.0)
  Valve_Manual    : REAL      // Manual valve position
  Control_Mode    : INT       // 0=Manual, 1=Auto, 2=Drain
  High_Alarm      : BOOL
  Low_Alarm       : BOOL
  Alarm_Count     : INT
  Last_Alarm_Time : TOD
```

---

## 🟡 Project 4 — Multi-Motor Drive System

### Difficulty: Intermediate-Advanced

### System Description
Industrial drive system with 3 motors, speed control via VFD (Variable Frequency Drive), fault management, and remote monitoring.

### System Overview

```
                    S7-1200 CPU 1214C
                         │
              ┌──────────┼──────────┐
              │          │          │
          VFD_1       VFD_2       VFD_3
         (Modbus)   (Modbus)    (Analog)
              │          │          │
          Motor_1    Motor_2    Motor_3
         (Main)     (Infeed)   (Output)
```

### VFD Communication (Modbus RTU via CM 1241)

| Register | Description |
|---|---|
| 40001 | Control word (start/stop/direction) |
| 40002 | Speed setpoint (0–16384 = 0–100%) |
| 40003 | Status word (running/fault) |
| 40004 | Actual speed (Hz × 10) |
| 40005 | Output current (A × 10) |

### Requirements

1. **FB_VFD_Modbus** — reusable FB for each VFD:
   - Parameters: Slave_Addr, Speed_SP, Enable, Direction
   - Outputs: Running, Faulted, Actual_Speed, Current
   - Uses MB_MASTER internally

2. **Sequencing logic:**
   - Motor_1 (main) starts first
   - Motor_2 starts 2s after Motor_1 running
   - Motor_3 starts 2s after Motor_2 running
   - Stop: reverse order

3. **Speed control:**
   - Group speed setpoint (all motors same %)
   - Individual trim per motor (±10% adjustment)

4. **Fault management:**
   - Any motor fault → group stop after 5s coast
   - Fault logging in DB with motor ID and code
   - HMI fault history screen

5. **HMI:**
   - Motor overview screen (speed, current, status)
   - Speed control group setpoint
   - Individual trim sliders
   - Fault history

---

## 🔴 Project 5 — Batch Process Controller

### Difficulty: Advanced

### System Description
Automated batch mixing/processing system with recipe management, temperature control, and HMI operation.

### Process Overview

```
Phase 1: FILLING      → Fill vessel to target volume
Phase 2: HEATING      → Heat to recipe temperature
Phase 3: MIXING       → Run agitator at recipe speed
Phase 4: DOSING       → Add chemical dose per recipe
Phase 5: REACTION     → Hold for reaction time
Phase 6: COOLING      → Cool to safe discharge temp
Phase 7: DRAINING     → Drain vessel
Phase 8: COMPLETE     → Ready for next batch
```

### Hardware I/O

| Category | Tags | Description |
|---|---|---|
| **Inlets** | Inlet_Valve_1, Inlet_Valve_2 | Water/chemical inlets |
| **Agitator** | Agitator_Motor, Agitator_Speed_AQ | Mixing motor + VFD |
| **Heater** | Heater_SSR | Solid State Relay (PID controlled) |
| **Cooling** | Cooling_Valve | Cooling water inlet |
| **Sensors** | Temp_AI, Level_AI, Flow_AI | Process measurements |
| **Drain** | Drain_Valve, Drain_Pump | Discharge |

### Recipe Structure (SCL)

```pascal
TYPE UDT_Recipe
  Name        : STRING[20];
  Fill_Volume : REAL;         // Target fill level %
  Heat_Temp   : REAL;         // Target temperature °C
  Mix_Speed   : INT;          // Agitator speed %
  Dose_Volume : REAL;         // Chemical dose %
  React_Time  : TIME;         // Reaction hold time
  Cool_Temp   : REAL;         // Cool-to temperature °C
END_TYPE;

DB "Recipe_DB"
  Recipes     : ARRAY[1..10] OF UDT_Recipe;
  Active_Recipe : UDT_Recipe;
  Recipe_Number : INT;
END_DATA_BLOCK
```

### Requirements

1. **FB_BatchController** (SCL) with 8-state machine
2. **FC_Load_Recipe** copies recipe to active DB
3. **PID_Compact** for temperature control in OB30
4. **Analog scaling** for temp/level/flow sensors
5. **Alarm management:**
   - High temperature (> setpoint + 20°C)
   - Low level (< 5%)
   - Agitator fault
   - Heater fault
6. **HMI:**
   - Batch overview (current phase, progress bar)
   - Recipe selection (1–10)
   - Process values (temp trend, level)
   - Alarm screen
   - Batch history (last 20 batches)

---

## 🔴 Project 6 — Complete Packaging Line (Capstone)

### Difficulty: Advanced (Capstone)

### System Description
Full industrial packaging line — integrates all course concepts into a real-world simulation.

### Line Overview

```
Feed Hopper → Weigh Station → Fill Station → Seal Station → Label Station → Output Conveyor
                  │                │               │               │
              Load Cell (AI)   Fill Valve      Seal Press      Label Dispenser
                               (Timed)         (Pressure AI)   (Modbus)
```

### Modules Used

| Module | Covered From |
|---|---|
| Basic I/O, motor control | M03 |
| Timers and counters | M04 |
| Data blocks and arrays | M05 |
| FB for each station | M06 |
| Load cell and pressure analog | M07 |
| HMI dashboard + Modbus label printer | M08 |
| SCL state machines | M09 |
| Fault management + safety | M10 |

### Full System Requirements

1. **5 Station FBs** (one per station), each with:
   - State machine (IDLE/ACTIVE/COMPLETE/FAULT)
   - Handshake signals (Station_Ready, Station_Done)
   - Individual fault detection

2. **Master Sequencer FB** coordinates all stations

3. **Recipe management:**
   - 5 product recipes
   - Weight target, fill time, seal pressure per recipe

4. **Complete HMI** (6 screens minimum):
   - Line overview (all stations graphical)
   - Production statistics
   - Recipe selection
   - Alarm management
   - Trend views (weight, pressure)
   - Manual operation

5. **OEE Calculation (Availability × Performance × Quality):**
   - Log good/reject counts
   - Track downtime per station
   - Calculate and display OEE%

6. **Communication:**
   - Modbus TCP to label printer
   - OPC UA tags exposed for MES

---

## 📋 Assessment Checklist

For each project, verify:

### Code Quality ✅
- [ ] All tags have meaningful names
- [ ] All networks have comments
- [ ] No double coils
- [ ] No hardcoded addresses in code
- [ ] OB100 initializes safe defaults
- [ ] EN/ENO used on all block calls

### Functionality ✅
- [ ] Normal operation works correctly
- [ ] E-Stop stops everything immediately
- [ ] Faults are detected and logged
- [ ] Fault reset works correctly
- [ ] All HMI buttons/displays function

### Safety ✅
- [ ] No output can cause hazard on power-up
- [ ] Division by zero protected
- [ ] Sensor range validation implemented
- [ ] Output feedback checked

### Documentation ✅
- [ ] I/O address table documented
- [ ] DB structures described
- [ ] State machine diagram drawn
- [ ] Alarm list documented
- [ ] Version noted in PLC properties

---

## 🏆 Final Certification Criteria

To complete the course, you should be able to:

| Skill | Demonstrated In |
|---|---|
| Create TIA Portal project | Project 1 |
| LAD motor control | Projects 1, 2 |
| Timers and counters | Projects 1, 2, 3 |
| Analog scaling | Projects 3, 4 |
| FB/FC/OB structure | Projects 4, 5, 6 |
| PID control | Projects 3, 5, 6 |
| HMI design | All projects P3+ |
| Modbus communication | Projects 4, 6 |
| SCL state machines | Projects 5, 6 |
| Fault management | Projects 4, 5, 6 |

---

*Return to: [Course Home](../README.md)*
