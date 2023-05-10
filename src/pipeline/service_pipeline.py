# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:35:58 2023

@author: Md Mamunur Rahman, PH: +1 6474473215
"""

from src.pipeline.action_manager import ActionResult
from components.prompt_generator import PromptGenerator

action_result = ActionResult()





def gpt_response_for_user(mlist):
    pg=PromptGenerator()
    #mlist = ['Romantic']
    #mlist=[]
    prompt = pg.generate_prompt(mlist)
    return action_result.final_action_result("user1",prompt, "user1_2023_04_29_12-12-23")