import argparse
import re

parser = argparse.ArgumentParser(description='bits of a hex')
parser.add_argument('hex', help='a hex to bitamize')


args = parser.parse_args()
hex_data = args.hex
if re.search(r'^[0-9A-Fa-f]+$', hex_data) is None:
  print("Your hexadecimal is not valid.")
  print("Please put in the form of: f20000000200008f")
  quit()

def hex_to_bin(hexed):
  num_of_bits = len(hexed)*4
  return bin(int(hexed, 16))[2:].zfill(num_of_bits)

def splitAt(w,n):
  for i in range(0,len(w),n):
    yield w[i:i+n]


my_bin=hex_to_bin(hex_data)

#print("hexadecimal: {}".format(hex_data))
#print("binary: {}".format(my_bin))
print(" ".join(splitAt(my_bin,4)))
print("    ".join(splitAt(hex_data,1)))

len_bin=len(my_bin)
count=len_bin-1

for i in my_bin:
  if i == "1":
    print("Bit: {}\tset".format(count))
  count = count - 1
    
for i in hex_data:
  binned=hex_to_bin(i)
  print("{} \t{}\t{}:{}".format(i,binned,len_bin-1,len_bin-4))
  len_bin=len_bin-4
  
  
  