"""Module 03 — Day 4, 5, 6 — Bit Logic Instructions"""
from generate_slides import *

def build():
    prs = new_prs()

    # ════════════════════════════════════════════════════════
    #  DAY 4  — Contacts & Coils
    # ════════════════════════════════════════════════════════
    D = "Module 03  |  Day 4"

    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 03 — Bit Logic Instructions",
        "Day 4  |  Beginner Level  |  Duration: 2 Hours",
        RGBColor(0x1A, 0x5C, 0x3A))

    make_agenda_slide(prs, "Day 4 — Agenda", [
        "Bit Logic কী? — Ladder এর ভিত্তি",
        "Normally Open Contact —| |— (LD, A, O)",
        "Normally Closed Contact —|/|— (LDN, AN, ON)",
        "Output Coil —( )— এবং কীভাবে কাজ করে",
        "Series Circuit (AND Logic)",
        "Parallel Circuit (OR Logic)",
        "Hands-on Lab: Motor Control Circuit",
    ], D)

    make_content_slide(prs, "Bit Logic — Ladder এর ভিত্তি", [
        "Ladder Diagram = Electric Circuit এর মতো দেখতে প্রোগ্রাম",
        "## দুটি Vertical Rail:",
        "  - Left Rail = Power Rail (Live)",
        "  - Right Rail = Neutral Rail",
        "## Network / Rung:",
        "  - প্রতিটি Horizontal Line = একটি Network",
        "  - Contact (Switch) + Coil (Load) দিয়ে তৈরি",
        "## Bit Logic মানে:",
        "  - প্রতিটি Bit এর মান হয় 0 (OFF) নয়তো 1 (ON)",
        "  - Contact গুলো Bit পড়ে",
        "  - Coil গুলো Bit লেখে",
        "## Addressing:",
        "  - I0.0 = Input Byte 0, Bit 0",
        "  - Q0.1 = Output Byte 0, Bit 1",
        "  - M5.3 = Memory Byte 5, Bit 3",
    ], D, note="Ladder Diagram মূলত একজন Electrician এর জন্য পড়া সহজ করে তৈরি করা হয়েছিল।")

    make_table_slide(prs,
        "Normally Open & Normally Closed Contact",
        ["Instruction", "Symbol", "STL", "কাজ"],
        [
            ["Normally Open",   "—| |—",  "LD / A / O",   "Bit=1 হলে Current প্রবাহিত হয়"],
            ["Normally Closed", "—|/|—",  "LDN / AN / ON","Bit=0 হলে Current প্রবাহিত হয়"],
            ["N.O. (Series)",   "—| |—",  "A",            "AND — আগের Contact এর পরে"],
            ["N.C. (Series)",   "—|/|—",  "AN",           "AND NOT — আগেরটার পরে"],
            ["N.O. (Parallel)", "—| |—",  "O",            "OR — সমান্তরাল সংযোগ"],
            ["N.C. (Parallel)", "—|/|—",  "ON",           "OR NOT — সমান্তরাল"],
            ["Output Coil",     "—( )—",  "=",            "Bit কে 1 করে (Power থাকলে)"],
        ], D, C_GREEN)

    make_content_slide(prs, "Series Circuit — AND Logic", [
        "## Circuit Structure:",
        "  - দুটি Contact পাশাপাশি সংযুক্ত",
        "  - উভয় Contact ON হলেই Output ON হবে",
        "## Ladder Diagram:",
        "  ——| I0.0 |——| I0.1 |——( Q0.0 )——",
        "## Truth Table:",
        "  - I0.0=0, I0.1=0  →  Q0.0 = 0",
        "  - I0.0=1, I0.1=0  →  Q0.0 = 0",
        "  - I0.0=0, I0.1=1  →  Q0.0 = 0",
        "  - I0.0=1, I0.1=1  →  Q0.0 = 1  ✅",
        "## Real Example:",
        "  - Safety Door Switch AND Start Button → Motor ON",
    ], D, note="AND Logic মানে — সব শর্ত পূরণ হলেই Output চালু হবে।")

    make_content_slide(prs, "Parallel Circuit — OR Logic", [
        "## Circuit Structure:",
        "  - দুটি Contact উপরে-নিচে সংযুক্ত",
        "  - যেকোনো একটি Contact ON হলেই Output ON হবে",
        "## Ladder Diagram:",
        "  ——| I0.0 |——+——( Q0.0 )——",
        "              | I0.1 |",
        "  ————————————+",
        "## Truth Table:",
        "  - I0.0=0, I0.1=0  →  Q0.0 = 0",
        "  - I0.0=1, I0.1=0  →  Q0.0 = 1  ✅",
        "  - I0.0=0, I0.1=1  →  Q0.0 = 1  ✅",
        "  - I0.0=1, I0.1=1  →  Q0.0 = 1  ✅",
        "## Real Example:",
        "  - Push Button 1 OR Push Button 2 → Light ON",
    ], D, note="OR Logic মানে — যেকোনো একটি শর্ত পূরণ হলেই Output চালু হবে।")

    make_practical_slide(prs,
        "Practical Lab: Start-Stop Motor Control",
        "Start Button চাপলে Motor চলবে, Stop চাপলে বন্ধ হবে",
        [
            "Network 1: Start (I0.0) N.O. + Self-Hold (Q0.0) N.O. — Parallel",
            "Network 1: Stop (I0.1) N.C. সিরিজে যোগ করুন",
            "Network 1: Output Coil Q0.0 রাখুন",
            "Compile ও Download করুন",
            "I0.0 = 1 করুন → Q0.0 = 1 (Motor ON)",
            "I0.0 = 0 করুন → Q0.0 = 1 (Self-Hold কাজ করছে!)",
            "I0.1 = 0 করুন → Q0.0 = 0 (Motor STOP)",
        ], D)

    make_summary_slide(prs,
        "Module 03 — Day 4: Contacts & Coils",
        ["N.O. Contact — Bit=1 হলে Pass করে",
         "N.C. Contact — Bit=0 হলে Pass করে",
         "Series = AND Logic",
         "Parallel = OR Logic",
         "Self-Hold Circuit = Latching"],
        "Day 5:\n• Transition Contacts (P, N)\n• Set & Reset Coil\n• SR ও RS Flip-Flop",
        D)

    # ════════════════════════════════════════════════════════
    #  DAY 5  — Advanced Bit Logic
    # ════════════════════════════════════════════════════════
    D = "Module 03  |  Day 5"

    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 03 — Set/Reset, Transition & Flip-Flop",
        "Day 5  |  Beginner Level  |  Duration: 2 Hours",
        RGBColor(0x1A, 0x5C, 0x3A))

    make_agenda_slide(prs, "Day 5 — Agenda", [
        "Positive Transition Contact —|P|— (Rising Edge)",
        "Negative Transition Contact —|N|— (Falling Edge)",
        "NOT Instruction",
        "Set Coil —(S)— ও Reset Coil —(R)—",
        "Immediate Instructions (SI, RI, I, NI)",
        "SR ও RS Flip-Flop",
        "NOP Instruction",
    ], D)

    make_table_slide(prs,
        "Transition Contacts — Edge Detection",
        ["Instruction", "Symbol", "Trigger", "ব্যবহার"],
        [
            ["Positive Transition", "—|P|—", "0→1 এর মুহূর্তে (Rising Edge)",  "Button Press এর মুহূর্তে একবার"],
            ["Negative Transition", "—|N|—", "1→0 এর মুহূর্তে (Falling Edge)", "Button Release এর মুহূর্তে একবার"],
            ["NOT",                 "—|NOT|—","Current Logic State উল্টায়",     "Logic Inversion"],
        ], D, C_ORANGE)

    make_content_slide(prs, "Set & Reset Coil — Latching", [
        "## Output Coil —( )— এর সমস্যা:",
        "  - Rung এ Power না থাকলে Output OFF হয়ে যায়",
        "  - Self-Hold circuit লাগে",
        "## Set Coil —(S)—:",
        "  - একবার ON হলে Power সরিয়ে নিলেও ON থাকে",
        "  - STL: S Qx.x, N (N = কতটি Bit Set হবে)",
        "## Reset Coil —(R)—:",
        "  - ON থাকা Output কে OFF করে",
        "  - STL: R Qx.x, N",
        "## Example:",
        "  - Network 1: Start (I0.0) → S Q0.0, 1",
        "  - Network 2: Stop  (I0.1) → R Q0.0, 1",
        "  - এটাই Latching বা Sealing Circuit",
    ], D, note="Set/Reset Coil ব্যবহার করলে আর Self-Hold Circuit লাগে না — code অনেক পরিষ্কার হয়!")

    make_two_col_slide(prs,
        "SR vs RS Flip-Flop",
        "SR (Set Dominant)",
        ["S1 input = Set করে",
         "R input = Reset করে",
         "S1=1, R=1 হলে → Output = 1 (SET জেতে)",
         "Power failure এর পরও অবস্থা মনে রাখে না",
         "Safety System এ ব্যবহার উপযোগী",
         "যেখানে SET Priority দরকার"],
        "RS (Reset Dominant)",
        ["S input = Set করে",
         "R1 input = Reset করে",
         "S=1, R1=1 হলে → Output = 0 (RESET জেতে)",
         "Emergency Stop system এ ব্যবহার হয়",
         "Safety Critical ক্ষেত্রে উপযোগী",
         "যেখানে RESET Priority দরকার"],
        D, C_RED)

    make_content_slide(prs, "Immediate Instructions — দ্রুত I/O", [
        "## সাধারণ I/O এর সমস্যা:",
        "  - Normal Instruction Scan Cycle শেষে Output Update করে",
        "  - Time-critical application এ এটি সমস্যা হতে পারে",
        "## Immediate Instructions:",
        "  - Scan Cycle wait না করে সাথে সাথে কাজ করে",
        "## Immediate Input —|I|—:",
        "  - Physical Input এর actual অবস্থা সরাসরি পড়ে",
        "## Immediate Output —(I)—:",
        "  - সাথে সাথে Physical Output আপডেট করে",
        "## Set Immediate —(SI)— / Reset Immediate —(RI)—:",
        "  - Immediate Set ও Reset",
        "## কখন ব্যবহার করবেন:",
        "  - High-speed machine, Safety circuit",
    ], D, note="Immediate Instructions ব্যবহারে Scan Cycle এর বাইরেও I/O control সম্ভব।")

    make_summary_slide(prs,
        "Module 03 — Day 5: Advanced Bit Logic",
        ["—|P|— Rising Edge: 0→1 এ একবার fire হয়",
         "—|N|— Falling Edge: 1→0 এ একবার fire হয়",
         "Set: একবার ON — সবসময় ON থাকে",
         "Reset: Set করা Output কে OFF করে",
         "SR = Set Dominant, RS = Reset Dominant"],
        "Day 6:\n• Bit Logic Practical Projects\n• Start-Stop + Self-Hold Review\n• Forward-Reverse Motor Control",
        D)

    # ════════════════════════════════════════════════════════
    #  DAY 6  — Bit Logic Practical
    # ════════════════════════════════════════════════════════
    D = "Module 03  |  Day 6"

    make_title_slide(prs,
        "Siemens S7-200 PLC Programming",
        "Module 03 — Bit Logic: Practical Session",
        "Day 6  |  Lab Day  |  Duration: 2 Hours",
        RGBColor(0x1A, 0x5C, 0x3A))

    make_agenda_slide(prs, "Day 6 — Practical Agenda", [
        "Review: সব Bit Logic Instructions এর Summary",
        "Project 1: Start-Stop Motor (Coil Method)",
        "Project 2: Start-Stop Motor (Set/Reset Method)",
        "Project 3: Forward-Reverse Motor Control",
        "Troubleshooting Tips",
        "Module 03 Quiz",
    ], D)

    make_table_slide(prs,
        "Module 03 — সমস্ত Bit Logic Instructions Summary",
        ["Instruction", "Symbol", "কাজ"],
        [
            ["Normally Open",       "—| |—",    "Bit=1 হলে Pass"],
            ["Normally Closed",     "—|/|—",    "Bit=0 হলে Pass"],
            ["Positive Transition", "—|P|—",    "0→1 Rising Edge"],
            ["Negative Transition", "—|N|—",    "1→0 Falling Edge"],
            ["NOT",                 "—|NOT|—",  "Logic Invert"],
            ["Output Coil",         "—( )—",    "Bit লেখে (Power থাকলে 1)"],
            ["Set Coil",            "—(S)—",    "Latch ON"],
            ["Reset Coil",          "—(R)—",    "Latch OFF"],
            ["Imm. Input",          "—|I|—",    "Scan wait না করে Input পড়ে"],
            ["Imm. Output",         "—(I)—",    "Scan wait না করে Output লেখে"],
            ["SR Flip-Flop",        "SR",        "Set Dominant Latch"],
            ["RS Flip-Flop",        "RS",        "Reset Dominant Latch"],
            ["NOP",                 "NOP",      "কিছু করে না (Placeholder)"],
        ], D, C_GREEN)

    make_practical_slide(prs,
        "Project: Forward-Reverse Motor Control",
        "Forward ও Reverse Button দিয়ে Motor এর দিক নিয়ন্ত্রণ",
        [
            "I/O Assignment: I0.0=FWD Button, I0.1=REV Button, I0.2=STOP",
            "Q0.0=Forward Contactor, Q0.1=Reverse Contactor",
            "Network 1: FWD (I0.0) + ~REV Running (Q0.1 N.C.) + STOP (I0.2 N.C.) → S Q0.0",
            "Network 2: REV (I0.1) + ~FWD Running (Q0.0 N.C.) + STOP (I0.2 N.C.) → S Q0.1",
            "Network 3: STOP (I0.2) → R Q0.0, 1  এবং  R Q0.1, 1",
            "Interlock গুরুত্বপূর্ণ: Q0.0 ও Q0.1 একসাথে ON হওয়া উচিত নয়!",
            "Compile, Download, Test করুন",
        ], D)

    make_summary_slide(prs,
        "Module 03 — Bit Logic: Complete",
        ["১৩টি Bit Logic Instruction সম্পন্ন",
         "Series (AND) ও Parallel (OR) Circuit তৈরি করতে পারি",
         "Self-Hold ও Set/Reset দুই পদ্ধতি জানা হয়েছে",
         "Edge Detection (P, N) ও Immediate I/O জানা হয়েছে",
         "Forward-Reverse Motor Control তৈরি করা হয়েছে"],
        "Day 7 (Module 04):\n• Timer Instructions শুরু\n• TON, TONR, TOF বিস্তারিত\n• Automatic ON/OFF Circuit",
        D)

    save(prs, "Module_03_Bit_Logic_Day4-6.pptx")

if __name__ == "__main__":
    build()
