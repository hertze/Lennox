#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

# Get the filename

filename = ""

if len(sys.argv) < 2:
    while (len(filename) == 0 ): 
        filename = raw_input("\n> Filename? ")
else:
    filename = sys.argv[1]

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
        output.addPage(input2.getPage(1))

outputStream = file("appended.pdf", "wb") # Write the appended file
output.write(outputStream)
outputStream.close()

# Now, let's rearrange that newly-saved PDF

output = PdfFileWriter()
input3 = PdfFileReader(open("appended.pdf", "rb"))  

print "%d pages in file.\n" % total_n

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
outputStream = file("treesaver-output.pdf", "wb")
output.write(outputStream)
outputStream.close()

print "Output written to *treesaver-output-pdf\n"

latex = "\\documentclass[11pt,titlepage,a4paper]{article}\n\n\\usepackage{pdfpages}\n\n\\begin{document}\n\n\\includepdf[pages=-, landscape, noautoscale=false, nup=1x2]{treesaver-output.pdf}\n\n\\end{document}"

f = open("mounted-file.tex", "w")
f.write(latex)

print "LaTeX-file written to *mounted-file.tex*\nDone!"
