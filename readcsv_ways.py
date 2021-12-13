import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file,delimiter = ',') # returns csv reader object
    for row in reader:
        print(row)

'''

import csv
with open("people.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

#{'Name': 'Jack', ' Age': ' 23', ' Profession': ' Doctor'}
#{'Name': 'Miller', ' Age': ' 22', ' Profession': ' Engineer'}


import pandas as pd
pd.read_csv("people.csv")



'''