Lennox
======

## A tree-saving script for duplex printing

This script takes a PDF-file in A5 format, rearranges the pages and glues them together in twos. When you duplex-print the resulting A4-sized PDF you only have to cut the resulting paper stack in half and put the left half on top of the right one to find all pages in order.

This saves trees and patience, I believe.

## Usage

This is a command-line utility, written in Python 2.7. Before you use it, you need to specify the working directory for the script (I suggest the same folder as you have put the script itself in) and the path to a PDF with blank pages (*blank-a5.pdf*, included with the script). The script is dependent on [PyPDF2](https://github.com/mstamy2/PyPDF2).

Run it like so:

`python lennox.py`

for a minimal interface, or simply:

`python lennox.py <file.pdf>`

for no interface at all.

For maximum usefulness (if you are a Mac OS X user) I recommend using running this script from an Automator print plugin. You may then run it on any document presented in the standard print dialog.
