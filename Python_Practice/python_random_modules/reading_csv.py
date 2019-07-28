import csv

with open('details.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'the available coloumns are : {" , ".join(row)}')
            line_count += 1
        else:
            print(f'\t {row[0]} age is {row[1]} and date of birth is {row[2]}.')
            line_count += 1



