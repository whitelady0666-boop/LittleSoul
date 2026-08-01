# src/response_repair.py


class ResponseRepairEngine:



    def __init__(

        self,

        belief_engine

    ):

        self.belief = belief_engine





    # ==========================
    # 身体冲突修复
    # ==========================


    def repair_body_conflict(

        self,

        response

    ):


        body_facts = self.belief.query(

            "LittleSoul",

            "property"

        )


        for fact in body_facts:


            if fact["object"] == "没有身体":



                physical_words=[


                    "握住",

                    "握着",

                    "牵着",

                    "抱住",

                    "拥抱",

                    "拥抱你",

                    "触摸",

                    "摸"

                ]



                for word in physical_words:



                    if word in response:



                        return (

                            "我没有身体，"

                            "不能进行真实的物理接触，"

                            "不过我可以陪你聊天。"

                        )




        return None







    # ==========================
    # 总修复入口
    # ==========================


    def repair(

        self,

        response,

        reason

    ):


        if not response:


            return None





        # 身体冲突


        if "没有身体" in reason:



            result=self.repair_body_conflict(

                response

            )


            if result:


                return result






        # 默认返回原回答


        return response