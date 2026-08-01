class LittleEvidence:


    def __init__(
        self,
        inference,
        beliefs=None,
        knowledge=None
    ):

        self.inference = inference

        self.beliefs = beliefs or []

        self.knowledge = knowledge or []



    def same_fact(
        self,
        a,
        b
    ):

        return (

            a.get("subject")
            ==
            b.get("subject")

            and

            a.get("relation")
            ==
            b.get("relation")

            and

            a.get("object")
            ==
            b.get("object")

        )



    def check_fact(
        self,
        fact
    ):


        # ======================
        # 1. Knowledge
        # ======================


        for item in self.knowledge:


            if self.same_fact(

                item,

                fact

            ):


                return {

                    "support": True,

                    "source": "knowledge",

                    "confidence":
                    item.get(
                        "confidence",
                        1.0
                    )

                }





        # ======================
        # 2. Belief
        # ======================


        for item in self.beliefs:


            if self.same_fact(

                item,

                fact

            ):


                return {

                    "support": True,

                    "source": "belief",

                    "confidence":
                    item.get(
                        "confidence",
                        1.0
                    )

                }





        # ======================
        # 3. Inference
        # ======================


        result = self.inference.infer(

            self.knowledge
            +
            self.beliefs

        )


        facts = result.get(

            "facts",

            []

        )



        for item in facts:


            if self.same_fact(

                item,

                fact

            ):


                confidence = 0



                for chain in result.get(

                    "new_facts",

                    []

                ):


                    if self.same_fact(

                        chain["to"],

                        fact

                    ):


                        confidence = chain.get(

                            "confidence",

                            1.0

                        )

                        break



                return {

                    "support": True,

                    "source": "inference",

                    "confidence": confidence

                }





        # ======================
        # 4. 无证据
        # ======================


        return {

            "support": False,

            "source": None,

            "confidence":0

        }