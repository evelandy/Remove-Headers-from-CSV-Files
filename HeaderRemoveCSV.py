#!/usr/bin/env python3
"""evelandy/W.G.
Nov. 3, 2018 7:31pm
Remove-Headers-from-CSV-Files
Python36-32
Removes Headers from .CSV files
"""
import csv
import os


# This makes a new folder in the directory that you input and leaves the one there if one exists
directory = input("Enter the directory for your .csv files: ")  # Enter full path for the directory w/ no quotes
os.makedirs(directory, exist_ok=True)

# Loops through the files in the directory and skips the non .csv files
for csv_file in os.listdir('.'):
    if not csv_file.endswith('.csv'):
        continue
    print("Working on {}".format(csv_file))  # Prints the finished header removal of each file

    # Reads through the .csv file leaving out the first row
    csv_rows = []
    with open(csv_file) as csv_obj:
        reader_obj = csv.reader(csv_obj)
        for row in reader_obj:
            if reader_obj.line_num == 1:
                continue
            csv_rows.append(row)

    # Write out the csv file
    with open(os.path.join('headerRemove', csv_file), 'w', newline='') as csv_obj:
        csv_writer = csv.writer(csv_obj)
        for row in csv_rows:
            csv_writer.writerow(row)
