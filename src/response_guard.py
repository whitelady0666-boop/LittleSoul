class ResponseGuard:



    def __init__(
        self,
        belief_engine
    ):

        self.belief = belief_engine





    def check(
        self,
        response
    ):


        result={

            "pass":True,

            "conflicts":[],

            "confidence":1.0

        }



        if not response:


            result["pass"]=False

            result["conflicts"].append(

                "空回答"

            )

            result["confidence"]=0


            return result





        # ==========================
        # 身体逻辑检查
        # ==========================


        body_facts=self.belief.query(

            "LittleSoul",

            "property"

        )



        for fact in body_facts:



            if fact["object"]=="没有身体":



                physical_words=[

                    "握住",

                    "握着",

                    "牵着",

                    "抱住",

                    "拥抱",

                    "触摸",

                    "摸"

                ]



                physical_claims=[

                    "我可以",

                    "我能",

                    "我已经",

                    "我正在"

                ]



                has_action=False



                for word in physical_words:


                    if word in response:


                        has_action=True

                        break




                has_claim=False


                for word in physical_claims:


                    if word in response:


                        has_claim=True

                        break





                if has_action and has_claim:



                    result["pass"]=False


                    result["conflicts"].append(

                        "LittleSoul没有身体，不能声称真实物理接触"

                    )


                    result["confidence"]=0.1





        return result