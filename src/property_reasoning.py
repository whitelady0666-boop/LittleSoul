import json
import os


class LittlePropertyReasoning:


    def __init__(self):


        self.concepts = self.load_concepts()



    def load_concepts(self):


        path = "dataset/concepts.json"


        if not os.path.exists(path):

            return []


        with open(

            path,

            "r",

            encoding="utf-8"

        ) as f:


            return json.load(f)




    def get_parent_concept(self, prop):


        for item in self.concepts:


            if item["concept"] == prop:


                return item["parent"]


        return None