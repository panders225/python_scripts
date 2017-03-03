# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 20:34:21 2017

@author: Philip
"""

import requests
from operator import itemgetter

# make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty'
r= requests.get(url)
print("Status Code:", r.status_code)

# process information about each submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids['kids']:
    url = ('https://hacker-news.firebaseio.com/v0/item/' + 
    str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    
    submission_dict = {
    'title': response_dict['title'],
    'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
    'comments': response_dict.get('descendants',0)    
        }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                              reverse=True)
                              
for sub in submission_ids['kids']:
    url = ('https://hacker-news.firebaseio.com/v0/item' + 
    str(submission_id) + '.json')
    print url

url = 'https://hacker-news.firebaseio.com/v0/item/9885099.json'
test = requests.get(url)
print test.status_code

url = ('https://hacker-news.firebaseio.com/v0/item' + 
    str(submission_id) + '.json')