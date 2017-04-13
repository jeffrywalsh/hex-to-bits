# hex-to-bits
A simple script to display hex to binary (bits) to quickly allow reading of an error displayed in hex.

## Requirements
This requires python 2.7 and the argparse module.

## What to expect
```
$ python2.7 hex_to_bits.py f2abcde
1111 0010 1010 1011 1100 1101 1110
f    2    a    b    c    d    e
Bit: 27    set
Bit: 26    set
Bit: 25    set
Bit: 24    set
Bit: 21    set
Bit: 19    set
Bit: 17    set
Bit: 15    set
Bit: 13    set
Bit: 12    set
Bit: 11    set
Bit: 10    set
Bit: 7    set
Bit: 6    set
Bit: 4    set
Bit: 3    set
Bit: 2    set
Bit: 1    set
f     1111    27:24
2     0010    23:20
a     1010    19:16
b     1011    15:12
c     1100    11:8
d     1101    7:4
e     1110    3:0
```
