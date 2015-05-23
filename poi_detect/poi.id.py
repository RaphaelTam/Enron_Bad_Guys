#!/usr/bin/python

import sys
import pickle
import numpy as np
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import test_classifier, dump_classifier_and_data

from stk_pay_ratio import stk_pay_ratio
from from_poi_ratio import from_poi_ratio
from to_poi_ratio import to_poi_ratio
from bonus_salary_ratio import bonus_salary_ratio

from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from fList_set import fList_set
from ptest import ptest
    
def detect_poi():
### Load the dictionary containing the dataset
    data_dict = pickle.load(open("final_project_dataset.pkl", "r") )
### Task 1: Remove outliers
    data_dict.pop('TOTAL',0)    
    
### Task 2: Select what features
### 'stk_pay_ratio','to_poi_ratio', 'from_poi_ratio','bonus_salary_ratio'
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
    my_dataset = data_dict
    stk_pay_ratio(my_dataset)
    from_poi_ratio(my_dataset)
    to_poi_ratio(my_dataset)
    bonus_salary_ratio(my_dataset)
     
### Task 3: Feature Selection
### Generate a set of 15 feature lists from these 4 features
### This way, all possible combinations of these features are tested

    all_features_list = fList_set()

### Because of the small size of the dataset, the script uses stratified
### shuffle split cross validation in tester.py
    metrics = []    
    clf = GaussianNB()    
### ptest uses Stratified shuffle split cross validation and calculates the precision
### Find the precision for every list
    for i in range(0,15):
        metrics.append(ptest(clf,my_dataset,all_features_list[i]))
### Go for the feature list that produces the best precision.  
### For this dataset only, it is harder to get a high precision.
    best = np.array(metrics).argmax()  
    
### Run test_classifier to print evaluation metrics to console
    test_classifier(clf, my_dataset,all_features_list[best])

### Now use the same feature list to run the decison tree classifier
    features_list = all_features_list[best]
### Task 4: Try a varity of classifiers
    samples_split_values = [2,4]
    samples_leaf_values = [1,2]

    for split in samples_split_values:
        for leaf in samples_leaf_values:
            clf = tree.DecisionTreeClassifier(min_samples_split=split,\
            min_samples_leaf=leaf)
            test_classifier(clf, my_dataset, features_list)
            print_feature_importances(features_list, clf)
###Choose best classfier and feature set    
    clf = GaussianNB()   

### Dump classifier, dataset, and features_list
    dump_classifier_and_data(clf, my_dataset, features_list)

def print_feature_importances(features_list, clf):
    print "feature_importances"
    print features_list[1:]
    print clf.feature_importances_
    print 

if __name__ == "__main__":
    detect_poi()
