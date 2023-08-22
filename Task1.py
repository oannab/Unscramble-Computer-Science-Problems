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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def counting():
    numCount = []
    for num in texts:
        numCount.append(num[0])
        numCount.append(num[1])
    for no in calls:
        numCount.append(no[0]) 
        numCount.append(no[1])   
    
    result = set(numCount) # transform list to set to remove duplicates

    return(len(result))      

print(f"There are {counting()} different telephone numbers")
