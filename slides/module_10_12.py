"""Module 10, 11, 12 — Day 18-21 — Convert, Logical Ops, Shift/Rotate"""
from generate_slides import *

def build():
    prs = new_prs()

    # ════════ DAY 18 — Convert Part 1 ════════
    D = "Module 10  |  Day 18"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 10 — Convert Instructions (Part 1)",
        "Day 18  |  Upper-Intermediate  |  Duration: 2 Hours",
        RGBColor(0x3D, 0x00, 0x5C))

    make_agenda_slide(prs, "Day 18 — Agenda", [
        "Convert Instruction কেন দরকার?",
        "B_I, I_B — Byte ↔ Integer",
        "I_DI, DI_I — Integer ↔ Double Integer",
        "DI_R, I_S — Integer/DInt → Real",
        "BCD_I, I_BCD — BCD ↔ Integer",
        "ROUND ও TRUNC — Real → Integer",
        "Hands-on: Data Type Conversion Chain",
    ], D)

    make_content_slide(prs, "Convert Instructions — কেন দরকার?", [
        "## Problem: Different Instructions চান Different Data Types",
        "  - ADD_I চায় INT + INT",
        "  - ADD_R চায় REAL + REAL",
        "  - MOV_B চায় BYTE",
        "  - এক ধরনের Data অন্য ধরনে Convert না করলে Error হবে",
        "## Example Scenario:",
        "  - AIW0 = Integer (Raw Analog Value)",
        "  - PID চায় REAL (0.0 ~ 1.0)",
        "  - Steps: AIW0 (INT) → I_DI → DINT → DI_R → REAL → ÷ 32000.0 → PID",
        "## BCD কেন দরকার?",
        "  - Thumb Wheel Switch, 7-Segment Display BCD দেয়/নেয়",
        "  - BCD = Binary Coded Decimal",
        "  - প্রতিটি Decimal Digit আলাদা 4 Bit এ থাকে",
        "  - Example: 59 decimal = 0101 1001 BCD",
    ], D, note="Convert Instructions না জানলে Analog, HMI বা Serial Communication ঠিকমতো করা যাবে না!")

    make_table_slide(prs,
        "Convert Instructions — Part 1",
        ["Instruction", "From", "To", "Note"],
        [
            ["B_I",    "BYTE (0~255)",    "INT",  "Byte → 16-bit Integer"],
            ["I_B",    "INT",             "BYTE", "Low byte only (0~255)"],
            ["I_DI",   "INT (-32768~+32767)","DINT","Sign extend to 32-bit"],
            ["DI_I",   "DINT",            "INT",  "Truncate to 16-bit"],
            ["DI_R",   "DINT",            "REAL", "32-bit Int → Float"],
            ["I_S",    "INT",             "REAL", "Direct Int → Float"],
            ["BCD_I",  "BCD Word",        "INT",  "Thumb wheel → Integer"],
            ["I_BCD",  "INT (0~9999)",    "BCD",  "Integer → 7-Seg Display"],
            ["ROUND",  "REAL",            "DINT", "ঘুরিয়ে Integer (4.7→5)"],
            ["TRUNC",  "REAL",            "DINT", "কেটে Integer (4.7→4)"],
        ], D, C_TEAL)

    make_summary_slide(prs,
        "Module 10 — Day 18: Convert Part 1",
        ["B_I/I_B: Byte ↔ Integer",
         "I_DI/DI_I: Integer ↔ Double Integer",
         "DI_R: Double Int → Real (PID এর আগে)",
         "BCD_I/I_BCD: BCD ↔ Integer (7-Segment)",
         "ROUND vs TRUNC: 4.7→5 vs 4.7→4"],
        "Day 19:\n• Convert Part 2\n• ASCII, HEX Conversion\n• DECO, ENCO, SEG Instructions",
        D)

    # ════════ DAY 19 — Convert Part 2 ════════
    D = "Module 10  |  Day 19"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 10 — Convert Instructions (Part 2)",
        "Day 19  |  Upper-Intermediate  |  Duration: 2 Hours",
        RGBColor(0x3D, 0x00, 0x5C))

    make_agenda_slide(prs, "Day 19 — Agenda", [
        "ITA, DTA, RTA — Number → ASCII String",
        "ATH, HTA — ASCII ↔ Hexadecimal",
        "S_I, S_DI, S_R — String → Number",
        "DECO — Decode (1-of-16)",
        "ENCO — Encode (16-of-1)",
        "SEG — Seven Segment Decode",
        "Practical: 7-Segment Display Controller",
    ], D)

    make_table_slide(prs,
        "Convert Instructions — Part 2 (ASCII & SEG)",
        ["Instruction", "From → To", "Output", "ব্যবহার"],
        [
            ["ITA",  "INT → ASCII",    "ASCII String",   "Number কে Text এ Serial Send"],
            ["DTA",  "DINT → ASCII",   "ASCII String",   "32-bit number display"],
            ["RTA",  "REAL → ASCII",   "ASCII String",   "Float number to HMI text"],
            ["ATH",  "ASCII → HEX",    "Hex String",     "Serial input parsing"],
            ["HTA",  "HEX → ASCII",    "ASCII String",   "Hex value display"],
            ["S_I",  "String → INT",   "INT",            "Keyboard/HMI input parse"],
            ["S_DI", "String → DINT",  "DINT",           "Large number input"],
            ["S_R",  "String → REAL",  "REAL",           "Float input from HMI"],
            ["DECO", "Bit position → Word", "WORD",       "Step → Output bit select"],
            ["ENCO", "Word → Bit pos", "BYTE",           "Find highest set bit"],
            ["SEG",  "Digit → Segments","BYTE (7-seg)",  "7-Segment LED display"],
        ], D, C_ORANGE)

    make_content_slide(prs, "SEG — Seven Segment Display", [
        "## কাজ:",
        "  - 0~9 Digit Input → 7-Segment Pattern Output",
        "  - Output Byte এর প্রতিটি Bit একটি Segment কে ON/OFF করে",
        "## Segment Mapping (a~g):",
        "  - Bit 0 = Segment a (top)",
        "  - Bit 1 = Segment b (top-right)",
        "  - Bit 2 = Segment c (bottom-right)",
        "  - Bit 3 = Segment d (bottom)",
        "  - Bit 4 = Segment e (bottom-left)",
        "  - Bit 5 = Segment f (top-left)",
        "  - Bit 6 = Segment g (middle)",
        "## Example:",
        "  - SEG +5, QB0 → QB0 = 2#01101101 (displays '5')",
        "## Multi-digit Display:",
        "  - প্রতিটি Digit আলাদা SEG Instruction দিয়ে",
    ], D, note="SEG Instruction দিয়ে সরাসরি 7-Segment LED কে Q Output এ connect করা যায়!")

    make_practical_slide(prs,
        "Practical: 7-Segment Counter Display",
        "Counter value কে 7-Segment Display এ দেখানো",
        [
            "CTU C0 দিয়ে 0~9 গণনা করুন",
            "MOV_W C0, VW10 (Counter value copy)",
            "I_B VW10, VB20 (Integer to Byte)",
            "SEG VB20, QB0 (Byte to 7-Segment pattern)",
            "Q0.0~Q0.6 → 7-Segment Display a~g Segments",
            "C0 Bit → Reset C0 (0 থেকে আবার শুরু হবে 10 হলে)",
            "Hardware: Common Cathode 7-Segment LED",
        ], D)

    make_summary_slide(prs,
        "Module 10 — Day 19: Convert Part 2",
        ["ITA/DTA/RTA: Number → ASCII (Serial/HMI এর জন্য)",
         "ATH/HTA: ASCII ↔ HEX",
         "DECO: একটি Bit position → একটি Bit ON করে",
         "ENCO: কোন Bit ON আছে তা বের করে",
         "SEG: Digit → 7-Segment pattern"],
        "Day 20 (Module 11):\n• Logical Operations\n• AND, OR, XOR, INV\n• Bit Masking Technique",
        D)

    # ════════ DAY 20 — Logical Operations ════════
    D = "Module 11  |  Day 20"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 11 — Logical Operations",
        "Day 20  |  Upper-Intermediate  |  Duration: 2 Hours",
        RGBColor(0x00, 0x3D, 0x3D))

    make_agenda_slide(prs, "Day 20 — Agenda", [
        "Logical Operations কী? Bit-wise ধারণা",
        "WAND_B/W/DW — AND Operation",
        "WOR_B/W/DW — OR Operation",
        "WXOR_B/W/DW — XOR Operation",
        "INV_B/W/DW — Invert (NOT)",
        "Bit Masking Technique",
        "Practical: Status Byte Control",
    ], D)

    make_content_slide(prs, "Logical Operations — Bit-wise কাজ", [
        "## সাধারণ Contact Logic vs Logical Instruction:",
        "  - Contact Logic: পুরো Bit (0 বা 1) নিয়ে কাজ",
        "  - Logical Instruction: Byte/Word এর প্রতিটি Bit আলাদাভাবে",
        "## AND (WAND):",
        "  - উভয় Input Bit = 1 হলেই Output = 1",
        "  - Mask দিয়ে নির্দিষ্ট Bit বের করতে ব্যবহার হয়",
        "  - Example: VB10 AND 16#0F → শুধু Lower Nibble রাখে",
        "## OR (WOR):",
        "  - যেকোনো একটি Bit = 1 হলে Output = 1",
        "  - Bit Force করতে ব্যবহার হয়",
        "  - Example: VB10 OR 16#80 → MSB কে Force 1 করে",
        "## XOR (WXOR):",
        "  - একটি Bit 1, অন্যটি 0 হলে Output = 1",
        "  - Bit Toggle করতে ব্যবহার",
        "## INV (Invert):",
        "  - সব Bit উল্টায় (0→1, 1→0)",
        "  - 1's Complement",
    ], D, note="Bit Masking হল Logical Operations এর সবচেয়ে গুরুত্বপূর্ণ application!")

    make_table_slide(prs,
        "Logical Operations — Truth Table",
        ["Operation", "IN1 Bit", "IN2 Bit", "Output Bit", "Example Use"],
        [
            ["AND", "0", "0", "0", "Mask unwanted bits"],
            ["AND", "0", "1", "0", "Keep only masked bits"],
            ["AND", "1", "0", "0", "Clear specific bits"],
            ["AND", "1", "1", "1", "Filter status byte"],
            ["OR",  "0", "0", "0", "Set specific bits"],
            ["OR",  "0", "1", "1", "Force bit to 1"],
            ["OR",  "1", "0", "1", "Combine two bytes"],
            ["OR",  "1", "1", "1", "Merge status flags"],
            ["XOR", "0", "0", "0", "Toggle specific bits"],
            ["XOR", "0", "1", "1", "Flip selected bits"],
            ["XOR", "1", "1", "0", "Check byte equality"],
        ], D, C_TEAL)

    make_summary_slide(prs,
        "Module 11 — Day 20: Logical Operations",
        ["AND: দুটি Bit উভয়ই 1 হলে 1",
         "OR: যেকোনো একটি 1 হলে 1",
         "XOR: শুধু একটি 1 হলে 1 (Toggle)",
         "INV: সব Bit উল্টে দেয়",
         "Masking: AND দিয়ে নির্দিষ্ট Bit বের করা"],
        "Day 21 (Module 12):\n• Shift ও Rotate Instructions\n• SHL, SHR, ROL, ROR\n• Running Light Project",
        D)

    # ════════ DAY 21 — Shift/Rotate ════════
    D = "Module 12  |  Day 21"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 12 — Shift & Rotate Instructions",
        "Day 21  |  Upper-Intermediate  |  Duration: 2 Hours",
        RGBColor(0x1A, 0x3D, 0x00))

    make_agenda_slide(prs, "Day 21 — Agenda", [
        "Shift ও Rotate — পার্থক্য কী?",
        "SHL_B/W/DW — Shift Left",
        "SHR_B/W/DW — Shift Right",
        "ROL_B/W/DW — Rotate Left",
        "ROR_B/W/DW — Rotate Right",
        "SHRB — Shift Register Bit (Sequencer)",
        "Practical: Running Light / Knight Rider",
    ], D)

    make_two_col_slide(prs,
        "Shift vs Rotate — পার্থক্য",
        "Shift (SHL / SHR)",
        ["Bits একদিকে সরে যায়",
         "বাইরে যাওয়া Bit হারিয়ে যায়",
         "SHL: ফাঁকা Bit = 0 দিয়ে পূরণ",
         "SHR: ফাঁকা Bit = 0 দিয়ে পূরণ",
         "SHL N = × 2ᴺ (গুণ)",
         "SHR N = ÷ 2ᴺ (ভাগ)",
         "Power of 2 calculation এ ব্যবহার"],
        "Rotate (ROL / ROR)",
        ["Bits একদিকে সরে যায়",
         "বাইরে যাওয়া Bit অন্যদিক থেকে ঢোকে",
         "ROL: বাম থেকে বের → ডানে প্রবেশ",
         "ROR: ডান থেকে বের → বামে প্রবেশ",
         "Bit Pattern টি Rotate হয়",
         "Running Light এ ব্যবহার",
         "Conveyor Sequence Control"],
        D, C_GREEN)

    make_content_slide(prs, "SHRB — Shift Register Bit", [
        "## কাজ:",
        "  - এক Bit কে একটি Bit Array তে Shift করে",
        "  - FIFO Buffer হিসেবে কাজ করে",
        "## Parameters:",
        "  - DATA: Shift হওয়া Bit এর মান (0 বা 1)",
        "  - S_BIT: Shift Register এর শুরুর Bit Address",
        "  - N: Register এর Length (Positive = Left, Negative = Right)",
        "## Example (Conveyor Tracking):",
        "  - Conveyor এ Product আছে কিনা Track করা",
        "  - প্রতিটি Sensor Position থেকে পরের Position এ Bit Shift হয়",
        "  - N = 8 মানে 8টি Position Track করা যাবে",
        "## Application:",
        "  - Paint/Welding Station — কোন Position এ Product আছে",
        "  - Product Tracking on Conveyor",
    ], D, note="SHRB হল Conveyor Product Tracking এর সবচেয়ে elegant solution!")

    make_practical_slide(prs,
        "Practical: Running Light (Knight Rider Effect)",
        "Q0.0 থেকে Q0.7 পর্যন্ত আলো ক্রমানুসারে জ্বলবে",
        [
            "MB0 = 8-bit Shift Register (QB0 তে connect)",
            "Network 1: SM0.0 (Always ON) → MOV_B +1, MB0 (Initialize)",
            "Network 2: T37 (0.2s Timer) → ROL_B MB0, 1 (Rotate Left)",
            "Network 3: MOV_B MB0, QB0 (Output এ দেখান)",
            "Timer T37: PT=+2 (200ms interval)",
            "Result: প্রতি 200ms এ একটি Light পরেরটিতে যাবে",
            "Extension: Reverse করতে ROR_B ব্যবহার করুন",
        ], D)

    make_table_slide(prs,
        "Module 10, 11, 12 — সমস্ত Instructions Summary",
        ["Module", "Instructions", "Key Application"],
        [
            ["10 Convert", "B_I, I_DI, DI_R, I_B", "Data type chain conversion"],
            ["10 Convert", "BCD_I, I_BCD", "7-Segment, Thumb Wheel"],
            ["10 Convert", "ROUND, TRUNC", "Float to Integer"],
            ["10 Convert", "ITA, RTA, ATH, HTA", "Serial/HMI communication"],
            ["10 Convert", "SEG, DECO, ENCO", "Display ও bit decoding"],
            ["11 Logic",   "WAND_B/W/DW", "Bit masking"],
            ["11 Logic",   "WOR_B/W/DW", "Bit setting/combining"],
            ["11 Logic",   "WXOR_B/W/DW", "Bit toggling"],
            ["11 Logic",   "INV_B/W/DW", "Bit inversion"],
            ["12 Shift",   "SHL/SHR B/W/DW", "Multiply/divide by power of 2"],
            ["12 Shift",   "ROL/ROR B/W/DW", "Running light, sequence"],
            ["12 Shift",   "SHRB", "Conveyor product tracking"],
        ], D, C_NAVY)

    make_summary_slide(prs,
        "Module 10-12 — Convert, Logic, Shift: Complete",
        ["Convert: Data Type পরিবর্তন করতে অপরিহার্য",
         "AND/OR/XOR: Bit-level manipulation",
         "SHL/SHR: ×2 বা ÷2 দ্রুত করে",
         "ROL/ROR: Circular shift — Running Light",
         "SHRB: Conveyor Product Tracking FIFO"],
        "Day 22 (Module 13):\n• String Instructions শুরু\n• SLEN, SCAT, SCPY\n• HMI Message System",
        D)

    save(prs, "Module_10_12_Convert_Logic_Shift_Day18-21.pptx")

if __name__ == "__main__":
    build()
