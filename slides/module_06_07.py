"""Module 06 & 07 — Day 11-13 — Compare & Move"""
from generate_slides import *

def build():
    prs = new_prs()

    # ════════ DAY 11 — Compare ════════
    D = "Module 06  |  Day 11"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 06 — Compare Instructions",
        "Day 11  |  Intermediate Level  |  Duration: 2 Hours",
        RGBColor(0x00, 0x4C, 0x6E))

    make_agenda_slide(prs, "Day 11 — Agenda", [
        "Compare Instruction কী এবং কেন দরকার?",
        "Byte Compare (==B, <>B, >=B, <=B, >B, <B)",
        "Integer Compare (==I, <>I, >=I, <=I, >I, <I)",
        "Double Integer Compare (==DI ~ <DI)",
        "Real / Float Compare (==R ~ <R)",
        "String Compare (==S, <>S)",
        "Practical: Temperature Range Alarm",
    ], D)

    make_content_slide(prs, "Compare Instruction — কীভাবে কাজ করে", [
        "## Compare Instruction Contact এর মতো কাজ করে:",
        "  - দুটি মান তুলনা করে",
        "  - তুলনা সত্য হলে Current Pass করে (Contact Closed)",
        "  - তুলনা মিথ্যা হলে Current Block করে (Contact Open)",
        "## Ladder এ Position:",
        "  - সাধারণ Contact এর মতো Series বা Parallel এ রাখা যায়",
        "  - Rung এ শুরু বা মাঝে রাখা যায়",
        "## Data Types:",
        "  - B = Byte (0 ~ 255)",
        "  - I = Integer (-32768 ~ +32767)",
        "  - DI = Double Integer (-2,147,483,648 ~ +2,147,483,647)",
        "  - R = Real / Float (Decimal number)",
        "  - S = String",
        "## Operands:",
        "  - Constant, V Memory, I, Q, M, T, C, AC, AI",
    ], D, note="Compare Instruction ব্যবহার করে Analog Sensor এর মান Check করা যায়।")

    make_table_slide(prs,
        "Compare Instructions — সমস্ত Operators",
        ["Operator", "মানে", "Byte", "Integer", "D.Integer", "Real"],
        [
            ["==", "Equal (সমান)",               "==B", "==I", "==DI", "==R"],
            ["<>", "Not Equal (সমান নয়)",        "<>B", "<>I", "<>DI", "<>R"],
            [">=", "Greater or Equal (বড় বা সমান)",">=B",">=I",">=DI",">=R"],
            ["<=", "Less or Equal (ছোট বা সমান)", "<=B", "<=I", "<=DI", "<=R"],
            [">",  "Greater Than (বড়)",           ">B",  ">I",  ">DI",  ">R"],
            ["<",  "Less Than (ছোট)",             "<B",  "<I",  "<DI",  "<R"],
        ], D, C_TEAL)

    make_content_slide(prs, "Compare — Analog Temperature Example", [
        "## Scenario: Temperature Controller",
        "  - Temperature Sensor → AI0 (Analog Input 0)",
        "  - AI0 Range: 0 ~ 32000 (0°C ~ 100°C)",
        "  - 80°C = AI0 Value ≈ 25600",
        "## Program Logic:",
        "  - Network 1: ==I AIW0, +25600 → Q0.0 (Normal LED)",
        "  - Network 2: >I  AIW0, +28800 → Q0.1 (High Temp Alarm)",
        "  - Network 3: <I  AIW0, +6400  → Q0.2 (Low Temp Alarm)",
        "  - Network 4: >=I AIW0, +28800 → R Q0.3, 1 (Heater OFF)",
        "  - Network 5: <=I AIW0, +6400  → S Q0.3, 1 (Heater ON)",
        "## Real Value Compare:",
        "  - ROUND বা DI_R দিয়ে Real Value এ Convert করে Compare",
    ], D, note="AI0 Raw Value কে Engineering Unit (°C) এ convert করতে Math Instruction লাগবে!")

    make_practical_slide(prs,
        "Practical: Temperature Range Alarm System",
        "Temperature Low/Normal/High তিনটি Zone এ LED জ্বালানো",
        [
            "AIW0 = Temperature Sensor Input",
            "Q0.0 = Green LED (Normal: 20°C~80°C)",
            "Q0.1 = Yellow LED (High: 80°C~90°C) ",
            "Q0.2 = Red LED + Alarm (Critical: >90°C)",
            "Network 1: >=I AIW0,+6400 AND <=I AIW0,+25600 → Q0.0",
            "Network 2: >I AIW0,+25600 AND <=I AIW0,+28800 → Q0.1",
            "Network 3: >I AIW0,+28800 → Q0.2",
            "Status Chart এ AIW0 monitor করুন",
        ], D)

    make_summary_slide(prs,
        "Module 06 — Day 11: Compare Instructions",
        ["6 ধরনের Compare: ==, <>, >=, <=, >, <",
         "4 Data Type: Byte, Integer, Double Int, Real",
         "Contact এর মতো Series/Parallel এ ব্যবহার করা যায়",
         "Analog Sensor Value Check এ সবচেয়ে বেশি ব্যবহার",
         "String Compare: ==S ও <>S"],
        "Day 12 (Module 07):\n• Move Instructions শুরু\n• MOV_B, MOV_W, MOV_DW\n• BLKMOV এবং SWAP",
        D)

    # ════════ DAY 12 — Move ════════
    D = "Module 07  |  Day 12"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 07 — Move Instructions",
        "Day 12  |  Intermediate Level  |  Duration: 2 Hours",
        RGBColor(0x00, 0x4C, 0x6E))

    make_agenda_slide(prs, "Day 12 — Agenda", [
        "Move Instruction কী এবং কেন দরকার?",
        "MOV_B — Move Byte",
        "MOV_W — Move Word (16-bit)",
        "MOV_DW — Move Double Word (32-bit)",
        "MOV_R — Move Real (Float)",
        "BLKMOV_B / W / D — Block Move",
        "SWAP, MOV_BIR, MOV_BIW",
    ], D)

    make_content_slide(prs, "Move Instructions — Overview", [
        "## কাজ: এক Memory Address থেকে অন্যটিতে Data কপি করা",
        "  - Source (IN) → Destination (OUT)",
        "  - Source এর মান পরিবর্তন হয় না",
        "## Data Sizes:",
        "  - BYTE (B) = 8 bits = 0 ~ 255",
        "  - WORD (W) = 16 bits = -32768 ~ +32767",
        "  - DWORD (DW) = 32 bits = ±2 billion",
        "  - REAL (R) = 32 bits = Floating Point",
        "## Usage Examples:",
        "  - Recipe loading: Constant → VW100",
        "  - Data copy: VW100 → VW200",
        "  - Output control: Set QB0 = 2#11001100",
        "## Enable Input:",
        "  - EN = 1 হলে Instruction Execute হয়",
        "  - EN = 0 হলে কিছু করে না (ENO = 0)",
    ], D, note="MOV Instruction দিয়ে একসাথে 8টি Output Bit একটি Byte হিসেবে নিয়ন্ত্রণ করা যায়!")

    make_table_slide(prs,
        "Move Instructions — সম্পূর্ণ তালিকা",
        ["Instruction", "Size", "IN Range", "ব্যবহার"],
        [
            ["MOV_B",    "Byte (8-bit)",   "0~255",           "Byte copy, Output byte set"],
            ["MOV_W",    "Word (16-bit)",  "-32768~+32767",   "Integer copy, Timer/Counter PV"],
            ["MOV_DW",   "DWord (32-bit)", "±2,147,483,647",  "Double integer, HC value"],
            ["MOV_R",    "Real (32-bit)",  "IEEE 754 Float",  "Analog scaling, PID setpoint"],
            ["BLKMOV_B", "N Bytes",        "N = 1~255",       "Array copy, Table initialize"],
            ["BLKMOV_W", "N Words",        "N = 1~255",       "Recipe block copy"],
            ["BLKMOV_D", "N DWords",       "N = 1~255",       "Large data copy"],
            ["SWAP",     "Word",           "VW, IW, QW",      "High/Low byte swap"],
            ["MOV_BIR",  "Byte",           "Input address",   "Immediate byte read"],
            ["MOV_BIW",  "Byte",           "Output address",  "Immediate byte write"],
        ], D, C_TEAL)

    make_content_slide(prs, "BLKMOV — Block Move (Array Copy)", [
        "## কাজ: একাধিক Memory Cell একসাথে Copy করা",
        "## Parameters:",
        "  - IN: Source শুরুর Address",
        "  - OUT: Destination শুরুর Address",
        "  - N: কতটি Cell Copy হবে",
        "## Example — Recipe Loading:",
        "  - Recipe 1 Data: VB100 ~ VB109 (10 bytes)",
        "  - Active Recipe: VB200 ~ VB209",
        "  - BLKMOV_B VB100, VB200, 10",
        "  - এক Instruction এ ১০টি Byte Copy হয়!",
        "## SWAP — Byte Swap:",
        "  - একটি Word এর High Byte ও Low Byte উল্টায়",
        "  - Modbus, Serial Communication এ প্রয়োজন হয়",
        "  - Example: VW100 = 0x1234 → SWAP → VW100 = 0x3412",
    ], D, note="BLKMOV দিয়ে Recipe System তৈরি করা S7-200 এর popular technique!")

    make_summary_slide(prs,
        "Module 07 — Day 12: Move Instructions",
        ["MOV_B/W/DW/R — এক Address থেকে অন্যটিতে copy",
         "Source পরিবর্তন হয় না",
         "BLKMOV দিয়ে Array/Recipe copy করা যায়",
         "SWAP — Word এর High/Low Byte উল্টায়",
         "MOV_BIR/BIW — Scan wait না করে Immediate"],
        "Day 13:\n• Compare + Move Combined Project\n• Module 06 & 07 Review\n• Data Management System",
        D)

    # ════════ DAY 13 — Compare+Move Project ════════
    D = "Module 06-07  |  Day 13"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 06-07 — Compare & Move: Combined Practical",
        "Day 13  |  Lab Day  |  Duration: 2 Hours",
        RGBColor(0x00, 0x3A, 0x5C))

    make_agenda_slide(prs, "Day 13 — Practical Agenda", [
        "Project: Multi-Recipe Selector System",
        "Compare দিয়ে Recipe Number Check",
        "BLKMOV দিয়ে Recipe Data Load",
        "Module 06 & 07 সমস্ত Instructions Review",
        "Common Programming Errors",
        "Quiz",
    ], D)

    make_practical_slide(prs,
        "Project: Recipe Selector System",
        "3টি Recipe থেকে Selector Switch দিয়ে একটি বেছে Load করা",
        [
            "IB0 = Recipe Selector (0=Recipe1, 1=Recipe2, 2=Recipe3)",
            "VB100~109 = Recipe 1 Data (Speed, Temp, Time ইত্যাদি)",
            "VB110~119 = Recipe 2 Data",
            "VB120~129 = Recipe 3 Data",
            "VB200~209 = Active Recipe (Machine এ ব্যবহৃত)",
            "Network 1: ==B IB0, 0 → BLKMOV_B VB100, VB200, 10",
            "Network 2: ==B IB0, 1 → BLKMOV_B VB110, VB200, 10",
            "Network 3: ==B IB0, 2 → BLKMOV_B VB120, VB200, 10",
            "Symbol Table এ Recipe Variables এর নাম দিন",
        ], D)

    make_table_slide(prs,
        "Module 06 & 07 — Combined Summary",
        ["Module", "Instructions", "Key Use Case"],
        [
            ["06 — Compare", "==B, <B, >B, ==I, <I, >I", "Sensor range check"],
            ["06 — Compare", "==DI, ==R (Float)", "Precision measurement"],
            ["06 — Compare", "==S, <>S (String)", "Barcode match"],
            ["07 — Move",    "MOV_B, MOV_W, MOV_DW", "Data register copy"],
            ["07 — Move",    "MOV_R (Float)", "PID setpoint load"],
            ["07 — Move",    "BLKMOV_B/W/D", "Recipe/Array copy"],
            ["07 — Move",    "SWAP", "Communication byte order"],
            ["07 — Move",    "MOV_BIR, MOV_BIW", "Immediate I/O"],
        ], D, C_TEAL)

    make_summary_slide(prs,
        "Module 06 & 07 — Compare & Move: Complete",
        ["Compare = Data এর মান check করে contact চালু করে",
         "6টি Operator: ==, <>, >=, <=, >, <",
         "Move = Source থেকে Destination এ data copy",
         "BLKMOV = একসাথে অনেক cell copy",
         "Recipe System = BLKMOV এর সেরা application"],
        "Day 14 (Module 08):\n• Integer Math শুরু\n• ADD, SUB, MUL, DIV\n• INC ও DEC Instructions",
        D)

    save(prs, "Module_06_07_Compare_Move_Day11-13.pptx")

if __name__ == "__main__":
    build()
