README.TEXT

Files and folders in this project: 
2 folders: poi_detect and tools

poi_detect:
project_report.pdf: provides the narrative on the workflow.  The way features are generated and selected for classification is discussed.  The results between Naive Bayes and Decision Tree are compared.  It includes a discussion on Stratified K-fold cross validation and ShuffleSplit iterator.  Evaluation metrics and their interpretation completes the analysis.

final_project_dataset.pkl: initial dataset that contains the financial and email information of 145 Enron employees

bonus_salary_ratio.py: generates a feature that is the ratio of bonus over salary.

from_poi_ratio.py: generates a feature that is the ratio of “from_this_person_to_poi” and “from_messages”.

to_poi_ratio.py: generates a feature that is the ratio of “from_poi_to_this_person” and “to_messages”.

tuning_tree.py: uses different values for the parameters of a decision tree classifier and calls test_classifier in tester.py to produce evaluation metrics as well as feature importances.

poi_id.py: workflow that removes outlier, generates features, selects features and instantiates a classifier.  Dump the engineered dataset, classifier and feature selection into pickle files: my_dataset.pkl, my_classifieer.pkl, my_features.pkl

tester.py: reads engineered dataset, classifier and feature files produced by poi_id.py, runs the classifier and produces evaluation metrics.

my_classifier.pkl: output from poi_id.py

my_dataset.pkl: output from poi_id.py

my_features.pkl: output from poi_id.py

salary_bonus_scatter_plot.py: produces a scatter plot of salary and bonus from final_project_dataset.pkl

outlier_check_2.py: check for outliers again after removing one outlier



The following is in tools folder:

feature_format.py: tools for converting data from the dictionary to a python list, as well as separating the labels from the features in the dataset.  




