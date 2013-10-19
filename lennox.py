#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

# Get the filename

filename = ""

if len(sys.argv) < 2:
    print ("\nThis is L E N N O X")
    print ("\n---------------------------------------------------------\n")
    print ("\nHello,\n")
    while (len(filename) == 0 ):
        filename = raw_input("What file shall I work with? ")
else:
    filename = sys.argv[1]
    
filenamecomps = filename.partition(".")
filetitle = filenamecomps[0] # Lets find out the name before the first period

output = PdfFileWriter()
input1 = PdfFileReader(open(filename, "rb"))
input2 = PdfFileReader(open("blank-a5.pdf", "rb")) # blank pages

# Let's check the file

total_n = input1.getNumPages()
rest = (( total_n / 4 ) * 4 + 4) - total_n # How much to add to get even quadruples?
q = total_n + rest
midpoint = q / 2

# Add blank pages to get complete quadruples
for num in range(input1.getNumPages()):
        output.addPage(input1.getPage(num))
for num in range(0, rest):
        output.addPage(input2.getPage(0))

outputStream = file("temp-1.pdf", "wb") # Write the appended file
output.write(outputStream)
outputStream.close()

# Now, let's rearrange that newly-saved PDF

output = PdfFileWriter()
input3 = PdfFileReader(open("temp-1.pdf", "rb"))  

print "\nThere are %d pages in this file.\n" % total_n

print "\nRearranging..."

# We'll divide the PDF in two stacks, where the first stack gets printed on the left side of the physical paper and the second stack on the right side.

n = 0 # Stack 1 start here
m = midpoint # Stack two starts here
    
while n < midpoint:
    # Frontpage, firststack
    output.addPage(input3.getPage(n))
    
    # Frontpage, second stack
    output.addPage(input3.getPage(m))
    
    # Flipside, second stack (since this is the flipside of the physical paper)
    output.addPage(input3.getPage(m + 1))
    
    # Flipside, first stack
    output.addPage(input3.getPage(n + 1))
    
    n = n + 2
    m = m + 2


# finally, write "output" to document-output.pdf
outputStream = file("temp-2.pdf", "wb")
output.write(outputStream)
outputStream.close()

print "\nDone."

print "\nWriting LaTeX..."

latex = "\\documentclass[11pt,titlepage,a4paper]{article}\n\n\\usepackage{pdfpages}\n\n\\begin{document}\n\n\\includepdf[pages=-, landscape, noautoscale=false, nup=1x2]{temp-2.pdf}\n\n\\end{document}"

f = open("temp-3.tex", "wb")
f.write(latex)
f.close()

print "\nDone."

print "\nTypesetting..."

os.system("xelatex temp-3.tex")
print ("\nDone.")
os.system("mv temp-3.pdf " + filetitle + "-lennoxed.pdf") # Rename temp-file to real filename
os.system("open " + filetitle + "-lennoxed.pdf") # Open the resulting PDF
print "\nCleaning up..."
os.system("rm temp*.*") # Delete all temp files
print "\nAll done. Have a nice day!"
