# Lossless-data-compression-using-Lempel-Ziv-Welch-LZW-algorithm
The Lempel–Ziv–Welch (LZW) algorithm is a lossless data compression algorithm. LZW is an adaptive compression algorithm that does not assume prior knowledge of the input data distribution. This algorithm works well when the input data is sufficiently large and there is redundancy in the data


**************************************
*  LEMPEL–ZIV–WELCH (LZW) ALGORITHM  *
**************************************
Author: RAKESH HARISH 
49er ID: 800984018

* Introduction
* File List
* Design/Implementation
* Usage Instructions
* References


I. INTRODUCTION
---------------

The Lempel–Ziv–Welch (LZW) algorithm is a lossless data compression algorithm.

LZW is an adaptive compression algorithm that does not assume prior knowledge
of the input data distribution. This algorithm works well when the input data
is sufficiently large and there is redundancy in the data.

Two examples of commonly used file formats that use LZW compression are the
GIF image format served from websites and the TIFF image format. LZW compression
is also suitable for compressing text files, and is the algorithm in the
compress Unix file compression utility.

This algorithm has two modules:
1. Encoding/Compressing
2. Decoding/Decompressing


II. FILE LIST
-------------
* comp.py		source code for Compression/Encoding inside LZW Folder
* decomp.py		source code for Decompression/Decoding inside LZW Folder
* lzwr.txt		example input file
* lzwr.lzw		example compressed output of comp.py
* lzwr_decoded.txt	example decompressed output of decomp.py
* README.txt		

III. DESIGN/IMPLEMENTATION
-------------------


A.  Data Structure

	The Data Struture used is Lists. Dynamically increasing array...

	Reason for using is because it is a most versatile datatype available in Python and a dynamic data structure.
	The items in a list need not be of the same type. And moreover, the lists can be concatenated, sliced and so on. 
	As a list is a sequentially ordered and sequentially searched ADT (Abstract Data Type) it can efficiently utilize the memory, 
	and hence I preferred using this over Hashtables or any other.

B. Encoder:

	i. Psuedo Code -

	MAX_TABLE_SIZE=2(bit_length) //bit_length is number of encoding bits
	initialize TABLE[0 to 255] = code for individual characters
	STRING = null
	while there are still input symbols:
	SYMBOL = get input symbol
	if STRING + SYMBOL is in TABLE:
	STRING = STRING + SYMBOL
	else:
	output the code for STRING
	If TABLE.size < MAX_TABLE_SIZE: // if table is not full
	add STRING + SYMBOL to TABLE // STRING + SYMBOL now has a code
	STRING = SYMBOL
	output the code for STRING
	

	ii. Design of Code - 
	
	STEP1:	Start with importing the sys module of Python which is needed for the access to variables used by interpreter and to functions to interact with interpreter.
	STEP2:	To read the code file, input file and bit length, arguments are required. sys.argv does that work.
	STEP3: 	Initialize dictionary to contain one entry for each byte with range 255. Initialize the encoded string with the first byte of the input stream. 
	STEP4: 	Further move into the logic of the LZW; Start a loop - a FOR loop is used to check if there are input symbols coming in.
	STEP5: 	Initialise an IF loop to see if String and Symbol (SS) in the table? 
		If concatenating the byte (SS) to the encoded string gives a string that's in the table, then concatenate the the byte to the encoded string (STRING). 
		And then check for incoming symbols.
	STEP6:	Else, If concatenating the byte (SS) to the encoded string produces a string that is not in the table;	
		the add the new sting to the dictionary using result.append(table.index(STRING))... 
	STEP7:	Next check if the Table is not full? by checking the 2^bit length input we would have given at the start.
		If so, append the table with STRING and SYMBOL. Assign Symbol to String then. String contains the output...
	STEP8: 	To encode the output, we need the output as char; so the FOR loop - CODE...
		Take the file input name without extension and concatenate .lzw to it. Write the output to that file in UTF-16BE format. Close the files.
	

C.  Decoder

	i. Psuedo Code - 

	MAX_TABLE_SIZE=2(bit_length)
	initialize TABLE[0 to 255] = code for individual characters
	CODE = read next code from encoder
	STRING = TABLE[CODE]
	output STRING
	while there are still codes to receive:
	CODE = read next code from encoder
	if TABLE[CODE] is not defined: // needed because sometimes the
	NEW_STRING = STRING + STRING[0] // decoder may not yet have code!
	else:
	NEW_STRING = TABLE[CODE]
	output NEW_STRING
	if TABLE.size < MAX_TABLE_SIZE:
	add STRING + NEW_STRING[0] to TABLE
	STRING = NEW_STRING
	

	ii. Design of Code - 
	
	STEP1:	Start by import the required modules - sys and io [io: for encoding the input file we need this while using open()].
	STEP2:	To read the code file, input file and bit length, arguments are required. sys.argv does that work. 
	STEP3:	As in the Encoder, Initialized dictionary to contain one entry for each byte with range 255. 
	STEP4:	Coming to the Decoder logic steps; to start with the first code from the input file is popped out and assigned to a variable named STRING.
		Append it to the table. Then by using FOR loop, read the next code word from the input stream.
	STEP5:	Firstly check if there is code to read. If not available, just concatenate STRING + STRING[0] and add it to a variable "entry".
		Else, read the code from input stream till EOF.
	STEP6:	Next check if the Table is not full; and concatenate the first character in the new code word to the string produced by the previous code word 
		and add the resulting string to the table by using table.append command - concatenating STRING and entry... FOR loop continues till length of input -> (arr)
	STEP7:	Output the result. Take the file input name without extension and concatenate _decoded and .txt to it. 
		Write the output to that file. Close the files.

D. Summary

	As given in the project requirements [Project1-2 PDF], the algorithm is programmed such a way that this application cannot encode/decode a file with a bit length larger than 16 and lesser than 9.
	
	Programing language used:
	Python. Version: 2.7 [Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32]

	IDE used:
	PyCharm 2016.3.2
	Build #PY-163.10154.50, built on December 28, 2016
	Licensed to PyCharm Evaluator
	Expiration date: March 19, 2017
	JRE: 1.8.0_112-release-408-b6 x86
	JVM: OpenJDK Server VM by JetBrains s.r.o


IV. USAGE INSTRUCTIONS

>	Pre Requisites:	Python. Version: 2.7 [Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32]
			
			Place the .py files and the input file in the same folder and open the CMD from that folder (cd to that folder).

>	Compression: The .py file can be run from the command line prompt from the folder where the files are placed by providing the following command: 
	python <filename>.py <inputfile>.txt <bit_length>

			EXAMPLE: python comp.py input.txt 12

	The Compressed Output file will be created in the same location as the input file with <inputfile>.lzw in 16bit format. EXAMPLE: input.lzw

>	Decompression: Similarly for Decompression, we can take the compressed output file in .lzw format as its input and rest of the command will be the same format.

			EXAMPLE: python decomp.py input.lzw 12

	The Decompressed Output file will be created in the same location as the Compressed input file with <inputfile_decoded>.txt format. EXAMPLE: input_decoded.txt


V. REFERENCES
--------------

1. https://en.wikipedia.org/wiki/Lempel–Ziv–Welch
2. https://en.wikipedia.org/wiki/Binary-to-text_encoding
3. https://youtu.be/j2HSd3HCpDs
4. https://uncc.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=05c0b32e-b354-4859-ade7-4df6ed6ba50b 
5. PDF - Project1-2
