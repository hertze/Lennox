#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import sys
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

filename = ""

if len(sys.argv) < 2:
    while (len(filename) == 0 ): 
        filename = raw_input("\n> Filename? ")
else:
    filename = sys.argv[1]

output = PdfFileWriter()
input1 = PdfFileReader(open(filename, "rb"))

total_n = input1.getNumPages()

rest = (( total_n / 4 ) * 4 + 4) - total_n

q = total_n + rest

print "%d pages in file.\n" % total_n

n = 0

while n < q:
    if n < total_n:
        output.addPage(input1.getPage(n))
    if n + 2 < total_n:
        output.addPage(input1.getPage(n+2))
    if n + 3 < total_n:
        output.addPage(input1.getPage(n+3))
    if n + 1 < total_n:
        output.addPage(input1.getPage(n+1))
    n = n + 4


# finally, write "output" to document-output.pdf
outputStream = file("treesaver-output.pdf", "wb")
output.write(outputStream)

print "Output written to *treesaver-output-pdf\n"

latex = "\\documentclass[11pt,titlepage]{article}\n\n\\usepackage{pdfpages}\n\n\\begin{document}\n\n\\includepdf[pages=-, landscape, noautoscale, nup=1x2]{treesaver-output.pdf}\n\n\\end{document}"

f = open("mounted-file.tex", "w")
f.write(latex)

print "LaTeX-file written to *mounted-file.tex*\nDone!"
