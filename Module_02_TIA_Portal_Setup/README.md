# Module 02 — TIA Portal Software & Project Setup

> **Level:** Basic | **Duration:** ~2.5 Hours | **Prerequisites:** Module 01

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Install and navigate TIA Portal V16/V17/V18
- Create a new PLC project from scratch
- Configure S7-1200 hardware in the device configurator
- Set up IP addressing and PROFINET settings
- Go online, download a project, and monitor the PLC
- Use simulation with PLCSIM

---

## 📖 Lesson 2.1 — TIA Portal Overview

### What is TIA Portal?
**Totally Integrated Automation (TIA) Portal** is Siemens' unified engineering framework for:
- PLC programming (STEP 7)
- HMI design (WinCC)
- Drive parameterization (Startdrive)
- Safety programming (Safety Advanced)

### TIA Portal Versions

| Version | Year | Notes |
|---|---|---|
| V13 SP1 | 2015 | S7-1200 FW 4.x support |
| V14 SP1 | 2017 | Improved SCL, F-CPU |
| V15.1 | 2018 | Web server enhancements |
| V16 | 2019 | S7-1500T, OPC UA server |
| V17 | 2021 | Improved simulation |
| V18 | 2023 | Latest — recommended |

### License Types

| License | Usage |
|---|---|
| **STEP 7 Basic** | S7-1200 only, basic features |
| **STEP 7 Professional** | S7-1200/1500/300/400, all features |
| **Trial License** | 21-day evaluation |

---

## 📖 Lesson 2.2 — TIA Portal Installation

### System Requirements (V18)

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 (64-bit) | Windows 10/11 (64-bit) |
| RAM | 8 GB | 16 GB or more |
| HDD | 30 GB free | SSD 50+ GB |
| CPU | Intel Core i5 | Intel Core i7/i9 |
| Display | 1024×768 | 1920×1080 or higher |

### Installation Steps
1. Run TIA Portal installer as **Administrator**
2. Accept license agreement
3. Select components:
   - ✅ STEP 7 Professional / Basic
   - ✅ PLCSIM (for simulation)
   - ✅ WinCC (if HMI needed)
4. Choose installation path (default recommended)
5. Install — may take **30–60 minutes**
6. Restart computer when prompted
7. Activate license using **Automation License Manager**

---

## 📖 Lesson 2.3 — TIA Portal Interface

### Main Views

```
┌─────────────────────────────────────────────────────────┐
│                    TIA PORTAL                           │
│  ┌──────────────┐  ┌──────────────────────────────────┐ │
│  │   Project    │  │                                  │ │
│  │   Tree       │  │         WORK AREA                │ │
│  │              │  │   (Editor / Configuration)       │ │
│  │  ├─ Device   │  │                                  │ │
│  │  ├─ PLC_1    │  │                                  │ │
│  │  │  ├─ OBs   │  │                                  │ │
│  │  │  ├─ FBs   │  └──────────────────────────────────┘ │
│  │  │  ├─ FCs   │  ┌──────────────────────────────────┐ │
│  │  │  └─ DBs   │  │         INSPECTOR WINDOW         │ │
│  │  └─ HMI_1    │  │    (Properties / Diagnostics)    │ │
│  └──────────────┘  └──────────────────────────────────┘ │
│                                                         │
│  [Portal View] [Project View]    [Task Cards] →→→       │
└─────────────────────────────────────────────────────────┘
```

### Portal View vs Project View
- **Portal View** — Startup screen, task-based navigation (for beginners)
- **Project View** — Full working environment (for everyday use)

### Key Areas
| Area | Description |
|---|---|
| **Project Tree** | Left panel — all project components |
| **Work Area** | Center — editors open here |
| **Inspector Window** | Bottom — properties, info, diagnostics |
| **Task Cards** | Right — hardware catalog, libraries, instructions |
| **Toolbar** | Top — save, compile, download, go online |

---

## 📖 Lesson 2.4 — Creating a New Project

### Step-by-Step: New Project

**Step 1:** Open TIA Portal → Click **"Create new project"**
```
Project name:  MY_FIRST_PLC
Path:          C:\TIA_Projects\
Author:        Your Name
Comment:       S7-1200 Training Project
```

**Step 2:** Click **Create** → Project View opens

**Step 3:** In Project Tree → Double-click **"Add new device"**

**Step 4:** Select your CPU:
```
Controllers → SIMATIC S7-1200 → CPU → CPU 1214C DC/DC/DC
                                      → 6ES7 214-1AG40-0XB0
                                      → Version: V4.4
```

**Step 5:** Click **OK** — Device view opens

---

## 📖 Lesson 2.5 — Hardware Configuration

### Device View
The Device View shows the physical rack with:
- CPU in slot 1
- Available slots for expansion modules

### Adding Expansion Modules

**Method 1: Drag & Drop**
1. Open **Hardware Catalog** (right side Task Card)
2. Navigate to: `Signal boards → DI/DQ → SM 1223`
3. Drag module to empty slot in rack

**Method 2: Double-click**
1. Double-click empty slot in rack
2. Hardware Catalog auto-filters
3. Select module and click OK

### Setting CPU Properties

Double-click the CPU in Device View → **Properties** tab in Inspector Window:

#### General Tab
```
Name:     PLC_1
Author:   [Your name]
Comment:  Main controller
```

#### PROFINET Interface
```
IP Address:      192.168.1.1
Subnet Mask:     255.255.255.0
Router Address:  192.168.1.254  (if needed)
```

#### Startup Behavior
```
Startup after POWER ON:  Warm restart - RUN
```

#### Protection
```
Access level:  Full access (no protection)   ← for learning
               HMI access                    ← for production
```

### I/O Address Overview (CPU 1214C)

| Component | Address Range |
|---|---|
| Onboard DI | I0.0 – I1.5 (14 inputs) |
| Onboard DQ | Q0.0 – Q1.1 (10 outputs) |
| Onboard AI | IW64, IW66 (2 analog inputs) |
| First SM slot | I2.0+ / Q2.0+ |

---

## 📖 Lesson 2.6 — Program Blocks Overview

### Block Types in TIA Portal

| Block | Full Name | Purpose |
|---|---|---|
| **OB** | Organization Block | Called by OS — main program entry point |
| **FC** | Function | Subroutine, no static memory |
| **FB** | Function Block | Subroutine with static memory (Instance DB) |
| **DB** | Data Block | Data storage — Global or Instance |

### Default Organization Blocks

| OB | Number | Trigger |
|---|---|---|
| Main [OB1] | OB1 | Cyclic — every scan |
| Startup [OB100] | OB100 | Once on PLC start/restart |
| Time Interrupt | OB10–OB17 | Time-based trigger |
| Hardware Interrupt | OB40–OB47 | I/O edge trigger |
| Cyclic Interrupt | OB30–OB38 | Fixed time interval |
| Diagnostic Error | OB82 | Hardware fault |

---

## 📖 Lesson 2.7 — Compiling & Downloading

### Compile the Project

1. Right-click **PLC_1** in Project Tree
2. Select **Compile → Hardware and Software (only changes)**
3. Check **Inspector Window → Info → Compile** tab
4. Ensure **0 errors, 0 warnings**

### Going Online

**Method 1: Via Project Tree**
1. Right-click **PLC_1** → **Go online**
2. Select interface: `PN/IE → [Your Network Card]`
3. Select subnet: `192.168.1.x`
4. Click **Go online**

**Method 2: Extended Download**
1. Click **Download to device** button (⬇ icon in toolbar)
2. Select PG/PC Interface
3. Click **Start search** → CPU appears
4. Select CPU → **Load** → **Finish**

### Online Indicators
```
PLC_1 [Online]          ← Green circle = connected
  └─ [RUN] ✅           ← CPU running
  └─ [Consistent] ✅    ← Program matches
  └─ [Not protected]    ← No password
```

### Download Process
```
1. Compile     → Check for errors
2. Stop CPU    → (if required)
3. Download    → Transfer program to CPU
4. Start CPU   → Resume execution
```

---

## 📖 Lesson 2.8 — PLCSIM — Software Simulation

### What is PLCSIM?
**PLCSIM** allows you to simulate an S7-1200 CPU on your computer **without real hardware**.

### Starting PLCSIM
1. Click **Start simulation** button (▶ icon with screen)
2. PLCSIM window opens — virtual CPU starts
3. Go online to PLCSIM (same as real CPU)
4. Download your project

### PLCSIM Features
- Simulate DI/DQ/AI/AQ
- Force values
- Monitor variables in Watch Tables
- Test program logic

### Watch Tables
1. Project Tree → **PLC_1 → Watch and force tables → Add new watch table**
2. Enter variable addresses or tag names
3. Click **Monitor all** (glasses icon)
4. Observe live values

---

## 📖 Lesson 2.9 — Tag Table (PLC Tags)

### Creating PLC Tags

Project Tree → **PLC_1 → PLC tags → Default tag table**

| Name | Data Type | Address | Comment |
|---|---|---|---|
| Start_Button | Bool | %I0.0 | Green start button |
| Stop_Button | Bool | %I0.1 | Red stop button |
| Motor_Run | Bool | %Q0.0 | Motor contactor |
| Fault_Light | Bool | %Q0.1 | Fault indicator lamp |
| Speed_Ref | Int | %MW10 | Motor speed reference |
| Temp_Value | Real | %MD20 | Temperature reading |

### Address Format
```
%I0.0    → Input Bit,  Byte 0, Bit 0
%Q0.0    → Output Bit, Byte 0, Bit 0
%M0.0    → Memory Bit, Byte 0, Bit 0
%IW64    → Input Word (Analog), starts at byte 64
%MW10    → Memory Word, starts at byte 10
%MD20    → Memory Double word, starts at byte 20
```

---

## ✅ Module 2 — Review Questions

1. What are the two main views in TIA Portal and when do you use each?
2. What is the difference between STEP 7 Basic and STEP 7 Professional?
3. What IP address format does PROFINET use?
4. Name the 4 block types in TIA Portal and explain each.
5. What does OB1 do and how often is it called?
6. What is PLCSIM and why is it useful?
7. What does `%I0.0` mean in Siemens addressing?
8. How do you compile a project and what should you check after?

---

## 🔬 Practical Exercise 2.1

**Task:** Create Your First TIA Portal Project
1. Create new project: `S7_1200_Training`
2. Add CPU 1214C DC/DC/DC (V4.4)
3. Set IP Address: `192.168.1.10`
4. Add SM 1223 expansion module
5. Create PLC tag table with at least 8 tags (use addresses above)
6. Compile successfully (0 errors)
7. Simulate using PLCSIM
8. Create a Watch Table and monitor 3 variables

---

*Previous: [Module 01](../Module_01_Intro_Hardware/README.md) | Next: [Module 03](../Module_03_Basic_Programming/README.md)*
