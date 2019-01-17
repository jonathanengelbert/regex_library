import csv
import re
import datetime

print("SCRIPT RUNNING...")

def transform_address_type (address):
  #REGEX LIBRARY
  case_mapping = {'st': 'street',
                  'ave': 'avenue',
                  'sq': 'square',
                  'pl': 'plaza',
                  'w' : 'west',
                  'e' : 'east',
                  's' : 'south',
                  'n' : 'north'
                  }

  case_list = ['st', 'ave', 'pl', 'sq', 'w', 'e', 's', 'n']

  #REGEX LIST
  cases = (r'\b(?:%s)\b' % '|'.join(case_list))

   
  return (re.sub(cases, lambda x: case_mapping[x.group()], address[0].lower().strip())).title()


lines = []

with open("./add.csv", newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    row[0] = transform_address_type(row)
    lines.append(row)
  
writer = csv.writer(open('./output.csv', 'w', newline=''))
writer.writerows(lines)

print(len(lines))


print("SCRIPT FINISHED SUCCESSFULLY AT ", datetime.datetime.now())
