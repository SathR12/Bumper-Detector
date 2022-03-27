import csv
import sys

def parser(num):
    with open('rapid_reacts_data.csv') as frc:
        csv_parser = csv.reader(frc, dialect = 'excel', delimiter = ',')
        line = 0
        for each_row in csv_parser:
            if line == 0:
               line += 1
            
            else:
                if each_row[0] == num:
                    return(f"team number: {each_row[0]}, average climb: {each_row[1]}, shooting: {each_row[2]}, defense: {each_row[3]}")
                    line += 1
                
 
    
