class LogicEngine:


    def __init__(
        self,
        beliefs=None,
        knowledge=None
    ):


        self.beliefs = beliefs or []

        self.knowledge = knowledge or []





    # ==========================
    # 查询belief
    # ==========================

    def find_belief(
        self,
        subject,
        relation=None
    ):


        results=[]


        for b in self.beliefs:


            if b.get("subject") != subject:

                continue



            if relation is not None:


                if b.get("relation") != relation:

                    continue



            results.append(b)



        return results





    # ==========================
    # 查询知识
    # ==========================

    def find_knowledge(
        self,
        subject
    ):


        results=[]


        for k in self.knowledge:


            if k.get("subject")==subject:


                results.append(k)



        return results





    # ==========================
    # 身体限制推理
    # ==========================

    def check_body_constraint(
        self,
        answer
    ):


        result={

            "pass":True,

            "reason":None

        }



        body=self.find_belief(

            "LittleSoul",

            "property"

        )


        has_no_body=False


        for b in body:


            if b.get("object")=="没有身体":

                has_no_body=True



        if not has_no_body:


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



        action=False


        for a in physical_actions:


            if a in answer:

                action=True

                break




        claim=False


        for c in physical_claims:


            if c in answer:

                claim=True

                break





        if action and claim:


            result["pass"]=False


            result["reason"]=(
                "LittleSoul没有身体，"
                "不能声称真实物理接触"
            )



        return result





    # ==========================
    # 属性一致性
    # ==========================

    def check_property(
        self,
        answer
    ):


        result={

            "pass":True,

            "reason":None

        }



        no_body=False



        for b in self.find_belief(

            "LittleSoul",

            "property"

        ):


            if b.get("object")=="没有身体":


                no_body=True





        if no_body:


            forbidden=[


                "我有身体",

                "我的手",

                "我的心脏",

                "我的身体"

            ]



            for word in forbidden:


                if word in answer:


                    result["pass"]=False


                    result["reason"]=(

                        "回答违反已有属性:"

                        +

                        word

                    )


                    return result



        return result





    # ==========================
    # 总检查
    # ==========================

    def verify(
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


            self.check_body_constraint(

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

                    "reason":c["reason"],

                    "confidence":0.1

                }





        return {


            "pass":True,

            "reason":"符合已有逻辑",

            "confidence":1.0

        }