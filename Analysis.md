_Abbreviation:_
_Time Complexity = TC_
_Space Complexity = SC_

**Task 0**
- reading csv files is TC O(n), n is the no of lines traversed/read
- SC is O(n) of csv data storage - is O(n + m), proportional to the no of lines and no of total sum of texts.csv and calls.csv
- printing is constant in TC - O(1)
- Overall TC is O(n)
- Overall SC is O(n)



**Task 1**
- reading csv files is TC O(n), n is the no of lines traversed/read
- SC is O(n) of csv data storage - is O(n + m), proportional to the no of lines and no of total sum of texts.csv and calls.csv
*counting()
- iterates trough both text and calls csv. - TC is O(n), total no of texts + calls
- SC is O(n), n is the no of stored phone no's in boths csv files. the set() removes duplicates too, but still remains proportional to the no of uniquee prefixes found in csv's files
- Overall TC is O(n)
- Overall SC is O(n)


**Task 2**
- reading csv files is TC O(n), n is the no of lines traversed/read
- SC is O(n) of csv data storage - is O(n + m), proportional to the no of lines and no of total sum of texts.csv and calls.csv
- TC is O(n) whilst traversing the calls.
- TC is O(n log n), for sorting operation, n is the no of unique phone no's
- SC is O(n), given by the storage in dictionary, which is directly proportional to the unique no's in csv file. n is the no of unique no
- Overall TC is O(n log n), due to sorting() method
- Overall SC is O(n)


**Task 3**
- reading csv files is TC O(n), n is the no of lines traversed/read
- SC is O(n) of csv data storage - is O(n + m), proportional to the no of lines and no of total sum of texts.csv and calls.csv

*get_area_codes() & relevant_calls & selected_calls()
- TC is O(n), n is the no of calls. it traverses all calls and proccesses them by splitting, addidng individually. 
- SC is O(n), given by the area_code set() which can be proportional to the unique no of prefixes. for extracting the relevant calls and their processing, relevant_calls() & selected_calls() store immediate results and not the full set of data, hence still O(n)
- Overall TC is O(n log n), due to sorting() method
- Overall SC is O(n)


**Task 4**
- reading csv files is TC O(n), n is the no of lines traversed/read
- SC is O(n) of csv data storage - is O(n + m), proportional to the no of lines and no of total sum of texts.csv and calls.csv
- TC is O(n), for tarversing the texts/calls lists, is the no of elems in each list
- TC is O(1) for adding elems to the set()
- TC is O(n log n) for sorting the array
- SC is O(n) for storing in set(), directly proportional to the potential unique no that can be extracted from csv files
- Overall TC is O(n log n), due to sorting() method
- Overall SC is O(n)
