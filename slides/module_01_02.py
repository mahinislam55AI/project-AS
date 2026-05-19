"""Module 01 & 02 — Day 1, 2, 3"""
from generate_slides import *

def build():
    prs = new_prs()

    # ════════════════════════════════════════════════════════
    #  DAY 1  — PLC Basic Concept & Introduction
    # ════════════════════════════════════════════════════════
    D = "Module 01  |  Day 1"

    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 01 — PLC Basic Concept & Introduction",
        "Day 1  |  Beginner Level  |  Duration: 2 Hours",
        C_NAVY)

    make_agenda_slide(prs, "Day 1 — Agenda", [
        "What is a PLC? (প্রোগ্রামেবল লজিক কন্ট্রোলার পরিচয়)",
        "PLC vs Relay Logic — পার্থক্য ও সুবিধা",
        "Industry Applications — কোথায় কোথায় ব্যবহার হয়",
        "PLC Hardware — CPU, Power Supply, I/O Modules",
        "Siemens S7-200 Series পরিচিতি",
        "Hands-on: S7-200 Hardware চেনা",
    ], D)

    make_content_slide(prs, "What is a PLC?", [
        "PLC = Programmable Logic Controller",
        "একটি শিল্প-গ্রেড কম্পিউটার যা মেশিন ও প্রক্রিয়া নিয়ন্ত্রণ করে",
        "Input → Process (CPU) → Output — এই তিন ধাপে কাজ করে",
        "## PLC কেন দরকার?",
        "  - Relay Circuit এর চেয়ে অনেক বেশি নির্ভরযোগ্য",
        "  - Program পরিবর্তন করলেই কাজ বদলানো যায়",
        "  - Maintenance সহজ ও দ্রুত",
        "  - একাধিক I/O একসাথে নিয়ন্ত্রণ সম্ভব",
        "## প্রথম PLC কে তৈরি করেন?",
        "  - 1968 সালে Dick Morley (Modicon 084)",
        "  - Siemens 1973 সালে প্রথম PLC বাজারে আনে",
    ], D, note="PLC মূলত Industrial Automation এর মেরুদণ্ড।")

    make_two_col_slide(prs,
        "PLC vs Relay Logic — পার্থক্য",
        "Relay Logic",
        ["Hardware Wiring দিয়ে তৈরি", "পরিবর্তন করতে Rewiring দরকার",
         "Physical contact — দ্রুত ক্ষয় হয়", "Complex circuit = বড় Panel",
         "Troubleshoot করা কঠিন", "Speed তুলনামূলক ধীর",
         "Cost বেশি (বড় সিস্টেমে)"],
        "PLC",
        ["Software Program দিয়ে তৈরি", "Program edit করলেই হয়",
         "No physical contact — দীর্ঘস্থায়ী", "হাজার I/O একটি ছোট বক্সে",
         "Status Monitor করা যায় Real-time", "Scan time: মাইক্রোসেকেন্ড",
         "Cost কম (বড় সিস্টেমে)"],
        D, C_TEAL)

    make_content_slide(prs, "Industry Applications — PLC কোথায় ব্যবহার হয়", [
        "## Manufacturing Industry",
        "  - Conveyor Belt Control, Robotic Assembly",
        "  - CNC Machine, Injection Molding",
        "## Process Industry",
        "  - Oil & Gas Pipeline Control",
        "  - Water Treatment Plant, Chemical Plant",
        "## Power & Energy",
        "  - Power Plant Control, Solar Farm",
        "  - Generator Synchronization",
        "## Building Automation",
        "  - HVAC Control, Elevator, Fire Alarm",
        "  - Parking System, Access Control",
    ], D, note="বাংলাদেশে Garments, Cement, Power Plant এ ব্যাপক ব্যবহার হচ্ছে।")

    make_content_slide(prs, "Siemens S7-200 Series — পরিচিতি", [
        "Siemens SIMATIC S7-200 — Micro PLC পরিবার",
        "## Available CPU Models:",
        "  - CPU 221 — 6 DI / 4 DO (সবচেয়ে ছোট)",
        "  - CPU 222 — 8 DI / 6 DO",
        "  - CPU 224 — 14 DI / 10 DO (সবচেয়ে জনপ্রিয়)",
        "  - CPU 224XP — 14 DI / 10 DO + 2 AI / 1 AO (আমাদের টার্গেট)",
        "  - CPU 226 — 24 DI / 16 DO (সবচেয়ে বড়)",
        "## CPU 224XP বিশেষত্ব:",
        "  - Built-in 2 Analog Input, 1 Analog Output",
        "  - 2টি RS-485 Communication Port",
        "  - 26KB Program Memory, 10KB Data Memory",
        "  - Real-Time Clock (RTC) সুবিধা",
    ], D)

    make_content_slide(prs, "S7-200 Hardware — মূল অংশসমূহ", [
        "## CPU Unit:",
        "  - Microprocessor, Program Memory, Data Memory",
        "  - Built-in I/O, Communication Port, RTC",
        "## Power Supply:",
        "  - AC Input: 85-264 VAC  |  DC Input: 24 VDC",
        "  - Sensor Power: 24 VDC / 280 mA সরবরাহ করে",
        "## Digital Input (DI):",
        "  - 24 VDC Sinking বা Sourcing",
        "  - I0.0 থেকে I1.5 পর্যন্ত (CPU 224XP)",
        "## Digital Output (DO):",
        "  - Relay Output বা Transistor Output",
        "  - Q0.0 থেকে Q1.1 পর্যন্ত",
        "## Expansion Module:",
        "  - EM231 (AI), EM232 (AO), EM235 (AI+AO)",
    ], D, note="CPU 224XP REL 02.01 — আমাদের কোর্সে এই মডেল ব্যবহার করা হবে।")

    make_summary_slide(prs,
        "Module 01 — Day 1: PLC Basics",
        ["PLC = Industrial Computer for Automation",
         "PLC, Relay Logic এর চেয়ে অনেক উন্নত",
         "S7-200 CPU 224XP — আমাদের কোর্সের Hardware",
         "14 DI, 10 DO, 2 AI, 1 AO — Built-in",
         "Program Memory: 26KB, Data Memory: 10KB"],
        "Day 2:\n• I/O Wiring (Sourcing & Sinking)\n• PLC Scan Cycle\n• S7-200 Memory Organization",
        D)

    # ════════════════════════════════════════════════════════
    #  DAY 2  — I/O Wiring, Scan Cycle, Memory
    # ════════════════════════════════════════════════════════
    D = "Module 01  |  Day 2"

    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 01 — I/O Wiring, Scan Cycle & Memory",
        "Day 2  |  Beginner Level  |  Duration: 2 Hours",
        C_NAVY)

    make_agenda_slide(prs, "Day 2 — Agenda", [
        "Digital Input Wiring — Sourcing vs Sinking",
        "Digital Output Wiring — Relay vs Transistor",
        "PLC Scan Cycle — Input → Process → Output",
        "S7-200 Memory Organization (I, Q, M, V, T, C)",
        "Analog I/O পরিচিতি (AI, AQ)",
        "Hands-on: Wiring Diagram তৈরি করা",
    ], D)

    make_two_col_slide(prs,
        "Input Wiring — Sourcing vs Sinking",
        "Sinking Input (NPN)",
        ["Current flows INTO the input terminal",
         "Sensor Common → +24V",
         "Signal wire → Input terminal",
         "NPN Proximity Sensor এর সাথে ব্যবহার হয়",
         "বাংলাদেশে সবচেয়ে বেশি প্রচলিত",
         "Input terminal LOW হলে Active"],
        "Sourcing Input (PNP)",
        ["Current flows OUT of the input terminal",
         "Sensor Common → 0V (GND)",
         "Signal wire → Input terminal",
         "PNP Proximity Sensor এর সাথে ব্যবহার হয়",
         "European system এ প্রচলিত",
         "Input terminal HIGH হলে Active"],
        D, C_ORANGE)

    make_content_slide(prs, "PLC Scan Cycle — কীভাবে কাজ করে", [
        "PLC প্রতিটি Cycle এ ৪টি কাজ করে:",
        "## Step 1 — Read Inputs:",
        "  - সমস্ত Input এর অবস্থা I-Memory তে লেখা হয়",
        "  - এটাকে Input Image Register বলে",
        "## Step 2 — Execute Program:",
        "  - Program এর প্রতিটি Network ক্রমানুসারে Execute হয়",
        "  - I-Memory পড়ে, Q-Memory তে লেখে",
        "## Step 3 — Process Communications:",
        "  - HMI, SCADA, অন্য PLC এর সাথে Data আদানপ্রদান",
        "## Step 4 — Write Outputs:",
        "  - Q-Memory থেকে Physical Output এ Signal পাঠানো হয়",
        "Scan Time: সাধারণত 1ms ~ 10ms (Program size এর উপর নির্ভরশীল)",
    ], D, note="Scan Cycle বোঝা ছাড়া Timer ও Counter সঠিকভাবে বোঝা যায় না!")

    make_table_slide(prs,
        "S7-200 Memory Organization",
        ["Memory Area", "Identifier", "Data Type", "ব্যবহার"],
        [
            ["Digital Input",   "I",  "BOOL/BYTE/WORD", "Physical Input এর অবস্থা"],
            ["Digital Output",  "Q",  "BOOL/BYTE/WORD", "Physical Output নিয়ন্ত্রণ"],
            ["Bit Memory",      "M",  "BOOL/BYTE/WORD", "Internal Flag / Marker"],
            ["Variable Memory", "V",  "BYTE to DWORD",  "Data Storage (10KB)"],
            ["Timer",           "T",  "WORD",           "Timer Value & Status"],
            ["Counter",         "C",  "WORD",           "Counter Value & Status"],
            ["Analog Input",    "AI", "WORD (0-32000)", "Analog Sensor Reading"],
            ["Analog Output",   "AQ", "WORD (0-32000)", "Analog Signal Output"],
            ["Special Memory",  "SM", "BOOL/BYTE",      "System Status & Control"],
            ["High Speed Counter","HC","DWORD",         "High Speed Pulse Count"],
        ],
        D, C_TEAL)

    make_summary_slide(prs,
        "Module 01 — Day 2: Wiring & Memory",
        ["Sinking (NPN) বেশি ব্যবহৃত বাংলাদেশে",
         "Scan Cycle: Read Input → Execute → Write Output",
         "Scan Time সাধারণত 1-10ms",
         "I=Input, Q=Output, M=Marker, V=Variable",
         "T=Timer, C=Counter, AI/AQ=Analog"],
        "Day 3 (Module 02):\n• STEP 7-Micro/WIN Installation\n• Software Interface\n• First Program তৈরি করা",
        D)

    # ════════════════════════════════════════════════════════
    #  DAY 3  — STEP 7 Software Overview
    # ════════════════════════════════════════════════════════
    D = "Module 02  |  Day 3"

    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 02 — STEP 7-Micro/WIN Software Overview",
        "Day 3  |  Beginner Level  |  Duration: 2 Hours",
        RGBColor(0x00, 0x40, 0x80))

    make_agenda_slide(prs, "Day 3 — Agenda", [
        "STEP 7-Micro/WIN Installation & Setup",
        "Software Interface পরিচয় (Project Tree, Editor)",
        "Program Block, Symbol Table, Data Block পরিচয়",
        "Communications Setup — PC থেকে PLC সংযোগ",
        "প্রথম Program লেখা ও Download করা",
        "Program Run, Stop ও Monitor করা",
    ], D)

    make_content_slide(prs, "STEP 7-Micro/WIN — Software Interface", [
        "## Main Window Components:",
        "  - Menu Bar: File, Edit, View, PLC, Debug, Tools",
        "  - Toolbar: Compile, Download, Upload, Run, Stop",
        "  - Project Tree (বামে): Program Blocks, Symbol Table ইত্যাদি",
        "  - LAD Editor (মাঝে): Ladder Diagram লেখার জায়গা",
        "  - Instruction Tree (ডানে): সব Instructions এর তালিকা",
        "## Project Tree এর অংশ:",
        "  - Program Block — MAIN, SBR, INT",
        "  - Symbol Table — Variable এর নাম দেওয়া",
        "  - Status Chart — Real-time monitoring",
        "  - Data Block — Initial values",
        "  - System Block — CPU Configuration",
        "  - Cross Reference — কোন Variable কোথায় আছে",
    ], D, note="View মেনু থেকে LAD, FBD বা STL editor select করা যায়।")

    make_content_slide(prs, "PC থেকে PLC সংযোগ — Setup", [
        "## Hardware দরকার:",
        "  - PC/PPI Cable (RS-232 to RS-485) অথবা",
        "  - USB/PPI Adapter (আধুনিক PC তে)",
        "## Software Setup:",
        "  - Tools → Set PG/PC Interface এ যান",
        "  - PC/PPI cable (PPI) সিলেক্ট করুন",
        "  - Properties: Baud Rate = 9600, Station = 0",
        "## PLC Address:",
        "  - Default PLC address = 2",
        "  - System Block এ পরিবর্তন করা যায়",
        "## Connection Test:",
        "  - Communications → Double Click on PLC icon",
        "  - PLC found হলে Green check দেখাবে",
        "  - CPU Type ও Version দেখাবে",
    ], D, note="USB/PPI Adapter ব্যবহারে Windows 10/11 এ driver manually install করতে হতে পারে।")

    make_practical_slide(prs,
        "Practical: প্রথম PLC Program — Single Output ON",
        "Push Button চাপলে একটি Light জ্বলবে",
        [
            "STEP 7-Micro/WIN খুলুন → New Project তৈরি করুন",
            "MAIN Block এ ক্লিক করুন",
            "Network 1 এ Normally Open Contact রাখুন (I0.0)",
            "Output Coil যোগ করুন (Q0.0)",
            "F7 চাপুন বা Menu থেকে Compile করুন",
            "PLC এর সাথে Cable সংযোগ করুন",
            "Download করুন (PLC → RUN Mode এ দিন)",
            "I0.0 তে 24V দিন — Q0.0 ON হওয়া দেখুন",
        ], D)

    make_summary_slide(prs,
        "Module 02 — Day 3: Software Overview",
        ["STEP 7-Micro/WIN V4.0 SP9 ব্যবহার করব",
         "LAD Editor এ Ladder Diagram লেখা হয়",
         "PC/PPI বা USB/PPI Cable দিয়ে সংযোগ",
         "Compile → Download → RUN — তিনটি ধাপ",
         "প্রথম Program সফলভাবে Run করা হয়েছে!"],
        "Day 4 (Module 03):\n• Bit Logic Instructions শুরু\n• Contacts ও Coils বিস্তারিত\n• Series ও Parallel Circuit",
        D)

    save(prs, "Module_01_02_PLC_Basics_and_Software_Day1-3.pptx")

if __name__ == "__main__":
    build()
