class EmotionIntentDetector:


    def __init__(self):

        self.patterns=[

            "握住",
            "牵手",
            "抱",
            "拥抱",
            "陪我",
            "想你",
            "需要你",
            "靠近",
            "留下",
            "不要走"

        ]


    def detect(self,text):


        for p in self.patterns:

            if p in text:

                return True


        return False