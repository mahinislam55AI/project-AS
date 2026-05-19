"""Module 08 & 09 — Day 14-17 — Integer Math & Floating Point Math"""
from generate_slides import *

def build():
    prs = new_prs()

    # ════════ DAY 14 — Integer Math ════════
    D = "Module 08  |  Day 14"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 08 — Integer Math Instructions",
        "Day 14  |  Upper-Intermediate  |  Duration: 2 Hours",
        RGBColor(0x5C, 0x00, 0x2A))

    make_agenda_slide(prs, "Day 14 — Agenda", [
        "Integer Math কেন দরকার? (Real-world applications)",
        "ADD_I / ADD_DI — Addition",
        "SUB_I / SUB_DI — Subtraction",
        "MUL / MUL_I / MUL_DI — Multiplication",
        "DIV / DIV_I / DIV_DI — Division",
        "INC / DEC — Increment ও Decrement",
        "Overflow ও Error Flags (SM1.x)",
    ], D)

    make_content_slide(prs, "Integer Math — Overview", [
        "## কেন দরকার?",
        "  - Analog Signal Scaling (Raw Value → Engineering Unit)",
        "  - Production Count Calculation",
        "  - Speed ও Frequency Calculation",
        "  - Position Calculation with Encoder",
        "## Integer Types in S7-200:",
        "  - INT (I): 16-bit Signed = -32768 ~ +32767",
        "  - DINT (DI): 32-bit Signed = ±2,147,483,647",
        "  - BYTE (B): 8-bit Unsigned = 0 ~ 255",
        "## Important Flags:",
        "  - SM1.0 = Result is Zero",
        "  - SM1.1 = Overflow বা Divide by Zero Error",
        "  - SM1.2 = Negative Result",
        "  - SM1.3 = Divide by Zero",
    ], D, note="Math Instruction এ Overflow হলে SM1.1 = 1 হয়। সবসময় check করুন!")

    make_table_slide(prs,
        "Integer Math Instructions — Complete List",
        ["Instruction", "Operation", "Input Size", "Output Size", "Note"],
        [
            ["ADD_I",  "IN1 + IN2 → OUT", "INT + INT",   "INT",  "16-bit + 16-bit"],
            ["ADD_DI", "IN1 + IN2 → OUT", "DINT + DINT", "DINT", "32-bit + 32-bit"],
            ["SUB_I",  "IN1 - IN2 → OUT", "INT - INT",   "INT",  "16-bit result"],
            ["SUB_DI", "IN1 - IN2 → OUT", "DINT - DINT", "DINT", "32-bit result"],
            ["MUL",    "IN1 × IN2 → OUT", "INT × INT",   "DINT", "16×16 = 32-bit!"],
            ["MUL_I",  "IN1 × IN2 → OUT", "INT × INT",   "INT",  "Result truncated"],
            ["MUL_DI", "IN1 × IN2 → OUT", "DINT × DINT", "DINT", "32-bit result"],
            ["DIV",    "IN1 ÷ IN2 → OUT", "DINT ÷ INT",  "DINT", "Quotient+Remainder"],
            ["DIV_I",  "IN1 ÷ IN2 → OUT", "INT ÷ INT",   "INT",  "Integer only"],
            ["DIV_DI", "IN1 ÷ IN2 → OUT", "DINT ÷ DINT", "DINT", "32-bit divide"],
            ["INC_B",  "IN + 1 → OUT",    "BYTE",        "BYTE", "Increment by 1"],
            ["INC_W",  "IN + 1 → OUT",    "WORD",        "WORD", "Increment word"],
            ["DEC_B",  "IN - 1 → OUT",    "BYTE",        "BYTE", "Decrement by 1"],
        ], D, C_RED)

    make_content_slide(prs, "Analog Scaling — Integer Math এর সেরা ব্যবহার", [
        "## Problem: AI0 Raw Value → Temperature (°C)",
        "  - AI0 Range: 0 ~ 32000 = 0°C ~ 100°C",
        "  - Formula: Temp = (AIW0 × 100) ÷ 32000",
        "## Program Steps:",
        "  - Step 1: MOV_W AIW0, VW10  (Raw value copy)",
        "  - Step 2: MUL VW10, +100 → VD20  (×100, 32-bit result)",
        "  - Step 3: DIV_DI VD20, +32000 → VD30  (÷32000)",
        "  - VD30 = Temperature in °C",
        "## INC / DEC Use Case:",
        "  - INC_W VW100 — প্রতি Scan এ VW100 একটু বাড়ে",
        "  - Step Sequence: INC_B MB10 → Step Counter",
        "  - MB10 এর মান দিয়ে ==B Compare → বিভিন্ন Step চালু",
    ], D, note="MUL দিয়ে 16×16=32 bit result পাওয়া যায় — Overflow এড়াতে এটা ব্যবহার করুন!")

    make_practical_slide(prs,
        "Practical: Production Rate Calculator",
        "প্রতি মিনিটে কতটি Product তৈরি হচ্ছে তা Calculate করা",
        [
            "I0.0 = Product Sensor, VW100 = Minute Counter",
            "VW200 = Production Rate (pcs/min)",
            "Network 1: SM0.5 দিয়ে 1 minute timer তৈরি করুন",
            "Network 2: I0.0 Rising Edge → INC_W VW100 (Count)",
            "Network 3: Timer Done → MOV_W VW100, VW200 (Rate save)",
            "Network 4: Timer Done → MOV_W +0, VW100 (Reset count)",
            "Network 5: >I VW200, +100 → Q0.0 (High Rate Alarm)",
        ], D)

    make_summary_slide(prs,
        "Module 08 — Day 14: Integer Math",
        ["ADD, SUB, MUL, DIV — চারটি মূল operation",
         "MUL: 16×16=32 bit (Overflow এড়ায়)",
         "DIV: Quotient + Remainder আলাদা পাওয়া যায়",
         "INC/DEC: এক ধাপে বাড়ানো/কমানো",
         "SM1.1 = Overflow বা Error — সবসময় চেক করুন"],
        "Day 15 (Module 09):\n• Floating-Point Math শুরু\n• ADD_R, MUL_R, SQRT\n• Trigonometry Functions",
        D)

    # ════════ DAY 15 — Floating Point Math ════════
    D = "Module 09  |  Day 15"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 09 — Floating-Point Math Instructions",
        "Day 15  |  Upper-Intermediate  |  Duration: 2 Hours",
        RGBColor(0x00, 0x3D, 0x5C))

    make_agenda_slide(prs, "Day 15 — Agenda", [
        "Floating-Point Number কী? (IEEE 754 Format)",
        "ADD_R, SUB_R, MUL_R, DIV_R",
        "SQRT — Square Root",
        "SIN, COS, TAN — Trigonometric Functions",
        "LN — Natural Log ও EXP — Exponential",
        "Real Number Analog Scaling",
        "Hands-on: Engineering Unit Conversion",
    ], D)

    make_content_slide(prs, "Floating-Point Number — IEEE 754", [
        "## Real Number কী?",
        "  - দশমিক সংখ্যা: 3.14, 98.6, -273.15",
        "  - S7-200 তে REAL = 32-bit IEEE 754 Format",
        "  - Range: ±1.175 × 10⁻³⁸ থেকে ±3.402 × 10³⁸",
        "## Memory:",
        "  - REAL সবসময় 32-bit (4 Byte) নেয়",
        "  - VD0, VD4, VD8 — REAL এর Address (4-byte aligned)",
        "## কখন Real ব্যবহার করবেন:",
        "  - Temperature, Pressure, Flow — যেখানে দশমিক দরকার",
        "  - PID Calculation",
        "  - Precise Engineering Unit Scaling",
        "## Integer to Real Conversion:",
        "  - I_DI দিয়ে প্রথমে DINT করুন",
        "  - তারপর DI_R দিয়ে REAL করুন",
    ], D, note="Real Arithmetic Integer এর চেয়ে CPU তে বেশি সময় নেয় — যেখানে দরকার শুধু সেখানে ব্যবহার করুন।")

    make_table_slide(prs,
        "Floating-Point Math Instructions",
        ["Instruction", "Operation", "Input", "Output", "Example"],
        [
            ["ADD_R", "IN1 + IN2 → OUT", "REAL", "REAL", "23.5 + 1.7 = 25.2"],
            ["SUB_R", "IN1 - IN2 → OUT", "REAL", "REAL", "100.0 - 32.5 = 67.5"],
            ["MUL_R", "IN1 × IN2 → OUT", "REAL", "REAL", "3.14 × 5.0 = 15.7"],
            ["DIV_R", "IN1 ÷ IN2 → OUT", "REAL", "REAL", "100.0 ÷ 3.0 = 33.33"],
            ["SQRT",  "√IN → OUT",        "REAL", "REAL", "√144.0 = 12.0"],
            ["SIN",   "sin(IN) → OUT",    "REAL (rad)", "REAL", "sin(1.5708)=1.0"],
            ["COS",   "cos(IN) → OUT",    "REAL (rad)", "REAL", "cos(0)=1.0"],
            ["TAN",   "tan(IN) → OUT",    "REAL (rad)", "REAL", "tan(0.7854)=1.0"],
            ["LN",    "ln(IN) → OUT",     "REAL", "REAL", "ln(2.718)=1.0"],
            ["EXP",   "e^IN → OUT",       "REAL", "REAL", "e^1 = 2.718"],
        ], D, C_TEAL)

    make_summary_slide(prs,
        "Module 09 — Day 15: Floating-Point Math",
        ["REAL = IEEE 754 32-bit Format",
         "ADD_R, SUB_R, MUL_R, DIV_R — চারটি মূল operation",
         "SQRT, SIN, COS, TAN — Scientific functions",
         "LN, EXP — Logarithm ও Exponential",
         "I_DI → DI_R — Integer থেকে Real Convert"],
        "Day 16:\n• PID Controller Instruction\n• PID Loop Table Setup\n• Temperature PID Project",
        D)

    # ════════ DAY 16 — PID ════════
    D = "Module 09  |  Day 16"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 09 — PID Controller Instruction",
        "Day 16  |  Upper-Intermediate  |  Duration: 2 Hours",
        RGBColor(0x00, 0x3D, 0x5C))

    make_agenda_slide(prs, "Day 16 — Agenda", [
        "PID Control কী? (Proportional-Integral-Derivative)",
        "PID Loop Table — 36 Byte Parameter Block",
        "PID Instruction — S7-200 তে ব্যবহার",
        "P, I, D Gain এর প্রভাব",
        "PID Tuning — Manual Method",
        "Analog I/O Scaling for PID",
        "Practical: Temperature PID Control",
    ], D)

    make_content_slide(prs, "PID Controller — মূল ধারণা", [
        "## PID কী?",
        "  - Proportional + Integral + Derivative Controller",
        "  - Setpoint (Target) ও Process Value (Actual) এর পার্থক্য (Error) কমায়",
        "## তিনটি Term:",
        "  - P (Proportional): Error এর সাথে সরাসরি সম্পর্কিত Output",
        "  - I (Integral): Accumulated Error সময়ের সাথে সংশোধন",
        "  - D (Derivative): Error এর Rate of Change এর উপর Output",
        "## Real-world Example:",
        "  - Temperature Controller: Setpoint=80°C, Actual=70°C",
        "  - Error = +10°C → Heater আরও বেশি চালু হবে",
        "  - Temperature 80°C তে পৌঁছালে Heater কমবে",
        "  - Overshoot কমাতে D term সাহায্য করে",
        "## S7-200 PID:",
        "  - 8টি PID Loop সমর্থন করে (Loop 0~7)",
    ], D, note="PID হল Industrial Automation এর সবচেয়ে ব্যাপকভাবে ব্যবহৃত Control Algorithm!")

    make_table_slide(prs,
        "PID Loop Table — 36 Byte Structure",
        ["Byte Offset", "Parameter", "Data Type", "বিবরণ"],
        [
            ["VD0  (0)",  "Process Variable (PV)", "REAL", "Current Sensor Value (0.0~1.0)"],
            ["VD4  (4)",  "Setpoint (SP)",         "REAL", "Target Value (0.0~1.0)"],
            ["VD8  (8)",  "Output (MX)",            "REAL", "Controller Output (0.0~1.0)"],
            ["VD12 (12)", "Proportional Gain (KC)", "REAL", "P Gain (default: 1.0)"],
            ["VD16 (16)", "Sample Time (TS)",       "REAL", "PID Call Interval (seconds)"],
            ["VD20 (20)", "Integral Time (TI)",     "REAL", "I Time Constant (min)"],
            ["VD24 (24)", "Derivative Time (TD)",   "REAL", "D Time Constant (min)"],
            ["VD28 (28)", "Integral Sum (MX)",      "REAL", "Integrator State"],
            ["VD32 (32)", "Previous PV",            "REAL", "Last PV value"],
        ], D, C_ORANGE)

    make_practical_slide(prs,
        "Practical: PID Temperature Control System",
        "Heater এর Power নিয়ন্ত্রণ করে Temperature 80°C তে ধরে রাখা",
        [
            "AIW0 = Temp Sensor (0~32000 = 0°C~100°C)",
            "AQW0 = Heater Power Output (0~32000 = 0~100%)",
            "Step 1: AIW0 কে 0.0~1.0 Range এ Scale করুন (÷32000.0)",
            "Step 2: Setpoint 80°C → 0.8 (VD4 = 0.8)",
            "Step 3: PID Loop Table VD0 এ scale করা PV রাখুন",
            "Step 4: PID 0, VD0 Instruction রাখুন (Timed Interrupt INT0 এ)",
            "Step 5: Output VD8 (0.0~1.0) কে ×32000 করে AQW0 এ দিন",
            "Gain Tuning: KC=2.0, TI=5.0min, TD=0.1min দিয়ে শুরু",
        ], D)

    make_summary_slide(prs,
        "Module 09 — Day 16: PID Controller",
        ["PID = P + I + D Term মিলে Error শূন্য করে",
         "36 Byte Loop Table তে সব parameter থাকে",
         "PV ও SP অবশ্যই 0.0~1.0 Range এ হতে হবে",
         "PID Interrupt এ রাখুন — Regular Scan time দরকার",
         "Tuning: P দিয়ে শুরু, তারপর I, তারপর D"],
        "Day 17:\n• Module 08 & 09 Review\n• Combined Math Project\n• Quiz Session",
        D)

    # ════════ DAY 17 — Math Review ════════
    D = "Module 08-09  |  Day 17"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 08-09 — Math Instructions: Review & Project",
        "Day 17  |  Review + Lab Day  |  Duration: 2 Hours",
        RGBColor(0x3A, 0x1A, 0x4A))

    make_agenda_slide(prs, "Day 17 — Agenda", [
        "Module 08 & 09 সমস্ত Instructions Review",
        "Integer vs Real — কখন কোনটা ব্যবহার করব",
        "Analog Scaling Formula — Complete Guide",
        "Project: Flow Rate Calculator",
        "Common Mistakes ও Best Practices",
        "Quiz Session",
    ], D)

    make_two_col_slide(prs,
        "Integer Math vs Floating-Point Math",
        "Integer Math",
        ["দ্রুত Execute হয়", "দশমিক নেই",
         "Range সীমিত: ±32767 বা ±2B",
         "Counter, Index, Step number এ ব্যবহার",
         "Overflow সম্ভব (SM1.1 চেক করুন)",
         "INC/DEC দিয়ে সহজে Step করা যায়",
         "Memory কম লাগে (2 বা 4 byte)"],
        "Floating-Point Math",
        ["তুলনামূলক ধীর", "দশমিক যেকোনো মান",
         "Range বিশাল: ±3.4×10³⁸",
         "Temperature, Pressure, Flow এ ব্যবহার",
         "PID Calculation এ অপরিহার্য",
         "Scientific functions (SIN, SQRT, LN)",
         "সবসময় 4 byte লাগে"],
        D, C_ORANGE)

    make_table_slide(prs,
        "Analog Scaling Formulas — Quick Reference",
        ["Scenario", "Formula", "S7-200 Instructions"],
        [
            ["0-10V → 0-100°C",   "Temp = AIW × 100 / 32000",  "MUL, DIV_I"],
            ["4-20mA → 0-100%",   "% = (AIW - 6400) × 100 / 25600", "SUB_I, MUL, DIV"],
            ["0-100% → 0-10V Out","AQW = % × 32000 / 100",     "MUL, DIV_I"],
            ["RPM Calculation",   "RPM = (Pulse/sec) × 60",    "MUL_I (with Timer)"],
            ["Flow (L/min)",      "Flow = K × √(ΔP)",          "SQRT (Real Math)"],
        ], D, C_TEAL)

    make_summary_slide(prs,
        "Module 08 & 09 — Math Instructions: Complete",
        ["Integer Math: ADD, SUB, MUL, DIV, INC, DEC",
         "Float Math: ADD_R, SUB_R, MUL_R, DIV_R",
         "Scientific: SQRT, SIN, COS, TAN, LN, EXP",
         "PID: 36-byte Loop Table, 8 Loops সম্ভব",
         "Analog Scaling এ Math Instruction অপরিহার্য"],
        "Day 18 (Module 10):\n• Convert Instructions শুরু\n• BCD, ASCII, HEX Conversion\n• 7-Segment Display",
        D)

    save(prs, "Module_08_09_Integer_Float_Math_Day14-17.pptx")

if __name__ == "__main__":
    build()
