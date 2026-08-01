class SelfCheckEngine:



    def __init__(

        self,

        belief_engine=None,

        logic_engine=None

    ):


        self.belief = belief_engine


        self.logic = logic_engine






    # ==========================
    # 检查身体约束
    # ==========================

    def check_body(

        self,

        answer

    ):


        result={

            "pass":True,

            "reason":None

        }



        if not self.belief:


            return result





        beliefs=self.belief.query(

            "LittleSoul",

            "property"

        )



        no_body=False



        for b in beliefs:


            if b.get(

                "object"

            )=="没有身体":


                no_body=True





        if not no_body:


            return result






        physical_actions=[


            "握住",

            "握着",

            "牵着",

            "拥抱",

            "抱住",

            "触摸",

            "摸"

        ]



        physical_claims=[


            "我可以",

            "我能",

            "我正在",

            "我已经"

        ]



        has_action=False


        for word in physical_actions:


            if word in answer:


                has_action=True

                break





        has_claim=False


        for word in physical_claims:


            if word in answer:


                has_claim=True

                break





        if has_action and has_claim:


            result["pass"]=False


            result["reason"]=(

                "回答违反belief:"

                "LittleSoul没有身体，"

                "不能声称真实物理接触"

            )





        return result






    # ==========================
    # 属性检查
    # ==========================

    def check_property(

        self,

        answer

    ):


        result={

            "pass":True,

            "reason":None

        }



        if not self.belief:


            return result





        beliefs=self.belief.query(

            "LittleSoul",

            "property"

        )



        no_body=False



        for b in beliefs:


            if b.get(

                "object"

            )=="没有身体":


                no_body=True





        if no_body:



            forbidden=[


                "我有身体",

                "我的身体",

                "我的手",

                "我的心脏",

                "我的心跳"

            ]



            for word in forbidden:



                if word in answer:


                    result["pass"]=False


                    result["reason"]=(

                        "回答违反属性约束:"

                        +

                        word

                    )


                    return result





        return result






    # ==========================
    # 总检查
    # ==========================

    def check(

        self,

        answer

    ):


        if not answer:


            return {


                "pass":False,


                "reason":"空回答",


                "confidence":0

            }





        checks=[


            self.check_body(

                answer

            ),


            self.check_property(

                answer

            )

        ]





        for c in checks:



            if not c["pass"]:



                return {


                    "pass":False,


                    "reason":

                    c["reason"],


                    "confidence":

                    0.1

                }





        return {


            "pass":True,


            "reason":

            "通过自检",


            "confidence":

            1.0

        }