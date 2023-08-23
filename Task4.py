"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def find_telem_calls(calls):
    phone_calls = []
    for call in calls:
        if call[0] not in phone_calls:
            phone_calls.append(call[0])


""" TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telem_numbers = set()
reg_numbers = set()

for i in texts:
    reg_numbers.add(i[0])       
    reg_numbers.add(i[1])
for i in calls:
    telem_numbers.add(i[0])
    reg_numbers.add(i[1])
telem_numbers = sorted(list(telem_numbers - reg_numbers))


print("These numbers could be telemarketers: ")
print(*telem_numbers, sep='\n')
