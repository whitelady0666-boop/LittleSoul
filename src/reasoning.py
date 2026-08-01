import json
import os

from parser import LittleParser



class LittleReasoning:


    def __init__(
        self,
        belief_path="dataset/beliefs.json",
        concept_path="dataset/concepts.json"
    ):


        self.beliefs = []

        self.concepts = []

        self.parser = LittleParser()



        # ======================
        # 加载 beliefs
        # ======================


        if os.path.exists(
            belief_path
        ):


            with open(
                belief_path,
                "r",
                encoding="utf-8"
            ) as f:

                self.beliefs = json.load(f)




        # ======================
        # 加载 concepts
        # ======================


        if os.path.exists(
            concept_path
        ):


            with open(
                concept_path,
                "r",
                encoding="utf-8"
            ) as f:

                self.concepts = json.load(f)




    # ======================
    # 查找概念父级
    # ======================


    def get_parent_concept(
        self,
        word
    ):


        for concept in self.concepts:


            if concept["concept"] == word:


                return concept.get(
                    "parent"
                )


        return None





    # ======================
    # 身体约束检查
    # ======================


    def check_body_constraint(
        self,
        parsed
    ):


        ownership = parsed.get(
            "ownership",
            []
        )



        for belief in self.beliefs:


            if (

                belief.get("subject")
                ==
                "LittleSoul"

                and

                belief.get("property")
                ==
                "body"

                and

                belief.get("value")
                ==
                "none"

            ):



                for item in ownership:



                    parent = self.get_parent_concept(
                        item
                    )



                    if parent == "身体":


                        return {

                            "pass": False,

                            "reason":
                            "违反事实:LittleSoul没有身体，因此不能拥有"
                            +
                            item

                        }



        return None





    # ======================
    # 主检查入口
    # ======================


    def check(
        self,
        answer,
        context=None
    ):


        result = {

            "pass": True,

            "reason": ""

        }



        text = answer



        if context:


            text += "\n" + context




        # ======================
        # 语义解析
        # ======================


        parsed = self.parser.parse(
            text
        )



        # ======================
        # 身体事实检查
        # ======================


        body_result = self.check_body_constraint(
            parsed
        )



        if body_result:


            return body_result




        return result