#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL',0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


b_cutoff = 5000000.
s_cutoff = 1000000.

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)
  

for person in data_dict.keys():
    if data_dict[person]['bonus'] != 'NaN':
        if data_dict[person]['bonus']> b_cutoff \
        and data_dict[person]['salary']> s_cutoff:
            print person

