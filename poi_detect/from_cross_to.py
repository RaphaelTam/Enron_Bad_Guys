# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 15:27:19 2015

@author: raphaeltam
"""
from from_poi_ratio import from_poi_ratio
from to_poi_ratio import to_poi_ratio
def from_cross_to(d_dict):
    from_poi_ratio(d_dict)
    to_poi_ratio(d_dict)
    for person in d_dict.keys():
        d_dict[person]['from_cross_to'] = d_dict[person]['from_poi_ratio']*\
        d_dict[person]['to_poi_ratio']