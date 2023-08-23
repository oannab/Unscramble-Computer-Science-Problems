"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:"""


phone = {}

for call in calls:
    if call[0] not in phone:
        phone[call[0]] = 0
    phone[call[0]] += int(call[3])

    if call[1] not in phone:
        phone[call[1]] = 0
    phone[call[1]] += int(call[3])

longest_phone = max(phone, key=phone.get)
longest_time = phone[longest_phone]
       

print(f"{longest_phone} spent the longest time, {longest_time} seconds, on the phone during September 2016.")
