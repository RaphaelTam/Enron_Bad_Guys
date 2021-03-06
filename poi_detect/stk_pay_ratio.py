# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 07:48:14 2015

@author: raphaeltam
Stock/Pay ratio feature
"""
from __future__ import division
def stk_pay_ratio(d_dict):
    for person in d_dict.keys():
        if d_dict[person]['total_payments'] == 'NaN' or \
        d_dict[person]['total_stock_value'] == 'NaN':
            d_dict[person]['stk_pay_ratio'] = 0
        
        else:
            
            d_dict[person]['stk_pay_ratio'] = d_dict[person]['total_stock_value']/ \
            d_dict[person]['total_payments']
            
    