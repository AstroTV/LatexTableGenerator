#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 22:16:44 2020

@author: thomas
"""

from tkinter import filedialog
from tkinter import Tk
import os
import csv

cwd = os.getcwd()
root = Tk()

filename = filedialog.askopenfilename(initialdir=cwd, title="Select file", filetypes=(
    ("csv files", "*.csv"), ("all files", "*.*")))
root.update()
print(filename)
root.destroy()

rows = []

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        rows.append(row[0].split(';'))


n_rows = len(rows)
n_cols = max([len(row) for row in rows])

out = "\\begin{table}[H]\n"
out += "\\centering\n\\begin{tabular}{"
out += "|c" * n_cols
out += "|}\n\\hline\n"
out += "TODO & " * (n_cols-1) + "TODO \\\\ \\hline\n"
for row in rows:
    for el in row[:-1]:
        out += el + " & "
    out += row[-1]
    out += " \\\\ \\hline \n"

out += "\\end{tabular}\n"
out += "\\caption{TODO}\n"
out += "\\label{tab:TODO}\n"
out += "\\end{table}"

with open("output.txt", "w") as f_out:
    f_out.write(out)
print(out)
