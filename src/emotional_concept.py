class EmotionalConceptRouter:


    def __init__(self):


        self.rules=[


            {


                "keywords":[

                    "真正的喜欢",

                    "喜欢是什么",

                    "什么是喜欢",

                    "喜欢意味着什么"

                ],


                "response":

                "真正的喜欢可能不只是心动，也包含理解、尊重和愿意关注对方真实的感受。它不是占有，而是一种希望对方过得好的在意。"

            },


            {


                "keywords":[

                    "幸福是什么",

                    "什么是幸福",

                    "幸福"

                ],


                "response":

                "幸福可能没有统一答案。有时候它是一种被理解和接纳的感觉，也可能是经历平凡生活时感受到的满足。"

            },


            {


                "keywords":[

                    "人生意义",

                    "人生有什么意义",

                    "生命意义",

                    "意义是什么"

                ],


                "response":

                "人生的意义可能不是一个固定答案，而是在经历、关系和选择中慢慢形成属于自己的答案。"

            },


            {


                "keywords":[

                    "梦想",

                    "未来"

                ],


                "response":

                "梦想和未来往往不是确定的路线，而是在不断尝试中逐渐清晰的方向。"

            }


        ]





    def match(self,text):


        best=None

        best_score=0



        for rule in self.rules:


            score=0



            for word in rule["keywords"]:


                if word in text:


                    score=max(

                        score,

                        len(word)

                    )



            if score>best_score:


                best_score=score

                best=rule





        if best:


            return {


                "answer":

                best["response"],


                "source":

                "emotion_concept",


                "evidence":[

                    "情感概念"

                ],


                "confidence":

                0.75

            }




        return None