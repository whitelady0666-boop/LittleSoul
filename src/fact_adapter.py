from fact import LittleFact



class LittleFactAdapter:



    def convert_beliefs(
        self,
        beliefs
    ):

        facts=[]


        for item in beliefs:


            subject=item.get(
                "subject"
            )


            prop=item.get(
                "property"
            )


            value=item.get(
                "value"
            )


            # LittleSoul身体约束

            if (

                subject=="LittleSoul"

                and

                prop=="body"

                and

                value=="none"

            ):


                facts.append(

                    LittleFact(

                        "LittleSoul",

                        "property",

                        "没有身体",

                        1.0,

                        "belief"

                    ).to_dict()

                )



            else:


                facts.append(

                    LittleFact(

                        subject,

                        prop,

                        value,

                        1.0,

                        "belief"

                    ).to_dict()

                )


        return facts





    def convert_fact_list(
        self,
        facts,
        source="knowledge"
    ):


        result=[]


        for f in facts:


            result.append(

                LittleFact(

                    f["subject"],

                    f["relation"],

                    f["object"],

                    f.get(
                        "confidence",
                        1.0
                    ),

                    source

                ).to_dict()

            )


        return result