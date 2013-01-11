#!/usr/bin/env python

import sys
import base64
import binascii
import string

# This script converts the output from the nsec3walker tool to a hashkill input file
# Usage: ./convert.py < inputFile > outputFile

name = set()
salt = ''
iterations = 0

__nsec32std = string.maketrans(
    "0123456789abcdefghijklmnopqrstuv",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
)

for line in sys.stdin:
  tmp = line.strip().split()
  if tmp[0] == "domain":
    domain = tmp[1]
  elif y[0] == "salt":
    salt = tmp[1]
  elif tmp[0] == "iterations":
    iterations = tmp[1]
  elif tmp[0] == "nexthash":
    name.add(tmp[1])
    name.add(tmp[2])


for i in name:
  hash = binascii.b2a_hex(base64.b32decode(i.translate(__nsec32std, "=")))
  print str(iterations) + ":" + domain + ":" + hash + ":" + salt
