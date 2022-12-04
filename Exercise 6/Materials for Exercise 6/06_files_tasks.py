# -*- coding: utf-8 -*-
"""
Author -- Michael Widrich, Van Quoc Phuong Huynh, Andreas Schörgenhumer
Contact -- schoergenhumer@ml.jku.at
Date -- 29.07.2022

################################################################################

The following copyright statement applies to all code within this file.

Copyright statement:
This material, no matter whether in printed or electronic form, may be used for
personal and non-commercial educational use only. Any reproduction of this
manuscript, no matter whether as a whole or in parts, no matter whether in
printed or in electronic form, requires explicit prior acceptance of the
authors.

################################################################################

Tasks for self-study. Try to solve these tasks on your own and compare your
solutions to the provided solutions file.
"""

import glob
import os

#
# Task 1
#

# Create a File "my_file.txt" and write some text to it. Then, open it again and
# append some text. Finally, open it only to read all the content and print it
# to the console. Use "with" blocks to open the files.

with open("my_file.txt", "w", encoding = "utf-8") as f:
    f.write("hello")

with open("my_file.txt", "a", encoding = "utf-8") as f:
    print("\nthis is a new line", end="#", file=f)

with open("my_file.txt", "r", encoding = "utf-8") as f:
    content_as_str = f.read

#
# Task 2
#

# Use the "glob" module to print a list of all files ending in ".txt" in the
# current working directory and all subdirectories. Also use the "os" module
# when joining paths.

glob.glob("**" "*.txt" recursive = True)

#
# Task 3
#

# Write a function that can write 2D nested lists/matrices (parameter 1) to a
# CSV file (parameter 2). As delimiter (parameter 3), a comma should be used by
# default. Optionally, matrix column names can be specified (parameter 4), which
# must then also be written to the CSV file as the first row. The character
# encoding should be hard-coded as UTF-8. You do not have to perform any error
# checking in this task like checking if the number of column names matches the
# number of columns in the specified matrix.
example_matrix = [
    [1, 10, 9, 12],
    [3, 10, 3, 10],
    [7, 14, 5, 28]
]

def write_matrix(matrix: list[list], path: str, delimiter: str = ",", header: list = None):
    if header is not None:
        matrix.insert(0, header)
    with open(path, "w", encoding = enc) as f:
        for row in matrix:
            f.write(delimiter.join(str(elem) for elem in row))
            f.write("\n")

# Task 4
#

# Write a function that can read CSV files (parameter 1) as produced by task 3
# (see above) and returns the data as a 2D nested list. The list elements can
# stay strings, i.e., no data type conversion is needed. A boolean flag should
# indicate whether the file contains column names in the first row, which should
# be False by default (parameter 2). If True, the column names (as list) should
# be returned in addition to the 2D nested list, i.e., a 2-tuple should be
# returned. The encoding should be UTF-8 by default (parameter 3).

def read_matrix(path: str, extract_header: bool = False, delimeter: str= ",", enc = "uft-8"):
    with open(path, "r") as f:
        if extract_header:
            header = f.readline() [:-1]
            header = header.split(delimeter)
        matrix = [line [:-1].split(delimeter) for line in f.readlines()]
    return (header, matrix) if extract_header else matrix

