from belief_engine import BeliefEngine


try:
    from context_memory import ContextMemory

except ImportError:
    ContextMemory = None



try:
    from logic_engine import LogicEngine

except ImportError:
    LogicEngine = None





class ReasoningEngine:


    def __init__(

        self,

        knowledge,

        memory,

        belief=None,

        context=None,

        logic=None

    ):


        self.knowledge = knowledge

        self.memory = memory



        if belief is None:

            self.belief = BeliefEngine()

        else:

            self.belief = belief





        if context is None:

            if ContextMemory:

                self.context = ContextMemory()

            else:

                self.context = None

        else:

            self.context = context





        if logic is None:

            if LogicEngine:

                self.logic = LogicEngine(

                    beliefs=self.belief.beliefs,

                    knowledge=[]

                )

            else:

                self.logic = None

        else:

            self.logic = logic





    # ==========================
    # 判断知识问题
    # ==========================


    def is_knowledge_question(

        self,

        text

    ):


        # 不再使用:
        #
        # 什么是
        # 是什么
        #
        # 避免误伤Memory人格数据


        keywords=[


            "太阳",

            "地球",

            "月球",

            "黑洞",

            "宇宙",

            "物理",

            "化学",

            "数学",

            "历史",

            "科学",

            "元素",

            "星球"

        ]



        for k in keywords:


            if k in text:

                return True



        return False







    # ==========================
    # 主推理
    # ==========================


    def reason(

        self,

        text

    ):


        trace={


            "steps":[],

            "evidence":[],

            "conflicts":[],

            "confidence":1.0

        }



        trace["steps"].append(

            "用户输入:"+text

        )




        # ======================
        # 1 belief
        # ======================


        trace["steps"].append(

            "执行belief推理"

        )


        belief_result=self.belief.infer(

            text

        )



        if belief_result.get(

            "answer"

        ):



            trace["steps"].append(

                "belief得到结论"

            )



            result={


                "answer":

                belief_result["answer"],


                "source":

                "belief",


                "evidence":

                belief_result.get(

                    "facts",

                    []

                ),


                "confidence":

                belief_result.get(

                    "confidence",

                    1.0

                )

            }



            result["reasoning"]=trace


            return self.final_check(

                result

            )







        # ======================
        # 2 Memory优先
        # ======================


        trace["steps"].append(

            "查询历史经验"

        )


        memory_answer=self.memory.search(

            text

        )



        if memory_answer:



            trace["steps"].append(

                "Memory命中"

            )


            trace["evidence"].append(

                {

                    "source":

                    "memory",

                    "fact":

                    memory_answer

                }

            )


            result={


                "answer":

                memory_answer,


                "source":

                "memory",


                "evidence":[

                    "历史经验"

                ],


                "confidence":

                0.9


            }


            result["reasoning"]=trace



            return self.final_check(

                result

            )







        # ======================
        # 3 Emotion/生成前知识
        # ======================


        if self.is_knowledge_question(

            text

        ):



            trace["steps"].append(

                "查询知识库"

            )


            answer=self.knowledge.search(

                text

            )



            if answer:



                trace["evidence"].append(

                    {

                        "source":

                        "knowledge",

                        "fact":

                        answer

                    }

                )



                result={


                    "answer":

                    answer,


                    "source":

                    "knowledge",


                    "evidence":[

                        "知识库事实"

                    ],


                    "confidence":

                    1.0


                }



                result["reasoning"]=trace



                return self.final_check(

                    result

                )





            trace["confidence"]=0





        # ======================
        # 4 无答案交给模型
        # ======================


        trace["steps"].append(

            "没有找到直接证据"

        )


        return {


            "answer":

            None,


            "source":

            "model",


            "evidence":[

                "没有直接证据，需要生成"

            ],


            "confidence":

            0.5,


            "reasoning":

            trace

        }








    # ==========================
    # SelfCheck
    # ==========================


    def final_check(

        self,

        result

    ):



        if not self.logic:


            return result




        check=self.logic.verify(

            result["answer"]

        )



        if not check["pass"]:



            result["reasoning"]["conflicts"].append(

                check["reason"]

            )


            return {


                "answer":

                None,


                "source":

                "logic_block",


                "evidence":[

                    check["reason"]

                ],


                "confidence":

                0,


                "reasoning":

                result["reasoning"]

            }



        result["reasoning"]["steps"].append(

            "SelfCheck通过"

        )


        return result