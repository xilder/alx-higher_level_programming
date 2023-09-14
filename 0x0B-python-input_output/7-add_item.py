#!/usr/bin/python3

"""adds elements to a list and stores them is json string"""
import sys
import json
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = 'add_item.json'
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for i in sys.argv[1:]:
    json_list.append(i)

save_to_json_file(json_list, filename)
