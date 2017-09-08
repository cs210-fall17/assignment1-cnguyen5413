"""
Christopher Nguyen
CSC 210, Section 1A
echo.py

This program mimics the echo command on cygwin
"""

import sys

def main():
  
  if(len(sys.argv) > 1):
    arg = [x for x in sys.argv[1:]]
    sys.stdout.write(" ".join(arg))

main()
