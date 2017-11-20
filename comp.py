# RAKESH HARISH
# 800984018

# *******************************************************************************************
# * @File          comp.py
# *
# * @Title         Implementation of LZW Encoding
# *
# * @Author        Rakesh Harish
# *
# * @Created       03/10/2017
# *
# * @Description   This code implements the Encoding/Compressing part of the LZW Algorithm.
# *
# *******************************************************************************************
print('### LZW Compression ###')

# Import the sys module - for access to variables used by interpreter and to functions to interact with interpreter

import sys

# Fetch the input file and read the input

ifile = sys.argv[1]

file = open(ifile, 'r')
inputstring = file.read()
print('\nInput is:\n'+ inputstring)

# Get the bit length from the user
# bit_length is number of encoding bits

bit_length = sys.argv[2]

if (int(bit_length) < 9) or (int(bit_length) > 16):
    print ("***************THE BIT LENGTH FOR ENCODING NEEDS TO BE IN THE RANGE OF 9 to 16!*************** \n**********************************ENTER THE BIT LENGTH AGAIN**********************************")
    exit
else:
	bl = int (bit_length)

MAX_TABLE_SIZE = 2 ** bl

# Initialise the table
table = []
for i in range(0,256):
    table.append(chr(i))
last = 256

STRING = ""
result = []

for SYMBOL in inputstring:
    SS = STRING + SYMBOL    # Get input symbol while there are input symbols left
    if SS in table:    		# SS is in the table
        STRING = SS
    else:
        result.append(table.index(STRING))     # Output the code for String
        if len(table) < MAX_TABLE_SIZE:        # Check if the Table is not full
            table.append(STRING + SYMBOL)
        STRING = SYMBOL
result.append(table.index(STRING))             # Output the String

y=""
for CODE in result:
    y+=unichr(CODE)

print('\nCompressed Output is:\n'+str(result))

# Save the compressed output to a .lzw file in 16bit encoded format

ofile = ifile.split(".")[0]+".lzw" 
lzwc = open(ofile,'wb')            		# open file to write in binary
lzwc.write(y.encode("UTF-16BE"))        # Encode to 16 Bit format by using UTF-16 Big Endian command; and save this to the output file
lzwc.close()                            # close the output file
file.close()							# close the input file

print('\nEND OF PROGRAM - Compressed output file saved in the specified path!')
