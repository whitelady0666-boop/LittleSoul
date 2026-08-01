class LittleWorldModel:


    def __init__(
        self,
        belief_engine,
        knowledge,
        memory
    ):


        self.belief = belief_engine

        self.knowledge = knowledge

        self.memory = memory



    # ======================
    # 查询belief
    # ======================

    def query_belief(
        self,
        subject,
        relation=None
    ):


        return self.belief.query(

            subject,

            relation

        )



    # ======================
    # 查询知识
    # ======================

    def query_knowledge(
        self,
        text
    ):


        return self.knowledge.search(

            text

        )



    # ======================
    # 查询记忆
    # ======================

    def query_memory(
        self,
        text
    ):


        return self.memory.search(

            text

        )



    # ======================
    # 世界事实
    # ======================

    def get_self_facts(self):


        return self.query_belief(

            "LittleSoul"

        )



    # ======================
    # 冲突检测
    # ======================

    def check_conflict(
        self,
        statement
    ):


        facts=self.get_self_facts()



        for fact in facts:


            # 没有身体

            if (

                fact["object"]=="没有身体"

            ):


                physical_words=[

                    "握住",

                    "牵着",

                    "抱住",

                    "拥抱",

                    "触摸",

                    "摸"

                ]



                for word in physical_words:


                    if word in statement:


                        return {

                            "conflict":True,

                            "reason":
                            "LittleSoul没有身体，不能进行真实物理接触"

                        }



        return {


            "conflict":False,

            "reason":""

        }