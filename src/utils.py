# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 01:27:38 2023

@author: Md Mamunur Rahman, PH: +1 6474473215
"""
import json
import os

def get_openai_key():
    filepath = os.getcwd() + '\src\\'
    apikey=""
    with open(r"" + filepath + ".env.example", "r") as readfile:
    #with open(r"" + filepath + "key.txt", "r") as readfile:
        apikey = json.load(readfile)["OPENAI_API_KEY"]
    return apikey 