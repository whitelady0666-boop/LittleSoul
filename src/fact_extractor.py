import re



class LittleFactExtractor:



    def extract(
        self,
        text
    ):


        facts=[]



        if not text:

            return facts




        entities=[

            "太阳",

            "地球",

            "LittleSoul"

        ]



        subject=None




        # ======================
        # 主体判断
        # ======================


        if "LittleSoul" in text:

            subject="LittleSoul"


        elif "太阳" in text:

            subject="太阳"


        elif "地球" in text:

            subject="地球"





        # 没有明确主体

        if subject is None:

            return []







        # ======================
        # 固定事实
        # ======================


        if "没有身体" in text:


            facts.append(

                {

                    "subject":"LittleSoul",

                    "relation":"property",

                    "object":"没有身体"

                }

            )







        # ======================
        # 类型关系
        # ======================


        match=re.search(

            r"(太阳|地球|LittleSoul)(?:是|是一|属于)([^，。！？]+)",

            text

        )



        if match:


            obj=match.group(2).strip()



            facts.append(

                {

                    "subject":match.group(1),

                    "relation":"type",

                    "object":obj

                }

            )








        # ======================
        # 属性关系
        # ======================


        match=re.search(

            r"(太阳|地球|LittleSoul)(?:有|拥有)([^，。！？]+)",

            text

        )


        if match:


            facts.append(

                {

                    "subject":match.group(1),

                    "relation":"property",

                    "object":
                    match.group(2).strip()

                }

            )








        # ======================
        # 动作检测
        # ======================

        # 只保留真实身体动作


        action_words=[


            "握住",

            "拥抱",

            "触摸",

            "走",

            "跑"

        ]



        for word in action_words:


            if word in text:


                facts.append(

                    {

                        "subject":
                        subject,


                        "relation":
                        "action",


                        "object":
                        word

                    }

                )





        # ======================
        # 去重
        # ======================


        result=[]


        for f in facts:


            if f not in result:

                result.append(f)




        return result