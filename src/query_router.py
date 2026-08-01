# ==========================
# LittleSoul Query Router
# ==========================


class LittleQueryRouter:


    def __init__(self):


        # ======================
        # 知识问题关键词
        # ======================

        self.knowledge_patterns = [

            "是什么",
            "是什么？",
            "什么是",
            "为什么",
            "怎么形成",
            "如何形成",
            "介绍一下",
            "解释一下",
            "定义",
            "原理",
            "原因",
            "作用",
            "区别",
            "有什么特点"

        ]


        # ======================
        # 情感/陪伴关键词
        # ======================

        self.emotion_patterns = [

            "累",
            "疲惫",
            "难过",
            "伤心",
            "孤独",
            "害怕",
            "焦虑",
            "睡不着",
            "压力",
            "烦",
            "开心",
            "快乐",
            "喜欢",
            "爱",
            "想你",
            "陪我",
            "安慰"

        ]



        # ======================
        # LittleSoul自我问题
        # ======================

        self.self_patterns = [

            "你有",
            "你会",
            "你是不是",
            "你能不能",
            "你是什么",
            "你是谁",
            "你真实",
            "你存在",
            "你有记忆"

        ]




    def classify(self, text):


        text = text.strip()



        # ======================
        # 知识优先
        # ======================

        for p in self.knowledge_patterns:


            if p in text:


                return "knowledge"



        # ======================
        # 情感
        # ======================

        for p in self.emotion_patterns:


            if p in text:


                return "emotion"



        # ======================
        # 关于LittleSoul自身
        # ======================

        for p in self.self_patterns:


            if p in text:


                return "self"



        # ======================
        # 默认聊天
        # ======================

        return "chat"