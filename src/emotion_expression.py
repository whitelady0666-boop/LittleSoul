class EmotionExpressionDetector:


    def __init__(self):


        # ======================
        # 情感关键词
        # ======================

        self.emotion_keywords = [

            "爱",

            "喜欢",

            "幸福",

            "孤独",

            "害怕",

            "压力",

            "累",

            "疲惫",

            "难过",

            "伤心",

            "开心",

            "快乐",

            "希望",

            "相信",

            "感觉",

            "想你",

            "想我",

            "陪你",

            "陪伴",

            "守护",

            "温柔",

            "意义",

            "人生",

            "未来",

            "梦想",

            "孤单",

            "痛苦",

            "失眠",

            "委屈",

            "焦虑"

        ]




        # ======================
        # AI人格表达
        # ======================

        self.expression_patterns = [

            "我会",

            "我在",

            "我陪",

            "我希望",

            "我想",

            "我愿意",

            "我相信",

            "我觉得",

            "我理解",

            "我知道你"

        ]




        # ======================
        # 强情感表达
        # ======================

        self.strong_patterns = [

            "我爱你",

            "我想你",

            "我陪你",

            "我会一直在",

            "别怕",

            "不用担心",

            "我懂你",

            "我在这里",

            "辛苦了",

            "抱抱"

        ]





    def is_expression(
        self,
        text
    ):


        if not text:


            return False




        score=0




        # ======================
        # 强表达
        # ======================

        for pattern in self.strong_patterns:


            if pattern in text:


                return True





        # ======================
        # 普通情感词
        # ======================


        for word in self.emotion_keywords:


            if word in text:


                score+=1






        # ======================
        # 人格表达
        # ======================


        for pattern in self.expression_patterns:


            if pattern in text:


                score+=1





        # ======================
        # 判断
        # ======================


        # 至少三个特征

        if score>=3:


            return True




        return False