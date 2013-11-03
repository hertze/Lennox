Lennox
======

## A tree-saving script for duplex PDF-printing of two A5 pages on one A4.

I find it difficult to explain this in words. This script takes a PDF-file in A5 format, rearranges the pages and glues them together in twos. When you duplex-print the resulting A4-sized PDF you only have to cut the resulting paper stack in half and put the left half on top of the right one to find all pages in order.

This saves trees and patience, I believe.

## Usage

This is a command-line utility, written in Python 2.7.

Run in like so:

`python lennox.py`

for a minimal interface, or simply:

`python lennox.py <file.pdf>`

for no interface at all.

I hole-heartedly recommend running this script from an Automator print plugin, though.
