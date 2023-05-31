"""
COMMANDS
infile = open('filename.txt', 'r')      //Close at end w/ infile.close()
outfile = open('filename.txt', 'w')     //Close at end w/ outfile.close()
appendfile = open('filename.txt', 'a')  //Close at end w/ outfile.close()
lines = infile.readLines()

splitline = line.split(None) //None splits on spaces
"""


"""
Input: Json Data
Output: Python dictionary / arrays / etc
Example Use: JSON file with 100 Pokemon objects with 3 move fields, becomes a Python array len 100 of arrays len 3

Variables: fields per line
"""

"""
Input: Data in the form X Y Z
Output: Data in the form { "x": ("y, "Z")}
"""
