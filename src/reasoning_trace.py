class ReasoningTrace:



    def __init__(

        self

    ):


        self.steps = []


        self.evidence = []


        self.conflicts = []


        self.confidence = 1.0





    # ==========================
    # 添加推理步骤
    # ==========================

    def add_step(

        self,

        step

    ):


        self.steps.append(

            step

        )





    # ==========================
    # 添加证据
    # ==========================

    def add_evidence(

        self,

        source,

        fact

    ):


        self.evidence.append(

            {

                "source":

                source,


                "fact":

                fact

            }

        )





    # ==========================
    # 添加冲突
    # ==========================

    def add_conflict(

        self,

        conflict

    ):


        self.conflicts.append(

            conflict

        )


        self.confidence *= 0.1





    # ==========================
    # 设置置信度
    # ==========================

    def set_confidence(

        self,

        value

    ):


        self.confidence=value





    # ==========================
    # 输出
    # ==========================

    def export(

        self

    ):


        return {


            "steps":

            self.steps,


            "evidence":

            self.evidence,


            "conflicts":

            self.conflicts,


            "confidence":

            self.confidence


        }





    # ==========================
    # 清空
    # ==========================

    def clear(

        self

    ):


        self.steps.clear()


        self.evidence.clear()


        self.conflicts.clear()


        self.confidence=1.0