import json
import os



class LittleActionReasoning:


    def __init__(
        self,
        rule_path="dataset/action_rules.json"
    ):


        self.rules=[]


        if os.path.exists(rule_path):

            with open(
                rule_path,
                "r",
                encoding="utf-8"
            ) as f:

                self.rules=json.load(f)



    def get_requirement(
        self,
        action
    ):


        for rule in self.rules:


            if rule["action"] == action:

                return rule["need"]



        return None



    def get_rule(
        self,
        action
    ):


        for rule in self.rules:


            if rule["action"] == action:

                return rule



        return None