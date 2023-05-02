# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:50:26 2023

@author: Md Mamunur Rahman, PH: +1 6474473215
"""
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import openai
import json
import utils as common

openai.api_key = common.get_openai_key()

class OpenAIGptPrompt:
    def __int__(self):
        self
        
    def gpt_info_prompt(self,input_text):
        response = openai.Completion.create(
            engine="text-davinci-003"
            ,
            prompt = input_text,
            max_tokens=1024,
            n = 1,
            stop=None,
            temperature=0.5
        )
        data = response.choices[0].text
        print(data)
        return data
        
    def chatgpt_prompt(self,input_info, instruction):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": instruction},
                {"role": "system", "name":"example_user", "content": input_info},

            ],
            temperature=0,
        )
        data = json.loads(str(response))
        #print(data['choices'][0]['message']['content'])
        return data['choices'][0]['message']['content']
        
# instruction ="You are a helpful, pattern-following and information indentifying assistant."