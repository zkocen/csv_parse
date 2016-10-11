import csv  #module that we use to work with csv
import time
import operator

input_file = csv.DictReader(open("TSE_sample_data.csv"))

result_list = []
for row in input_file:  #loop through the entire csv

    start_date_epoch = int(row["start_date"])   #select start date row
    start_date_human = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(start_date_epoch)))  #put start_date row in start_date list ant parse it to integer
    if start_date_epoch < 1283731200:  #if stat time is before 1283731200 == 2010-9-06
        word = row["words"]  #put keywords row into word list
        word_date = {"date": start_date_human, "word": word}  #create dictionary with keys "date" for human fates and key "word" for keywords
        result_list.append(word_date)  #build a list of dictionaries


result_list.sort(key=lambda item:item['date'])  #soert the list of dictionaries by date ascending

for x in result_list:  #delete the pair {'date': '%Y-%m-%d %H:%M:%S'} with key date and just leave {'word': 'keyword'} then print out just the keyword
    del x["date"]
    print(x["word"])

