import json
import os
import difflib


class LittleKnowledge:


    def __init__(self):

        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )


        self.data_path = os.path.join(

            base_dir,

            "dataset",

            "fact_knowledge.json"

        )


        self.facts=[]


        self.load()



    # ======================
    # load
    # ======================

    def load(self):


        if not os.path.exists(self.data_path):

            print(
                "知识库不存在:",
                self.data_path
            )

            return



        with open(

            self.data_path,

            "r",

            encoding="utf-8"

        ) as f:


            data=json.load(f)



        for item in data:


            self.facts.append(

                {

                    "subject":item["subject"],

                    "relation":item["relation"],

                    "object":item["object"]

                }

            )



        print(

            "Knowledge加载:",

            len(self.facts)

        )



    # ======================
    # normalize
    # ======================

    def normalize(self,text):


        replace={

            "?":"？",

            "!":"！",

            ",":"，",

            ".":"。",

            " ":""

        }


        for a,b in replace.items():

            text=text.replace(

                a,

                b

            )


        return text.strip()



    # ======================
    # search
    # ======================

    def search(

        self,

        query,

        threshold=0.65

    ):


        query=self.normalize(query)



        for fact in self.facts:


            subject=fact["subject"]


            if subject in query:


                # type关系

                if fact["relation"]=="type":


                    return (

                        subject

                        +

                        "是"

                        +

                        fact["object"]

                        +

                        "。"

                    )



                else:


                    return (

                        subject

                        +

                        "的"

                        +

                        fact["relation"]

                        +

                        "是"

                        +

                        fact["object"]

                        +

                        "。"

                    )



        return None