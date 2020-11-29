# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 12:26:20 2020

@author: nnath
"""
import re
import copy
from datetime import datetime
'''
PROBLEM STATEMENT : 
    
Caputring all type of month year format as shown below and append the numeric string value in the list wihtout duplicate capturings

jan 2020
january 2020
jan-2020
jan - 2020
jan/2020
january / 2020
12/2020
12 - 2020
12 2020
'''
genericText = input('Enter : ').lower()
# and 2 2020; capturing 'and 2'-- hence need to defined month name in patten  rather than '\w{3,}'
month_list = ['january','february','march','april','may','june','july','august','september','october','november','december',
              'jan','feb','mar','apr','jun','jul','aug','sep','oct','nov','dec']


#entities_extracted - capturing numbers (mainParser)
entities_extracted=[{'value': '23', 'entity': 'num', 'start': 24, 'end': 26, 'extractor': 'regex_tin'}, 
{'value': '01', 'entity': 'num', 'start': 47, 'end': 49, 'extractor': 'regex_tin'}, 
{'value': '20', 'entity': 'num', 'start': 50, 'end': 52, 'extractor': 'regex_tin'}]


def input_capture_month_year(genericText):
    month_year_reg = r'\b(\d{1,2}|january|february|march|april|may|june|july|august|september|october|november|december|jan|feb|mar|apr|jun|jul|aug|sep|oct|nov|dec)\s*(-|\/|\s+)\s*(\d{2,4})\b'
    
    match = re.compile(month_year_reg)
    remove_spcl = [' ','/','-','']
    list_tuple_match = match.findall(genericText)
    res=[]
    for tuple_gp in list_tuple_match:
        m_y=list(tuple_gp)
        m_y=[i for i in m_y if i not in remove_spcl]
        #len(m_y)==2 --> regex capturing single digit 
        if len(m_y)==2 and m_y[0].isalpha() and (m_y[0]  in month_list):
            m_y[0] = str(month_convertion(m_y))
            res.append(m_y)
            entities_extracted.append({'value': m_y[0], 'entity': 'month_num', 'start': 0, 'end': 0})
            entities_extracted.append({'value': m_y[1], 'entity': 'year_num', 'start': 0, 'end': 0})
            
        elif len(m_y)==2 and m_y[0].isdigit() and  int(m_y[0])  in range(1,13):#month number 1 to 12
            entities_extracted.append({'value': str(m_y[0]), 'entity': 'month_num', 'start': 0, 'end': 0})
            entities_extracted.append({'value': str(m_y[1]), 'entity': 'year_num', 'start': 0, 'end': 0})
            res.append(m_y)#for num entity
            
        else:
            continue
        
    e_e = num_removal(res,entities_extracted)
            
    return e_e

def month_convertion(month_str):
    month_abr = month_str[0][:3] if len(month_str[0]) > 3 else month_str[0]
    month_num = datetime.strptime(month_abr,'%b').month
    return month_num

#remove the duplicate mainParser entity value in num entity of entities_extracted 
def num_removal(list_month_year,entities_extracted):
    entities_extracted_copy = copy.deepcopy(entities_extracted)
    res_ = [j for i in list_month_year for j in i]
    for i in entities_extracted_copy:
        if 'num' == i['entity'] and i['value'] in res_ :
            res_.remove(i['value'])
            entities_extracted.remove(i)        
    return entities_extracted

A = input_capture_month_year(genericText)
print('*'*20)
print(A)