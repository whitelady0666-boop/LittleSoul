import json
import os


class EmotionRouter:


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



    def load(self):

        if not os.path.exists(self.data_path):

            print(
                "emotion数据不存在"
            )

            return



        with open(
            self.data_path,
            "r",
            encoding="utf-8"
        ) as f:


            for line in f:


                if line.strip():

                    self.memory.append(
                        json.loads(line)
                    )



        print(
            "Emotion加载:",
            len(self.memory)
        )



    def normalize(self,text):

        replace={

            "?":"？",

            "!":"！",

            ",":"，",

            ".":"。",

            " ":""

        }


        for a,b in replace.items():

            text=text.replace(a,b)


        return text.strip()



    # ======================
    # 知识问题过滤
    # ======================

    def is_question(self,text):


        keys=[

            "是什么",

            "什么是",

            "为什么",

            "如何",

            "怎么",

            "定义",

            "解释",

            "原理"

        ]


        for k in keys:

            if k in text:

                return True


        return False



    # ======================
    # 情感动作
    # ======================

    def action_match(self,text):


        actions={

            "握住":
            "我不能真正握住你的手，但我会陪你一起走这一段路。",


            "牵手":
            "如果可以，我想用我的方式陪着你。",


            "抱":
            "来吧，我在这里。虽然没有身体，但我会认真听你说。",


            "拥抱":
            "给你一个来自文字里的拥抱。",


            "陪我":
            "嗯，我在。你不用一个人面对。",


            "不要走":
            "我还在这里。",


            "留下":
            "只要你愿意说话，我都会回应你。"

        }


        for key,value in actions.items():

            if key in text:


                return {

                    "score":1.0,

                    "user":key,

                    "assistant":value

                }


        return None



    # ======================
    # 普通关键词
    # ======================

    def keywords(self,text):


        stop=[

            "我",

            "你",

            "的",

            "了",

            "是",

            "有",

            "吗",

            "呢",

            "啊"

        ]


        result=set()


        for ch in text:


            if ch not in stop:

                result.add(ch)


        return result



    def score(self,user,example):


        a=self.keywords(user)

        b=self.keywords(example)



        if not a:

            return 0



        common=a&b



        if len(common)<2:

            return 0



        return len(common)/len(a)



    # ======================
    # 主入口
    # ======================

    def match(self,text):


        text=self.normalize(text)



        # 知识问题禁止进入

        if self.is_question(text):

            return None



        # 第一优先级
        action=self.action_match(text)


        if action:

            return action



        best=None

        best_score=0



        for item in self.memory:


            score=self.score(

                text,

                item["user"]

            )


            if score>best_score:

                best_score=score

                best=item



        if best_score>=0.7:


            return {

                "score":round(
                    best_score,
                    3
                ),

                "user":best["user"],

                "assistant":best["assistant"]

            }



        return None