"""Module 16, 17, 18 — Day 26-30 — Interrupt, Communications, Final Projects"""
from generate_slides import *

def build():
    prs = new_prs()

    # ════════ DAY 26 — Interrupt ════════
    D = "Module 16  |  Day 26"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 16 — Interrupt Instructions",
        "Day 26  |  Advanced Level  |  Duration: 2 Hours",
        RGBColor(0x5C, 0x00, 0x00))

    make_agenda_slide(prs, "Day 26 — Agenda", [
        "Interrupt কী? কখন ব্যবহার করবেন?",
        "Interrupt Types — I/O, Timer, Communication",
        "ATCH — Attach Interrupt Routine",
        "DTCH — Detach Interrupt Routine",
        "ENI / DISI — Enable / Disable Interrupt",
        "CRETI — Conditional Return from Interrupt",
        "Interrupt Event Table (Event 0~33)",
        "Practical: Emergency Stop with Interrupt",
    ], D)

    make_content_slide(prs, "Interrupt — কীভাবে কাজ করে", [
        "## Interrupt মানে:",
        "  - Program চলার মাঝে হঠাৎ একটি জরুরি ঘটনা ঘটলে",
        "  - Main Program থামিয়ে Interrupt Routine (INT) চালু হয়",
        "  - INT শেষে আবার Main Program চলতে থাকে",
        "## কেন Scan Cycle এর চেয়ে ভালো?",
        "  - Scan Time: 1~10ms — এটুকু দেরি অনেক সময় অনেক বেশি",
        "  - Emergency Stop: মাইক্রোসেকেন্ডে Response দরকার",
        "  - HSC, PLS, Timer Events এ Precise Timing দরকার",
        "## Interrupt Priority (উচ্চ থেকে নিম্ন):",
        "  - 1st: Communication Interrupts",
        "  - 2nd: I/O Interrupt (Rising/Falling Edge)",
        "  - 3rd: Time-based Interrupts",
        "## Important Rules:",
        "  - INT Routine সংক্ষিপ্ত রাখুন",
        "  - INT এ CALL, FOR, END, STOP ব্যবহার করা যাবে না",
    ], D, note="Interrupt Routine যত ছোট তত ভালো — মূল কাজটুকুই শুধু করুন!")

    make_table_slide(prs,
        "Interrupt Event Table — গুরুত্বপূর্ণ Events",
        ["Event #", "Event Type", "Trigger", "সাধারণ ব্যবহার"],
        [
            ["0",  "I0.0 Rising Edge",   "I0.0: 0→1",           "Emergency Button Press"],
            ["1",  "I0.0 Falling Edge",  "I0.0: 1→0",           "Button Release detect"],
            ["2",  "I0.1 Rising Edge",   "I0.1: 0→1",           "Encoder Z-pulse"],
            ["8",  "Port 0 Receive",     "Serial Data Received", "Barcode / HMI data"],
            ["9",  "Port 0 Transmit",    "Tx Buffer Empty",      "Next byte send"],
            ["10", "Timed Interrupt 0",  "Every N ms",           "PID, Regular sampling"],
            ["11", "Timed Interrupt 1",  "Every N ms",           "Second PID loop"],
            ["12", "HSC0 CV=PV",         "HSC0 Count Match",     "Position target reached"],
            ["19", "PLS0 Complete",      "Pulse train done",     "Stepper motion complete"],
        ], D, C_RED)

    make_content_slide(prs, "ATCH, DTCH, ENI, DISI — Interrupt Control", [
        "## ATCH (Attach Interrupt):",
        "  - একটি Event কে একটি INT Routine এর সাথে যুক্ত করে",
        "  - ATCH INT_0, 0 → Event 0 (I0.0 Rising) → INT_0 চালাবে",
        "## DTCH (Detach Interrupt):",
        "  - Event থেকে INT Routine বিচ্ছিন্ন করে",
        "  - DTCH 0 → Event 0 এর Interrupt বন্ধ করে",
        "## ENI (Enable All Interrupts):",
        "  - সব Interrupt চালু করে",
        "  - Program শুরুতে একবার ENI দিতে হয়",
        "## DISI (Disable All Interrupts):",
        "  - সব Interrupt সাময়িক বন্ধ করে",
        "  - Critical Section এর সময় ব্যবহার",
        "## Setup Sequence:",
        "  - Step 1: ATCH INT_0, Event#",
        "  - Step 2: ENI (Enable করুন)",
        "  - INT_0 Block এ Response Code লিখুন",
    ], D, note="ENI ছাড়া ATCH করলেও Interrupt কাজ করবে না — ENI অবশ্যই দিতে হবে!")

    make_practical_slide(prs,
        "Practical: Emergency Stop with Interrupt",
        "Emergency Button চাপলে সাথে সাথে সব Output বন্ধ হবে",
        [
            "I0.0 = Emergency Stop Button (N.C. — সবসময় Closed)",
            "I0.0 Falling Edge (0→1, Button Press) = Event 1",
            "Main Program: ATCH INT_0, 1 (Event 1 Attach)",
            "Main Program: ENI (Interrupt Enable করুন)",
            "INT_0 Block এ: MOV_B +0, QB0 (All Output OFF)",
            "INT_0 Block এ: MOV_B +0, QB1 (All Output OFF)",
            "INT_0 Block এ: STOP (CPU Stop করুন)",
            "Test: Normal operation চলার সময় E-Stop চাপুন",
        ], D)

    make_summary_slide(prs,
        "Module 16 — Day 26: Interrupt Instructions",
        ["Interrupt: Scan wait না করে সাথে সাথে Response",
         "ATCH: Event + INT Routine যুক্ত করে",
         "ENI: সব Interrupt চালু করে",
         "DISI: সব Interrupt সাময়িক বন্ধ করে",
         "INT Routine ছোট রাখুন — শুধু জরুরি কাজ"],
        "Day 27 (Module 17):\n• Communications শুরু\n• PPI Protocol\n• NETR ও NETW Instructions",
        D)

    # ════════ DAY 27 — Communications ════════
    D = "Module 17  |  Day 27"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 17 — Communications",
        "Day 27  |  Advanced Level  |  Duration: 2 Hours",
        RGBColor(0x00, 0x3D, 0x5C))

    make_agenda_slide(prs, "Day 27 — Agenda", [
        "S7-200 Communication Ports (Port 0, Port 1)",
        "PPI Protocol — Network Read/Write",
        "NETR ও NETW Instructions",
        "Freeport Mode — Custom Serial Protocol",
        "XMT (Transmit) ও RCV (Receive)",
        "USS Protocol — Variable Speed Drive",
        "Modbus RTU Protocol",
        "HMI (TD400C) সংযোগ",
    ], D)

    make_content_slide(prs, "S7-200 Communication Overview", [
        "## Physical Interface:",
        "  - RS-485 Serial Port (Port 0 ও Port 1)",
        "  - 9-pin D-sub Connector",
        "  - Half-duplex, 2-wire",
        "## Communication Protocols:",
        "  - PPI (Point-to-Point Interface) — Siemens proprietary",
        "  - MPI (Multi-Point Interface) — Multi-device",
        "  - Freeport — Custom ASCII/Binary protocol",
        "  - USS — Variable Speed Drive Control",
        "  - Modbus RTU — Industry Standard",
        "## Baud Rates:",
        "  - PPI: 9600 বা 19200 bps",
        "  - Freeport: 1200 ~ 115200 bps",
        "## PPI Network:",
        "  - সর্বোচ্চ 126টি Device একটি Network এ",
        "  - Master-Slave Architecture",
    ], D, note="S7-200 একই সময়ে Port 0 এ STEP 7-Micro/WIN এবং Port 1 এ HMI connect করা যায়!")

    make_table_slide(prs,
        "Communication Instructions",
        ["Instruction", "Protocol", "কাজ", "ব্যবহার"],
        [
            ["NETR", "PPI",      "Network Read — অন্য PLC থেকে Data পড়া",  "Multi-PLC system"],
            ["NETW", "PPI",      "Network Write — অন্য PLC তে Data লেখা",  "PLC → PLC data share"],
            ["XMT",  "Freeport", "Serial Data পাঠানো",                     "Printer, Barcode, HMI"],
            ["RCV",  "Freeport", "Serial Data গ্রহণ করা",                   "Barcode reader, PC"],
            ["USS_INIT","USS",   "USS Drive Initialize",                    "VFD setup"],
            ["USS_CTRL","USS",   "Drive Speed Control",                     "Motor speed command"],
            ["USS_RPM_R","USS",  "Drive Parameter Read",                    "Drive status read"],
            ["MBUS_INIT","Modbus","Modbus Slave Initialize",                "HMI, SCADA connect"],
            ["MBUS_SLAVE","Modbus","Modbus Slave Execution",                "Regular call in main"],
        ], D, C_TEAL)

    make_content_slide(prs, "Freeport — XMT/RCV ব্যবহার", [
        "## Freeport Setup:",
        "  - SMB30 এ Baud Rate ও Mode Configure করুন",
        "  - SMB30 = 16#09 → 9600 bps, 8N1, Freeport Mode",
        "## XMT (Transmit):",
        "  - XMT VB100, 0 → Port 0 দিয়ে VB100 এর Buffer পাঠায়",
        "  - VB100 = Message Length, VB101~ = Data",
        "  - Transmit Done → Event 9 Interrupt Fire করে",
        "## RCV (Receive):",
        "  - SMB86~SMB94 এ Receive Conditions Configure করুন",
        "  - RCV VB200, 0 → Port 0 থেকে VB200 তে Data গ্রহণ",
        "  - Receive Done → Event 8 Interrupt",
        "## Example: Barcode Scanner",
        "  - Barcode Scanner → RS-232 → USB/RS-485 Converter → Port 0",
        "  - RCV দিয়ে Barcode String গ্রহণ করুন",
        "  - SFND দিয়ে Product Code Match করুন",
    ], D, note="Freeport দিয়ে যেকোনো RS-232/RS-485 Device এর সাথে S7-200 কে যুক্ত করা যায়!")

    make_summary_slide(prs,
        "Module 17 — Day 27: Communications",
        ["PPI: Siemens PLC to PLC — NETR/NETW",
         "Freeport: Custom Serial — XMT/RCV",
         "USS: VFD/Drive Control",
         "Modbus RTU: Industry standard — HMI/SCADA",
         "Port 0 = PC/Programming, Port 1 = HMI/Device"],
        "Day 28 (Module 18):\n• Subroutines ও Structured Programming\n• Final Projects শুরু\n• Traffic Light System",
        D)

    # ════════ DAY 28 — Subroutines ════════
    D = "Module 18  |  Day 28"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 18 — Subroutines & Structured Programming",
        "Day 28  |  Advanced Level  |  Duration: 2 Hours",
        RGBColor(0x1A, 0x1A, 0x1A))

    make_agenda_slide(prs, "Day 28 — Agenda", [
        "Subroutine (SBR) কী এবং কেন দরকার?",
        "Local Variable ও Parameter Passing",
        "Structured Programming Approach",
        "Cross Reference ব্যবহার",
        "Status Chart দিয়ে Debug করা",
        "Project 1: Traffic Light Control System",
    ], D)

    make_content_slide(prs, "Subroutine — Modular Programming", [
        "## কেন Subroutine?",
        "  - একই Code বারবার লেখার দরকার নেই",
        "  - Program কে ছোট ছোট ব্লকে ভাগ করা যায়",
        "  - Testing সহজ হয়",
        "  - Code Reuse — Library তৈরি করা যায়",
        "## S7-200 তে Subroutine:",
        "  - SBR_0, SBR_1 ... SBR_63 (64টি পর্যন্ত)",
        "  - CALL SBR_0 দিয়ে Call করা হয়",
        "  - RET বা CRET দিয়ে Return হয়",
        "## Local Variable:",
        "  - IN: Input Parameter (Caller থেকে দেওয়া)",
        "  - OUT: Output Parameter (SBR থেকে ফেরত)",
        "  - IN_OUT: উভয় দিকে",
        "  - TEMP: Subroutine এর ভেতরে সাময়িক",
        "## Calling with Parameters:",
        "  - CALL SBR_0, VW100, VW200 (IN=VW100, OUT=VW200)",
    ], D, note="Parameter ব্যবহার করে Subroutine আরও Flexible ও Reusable হয়!")

    make_practical_slide(prs,
        "Project 1: Traffic Light Control System",
        "৩টি Signal এর Traffic Light — Green 30s, Yellow 5s, Red 30s",
        [
            "Q0.0=Red, Q0.1=Yellow, Q0.2=Green (Road A)",
            "Q0.3=Red, Q0.4=Yellow, Q0.5=Green (Road B)",
            "MB10 = Traffic Step (0=Init, 1=A-Green, 2=A-Yellow, 3=B-Green, 4=B-Yellow)",
            "SBR_0: Traffic_Timer Subroutine (IN: PT, OUT: Done Bit)",
            "Step 1 (MB10==1): A-Green ON, B-Red ON → Timer 30s",
            "Step 2 (MB10==2): A-Yellow ON → Timer 5s",
            "Step 3 (MB10==3): B-Green ON, A-Red ON → Timer 30s",
            "Step 4 (MB10==4): B-Yellow ON → Timer 5s → Back to Step 1",
        ], D)

    make_summary_slide(prs,
        "Module 18 — Day 28: Subroutines",
        ["SBR: Reusable code block",
         "CALL দিয়ে যেকোনো জায়গা থেকে চালানো যায়",
         "Local Variable দিয়ে Parameter pass করা যায়",
         "Cross Reference: কোন Variable কোথায় আছে",
         "Traffic Light: Step Sequencer + Timer এর সমন্বয়"],
        "Day 29:\n• Final Projects 2, 3, 4\n• Conveyor Sorting System\n• Water Level Control\n• PID Temperature Control",
        D)

    # ════════ DAY 29 — Final Projects ════════
    D = "Module 18  |  Day 29"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 18 — Real-World Projects",
        "Day 29  |  Final Projects Day  |  Duration: 3 Hours",
        RGBColor(0x00, 0x3D, 0x1A))

    make_agenda_slide(prs, "Day 29 — Projects Agenda", [
        "Project 2: Conveyor Belt with Product Sorting",
        "Project 3: Water Level Control System",
        "Project 4: PID Temperature Controller",
        "Project 5: Batch Process with Recipe",
        "Debugging ও Troubleshooting Techniques",
        "Program Documentation Best Practices",
    ], D)

    make_practical_slide(prs,
        "Project 2: Conveyor Belt with Sorting",
        "Product Size অনুযায়ী ৩টি Bin এ Sort করা",
        [
            "I0.0=Start, I0.1=Stop, I0.2=Size Sensor (Analog)",
            "Q0.0=Conveyor Motor, Q0.1=Diverter 1, Q0.2=Diverter 2",
            "AIW0 = Product Size (0=Small, 1000=Medium, 2000=Large)",
            "Network 1: I0.0/I0.1 → Start-Stop Motor (Q0.0)",
            "Network 2: <I AIW0,+1000 → Q0.1 (Bin 1 — Small)",
            "Network 3: >=I AIW0,+1000 AND <I AIW0,+2000 → Q0.2 (Bin 2)",
            "Network 4: >=I AIW0,+2000 → Q0.1+Q0.2 (Bin 3 — Large)",
            "SHRB I0.3, M0.0, 8 (Conveyor position tracking)",
        ], D)

    make_practical_slide(prs,
        "Project 3: Water Level Control System",
        "Tank এর Water Level Low/High অনুযায়ী Pump নিয়ন্ত্রণ",
        [
            "AIW0 = Level Sensor (0=Empty, 32000=Full)",
            "I0.0=High Level Float Switch, I0.1=Low Level Float Switch",
            "Q0.0=Inlet Pump, Q0.1=Outlet Valve, Q0.2=Alarm",
            "Network 1: <=I AIW0,+6400 → S Q0.0 (Level <20%, Pump ON)",
            "Network 2: >=I AIW0,+28800 → R Q0.0 (Level >90%, Pump OFF)",
            "Network 3: >=I AIW0,+30000 → Q0.2 (Overflow Alarm)",
            "Network 4: I0.0 N.C. → S Q0.1 (Float: Not High → Outlet open)",
            "Hysteresis দিয়ে Pump Chattering এড়ানো",
        ], D)

    make_practical_slide(prs,
        "Project 4: PID Temperature Controller",
        "Oven Temperature 180°C তে PID দিয়ে সঠিকভাবে Control করা",
        [
            "AIW0 = Thermocouple Input (0~32000 = 0°C~300°C)",
            "AQW0 = Heater SSR Output (0~32000 = 0~100% Power)",
            "Timed Interrupt (Event 10): Every 100ms → PID Call",
            "INT_0: AIW0 কে 0.0~1.0 তে Scale → VD0 (PV)",
            "INT_0: VD4 = 0.60 (SP = 180/300 = 0.60)",
            "INT_0: PID 0, VD0 (KC=2.5, TI=3.0, TD=0.05)",
            "INT_0: VD8 × 32000.0 → AQW0 (Output Scale)",
            "Tuning: Monitor PV Response → Adjust KC, TI",
        ], D)

    make_summary_slide(prs,
        "Module 18 — Day 29: Real-World Projects",
        ["Conveyor Sorting: Compare + SHRB + Output",
         "Water Level: Compare + Set/Reset + Hysteresis",
         "PID Controller: Interrupt + Analog + PID",
         "Debugging: Status Chart সবচেয়ে গুরুত্বপূর্ণ Tool",
         "Symbol Table ব্যবহার করলে Code পড়া সহজ হয়"],
        "Day 30 (Final Day):\n• Project 5, 6 — Final Assembly Line\n• Course Summary\n• Certification Assessment",
        D)

    # ════════ DAY 30 — Final Day ════════
    D = "Day 30  |  Final"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Day 30 — Course Completion & Assessment",
        "Final Day  |  All Modules Completed  |  Duration: 3 Hours",
        C_NAVY)

    make_agenda_slide(prs, "Day 30 — Final Agenda", [
        "Project 5: Batch Process with Recipe System",
        "Project 6: Multi-Station Assembly Line (Capstone)",
        "Full Course Summary — 18 Modules Review",
        "Career Path ও Industry Certification",
        "Final Assessment / Quiz",
        "Congratulations & Certificate!",
    ], D)

    make_practical_slide(prs,
        "Project 5: Batch Process with Recipe System",
        "3টি Recipe থেকে নির্বাচন করে Batch Process চালানো",
        [
            "VB100~VB109 = Recipe 1 (Speed, Temp, Time, Qty...)",
            "VB110~VB119 = Recipe 2",
            "VB120~VB129 = Recipe 3",
            "IB0 = Recipe Selector Switch",
            "BLKMOV দিয়ে Active Recipe লোড করুন",
            "Math Instruction দিয়ে Analog Output Scale করুন",
            "Step Sequencer দিয়ে Process চালান",
            "Counter দিয়ে Batch Quantity গণুন",
        ], D)

    make_table_slide(prs,
        "Complete Course Summary — 18 Modules",
        ["Module", "Topic", "Key Instructions", "Day"],
        [
            ["01", "PLC Basics",         "Hardware, Scan Cycle, Memory",     "1-2"],
            ["02", "STEP 7 Software",    "LAD Editor, Download, Monitor",     "3"],
            ["03", "Bit Logic",          "Contacts, Coils, SR, RS",           "4-6"],
            ["04", "Timers",             "TON, TONR, TOF",                    "7"],
            ["05", "Counters",           "CTU, CTD, CTUD, HSC, PLS",         "8-9"],
            ["06", "Compare",           "==I, >I, <I, ==R",                   "11"],
            ["07", "Move",              "MOV, BLKMOV, SWAP",                  "12"],
            ["08", "Integer Math",      "ADD, SUB, MUL, DIV, INC, DEC",      "14"],
            ["09", "Float Math + PID",  "ADD_R, SQRT, SIN, PID",             "15-16"],
            ["10", "Convert",           "BCD, ROUND, SEG, ITA",              "18-19"],
            ["11", "Logical Ops",       "AND, OR, XOR, INV",                 "20"],
            ["12", "Shift/Rotate",      "SHL, SHR, ROL, ROR, SHRB",         "21"],
            ["13", "String",            "SCPY, SCAT, SFND",                  "22"],
            ["14", "Table",             "ATT, FIFO, LIFO, FND",              "23"],
            ["15", "Program Control",   "JMP, FOR, CALL, WDR",               "24"],
            ["16", "Interrupt",         "ATCH, ENI, DISI, CRETI",            "26"],
            ["17", "Communications",    "NETR, NETW, XMT, RCV",             "27"],
            ["18", "Projects",          "All Instructions Combined",          "28-30"],
        ], D, C_NAVY)

    # Final Congratulations slide
    slide = blank_slide(prs)
    fill_bg(slide, C_NAVY)
    add_rect(slide, 0, 0, SLIDE_W, Inches(0.08), C_YELLOW)
    add_rect(slide, 0, Inches(6.9), SLIDE_W, Inches(0.6), RGBColor(0x00,0x1A,0x40))

    add_textbox(slide, Inches(1), Inches(0.8), Inches(11), Inches(1.2),
                "🎓 Congratulations!", 48, bold=True,
                color=C_YELLOW, align=PP_ALIGN.CENTER)
    add_rect(slide, Inches(2), Inches(2.1), Inches(9), Inches(0.06), C_TEAL)
    add_textbox(slide, Inches(1), Inches(2.3), Inches(11), Inches(0.7),
                "আপনি Siemens S7-200 PLC Programming Course সম্পন্ন করেছেন!",
                20, color=C_WHITE, align=PP_ALIGN.CENTER)
    add_textbox(slide, Inches(1), Inches(3.1), Inches(11), Inches(0.55),
                "18 Modules  |  30 Days  |  60+ Hours of Learning",
                16, color=C_TEAL, align=PP_ALIGN.CENTER)

    add_rect(slide, Inches(1.5), Inches(3.9), Inches(10), Inches(2.3), RGBColor(0x00,0x1F,0x50))
    add_textbox(slide, Inches(2), Inches(4.0), Inches(9), Inches(0.45),
                "✅  You can now:", 15, bold=True, color=C_YELLOW, align=PP_ALIGN.CENTER)
    skills = [
        "Design ও Program করতে পারবেন যেকোনো Industrial Automation System",
        "Bit Logic, Timer, Counter, Math, PID — সব ব্যবহার করতে পারবেন",
        "HMI, VFD, Modbus Device এর সাথে Communication করতে পারবেন",
    ]
    y = Inches(4.55)
    for s in skills:
        add_textbox(slide, Inches(2), y, Inches(9.5), Inches(0.38),
                    "▸  " + s, 13, color=C_WHITE, align=PP_ALIGN.CENTER)
        y += Inches(0.44)

    add_textbox(slide, Inches(1), Inches(7.0), Inches(11), Inches(0.28),
                "Siemens S7-200 PLC Programming  |  STEP 7-Micro/WIN  |  30 Days Complete",
                10, color=C_TEAL, align=PP_ALIGN.CENTER)

    save(prs, "Module_16_18_Interrupt_Comms_Projects_Day26-30.pptx")

if __name__ == "__main__":
    build()
