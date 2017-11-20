# RAKESH HARISH
# 800984018

# *******************************************************************************************
# * @File          decomp.py
# *
# * @Title         Implementation of LZW Decoding
# *
# * @Author        Rakesh Harish
# *
# * @Created       03/10/2017
# *
# * @Description   This code implements the Decoding/Decompressing part of the LZW Algorithm.
# *
# *******************************************************************************************

print('### LZW Decompression ###')

import sys
import io

# Fetch the encoded file as the input file and read the input
ifile = sys.argv[1]

file = io.open(ifile, 'r', encoding = 'UTF-16BE')
arr = file.read()

# Get the bit length from the user
bit_length = sys.argv[2]

if (int(bit_length) < 9) or (int(bit_length) > 16):
    print ("********************THE BIT LENGTH NEEDS TO BE IN THE RANGE OF 9 to 16!*********************** \n**********************************ENTER THE BIT LENGTH AGAIN**********************************")
    exit
else:
	bl = int (bit_length)
	
MAX_TABLE_SIZE = 2 ** (bl)

# Initialise the table
table = []
for i in range(0,256):
    table.append(chr(i))
last = 256

result = []
STRING = table[ord(arr[0])]								# The first code is popped out and assigned to STRING
result.append(table[ord(STRING)])

for j in range(1,len(arr)):								# Get input while there are codes are left to be received
    if ord(arr[j]) >= len(table):						# Check if the Decoder has codes to decode
        entry = STRING + STRING[0]
    else:
        entry = table[ord(arr[j])]
    result.append(entry)								# Output the new string
    if len(table) < MAX_TABLE_SIZE:						# Check if the Table is not full
        table.append(STRING + entry[0])
    STRING = entry	
j+=1
print('\nDecompressed Output is:\n'+''.join(result))  	# Output the String

# Request the user for the output filename and path

ofile = ifile.split(".")[0]+"_decoded"+".txt"
lzwd = open(ofile,'w')                       			# Open file to write
lzwd.write(''.join(result))
lzwd.close()                            				# Close the output file
file.close()											# Close the input file

print('\nEND OF PROGRAM - Decompressed output file saved in the specified path!')
