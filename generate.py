#!/usr/bin/env python

import hashlib
import binascii
import base64
import string
import sys

__std2nsec3 = string.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567',
    '0123456789abcdefghijklmnopqrstuv'
)

if len(sys.argv) < 4:
    sys.exit('Usage:   ' + sys.argv[0] + ' <domain> <salt> <iterations>\nExample: ' + sys.argv[0] + ' foo.bar.example.com c0ffee 5')

domain     = sys.argv[1]
salt       = sys.argv[2]
iterations = sys.argv[3]

lsalt = int(len(salt))

tmp = domain.split('.')
toHash = ''
# all dots get replaced by the length (in byte) of the following string
for i in tmp:
    toHash += chr(len(i))
    toHash += i
#append a NULL byte following with the salt(as bytes)
toHash += '\0' + binascii.a2b_hex(salt)

#initial hashround
hash = hashlib.sha1(toHash).digest() + binascii.a2b_hex(salt)
#hash it again with number of iterations
for i in range(int(iterations)):
    # salt gets appended in each iteration
    hash = hashlib.sha1(hash).digest() + binascii.a2b_hex(salt)
print base64.b32encode(hash[:-lsalt/2]).translate(__std2nsec3, '=')
