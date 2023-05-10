# -*- coding: utf-8 -*-
"""
@author: Md Mamunur Rahman, PH: +1 6474473215
"""

class PromptGenerator:
    def __init__(self) -> None:
        pass

    def generate_prompt(self,intents):
        number_of_intents=0
        prompt=""
        intents_text = ""
        if intents:
            number_of_intents = len(intents)
        if number_of_intents > 1:    
            prompt = "write " + str(number_of_intents) + " alternative paragraph with " + str(number_of_intents) + " alternative intents with <br><br> at the end of each intnets to impress the person based on information from below intents and python dictionary. If value is N/A or Unknown ignore those."
            intents_text = " Intents: "
            for i, intent in enumerate(intents):
                intents_text = intents_text + " " + str(i+1) + ". " + intent + " "

            intents_text = intents_text + " Python Directory: "
            prompt = prompt + intents_text
        elif number_of_intents == 1 :
            prompt = "write a " + intents[0] + " paragraph to impress the person based on information from below intents with <br><br> at the end of each intnets and python dictionary. If value is N/A or Unknown ignore those."
            intents_text = intents_text + " Python Directory: "
            prompt = prompt + intents_text 
        else:
            prompt = "write a friendly paragraph to impress the person based on information from below intents with <br><br> at the end of each intnets and python dictionary. If value is N/A or Unknown ignore those."
            intents_text = intents_text + " Python Directory: "
            prompt = prompt + intents_text           

        return prompt

  

