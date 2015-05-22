# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 08:40:49 2015

@author: raphaeltam
"""

from __future__ import division
def from_poi_ratio(d_dict):
    for person in d_dict.keys():
        if d_dict[person]['from_poi_to_this_person'] == 'NaN' or \
        d_dict[person]['to_messages'] == 'NaN':
            d_dict[person]['from_poi_ratio'] = 0
        else:
            d_dict[person]['from_poi_ratio'] = \
            d_dict[person]['from_poi_to_this_person']/ \
            d_dict[person]['to_messages']