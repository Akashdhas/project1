# wi-*- coding: utf-8 -*-
import json
from difflib import get_close_matches

data1 = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if data1.__contains__(w):
        return data1[w]
    elif data1.__contains__(w.title()):
        return data1[w.title()]
    elif data1.__contains__(w.upper()):
        return data1[w.upper()]
    elif len(get_close_matches(w,data1.keys(),cutoff=0.8))>0 :
        k= input("Did you mean %s insted? enter Y if yes else enter N: " % get_close_matches(w,data1.keys())[0])
        if k == 'Y' :
            return data1[get_close_matches(w,data1.keys())[0]]
        elif k == 'N' :
            return "no such word exist. please check again"
        else :
            return "we didnt understand your entry"
    else:
        return "no such word exist. please check again"

word = input("Enter you want to search: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)




