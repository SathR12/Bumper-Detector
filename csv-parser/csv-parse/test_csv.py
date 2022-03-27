import csv
import sys


with open('rapid_reacts_data.csv') as frc:
    csv_parser = csv.reader(frc, dialect = 'excel', delimiter = ',')
    line = 0
    for each_row in csv_parser:
        if line == 0:
            print("Data table for FRC")
            line += 1
        else:
            print(f"team number: {each_row[0]}, average climb: {each_row[1]}, shooting: {each_row[2]}, defense: {each_row[3]}")
            line += 1
                

 
    
