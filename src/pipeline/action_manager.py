# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:35:58 2023

@author: Md Mamunur Rahman, PH: +1 6474473215
"""
import os
import sys
 
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)

import json
from components.ocr import OCRTesseract
from components.openai_gpt_prompt import OpenAIGptPrompt
import utils as common
from components.file_manager import FileManager

BASE_PATH = str(os.getcwd())
TEMPT_PATH = BASE_PATH + "\data\image_temp" + "\\" 
#print(TEMPT_PATH)

# Extract data from image by ocs
def ocr_action(image_address):
    ocr = OCRTesseract()
    ocr_text = ocr.image_to_text(image_address)
    return ocr_text

# extract information from ocr text
def info_prompt(callback):
    input_text = "identify name, age, gender, height, marital status and other description from below text and show in a python dictionary format."
    input_text = input_text + "\"" + callback + "\""
    #print(input_text)
    chatgpt_prompt = OpenAIGptPrompt()
    info_prompt_responses = chatgpt_prompt.gpt_info_prompt(input_text)
    return info_prompt_responses

# write a pragraph based on extracted info
def chatgpt_prompt(prompt_txt, callback):
    #input_text = "write a romantic paragraph to impress the person based on information from below python dictionary. If value is N/A or Unknown ignore those."
    input_text = prompt_txt # "write 3 alternative paragraph with 3 alternative intents to impress the person based on information from below intents and python dictionary. If value is N/A or Unknown ignore those. Intents: 1. Romantic 2. Funny 3. Friendly Python Directory:"
    input_text = input_text + "\"" + callback + "\""
    #print(input_text)
    chatgpt_prompt = OpenAIGptPrompt()
    instruction ="You are a helpful, writing assistant."
    chat_prompt_responses = chatgpt_prompt.chatgpt_prompt(input_text, instruction)
    return chat_prompt_responses

def get_image_file_list(userid,tempt_folder_name):
    file_manager = FileManager()
    files = file_manager.create_file_list_from_tempt(userid, TEMPT_PATH + tempt_folder_name)
    return files


class ActionResult:
    def __init__(self):
        self
    def final_action_result(self,userid,prompt, tempt_folder_name):
        files = get_image_file_list(userid,tempt_folder_name)
        return chatgpt_prompt(prompt, info_prompt(ocr_action(files)))







"""
write 3 alternative paragraph with 3 alternative intents to impress the person based on information from below intents and python dictionary. If value is N/A or Unknown ignore those.

Intents:
1. Romantic
2. Funny
3. Friendly

Python Directory:

Sharjeel = {
    "Name": "Sharjeel",
    "Age": 20,
    "Gender": "Man",
    "Height": 162,
    "Marital Status": "Don't Know Yet",
    "Description": {
        "Basics": {
            "In College": "2%",
            "Smoke": "Never",
            "Drink": "Never"
        },
        "Interests": {
            "Art": True,
            "Writing": True,
            "Fantasy": True,
            "Coffee": True
        },
        "Location": {
            "City": "Multan",
            "Province": "Punjab",
            "Distance from Lahore": "51 km"
        },
        "Recommendation": "Recommend to a friend"
    }
}


"""







# def fun1(arg1):
#     time.sleep(3)
#     print("3")
#     print(arg1)
#     return arg1
# def fun2(callback):
#     time.sleep(3)
#     print("2")
#     aa = callback
#     print(str(aa) + "ggg")
#     return str(aa) + "ggg"

# def fun3(callback):
#     time.sleep(3)
#     print("1")
#     return callback + "nnnn"



# #fun2("3",fun1)
# print (fun3(fun2(fun1("text"))))
# #fun3(fun2(fun1))