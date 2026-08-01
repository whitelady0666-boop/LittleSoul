class LittleParser:


    def __init__(self):


        # 明确拥有

        self.self_patterns = [

            "我的手",

            "我的身体",

            "我的心跳",

            "我的眼睛",

            "我的声音",

        ]


        # 拥有关系关键词

        self.ownership_words = [

            "有",

            "拥有",

            "具备",

            "具有",

        ]



    def parse(
        self,
        text
    ):


        result = {

            "subject": None,

            "ownership": [],

            "text": text

        }



        # ======================
        # 主体判断
        # ======================


        if "我" in text:


            result["subject"] = "LittleSoul"




        # ======================
        # 我的xxx
        # ======================


        for word in self.self_patterns:


            if word in text:


                result["ownership"].append(

                    word.replace(
                        "我的",
                        ""
                    )

                )




        # ======================
        # 我有xxx
        # ======================


        for key in self.ownership_words:


            if key in text:


                index = text.find(
                    key
                )


                after = text[

                    index + len(key):

                ]



                candidates = [

                    "手",

                    "心跳",

                    "身体",

                    "眼睛",

                    "声音",

                ]



                for item in candidates:


                    if item in after:


                        result["ownership"].append(
                            item
                        )



        return result