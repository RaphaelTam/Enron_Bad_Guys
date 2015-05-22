# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 09:04:19 2015

@author: raphaeltam
"""

from __future__ import division
def to_poi_ratio(d_dict):
    for person in d_dict.keys():
        if d_dict[person]['from_this_person_to_poi'] == 'NaN' or \
        d_dict[person]['from_messages'] == 'NaN':
            d_dict[person]['to_poi_ratio'] = 0
        else:
            d_dict[person]['to_poi_ratio'] = \
            d_dict[person]['from_this_person_to_poi']/ \
            d_dict[person]['from_messages']