import json
import os
import difflib



class LittleMemory:


    def __init__(self):


        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )


        self.data_path = os.path.join(
            base_dir,
            "dataset",
            "emotion.jsonl"
        )


        self.memory=[]


        self.load()



    def load(self):


        with open(
            self.data_path,
            "r",
            encoding="utf-8"
        ) as f:


            for line in f:


                item=json.loads(line)


                self.memory.append(
                    {
                        "user":item["user"],
                        "assistant":item["assistant"]
                    }
                )


        print(
            "Memory加载:",
            len(self.memory)
        )



    def normalize(
        self,
        text
    ):


        text=text.strip()


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


        return text



    def similarity(
        self,
        a,
        b
    ):


        return difflib.SequenceMatcher(
            None,
            a,
            b
        ).ratio()



    def search(
        self,
        query,
        threshold=0.75
    ):


        query=self.normalize(
            query
        )


        best_answer=None

        best_score=0



        for item in self.memory:


            user_text=self.normalize(
                item["user"]
            )


            score=self.similarity(
                query,
                user_text
            )


            if score>best_score:


                best_score=score

                best_answer=item["assistant"]




        print(
            "Memory匹配:",
            round(best_score,3)
        )



        if best_score>=threshold:


            return best_answer



        return None