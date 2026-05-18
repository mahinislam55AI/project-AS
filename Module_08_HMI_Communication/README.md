# Module 08 — HMI Integration & Communication

> **Level:** Advanced | **Duration:** ~5 Hours | **Prerequisites:** Module 05, 06

---

## 🎯 Learning Objectives

By the end of this module, you will be able to:
- Configure SIMATIC HMI panels (KTP series)
- Create HMI screens with buttons, indicators, and values
- Set up PLC-HMI communication via PROFINET
- Implement Modbus TCP and Modbus RTU communication
- Use PUT/GET communication between PLCs
- Configure OPC UA server on S7-1200

---

## 📖 Lesson 8.1 — Communication Interfaces

### S7-1200 Built-in Communication

| Interface | Protocol | Notes |
|---|---|---|
| **PROFINET** (onboard) | PROFINET IO, S7 protocol, OPC UA | 1 port (CPU 1211-1214), 2 ports (1215/1217) |
| **PROFINET** | Modbus TCP, TCP/IP | Via PROFINET |
| **RS485/RS232** | Modbus RTU, USS, ASCII | Via CM 1241 module |
| **PROFIBUS** | PROFIBUS DP | Via CM 1242/1243 |

### Communication Protocols Overview

| Protocol | Type | Use Case |
|---|---|---|
| **S7 (PUT/GET)** | Siemens proprietary | PLC-to-PLC (Siemens) |
| **PROFINET IO** | Siemens/Open | I/O devices, drives |
| **Modbus TCP** | Open standard | Third-party devices, SCADA |
| **Modbus RTU** | Open standard | Serial devices, drives |
| **OPC UA** | Open standard | Industry 4.0, SCADA, Cloud |
| **USS** | Siemens | SINAMICS/MICROMASTER drives |
| **TCP/UDP** | Open | Custom protocols |

---

## 📖 Lesson 8.2 — SIMATIC HMI Panels

### KTP Panel Family

| Panel | Size | Resolution | Notes |
|---|---|---|---|
| **KTP400 Basic** | 4" | 480×272 | Entry-level, touch |
| **KTP700 Basic** | 7" | 800×480 | Popular, touch + function keys |
| **KTP900 Basic** | 9" | 800×480 | Larger display |
| **KTP1200 Basic** | 12" | 1280×800 | Large format |
| **TP700 Comfort** | 7" | 800×480 | Advanced features |
| **TP1200 Comfort** | 12" | 1280×800 | High-end |

### KTP700 Basic — Key Features
- 7" widescreen TFT
- 800×480 resolution
- 8 function keys (F1–F8)
- PROFINET interface
- USB host for backup
- 24V DC supply

---

## 📖 Lesson 8.3 — Adding HMI to TIA Portal Project

### Step 1: Add HMI Device

1. Project Tree → **Add new device → HMI**
2. Select: `SIMATIC Basic Panel → 7" Display → KTP700 Basic → 6AV2 123-2GB03-0AX0`
3. **HMI Wizard** opens automatically

### Step 2: HMI Wizard Configuration

```
Page 1: PLC Connections
  → Select PLC: PLC_1
  → Connection: HMI_Connection_1 (auto-created)
  → Interface: PROFINET

Page 2: Screen layout
  → Select screen template

Page 3: Alarms (optional)

Page 4: Screen navigation

Page 5: System screens

Page 6: Finish
```

### Step 3: Network View

1. Open **Network View** (Devices & Networks)
2. Drag PROFINET line from HMI to PLC
3. Assign IP addresses:
   ```
   PLC_1:    192.168.1.10
   HMI_1:    192.168.1.20
   Subnet:   255.255.255.0
   ```

---

## 📖 Lesson 8.4 — HMI Screen Design

### Screen Types

| Screen Type | Purpose |
|---|---|
| **Root screen** | Main navigation screen |
| **Template** | Header/footer applied to all screens |
| **Popup screen** | Overlays for alarms, entry dialogs |
| **Permanent screen** | Always visible (e.g., header) |

### Basic HMI Objects

| Object | Use | Connected to |
|---|---|---|
| **Button** | Trigger actions | PLC tag or script |
| **Text field** | Static labels | None |
| **I/O Field** | Display/enter values | PLC tag (REAL/INT) |
| **Text list** | Enumerated values | PLC tag (INT) |
| **Graphic I/O** | Image-based display | PLC tag |
| **Bar graph** | Level/progress display | PLC tag (REAL) |
| **Alarm view** | Show active alarms | Alarm system |
| **Trend view** | Historical trends | Analog tags |

### Creating a Main Screen

**Step 1:** Double-click **Screen_1** in HMI project tree

**Step 2:** From Toolbox, add:
- **Text field:** "MACHINE CONTROL SYSTEM"
- **Button:** "START" → Event → Set bit → `"Start_Command"` (PLC tag)
- **Button:** "STOP"  → Event → Reset bit → `"Stop_Command"`
- **Circle:** Motor indicator → Color animation → linked to `"Motor_Running"`
- **I/O Field:** Current speed → linked to `"Current_Speed_RPM"` (INT)
- **Bar Graph:** Temperature → linked to `"Temperature_C"` (REAL), 0–200

### Animations

**Color Animation (for status indicators):**
```
Object: Circle (Motor status)
Animation → Appearance → Background Color
  Condition: PLC_tag = 0 → Color: Gray
  Condition: PLC_tag = 1 → Color: Green
```

**Visibility Animation:**
```
Object: Alarm text
Animation → Visibility
  Visible when: "Fault_Active" = TRUE
```

---

## 📖 Lesson 8.5 — HMI Tags

### Creating HMI Tags

Project Tree → **HMI_1 → HMI tags → Default tag table**

| Name | Connection | PLC Tag | Data Type | Access |
|---|---|---|---|---|
| Motor_Start | HMI_Connection_1 | Motor_Start_Cmd | Bool | Read/Write |
| Motor_Stop | HMI_Connection_1 | Motor_Stop_Cmd | Bool | Read/Write |
| Motor_Run_FB | HMI_Connection_1 | Motor_Running | Bool | Read |
| Speed_Display | HMI_Connection_1 | Current_Speed | Int | Read |
| Temp_Display | HMI_Connection_1 | Temperature_C | Real | Read |
| Temp_Setpoint | HMI_Connection_1 | Temp_SP | Real | Read/Write |

### HMI Tag Update Cycles

| Cycle | Typical Use |
|---|---|
| 100ms | Fast changing values, critical status |
| 500ms | Normal process values |
| 1s | Slow changing data |
| 2s | Non-critical information |

---

## 📖 Lesson 8.6 — HMI Alarms

### Alarm Types

| Type | Description | Display |
|---|---|---|
| **Discrete alarm** | Bit-triggered alarm | Alarm view |
| **Analog alarm** | Value threshold alarm | Alarm view |
| **System alarm** | HMI/communication errors | System alarm view |

### Creating Discrete Alarms

Project Tree → **HMI_1 → Alarms → Discrete alarms → Add**

```
Name:           Motor_Fault
Trigger tag:    Fault_Active (PLC Bool tag)
Trigger bit:    0
Class:          Errors
Alarm text:     "MOTOR FAULT — Check Drive"
Priority:       High

Acknowledgment: Required
```

### Alarm Classes

| Class | Typical Use | Color |
|---|---|---|
| Errors | Faults requiring stop | Red |
| Warnings | Caution conditions | Yellow |
| System | HMI/PLC comm issues | Blue |

---

## 📖 Lesson 8.7 — Modbus TCP

### What is Modbus TCP?
- Open standard protocol over **Ethernet/PROFINET**
- Master/Slave architecture (now Client/Server)
- S7-1200 can be **Client** (master) or **Server** (slave)
- Uses TCP port **502**

### S7-1200 as Modbus TCP Client (Master)

**Instructions needed:**
- `MB_CLIENT` — connects and communicates with Modbus server

**MB_CLIENT Call in OB1:**
```
MB_CLIENT [DB: "ModbusTCP_Client"]
EN           ENO
REQ:      M10.0  (trigger request)
DISCONNECT: FALSE
MB_ADDR:  192.168.1.100  (server IP)
MB_PORT:  502            (Modbus port)
MODE:     0              (read coils=0, read holding=3, write=5)
MB_DATA_ADDR: 40001      (Modbus address)
MB_DATA_LEN:  10         (number of registers)
MB_DATA_PTR:  P#DB5.DBX0.0 WORD 10  (local storage)
→ DONE:   M10.1
→ BUSY:   M10.2
→ ERROR:  M10.3
→ STATUS: MW100
```

### Modbus Address Map

| Function Code | Address Range | Data Type | Description |
|---|---|---|---|
| FC01 Read | 00001–09999 | Bit | Read Coils (outputs) |
| FC02 Read | 10001–19999 | Bit | Read Discrete Inputs |
| FC03 Read | 40001–49999 | Word | Read Holding Registers ← most common |
| FC04 Read | 30001–39999 | Word | Read Input Registers |
| FC05 Write | 00001–09999 | Bit | Write Single Coil |
| FC06 Write | 40001–49999 | Word | Write Single Register |
| FC15 Write | 00001–09999 | Bit | Write Multiple Coils |
| FC16 Write | 40001–49999 | Word | Write Multiple Registers |

### S7-1200 as Modbus TCP Server (Slave)

```
MB_SERVER [DB: "ModbusTCP_Server"]
EN           ENO
MB_HOLD_REG: P#DB6.DBX0.0 WORD 100  (holding registers storage)
CONNECT:     DB7.Connection_Params
→ NDR:    M11.0  (new data received)
→ DR:     M11.1  (data request sent)
→ ERROR:  M11.2
→ STATUS: MW102
```

---

## 📖 Lesson 8.8 — Modbus RTU (Serial)

### Hardware Required
**CM 1241** — Communication Module for RS485/RS232

### Modbus RTU Configuration

1. Add CM 1241 to hardware config (left of CPU)
2. Configure: RS485, 9600 baud, No parity, 1 stop bit (or per device)

### MB_COMM_LOAD — Initialize Serial Port

```
(Call once in OB100 or on first scan)
MB_COMM_LOAD
EN           ENO
REQ:     M1.0 (first scan)
PORT:    270  (CM 1241 port number)
BAUD:    9600
PARITY:  0    (none=0, odd=1, even=2)
FLOW_CTRL: 0
RTS_ON_DLY: 0
RTS_OFF_DLY: 0
→ DONE:  M12.0
→ ERROR: M12.1
→ STATUS: MW110
```

### MB_MASTER — Communicate with Modbus RTU Slave

```
MB_MASTER [DB: "ModbusRTU_Master"]
EN           ENO
REQ:      M13.0  (trigger)
PORT:     270    (CM 1241)
MB_ADDR:  1      (slave address 1–247)
MODE:     3      (read holding registers)
DATA_ADDR: 40001
DATA_LEN:  5
DATA_PTR: P#DB8.DBX0.0 WORD 5
→ DONE:   M13.1
→ BUSY:   M13.2
→ ERROR:  M13.3
→ STATUS: MW112
```

---

## 📖 Lesson 8.9 — S7 PUT/GET Communication (PLC-to-PLC)

### Overview
PUT/GET allows direct data exchange between **Siemens PLCs** over PROFINET.

```
PLC_1 (Client)          PROFINET          PLC_2 (Server)
PUT/GET FB ────────────────────────────── Data in DB
```

### Enabling GET/PUT on Server PLC
TIA Portal → **PLC_2 → Properties → Protection**
→ **Allow access via PUT/GET** ✅

> ⚠️ Security: Enable only on trusted networks!

### TPUT Instruction (PUT)

```
PUT [DB: "PUT_DB"]
EN           ENO
REQ:      M20.0   (trigger)
ID:       W#16#0001  (connection ID)
ADDR_1:   P#DB2.DBX0.0 BYTE 10  (remote address in PLC_2)
SD_1:     P#DB1.DBX0.0 BYTE 10  (local data to send)
→ DONE:   M20.1
→ ERROR:  M20.2
→ STATUS: MW120
```

### TGET Instruction (GET)

```
GET [DB: "GET_DB"]
EN           ENO
REQ:      M21.0   (trigger)
ID:       W#16#0001
ADDR_1:   P#DB3.DBX0.0 BYTE 20  (remote address in PLC_2)
RD_1:     P#DB4.DBX0.0 BYTE 20  (local storage for received data)
→ NDR:    M21.1
→ ERROR:  M21.2
→ STATUS: MW122
```

---

## 📖 Lesson 8.10 — OPC UA Server

### What is OPC UA?
**OPC Unified Architecture** — Industry 4.0 open standard for:
- PLC → SCADA integration
- PLC → Cloud connectivity (Azure, AWS)
- PLC → MES/ERP systems
- Cross-vendor communication

### Enabling OPC UA Server on S7-1200

1. TIA Portal → **PLC_1 → Properties → OPC UA**
2. **Enable OPC UA server** ✅
3. Configure:
   ```
   Server port:    4840 (default)
   Security Mode:  None (for testing), Sign+Encrypt (production)
   ```
4. Export tags as OPC UA nodes:
   - Right-click Global DB → Properties → **Accessible from HMI/OPC UA** ✅

### Connecting from OPC UA Client
```
Endpoint URL: opc.tcp://192.168.1.10:4840
Node ID:      ns=3;s="Production_DB".Temperature_C
```

---

## ✅ Module 8 — Review Questions

1. What communication protocols are built into S7-1200?
2. What IP settings do you need for PLC-HMI PROFINET?
3. What is the Modbus TCP default port number?
4. What is the difference between Modbus TCP Client and Server?
5. What hardware is needed for Modbus RTU on S7-1200?
6. What Modbus function code reads holding registers?
7. What must be enabled on the server PLC for PUT/GET?
8. What is OPC UA and what is it used for in Industry 4.0?
9. How do you create an alarm in the HMI?
10. What is the difference between discrete and analog alarms?

---

## 🔬 Practical Exercise 8.1 — HMI Machine Dashboard

**Task:** Create a complete machine HMI:
1. Screen 1 (Main): Motor start/stop buttons, run indicator, speed display
2. Screen 2 (Process): Temperature bar graph, setpoint I/O field, PID output
3. Screen 3 (Alarms): Alarm view showing all active alarms
4. Add 3 discrete alarms: Motor_Fault, High_Temp, E_Stop_Active
5. Navigation buttons between screens
6. Simulate and test all functions

---

*Previous: [Module 07](../Module_07_Analog_PID/README.md) | Next: [Module 09](../Module_09_SCL_Advanced/README.md)*
