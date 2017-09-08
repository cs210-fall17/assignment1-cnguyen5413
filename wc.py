"""
Christopher Nguyen
CSC 210, Section 1A
wc.py
This program imitates the wc command on cygwin
"""

import sys

def main():
  
  file = (open(sys.argv[-1]))
  new_lines = 0
  words = 0
  bits = 0
  
  for line in file.readlines():
    words += len(line.split())
    new_lines += 1
    bits += len(line)
  
  if(sys.argv[1] == "-w"):
    sys.stdout.write(str(words))
  elif(sys.argv[1] == "-b"):
    sys.stdout.write(str(bits))
  elif(sys.argv[1] == "-n"):
    sys.stdout.write(str(new_lines))
  else:
    sys.stdout.write(str(new_lines) + " " + str(words) + " " + str(bits))


main()
