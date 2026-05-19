"""Module 13, 14, 15 — Day 22-25 — String, Table, Program Control"""
from generate_slides import *

def build():
    prs = new_prs()

    # ════════ DAY 22 — String ════════
    D = "Module 13  |  Day 22"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 13 — String Instructions",
        "Day 22  |  Advanced Level  |  Duration: 2 Hours",
        RGBColor(0x5C, 0x2A, 0x00))

    make_agenda_slide(prs, "Day 22 — Agenda", [
        "String কী? S7-200 তে String Memory Format",
        "SLEN — String Length বের করা",
        "SCPY — String Copy",
        "SCAT — String Concatenate (জোড়া লাগানো)",
        "SSCPY — Substring Copy",
        "SFND ও CFND — String ও Character Search",
        "Practical: HMI Message Builder",
    ], D)

    make_content_slide(prs, "String — S7-200 তে কীভাবে Store হয়", [
        "## String Structure:",
        "  - Byte 0: String Length (Character সংখ্যা)",
        "  - Byte 1~N: প্রতিটি ASCII Character",
        "  - Maximum Length: 254 Characters",
        "## Example: 'HELLO' String",
        "  - VB100 = 5 (length)",
        "  - VB101 = 72 (H)",
        "  - VB102 = 69 (E)",
        "  - VB103 = 76 (L)",
        "  - VB104 = 76 (L)",
        "  - VB105 = 79 (O)",
        "## String Constants:",
        "  - Program এ: 'Hello PLC' লিখলে Auto-convert",
        "## কেন String লাগে:",
        "  - HMI Display, Serial Printer, SCADA Message",
        "  - Barcode Reader থেকে Data Processing",
    ], D, note="String Address সবসময় VB (Variable Byte) তে রাখতে হবে।")

    make_table_slide(prs,
        "String Instructions — Complete List",
        ["Instruction", "কাজ", "Parameters", "ব্যবহার"],
        [
            ["SLEN",  "String Length বের করা",      "IN=String, OUT=Byte", "কত character আছে জানতে"],
            ["SCPY",  "String Copy",                 "IN=String, OUT=String","এক জায়গা থেকে অন্যত্র"],
            ["SCAT",  "String Concatenate",          "IN=String, OUT=String","দুটো String জোড়া লাগানো"],
            ["SSCPY", "Substring Copy",              "IN, INDX, N, OUT",   "String এর অংশ কপি"],
            ["SFND",  "String Find",                 "IN1, IN2, OUT",      "String এর মধ্যে খোঁজা"],
            ["CFND",  "Character Find",              "IN1, IN2, OUT",      "Character খোঁজা"],
        ], D, C_ORANGE)

    make_practical_slide(prs,
        "Practical: Alarm Message Builder",
        "Sensor Status থেকে Dynamic Alarm Message তৈরি করা",
        [
            "VB100 = Base Message: 'ALARM: '",
            "VB200 = Alarm Type: 'HIGH TEMP' বা 'LOW PRESS'",
            "VB300 = Final Message (Combined)",
            "Network 1: SCPY VB100, VB300  (Base copy করুন)",
            "Network 2: High Temp → SCAT 'HIGH TEMP', VB300",
            "Network 3: Low Pressure → SCAT 'LOW PRESS', VB300",
            "Network 4: XMT VB300 → Serial Port (HMI/Printer)",
        ], D)

    make_summary_slide(prs,
        "Module 13 — Day 22: String Instructions",
        ["String = Length Byte + ASCII Characters",
         "SCPY: পুরো String copy করে",
         "SCAT: দুটো String জোড়া লাগায়",
         "SSCPY: String এর একটা অংশ বের করে",
         "SFND/CFND: String এর মধ্যে খোঁজে"],
        "Day 23 (Module 14):\n• Table Instructions\n• ATT, FIFO, LIFO\n• Data Logging System",
        D)

    # ════════ DAY 23 — Table ════════
    D = "Module 14  |  Day 23"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 14 — Table Instructions",
        "Day 23  |  Advanced Level  |  Duration: 2 Hours",
        RGBColor(0x00, 0x3D, 0x5C))

    make_agenda_slide(prs, "Day 23 — Agenda", [
        "Table (TBL) কী এবং Memory Structure",
        "ATT — Add to Table",
        "LIFO — Last In First Out (Stack)",
        "FIFO — First In First Out (Queue)",
        "FND= / FND<> / FND< / FND> — Table Search",
        "FILL — Fill Memory",
        "Practical: Measurement Data Logger",
    ], D)

    make_content_slide(prs, "Table Structure — কীভাবে কাজ করে", [
        "## Table Memory Layout:",
        "  - Word 0 (TL): Table Length — সর্বোচ্চ কতটি Entry",
        "  - Word 1 (EC): Entry Count — এখন কতটি Entry আছে",
        "  - Word 2~N: Actual Data Entries",
        "## Example: TBL শুরু VW100 এ, Length=5",
        "  - VW100 = 5 (Maximum 5 entries)",
        "  - VW102 = 3 (Currently 3 entries filled)",
        "  - VW104 = Data Entry 1",
        "  - VW106 = Data Entry 2",
        "  - VW108 = Data Entry 3",
        "## Error Flags:",
        "  - SM1.4 = Table Full (ATT করতে গেলে)",
        "  - SM1.5 = Table Empty (FIFO/LIFO করতে গেলে)",
        "## Data Type: শুধুমাত্র WORD (16-bit)",
    ], D, note="Table ব্যবহার করলে Array এর মতো Structured Data সহজে manage করা যায়!")

    make_table_slide(prs,
        "Table Instructions — Complete Reference",
        ["Instruction", "কাজ", "Parameters", "Error Flag"],
        [
            ["ATT",   "Table এ Data যোগ করা",       "DATA, TBL",      "SM1.4=1 if Full"],
            ["LIFO",  "শেষ entry বের করা (Stack)",   "TBL, DATA",      "SM1.5=1 if Empty"],
            ["FIFO",  "প্রথম entry বের করা (Queue)", "TBL, DATA",      "SM1.5=1 if Empty"],
            ["FND=",  "Equal value খোঁজা",            "TBL, PTN, INDX","INDX=EC if not found"],
            ["FND<>", "Not equal value খোঁজা",        "TBL, PTN, INDX","INDX=EC if not found"],
            ["FND<",  "Less than value খোঁজা",        "TBL, PTN, INDX","INDX=EC if not found"],
            ["FND>",  "Greater than value খোঁজা",     "TBL, PTN, INDX","INDX=EC if not found"],
            ["FILL",  "Memory Block এ Value ভরা",     "IN, OUT, N",     "N bytes fill"],
        ], D, C_TEAL)

    make_practical_slide(prs,
        "Practical: Temperature Data Logger",
        "প্রতি মিনিটে Temperature রেকর্ড করে Table এ জমা রাখা",
        [
            "VW100 = Table শুরু (TL=60, max 60 entries = 1 hour)",
            "FILL +0, VW100, 62 → Initialize করুন (startup এ)",
            "MOV_W +60, VW100 (TL = 60 set করুন)",
            "1-minute Timer → ATT AIW0, VW100 (Temp record)",
            "Table Full (SM1.4) → FIFO VW100, VW500 (পুরোনোটা বের করুন)",
            "FND> VW100, +28800, VW600 → Overheat কখন হয়েছিল",
            "LIFO দিয়ে সবচেয়ে সাম্প্রতিক Reading বের করুন",
        ], D)

    make_summary_slide(prs,
        "Module 14 — Day 23: Table Instructions",
        ["Table = TL (max) + EC (current) + Data Words",
         "ATT: Table এ নতুন entry যোগ করে",
         "FIFO: Queue — আগে যেটা ঢুকেছে আগে বের হয়",
         "LIFO: Stack — শেষে যেটা ঢুকেছে প্রথমে বের হয়",
         "FND: Table এ নির্দিষ্ট মান খোঁজে"],
        "Day 24 (Module 15):\n• Program Control Instructions\n• JMP, FOR-NEXT, CALL\n• Sequential Process Control",
        D)

    # ════════ DAY 24 — Program Control ════════
    D = "Module 15  |  Day 24"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 15 — Program Control Instructions",
        "Day 24  |  Advanced Level  |  Duration: 2 Hours",
        RGBColor(0x3D, 0x3D, 0x00))

    make_agenda_slide(prs, "Day 24 — Agenda", [
        "Program Control কেন দরকার?",
        "END ও STOP — Program শেষ করা",
        "WDR — Watchdog Reset",
        "JMP ও LBL — Conditional Jump",
        "CALL ও RET — Subroutine Call",
        "FOR ও NEXT — Loop",
        "DLED — Diagnostic LED",
    ], D)

    make_content_slide(prs, "JMP, FOR-NEXT, CALL — Program Flow", [
        "## JMP (Jump to Label):",
        "  - Condition সত্য হলে Program একটি Label এ লাফ দেয়",
        "  - JMP n → LBL n (n = 0~255)",
        "  - সতর্কতা: JMP দিয়ে Timer/Counter এর মাঝে লাফ দেবেন না",
        "## FOR-NEXT Loop:",
        "  - FOR INDX, INIT, FINAL",
        "  - NEXT পর্যন্ত Instruction গুলো INDX বারের মতো চলে",
        "  - INIT থেকে FINAL পর্যন্ত INDX বাড়ে",
        "  - Example: FOR VW0, +1, +10 → 10 বার loop",
        "## CALL (Call Subroutine):",
        "  - SBR_0, SBR_1... Subroutine Block এ Jump করে",
        "  - Subroutine শেষে RET দিয়ে ফিরে আসে",
        "  - Parameter pass করা যায় (Local Variable দিয়ে)",
        "## WDR (Watchdog Reset):",
        "  - Watchdog Timer Reset করে",
        "  - Loop এ বেশি সময় থাকলে WDR দরকার (>500ms)",
    ], D, note="FOR-NEXT Loop এ বেশি iteration থাকলে Scan Time বাড়ে — সতর্ক থাকুন!")

    make_table_slide(prs,
        "Program Control Instructions — Summary",
        ["Instruction", "কাজ", "Operand", "Note"],
        [
            ["END",  "Program এর শেষ (Conditional)", "None",         "Rung এ Power থাকলে Scan end"],
            ["STOP", "CPU কে Stop Mode এ নেয়",        "None",         "Emergency use only"],
            ["WDR",  "Watchdog Timer Reset",           "None",         "Long loop এ ব্যবহার"],
            ["JMP",  "Label এ Jump করে",               "n (0~255)",    "Condition সত্য হলে"],
            ["LBL",  "Jump এর Destination",            "n (0~255)",    "JMP এর Target"],
            ["CALL", "Subroutine Call",                "SBR_n",        "Modular programming"],
            ["RET",  "Subroutine থেকে Return",         "None",         "Conditional/Unconditional"],
            ["CRET", "Conditional Return",             "None",         "শর্ত সাপেক্ষে Return"],
            ["FOR",  "Loop শুরু",                      "INDX,INIT,FIN","INDX = Loop counter"],
            ["NEXT", "Loop শেষ",                       "None",         "FOR এর সাথে pair"],
            ["DLED", "Diagnostic LED চালু",            "IN",           "SF/DIAG LED control"],
        ], D, C_ORANGE)

    make_practical_slide(prs,
        "Practical: Multi-Step Sequential Process",
        "৫টি ধাপে একটি Manufacturing Process চালানো",
        [
            "MB10 = Step Counter (0~5)",
            "Step 0: Start Button → S MB10.0 (Initialize)",
            "Network: ==B MB10, +1 → Mixer ON (Q0.0), Timer T37",
            "Network: ==B MB10, +2 → Heater ON (Q0.1), Timer T38",
            "Network: ==B MB10, +3 → Pump ON (Q0.2), Timer T39",
            "Network: ==B MB10, +4 → Cooler ON (Q0.3), Timer T40",
            "Network: ==B MB10, +5 → Done Alarm (Q0.4), Reset Step",
            "Each Timer Done → INC_B MB10 (পরের Step এ যায়)",
        ], D)

    make_summary_slide(prs,
        "Module 15 — Day 24: Program Control",
        ["JMP/LBL: Conditional program jump",
         "FOR/NEXT: Fixed count loop",
         "CALL/RET: Subroutine — Modular Programming",
         "WDR: Long execution এ Watchdog reset",
         "Step Sequencer: INC_B + Compare = Elegant Solution"],
        "Day 25:\n• Module 13-15 Combined Review\n• Advanced Sequencer Project\n• Quiz",
        D)

    # ════════ DAY 25 — Review ════════
    D = "Module 13-15  |  Day 25"
    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 13-15 — String, Table, Control: Review & Project",
        "Day 25  |  Review + Lab Day  |  Duration: 2 Hours",
        RGBColor(0x2A, 0x2A, 0x3D))

    make_agenda_slide(prs, "Day 25 — Agenda", [
        "Module 13 String Instructions — Quick Review",
        "Module 14 Table Instructions — Quick Review",
        "Module 15 Program Control — Quick Review",
        "Project: Smart Alarm Logger with Message",
        "Common Mistakes ও Best Practices",
        "Quiz — Advanced Level",
    ], D)

    make_table_slide(prs,
        "Module 13-15 — Combined Summary Table",
        ["Module", "Key Instructions", "Real-world Use"],
        [
            ["13 String", "SCPY, SCAT, SSCPY", "HMI message building"],
            ["13 String", "SFND, CFND, SLEN",  "Barcode parsing"],
            ["13 String", "ITA/RTA → SCAT",    "Value to message"],
            ["14 Table",  "ATT + FIFO",         "Production Queue"],
            ["14 Table",  "ATT + LIFO",         "Last event recall"],
            ["14 Table",  "FND= / FND>",        "Data search"],
            ["14 Table",  "FILL",               "Initialize memory"],
            ["15 Control","FOR-NEXT",           "Batch processing loop"],
            ["15 Control","CALL / SBR",         "Reusable code blocks"],
            ["15 Control","JMP / LBL",          "Skip disabled sections"],
            ["15 Control","Step + INC_B",       "Sequential machine control"],
        ], D, C_NAVY)

    make_summary_slide(prs,
        "Module 13-15 — Advanced Instructions: Complete",
        ["String: HMI Message তৈরি ও Communication",
         "Table: FIFO Queue ও LIFO Stack Data Management",
         "JMP: Conditional skip in program",
         "FOR/NEXT: Counted loop for batch tasks",
         "Step Sequencer: সবচেয়ে clean sequential control method"],
        "Day 26 (Module 16):\n• Interrupt Instructions\n• ATCH, DTCH, ENI, DISI\n• Emergency Stop System",
        D)

    save(prs, "Module_13_15_String_Table_Control_Day22-25.pptx")

if __name__ == "__main__":
    build()
