import json
import os
import difflib


class LittleMemory:

    def __init__(self):

        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        self.data_path = os.path.join(
            base_dir,
            "dataset",
            "emotion.jsonl"
        )

        self.memory = []

        self.load()


    def load(self):

        with open(
            self.data_path,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                item = json.loads(line)

                self.memory.append(
                    {
                        "user": item["user"],
                        "assistant": item["assistant"]
                    }
                )


        print(
            "Memory加载:",
            len(self.memory)
        )


    def normalize(
        self,
        text
    ):

        text = text.strip()


        replace = {

            "?": "？",

            "!": "！",

            ",": "，",

            ".": "。",

            " ": ""

        }


        for a, b in replace.items():

            text = text.replace(
                a,
                b
            )


        return text



    def similarity(
        self,
        a,
        b
    ):


        # ======================
        # 顺序相似度
        # ======================

        sequence_score = difflib.SequenceMatcher(

            None,

            a,

            b

        ).ratio()



        # ======================
        # 字符覆盖
        # ======================

        common = 0


        for ch in a:

            if ch in b:

                common += 1



        if len(a) > 0:

            coverage = (

                common /

                len(a)

            )

        else:

            coverage = 0



        # ======================
        # 无序字符匹配
        # ======================

        set_a = set(a)

        set_b = set(b)


        if len(set_a) > 0:

            unordered_score = (

                len(

                    set_a & set_b

                )

                /

                len(set_a)

            )

        else:

            unordered_score = 0



        # ======================
        # 综合评分
        # ======================

        score = (

            sequence_score * 0.55

            +

            coverage * 0.25

            +

            unordered_score * 0.20

        )



        # ======================
        # 长度差惩罚
        # ======================

        length_diff = abs(

            len(a) - len(b)

        )


        if length_diff > 15:

            score -= 0.05



        return min(

            max(

                score,

                0

            ),

            1.0

        )



    def search(

        self,

        query,

        threshold=0.60

    ):


        query = self.normalize(
            query
        )


        # ======================
        # 短句保护
        # ======================

        if len(query) <= 5:

            threshold = 0.45



        candidates = []



        for item in self.memory:


            user_text = self.normalize(

                item["user"]

            )


            score = self.similarity(

                query,

                user_text

            )


            candidates.append(

                (

                    score,

                    item["assistant"]

                )

            )



        candidates.sort(

            key=lambda x: x[0],

            reverse=True

        )



        best_score, best_answer = candidates[0]



        print(

            "Memory匹配:",

            round(

                best_score,

                3

            )

        )



        if best_score >= threshold:

            return best_answer



        return None