# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 16:03:39 2015

@author: raphaeltam
"""

from __future__ import division
def bonus_salary_ratio(d_dict):
    for person in d_dict.keys():
        if d_dict[person]['bonus'] == 'NaN' or \
        d_dict[person]['salary'] == 'NaN':
            d_dict[person]['bonus_salary_ratio'] = 0
        else:
            d_dict[person]['bonus_salary_ratio'] = d_dict[person]['bonus']/ \
            d_dict[person]['salary']