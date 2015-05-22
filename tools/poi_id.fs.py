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
from from_cross_to import from_cross_to
from from_squared import from_squared
from bonus_salary_ratio import bonus_salary_ratio
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


### Task 1: Select what features
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
def detect_poi():
    features = ['stk_pay_ratio','to_poi_ratio', 'from_poi_ratio',\
            'bonus_salary_ratio', 'from_cross_to', 'from_squared']

### Load the dictionary containing the dataset
    data_dict = pickle.load(open("final_project_dataset.pkl", "r") )
    data_dict['BELFER ROBERT']['total_payments']=3285
    data_dict['BELFER ROBERT']['total_stock_value']= 'NaN'
### Task 2: Remove outliers
    data_dict.pop('TOTAL',0)
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
    my_dataset = data_dict
    stk_pay_ratio(my_dataset)
    from_poi_ratio(my_dataset)
    to_poi_ratio(my_dataset)
    bonus_salary_ratio(my_dataset)
    from_cross_to(my_dataset)
    from_squared(my_dataset)

### Because of the small size of the dataset, the script uses stratified
### shuffle split cross validation in tester.py

    features_list = ['poi','from_cross_to', 'from_squared','stk_pay_ratio','to_poi_ratio', 'from_poi_ratio',\
            'bonus_salary_ratio','shared_receipt_with_poi','total_payments','restricted_stock_deferred' ]
#            , 'shared_receipt_with_poi','total_payments','restrcited_stock_deferred' ]
    data_f = featureFormat(my_dataset, features_list)
    n_features = len(features_list)-1
    y = data_f[:,0]
    X = data_f[:,1:n_features]      
    features_sel = SelectKBest(chi2, k=3).fit(X, y)
    features_ind = features_sel.get_support(indices=True)
#    data = featureFormat(my_dataset, features_list)
#    labels, features = targetFeatureSplit(data)  
    features_list = features_list[1:]
    sel_features_list=['poi']
    for f in features_ind:
        sel_features_list.append(features_list[f])
    sel_features_list = ['poi','stk_pay_ratio','to_poi_ratio', 'from_poi_ratio']
    clf = GaussianNB()    
    test_classifier(clf, my_dataset, sel_features_list)
    
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
    features_list = ['poi','stk_pay_ratio','to_poi_ratio', 'from_poi_ratio']

### Dump classifier, dataset, and features_list
    dump_classifier_and_data(clf, my_dataset, features_list)

def print_feature_importances(features_list, clf):
    print "feature_importances"
    print features_list[1:]
    print clf.feature_importances_
    print 

if __name__ == "__main__":
    detect_poi()
