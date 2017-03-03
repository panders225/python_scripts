# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 19:06:42 2017

@author: Philip

Script will follow chapter 17 of python crash course from no starch press
Interacting with the Github API to pull data and visualize it
"""

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# make an API call - github doesn't require a license
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

r.__sizeof__()
r.__class__

print("Status Code:", r.status_code) #200 indicates success

response_dict = r.json() #the json will correspond to a python dictionary

response_dict.viewkeys()

# how many repositories do we have in total?
print("Total Repositories:", response_dict['total_count'] )

# take a 
repo_dicts = response_dict['items']
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# make a visualization
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on Github"
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('C:/Users/Philip/Documents/Python Scripts/progs/python_scripts/api_calls/output/test.svg')



print("Repositories Returned:", len(repo_dicts))

# check out the first repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected information about first repository:")
print("Name:", repo_dict['name'])
print("Owner:", repo_dict['owner']['login'])
print("Stars:", repo_dict["stargazers_count"])
print("Repository:", repo_dict['html_url'])
print("Created:", repo_dict['created_at'])
print("Updated:", repo_dict['updated_at'])
print("Description:", repo_dict['description'])

# that was good, let's create a loop to do this more efficiently

print("\nSelected Information about each repository:")
for repo_dict in repo_dicts:
    print("\nName:", repo_dict['name'])
    print("Owner:", repo_dict['owner']['login'])
    print("Stars:", repo_dict["stargazers_count"])
    print("Repository:", repo_dict['html_url'])
    print("Description:", repo_dict['description'])



# quick python visualization, to work on tooltips







