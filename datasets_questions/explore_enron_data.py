#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
'''
count = 0
for value in enron_data:
	if (enron_data[value]['poi'] == True):
		count +=1
print count
print enron_data
'''
#print enron_data["PRENTICE JAMES"]["total_stock_value"]
#print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
'''
a = ['LAY KENNETH L','SKILLING JEFFREY K','FASTOW ANDREW S']
for i in a:
	print enron_data[i]["total_payments"]

'''
print len(dict((key, value) for key, value in enron_data.items() if value["salary"] != 'NaN'))
print len(dict((key, value) for key, value in enron_data.items() if value["email_address"] != 'NaN'))

no_total_payments = len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))
print float(no_total_payments)/len(enron_data) * 100,'%'

POIs = dict((key,value) for key, value in enron_data.items() if value['poi'] == True)
number_POIs = len(POIs)
print 10+ len(dict((key, value) for key, value in POIs.items() if value["total_payments"] == 'NaN'))
print len(enron_data)+ 10

print 10 + len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))

# What is the new number of POIs?
print 10 + len(POIs)

print len(enron_data) + 10
print 10 + len(dict((key, value) for key, value in enron_data.items() if value["total_payments"] == 'NaN'))
