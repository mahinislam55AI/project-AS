"""Master runner — generates all PPTX files"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

print("=" * 60)
print("  S7-200 PLC Course — PowerPoint Generator")
print("=" * 60)

import module_01_02; module_01_02.build()
import module_03;    module_03.build()
import module_04_05; module_04_05.build()
import module_06_07; module_06_07.build()
import module_08_09; module_08_09.build()
import module_10_12; module_10_12.build()
import module_13_15; module_13_15.build()
import module_16_18; module_16_18.build()

print("=" * 60)
print("  All slides generated successfully!")
print("=" * 60)
