import json
import os
import difflib
import re
import random




class LittleMemory:


    def __init__(self):


        base_dir=os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )


        self.data_path=os.path.join(

            base_dir,

            "dataset",

            "emotion.jsonl"

        )


        self.memory=[]


        self.load()





    # ==========================
    # load
    # ==========================


    def load(self):


        if not os.path.exists(self.data_path):

            print(
                "Memory文件不存在:",
                self.data_path
            )

            return



        with open(

            self.data_path,

            "r",

            encoding="utf-8"

        ) as f:


            for line in f:


                if line.strip():


                    item=json.loads(line)


                    self.memory.append({

                        "user":
                        item["user"],


                        "assistant":
                        item["assistant"]

                    })



        print(

            "Memory加载:",

            len(self.memory)

        )






    # ==========================
    # normalize
    # ==========================


    def normalize(self,text):


        replace={

            "?":"？",

            "!":"！",

            ",":"，",

            ".":"。",

            " ":"",

            "\n":""

        }



        for a,b in replace.items():


            text=text.replace(

                a,

                b

            )



        return text.strip()






    # ==========================
    # 中文关键词切分
    # ==========================


    def tokenize(self,text):


        text=self.normalize(text)



        words=re.findall(

            r"[\u4e00-\u9fa5]{2,}",

            text

        )



        return set(words)







    # ==========================
    # 相似度
    # ==========================


    def similarity(self,a,b):


        a=self.normalize(a)

        b=self.normalize(b)



        # 完全一致

        if a==b:

            return 1.0





        # 字符顺序相似

        seq=difflib.SequenceMatcher(

            None,

            a,

            b

        ).ratio()






        # 关键词交集

        ka=self.tokenize(a)

        kb=self.tokenize(b)




        if not ka or not kb:


            keyword=0



        else:


            keyword=len(

                ka & kb

            ) / len(

                ka | kb

            )







        # ======================
        # 核心评分
        # ======================

        score=(

            keyword*0.7

            +

            seq*0.3

        )



        return score







    # ==========================
    # Memory搜索
    # ==========================


    def search(

        self,

        query,

        threshold=0.45

    ):


        query=self.normalize(query)



        candidates=[]





        for item in self.memory:


            score=self.similarity(

                query,

                item["user"]

            )



            if score>=threshold:


                candidates.append({

                    "score":score,

                    "item":item

                })







        # 没找到

        if not candidates:


            print(

                "Memory匹配:0 来源:None"

            )


            return None







        # 高分排序

        candidates.sort(

            key=lambda x:x["score"],

            reverse=True

        )





        # Top K

        top=candidates[:5]






        # ======================
        # 随机采样
        # ======================

        selected=random.choice(

            top

        )





        print(

            "Memory采样:",

            round(

                selected["score"],

                3

            ),

            "来源:",

            selected["item"]["user"]

        )





        return selected["item"]["assistant"]