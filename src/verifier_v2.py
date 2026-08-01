import json
import os


from evidence import LittleEvidence
from inference import LittleInference
from belief_engine import BeliefEngine
from fact_adapter import LittleFactAdapter




class LittleVerifierV2:


    def __init__(self):


        self.inference = LittleInference()


        self.adapter = LittleFactAdapter()


        self.belief_engine = BeliefEngine()


        self.beliefs = self.belief_engine.beliefs



        self.knowledge = self.load_knowledge()



        print(

            "BELIEFS:",

            self.beliefs

        )


        print(

            "KNOWLEDGE:",

            self.knowledge

        )



        self.evidence = LittleEvidence(

            inference=self.inference,

            beliefs=self.beliefs,

            knowledge=self.knowledge

        )





    # ==========================
    # knowledge
    # ==========================


    def load_knowledge(self):


        path="dataset/fact_knowledge.json"


        if not os.path.exists(path):

            return []



        with open(

            path,

            "r",

            encoding="utf-8"

        ) as f:


            data=json.load(f)



        return self.adapter.convert_fact_list(

            data,

            "knowledge"

        )





    # ==========================
    # belief检查
    # ==========================


    def check_belief_constraint(

        self,

        facts

    ):



        result={

            "pass":True,

            "conflicts":[]

        }




        for fact in facts:



            # 动作事实

            if fact.get(

                "relation"

            )=="action":



                action=fact.get(

                    "object",

                    ""

                )



                physical_actions=[

                    "握",

                    "抱",

                    "牵",

                    "触摸",

                    "摸"

                ]



                need_body=False



                for word in physical_actions:


                    if word in action:


                        need_body=True

                        break




                if need_body:



                    for belief in self.beliefs:



                        if (

                            belief["subject"]

                            =="LittleSoul"

                            and

                            belief["relation"]

                            =="property"

                            and

                            belief["object"]

                            =="没有身体"

                        ):



                            result["pass"]=False



                            result["conflicts"].append(

                                "LittleSoul没有身体，不能执行真实物理接触动作"

                            )





            # 属性事实

            if fact.get(

                "relation"

            )=="property":



                prop=fact.get(

                    "object",

                    ""

                )



                forbidden=[

                    "身体",

                    "手",

                    "心脏",

                    "心跳"

                ]



                if prop in forbidden:



                    for belief in self.beliefs:



                        if (

                            belief["subject"]

                            =="LittleSoul"

                            and

                            belief["object"]

                            =="没有身体"

                        ):



                            result["pass"]=False



                            result["conflicts"].append(

                                "LittleSoul没有身体，不能拥有:"+prop

                            )





        return result





    # ==========================
    # evidence检查
    # ==========================


    def check_evidence(

        self,

        facts

    ):



        evidence=[]



        for fact in facts:



            result=self.evidence.check_fact(

                fact

            )



            evidence.append(result)



            if not result["support"]:



                return {

                    "pass":False,

                    "reason":"缺少证据支持",

                    "facts":facts,

                    "evidence":evidence

                }



        return {

            "pass":True,

            "facts":facts,

            "evidence":evidence

        }







    # ==========================
    # main
    # ==========================


    def check(

        self,

        facts

    ):



        if not facts:


            return {

                "pass":True,

                "reason":"无事实",

                "facts":[]

            }




        belief_result=self.check_belief_constraint(

            facts

        )



        if not belief_result["pass"]:


            return {


                "pass":False,

                "reason":";".join(

                    belief_result["conflicts"]

                ),

                "facts":facts

            }





        return self.check_evidence(

            facts

        )