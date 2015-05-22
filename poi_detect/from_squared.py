# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 15:52:19 2015

@author: raphaeltam
"""
from from_poi_ratio import from_poi_ratio
def from_squared(d_dict):    
    from_poi_ratio(d_dict)
    for person in d_dict.keys():
        d_dict[person]['from_squared'] = d_dict[person]['from_poi_ratio']*\
        d_dict[person]['from_poi_ratio']
    