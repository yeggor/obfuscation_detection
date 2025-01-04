#!/usr/bin/python
import sys

import binaryninja
from obfuscation_detection import detect_crypto

# check file arguments
if len(sys.argv) < 2:
    print("[*] Syntax: {} <path to binary>".format(sys.argv[0]))
    exit(0)

# parse arguments
file_name = sys.argv[1]

# init binary ninja
with binaryninja.load(file_name) as bv:
    if not file_name.endswith(".bndb"):
        bv.update_analysis_and_wait()

    # look for obfuscation heuristics
    detect_crypto(bv)
