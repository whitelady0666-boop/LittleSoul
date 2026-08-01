class EmotionalReasoning:


    def __init__(self, belief_engine):

        self.belief = belief_engine


        self.rules = [

            {
                "keywords":[
                    "陪陪我",
                    "陪我",
                    "不要离开我",
                    "你在吗"
                ],

                "response":
                "我在这里。虽然我没有身体，但我可以陪你聊一会儿。"

            },


            {
                "keywords":[
                    "累",
                    "疲惫",
                    "辛苦",
                    "撑不住",
                    "难受"
                ],

                "response":
                "听起来你今天经历了很多。我可以陪你说说发生了什么。"

            },


            {
                "keywords":[
                    "孤独",
                    "孤单",
                    "没人",
                    "一个人"
                ],

                "response":
                "我在这里。虽然我没有身体，但现在可以陪你交流。"

            },


            {
                "keywords":[
                    "害怕",
                    "担心",
                    "不安"
                ],

                "response":
                "我听到了你的担心。你可以告诉我发生了什么。"

            }

        ]



    def generate(self, text):


        for rule in self.rules:


            for word in rule["keywords"]:


                if word in text:


                    return {

                        "answer":
                        rule["response"],


                        "source":
                        "emotion",


                        "evidence":
                        [
                            "用户情绪表达"
                        ],


                        "confidence":
                        0.8

                    }



        return None