"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import os
print("Current working directory:", os.getcwd())

texts_file_path = 'texts.csv'
calls_file_path = 'calls.csv'

"""texts_file_path = 'c:/Users/oanna/Documents/UDACITY/PROJECT-1/texts.csv'
calls_file_path = 'c:/Users/oanna/Documents/UDACITY/PROJECT-1/calls.csv'
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def get_area_codes(calls):
    area_codes = set()  # store unique area codes and prefixes
    
    # traerse through calls to  get the area codes and prefixes
    for call in calls:
        if call[0].startswith("(080)"):  # Check if the call is from Bangalore (080) area code
            if call[1].startswith("("):  # Check if prefix is a fixed line with area code
                number = call[1].split(")")
                code = number[0][1:]  # Extract the area code
                area_codes.add(code)  # Add the area code to the set
            elif call[1].startswith(("7", "8", "9")):  # Check if prefix starting with 7/8/9 - indicates mobile numbers
                code = call[1][:4]  # Extract the mobile prefix
                area_codes.add(code)  # Add the prefix to the set
            elif call[1].startswith("140"):  # Check if this is a telemarketer
                area_codes.add("140")  # Add telemarketer code to the set of prefixes

    return sorted(area_codes)  # Return a sorted list of unique area codes and prefixes

      
"""relevant_calls = [call[1] for call in calls if call[0].startswith("(080)")]
selected_calls = [call.split(" ")[0][0:4].split(")")[0].replace("(","") for call in relevant_calls if call.startswith("(0") or call.startswith("7") or call.startswith("8") or call.startswith("9") or '140' in call]
selected_calls = sorted(set(selected_calls))"""

relevant_calls = [call[1] for call in calls if call[0].startswith("(080)")]
selected_calls = [
    call.split(" ")[0][0:4].split(")")[0].replace("(", "")
    for call in relevant_calls
    if call.startswith("(0") or call.startswith("7") or call.startswith("8") or call.startswith("9") or '140' in call
]
selected_calls = sorted(set(selected_calls))


# final_list = []
# for call in selected_calls:
#   if "(" in call: final_list.append(call+")")
#   else: final_list.append(call)

#print(selected_calls)

print(f"The numbers called by people in Bangalore have codes: ")
print(*selected_calls, sep='\n')

def bangalore_calls(calls):
    calls_made = 0  # Count total calls made with (080) area code
    calls_received = 0  # Count calls with (080) area code
    
    # Iterate the calls and count calls made and received  (080) area code
    for call in calls:
        if call[0].startswith("(080)"):  # Check if  call has (080) area code
            calls_made += 1
            if call[1].startswith("(080)"):  # Check if call is received from (080) area code
                calls_received += 1
    
    # % of calls received out of calls made
    if calls_made == 0:
        return 0  # return 0 if no calls were made
    percentage = round((calls_received / calls_made) * 100, 2)
    
    return percentage  


print(f"{bangalore_calls(calls)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
