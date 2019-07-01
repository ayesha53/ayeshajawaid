import csv
with open('data.csv' , 'r') as fdr:
    students = csv.reader(fdr)
    for student in students:
        print(student)
