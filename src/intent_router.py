class IntentRouter:


    def __init__(self):

        self.knowledge_words=[

            "是什么",
            "什么是",
            "定义",
            "原理",
            "介绍"

        ]


        self.emotion_words=[

            "累",
            "难过",
            "伤心",
            "害怕",
            "孤独",
            "陪我",
            "抱",
            "握",
            "牵",
            "留下",
            "离开"

        ]



    def detect(self,text):


        result={

            "type":"unknown",

            "confidence":0,

            "reason":[]

        }



        # 知识问题

        for w in self.knowledge_words:

            if w in text:


                result["type"]="knowledge"

                result["confidence"]=0.9

                result["reason"].append(

                    "知识关键词:"+w

                )

                return result



        # 情感问题

        for w in self.emotion_words:

            if w in text:


                result["type"]="emotion"

                result["confidence"]=0.8

                result["reason"].append(

                    "情感关键词:"+w

                )

                return result



        # 普通思考

        result["type"]="reasoning"

        result["confidence"]=0.5

        result["reason"].append(

            "普通对话"

        )


        return result