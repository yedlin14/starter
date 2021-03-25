import csv
import random

iterations =int(input("How many groups? : "))

with open('123.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar=',')
 # Following command skips the first row of the CSV file.

 fields = next(data)
 for row in data:
   print(', '.join(row))

rows=data.line_num
print('row: %d'%(rows))
groups=4
print('group: %d'%(groups))

number_exists=[]
count=0
count_groups=0
groups_id=1

while count <= rows:
    rnd = random.randint(0, rows)
    if rnd in number_exists:
        continue
    else :
        number_exists.append(rnd)
        count=count+1

print(number_exists)

for x in number_exists:
    if count_groups <= groups:
        print('Group : %d -->  Student id : %d '%(groups_id,number_exists[x]))

        count_groups=count_groups+1
    else:
        count_groups=0
        groups_id=groups_id+1