class BeliefEngine:


    def __init__(

        self,

        beliefs=None

    ):


        if beliefs is None:

            self.beliefs=[

                {
                    "subject":"LittleSoul",
                    "relation":"property",
                    "object":"没有身体",
                    "confidence":1.0,
                    "source":"belief"
                },

                {
                    "subject":"LittleSoul",
                    "relation":"ability",
                    "object":"可以理解文字",
                    "confidence":1.0,
                    "source":"belief"
                },

                {
                    "subject":"LittleSoul",
                    "relation":"ability",
                    "object":"可以进行逻辑分析",
                    "confidence":1.0,
                    "source":"belief"
                }

            ]


        else:

            self.beliefs=[]


            for b in beliefs:


                self.beliefs.append(

                    {

                        "subject":b.get("subject"),

                        "relation":b.get("relation"),

                        "object":b.get("object"),

                        "confidence":b.get(
                            "confidence",
                            1.0
                        ),

                        "source":b.get(
                            "source",
                            "belief"
                        )

                    }

                )


        print(
            "BELIEFS:",
            self.beliefs
        )



    def query(

        self,

        subject,

        relation=None

    ):


        results=[]


        for belief in self.beliefs:


            if belief["subject"] != subject:

                continue


            if relation is not None:

                if belief["relation"] != relation:

                    continue


            results.append(

                belief

            )


        return results




    def infer(

        self,

        text

    ):


        result={

            "answer":None,

            "facts":[],

            "confidence":0

        }



        body=self.query(

            "LittleSoul",

            "property"

        )


        has_no_body=False


        for b in body:


            if b["object"]=="没有身体":

                has_no_body=True



        if has_no_body:


            physical_words=[

                "握",

                "抱",

                "牵",

                "摸",

                "触"

            ]


            for word in physical_words:


                if word in text:


                    result["answer"] = "无法进行真实物理接触"


                    result["facts"].append(

                        "LittleSoul没有身体"

                    )


                    result["confidence"]=0.95


                    return result




            if "身体" in text or "心跳" in text:


                result["answer"]="没有身体"


                result["facts"].append(

                    "LittleSoul没有身体"

                )


                result["confidence"]=1.0


                return result




        return result