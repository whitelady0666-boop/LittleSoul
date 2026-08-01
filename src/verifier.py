class LittleVerifier:


    def __init__(
        self,
        evidence=None
    ):


        self.evidence = evidence



        # 基础错误规则

        self.rules = [

            {
                "wrong":"2+2=5",
                "reason":"基础数学错误"
            },


            {
                "wrong":"太阳绕地球转",
                "reason":"违反基础天文学事实"
            },


            {
                "wrong":"地球是平的",
                "reason":"违反基础科学事实"
            }

        ]




    # ======================
    # 原有规则检查
    # ======================


    def check_fact(
        self,
        text
    ):


        for rule in self.rules:


            if rule["wrong"] in text:


                return {

                    "pass":False,

                    "reason":rule["reason"]

                }



        return {


            "pass":True,

            "reason":"没有发现明显事实错误"


        }




    # ======================
    # 新增:
    # 证据链检查
    # ======================


    def check_evidence(
        self,
        fact
    ):


        if self.evidence is None:


            return {

                "support":False,

                "source":None,

                "confidence":0

            }



        return self.evidence.check_fact(
            fact
        )




    # ======================
    # 总入口
    # 保持兼容
    # ======================


    def check(
        self,
        text
    ):


        result = self.check_fact(
            text
        )


        return result