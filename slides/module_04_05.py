"""Module 04 & 05 — Day 7-10 — Timers & Counters"""
from generate_slides import *

def build():
    prs = new_prs()

    # ════════ DAY 7 — Timer Basics ════════
    D = "Module 04  |  Day 7"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 04 — Timer Instructions",
        "Day 7  |  Intermediate Level  |  Duration: 2 Hours",
        RGBColor(0x5C, 0x2A, 0x00))

    make_agenda_slide(prs, "Day 7 — Agenda", [
        "Timer কী এবং কীভাবে কাজ করে?",
        "Timer Memory Area (T0 ~ T255)",
        "Timer Resolution — 1ms, 10ms, 100ms",
        "TON — Timer On-Delay (সবচেয়ে গুরুত্বপূর্ণ)",
        "Timer Preset Value (PT) ও Accumulated Value (AT)",
        "Timer Reset করার পদ্ধতি",
        "Hands-on: 5 Second Delay Circuit",
    ], D)

    make_table_slide(prs,
        "Timer Memory Area — T0 থেকে T255",
        ["Timer Range", "Type", "Resolution", "Max Time"],
        [
            ["T0 ~ T4",      "TONR", "1 ms",    "32.767 sec"],
            ["T5 ~ T31",     "TON / TOF", "1 ms","32.767 sec"],
            ["T32 ~ T36",    "TONR", "10 ms",   "327.67 sec"],
            ["T37 ~ T63",    "TON / TOF", "10 ms","327.67 sec"],
            ["T64 ~ T65",    "TONR", "100 ms",  "3276.7 sec"],
            ["T66 ~ T85",    "TON / TOF", "100 ms","3276.7 sec"],
            ["T96 ~ T100",   "TONR", "1 ms",    "32.767 sec"],
            ["T101 ~ T255",  "TON / TOF", "100 ms","3276.7 sec"],
        ], D, C_ORANGE)

    make_content_slide(prs, "TON — Timer On-Delay", [
        "## কীভাবে কাজ করে:",
        "  - Enable (IN) = 1 হলে Timer গণনা শুরু করে",
        "  - Accumulated Value (AT) বাড়তে থাকে",
        "  - AT >= Preset Time (PT) হলে Timer Bit = 1",
        "  - Enable = 0 হলে AT রিসেট হয়ে যায়",
        "## Parameters:",
        "  - IN: Enable Input (BOOL)",
        "  - PT: Preset Time — কত Resolution Unit এ গণবে",
        "  - PT = 50, Resolution = 100ms → Delay = 5 Seconds",
        "## Example Program:",
        "  - Network 1: I0.0 → TON T37, +50",
        "  - Network 2: T37 (N.O.) → Q0.0",
        "  - I0.0 ON করলে 5 সেকেন্ড পরে Q0.0 ON হবে",
        "## Timer Number টি দেখেই Resolution বোঝা যায়!",
    ], D, note="PT value সবসময় +ve Integer দিতে হবে। Maximum PT = +32767")

    make_content_slide(prs, "TONR — Retentive Timer & TOF — Off-Delay", [
        "## TONR (Retentive On-Delay):",
        "  - Enable = 0 হলেও AT রিসেট হয় না!",
        "  - পরের বার Enable হলে আগের থেকে গণনা শুরু",
        "  - Reset করতে হলে আলাদা Reset Input লাগে",
        "  - ব্যবহার: Machine Running Time Counter",
        "## TOF (Off-Delay Timer):",
        "  - Enable = 1 হলে Output সাথে সাথে ON হয়",
        "  - Enable = 0 হলে Timer গণনা শুরু করে",
        "  - AT >= PT হলে Output OFF হয়",
        "  - ব্যবহার: Cooling Fan — Motor বন্ধের পর কিছুক্ষণ চলে",
        "## BGN_ITIME ও CAL_ITIME:",
        "  - Millisecond precision এর জন্য Interval Timer",
        "  - BGN_ITIME: Start time ধরে রাখে",
        "  - CAL_ITIME: Elapsed time হিসাব করে",
    ], D, note="TONR সেই Timer যেটা Power Cut এর পরেও মান মনে রাখে!")

    make_practical_slide(prs,
        "Practical: Automatic Light ON/OFF with Delay",
        "Motion Sensor দেখলে Light জ্বলবে, 10 সেকেন্ড পরে নিভবে",
        [
            "I0.0 = Motion Sensor, Q0.0 = Light",
            "Network 1: I0.0 (N.O.) → S Q0.0, 1  (Light চালু)",
            "Network 2: I0.0 (N.O.) → TON T37, +100  (10s Timer)",
            "Network 3: T37 (N.O.) → R Q0.0, 1  (Light বন্ধ)",
            "Download ও Test করুন",
            "Timer এর AT Value Status Chart এ Monitor করুন",
        ], D)

    make_summary_slide(prs,
        "Module 04 — Day 7: Timer Basics",
        ["TON: Enable ON → delay পরে Output ON",
         "TONR: Accumulated — Reset না হলে মান থাকে",
         "TOF: Enable OFF → delay পরে Output OFF",
         "T37 = 10ms resolution (সবচেয়ে ব্যবহৃত)",
         "PT=50, T37 → 50×10ms = 500ms = 0.5 sec"],
        "Day 8 (Module 05):\n• Counter Instructions শুরু\n• CTU Count Up Counter\n• CTD ও CTUD",
        D)

    # ════════ DAY 8 — Counter Basics ════════
    D = "Module 05  |  Day 8"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 05 — Counter Instructions",
        "Day 8  |  Intermediate Level  |  Duration: 2 Hours",
        RGBColor(0x2A, 0x00, 0x5C))

    make_agenda_slide(prs, "Day 8 — Agenda", [
        "Counter কী এবং কখন দরকার?",
        "Counter Memory Area (C0 ~ C255)",
        "CTU — Count Up Counter",
        "CTD — Count Down Counter",
        "CTUD — Count Up/Down Counter",
        "Counter Reset করার পদ্ধতি",
        "Hands-on: Bottle Counter",
    ], D)

    make_content_slide(prs, "CTU — Count Up Counter", [
        "## কীভাবে কাজ করে:",
        "  - CU (Count Up) Input এর প্রতিটি Rising Edge এ CV বাড়ে",
        "  - CV (Current Value) >= PV (Preset Value) হলে Counter Bit = 1",
        "  - R (Reset) = 1 হলে CV = 0 এবং Counter Bit = 0",
        "## Parameters:",
        "  - CU: Count Up Pulse Input",
        "  - R: Reset Input",
        "  - PV: Preset Value (কত গণলে Output হবে)",
        "## Example:",
        "  - CTU C0, +10 — ১০টি গুনলে C0 Bit = 1",
        "  - Network 1: I0.0 (N.O.) — CU, I0.1 — R, PV=+10",
        "  - Network 2: C0 (N.O.) → Q0.0",
        "## Maximum Count:",
        "  - PV সর্বোচ্চ +32767 (16-bit signed integer)",
    ], D, note="Counter Bit এবং Counter Value আলাদা — C0 মানে Bit, C0 (WORD) মানে Value!")

    make_two_col_slide(prs,
        "CTD ও CTUD Counter",
        "CTD — Count Down",
        ["CD (Count Down) Input এ pulse দিলে CV কমে",
         "LD (Load) = 1 হলে CV = PV দিয়ে শুরু",
         "CV = 0 হলে Counter Bit = 1",
         "Example: PV=10, 10টি pulse → CV=0 → ON",
         "ব্যবহার: Remaining Quantity দেখানো",
         "Batch production এ কতটি বাকি"],
        "CTUD — Count Up/Down",
        ["CU = Count Up Input",
         "CD = Count Down Input",
         "R = Reset",
         "PV = Preset Value",
         "CV >= PV → Counter Bit = 1",
         "CV <= -32768 → Underflow (সতর্কতা!)"],
        D, C_TEAL)

    make_table_slide(prs,
        "Counter Instructions — Summary Table",
        ["Instruction", "কাজ", "Input", "Reset", "Output Condition"],
        [
            ["CTU", "Count Up",      "CU (Rising Edge)", "R=1 → CV=0",      "CV >= PV → Bit=1"],
            ["CTD", "Count Down",    "CD (Rising Edge)", "LD=1 → CV=PV",    "CV <= 0 → Bit=1"],
            ["CTUD","Count Up/Down", "CU ও CD",          "R=1 → CV=0",      "CV >= PV → Bit=1"],
            ["HSC", "High Speed",    "Hardware Input",   "SM37/SM47",       "HDEF দিয়ে Configure"],
        ], D, C_TEAL)

    make_practical_slide(prs,
        "Practical: Conveyor Belt Bottle Counter",
        "১০০টি Bottle গণনার পর Conveyor বন্ধ করা",
        [
            "I0.0 = Proximity Sensor (Bottle detect করলে Pulse)",
            "I0.1 = Reset Button, Q0.0 = Conveyor Motor",
            "Network 1: I0.0 → CU, I0.1 → R, PV=+100 (CTU C0)",
            "Network 2: C0 N.C. (Counter না পৌঁছালে) → Q0.0 (Motor ON)",
            "Network 3: C0 N.O. → Q0.1 (Alarm ON, 100 হয়েছে)",
            "Status Chart এ C0 Current Value monitor করুন",
            "Test: ১০০ বার I0.0 pulse দিন",
        ], D)

    make_summary_slide(prs,
        "Module 05 — Day 8: Counter Basics",
        ["CTU: Rising Edge এ গণে, CV>=PV → Bit=1",
         "CTD: গণে কমে, CV<=0 → Bit=1",
         "CTUD: দুদিকেই গণে",
         "Counter Address: C0 ~ C255",
         "Reset না করলে CV মান থেকে যায়"],
        "Day 9:\n• High Speed Counter (HSC)\n• HDEF Configuration\n• PLS Pulse Output",
        D)

    # ════════ DAY 9 — HSC & PLS ════════
    D = "Module 05  |  Day 9"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 05 — High Speed Counter & Pulse Output",
        "Day 9  |  Intermediate Level  |  Duration: 2 Hours",
        RGBColor(0x2A, 0x00, 0x5C))

    make_agenda_slide(prs, "Day 9 — Agenda", [
        "High Speed Counter (HSC) — কেন দরকার?",
        "HDEF — High Speed Counter Definition",
        "HSC Instruction — Execute করা",
        "HSC Modes (0 ~ 11) পরিচয়",
        "PLS — Pulse Output (Stepper Motor Control)",
        "Encoder এর সাথে HSC ব্যবহার",
        "Hands-on: Encoder Position Reading",
    ], D)

    make_content_slide(prs, "High Speed Counter — কেন দরকার?", [
        "## সাধারণ Counter এর সমস্যা:",
        "  - Scan Cycle প্রতি একটি Pulse গোনে",
        "  - S7-200 Scan Time ≈ 1-5ms",
        "  - Maximum Count Rate ≈ 200-1000 Hz",
        "## HSC এর সুবিধা:",
        "  - Hardware Counter — CPU Independent",
        "  - Count Rate: 30 kHz পর্যন্ত (CPU 224XP)",
        "  - Encoder, High-speed Sensor এর সাথে ব্যবহার",
        "## S7-200 HSC Channels:",
        "  - HSC0: I0.0, I0.1, I0.2",
        "  - HSC1: I0.6, I0.7, I1.0",
        "  - HSC2: I1.1, I1.2",
        "  - HSC3: I0.1",
        "  - HSC4: I0.3, I0.4, I0.5",
        "  - HSC5: I0.4",
    ], D, note="Encoder সাধারণত 500~5000 PPR — HSC ছাড়া গণনা সম্ভব নয়!")

    make_content_slide(prs, "PLS — Pulse Output Instruction", [
        "## কী কাজে লাগে:",
        "  - Stepper Motor ও Servo Drive কে Pulse দেওয়া",
        "  - PWM (Pulse Width Modulation) Signal তৈরি",
        "## PLS Output Pins (CPU 224XP):",
        "  - Q0.0 — PTO/PWM Channel 0",
        "  - Q0.1 — PTO/PWM Channel 1",
        "## PTO Mode (Pulse Train Output):",
        "  - নির্দিষ্ট সংখ্যক Pulse তৈরি করে",
        "  - Frequency ও Pulse Count নির্ধারণ করা যায়",
        "## PWM Mode:",
        "  - Duty Cycle পরিবর্তন করা যায়",
        "  - Speed Control, Dimmer এ ব্যবহার",
        "## Special Memory:",
        "  - SMB67 ~ SMB85 দিয়ে PLS Configure করতে হয়",
    ], D, note="PLS শুধুমাত্র Transistor Output CPU তে কাজ করে — Relay Output এ কাজ করে না!")

    make_summary_slide(prs,
        "Module 05 — Day 9: HSC & PLS",
        ["HSC: 30kHz পর্যন্ত pulse গুনতে পারে",
         "HDEF দিয়ে HSC configure করতে হয়",
         "HSC0~HSC5 পর্যন্ত 6টি channel",
         "PLS: Stepper/Servo Motor control",
         "Q0.0, Q0.1 Transistor Output — PLS এর জন্য"],
        "Day 10:\n• Timer + Counter Combined Projects\n• Module 04 & 05 Review Quiz\n• Practical Exam",
        D)

    # ════════ DAY 10 — Timer+Counter Combined ════════
    D = "Module 04-05  |  Day 10"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 04-05 — Timer & Counter: Combined Practical",
        "Day 10  |  Lab + Review Day  |  Duration: 2 Hours",
        RGBColor(0x4A, 0x1A, 0x3A))

    make_agenda_slide(prs, "Day 10 — Agenda", [
        "Timer ও Counter একসাথে ব্যবহার — Extended Timer",
        "Project: Flashing Light (Blink) Circuit",
        "Project: Production Shift Counter with Timer",
        "Module 04 & 05 — সমস্ত Instructions Review",
        "Common Mistakes ও Troubleshooting",
        "Quiz Session",
    ], D)

    make_content_slide(prs, "Extended Timer — Timer + Counter দিয়ে দীর্ঘ সময় গণনা", [
        "## সমস্যা: TON সর্বোচ্চ 3276.7 sec (≈ 54 min)",
        "  - এর বেশি সময় দরকার হলে কী করব?",
        "## সমাধান: Timer + Counter Cascade",
        "  - Network 1: T37 দিয়ে 1 minute Timer তৈরি করুন",
        "  - T37 PT = +600 (600 × 100ms = 60 sec)",
        "  - Network 2: T37 Bit দিয়ে CTU C0 গণে",
        "  - C0 PV = +60 → 60 minutes = 1 Hour",
        "  - Network 3: T37 Bit দিয়ে T37 নিজেই Reset করে",
        "  - এভাবে ঘণ্টা, দিন পর্যন্ত গণনা সম্ভব!",
        "## Application:",
        "  - Maintenance Reminder (প্রতি 500 ঘণ্টায়)",
        "  - Shift Change Alarm",
    ], D, note="Timer + Counter Cascade — PLC Programming এর একটি classic technique!")

    make_practical_slide(prs,
        "Project: Flashing Light (Blink) Circuit",
        "একটি Light ০.৫ সেকেন্ড ON, ০.৫ সেকেন্ড OFF করে Flash করবে",
        [
            "Network 1: M0.0 (N.C.) → TON T37, +5 (500ms ON timer)",
            "Network 2: T37 (N.O.) → TON T38, +5 (500ms OFF timer)",
            "Network 3: T38 (N.O.) → R M0.0, 1 এবং T37 Reset",
            "বা সহজ পদ্ধতি: SM0.5 Special Memory Bit ব্যবহার করুন",
            "SM0.5 = Built-in 1 second clock (0.5s ON / 0.5s OFF)",
            "Network 1: SM0.5 → Q0.0 (সরাসরি Blink!)",
            "SM0.4 = 1 minute clock, SM0.3 = 0.1 sec clock",
        ], D)

    make_table_slide(prs,
        "Special Memory Clock Bits — SM0.x",
        ["SM Bit", "Period", "ON Time", "OFF Time", "ব্যবহার"],
        [
            ["SM0.4", "1 minute", "30 sec", "30 sec", "Slow Blink, Shift Timer"],
            ["SM0.5", "1 second", "0.5 sec","0.5 sec","Standard Blink Signal"],
            ["SM0.3", "0.1 sec",  "50 ms",  "50 ms",  "Fast Pulse"],
        ], D, C_ORANGE)

    make_summary_slide(prs,
        "Module 04 & 05 — Timer & Counter: Complete",
        ["TON, TONR, TOF — তিনটি Timer Type শেখা হয়েছে",
         "CTU, CTD, CTUD — তিনটি Counter Type শেখা হয়েছে",
         "HSC — High Speed Counter 30kHz পর্যন্ত",
         "PLS — Pulse Output for Stepper Motor",
         "Timer + Counter Cascade দিয়ে ঘণ্টা গণনা সম্ভব"],
        "Day 11 (Module 06):\n• Compare Instructions শুরু\n• Byte, Integer, Real Compare\n• Temperature Alarm System",
        D)

    save(prs, "Module_04_05_Timers_Counters_Day7-10.pptx")

if __name__ == "__main__":
    build()
