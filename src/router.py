# src/router.py


class LittleRouter:


    def __init__(self):


        # ======================
        # 情感关键词
        # ======================

        self.emotion_words = [

            "累",
            "疲惫",
            "压力",
            "难过",
            "伤心",
            "孤独",
            "害怕",
            "焦虑",
            "失眠",
            "睡不着",
            "想哭",
            "不开心",
            "快乐",
            "幸福",
            "喜欢",
            "爱",
            "陪",
            "晚安",
            "早安"

        ]



        # ======================
        # 知识问题关键词
        # ======================

        self.knowledge_words = [

            "是什么",
            "什么是",
            "为什么",
            "怎么",
            "如何",
            "定义",
            "原理",
            "介绍",
            "解释"

        ]



        # ======================
        # 明确知识对象
        # ======================

        self.knowledge_entities = [

            "太阳",
            "地球",
            "黑洞",
            "宇宙",
            "星球",
            "恒星",
            "行星"

        ]




    def classify(self,text):


        text=text.strip()



        emotion_score=0

        knowledge_score=0



        # ======================
        # 情感评分
        # ======================

        for w in self.emotion_words:

            if w in text:

                emotion_score += 1



        # ======================
        # 知识评分
        # ======================

        for w in self.knowledge_words:

            if w in text:

                knowledge_score += 1



        for w in self.knowledge_entities:

            if w in text:

                knowledge_score += 2




        # ======================
        # 知识优先
        # ======================

        if knowledge_score >= 2:


            return "knowledge"



        if emotion_score >= 1:


            return "emotion"



        return "chat"