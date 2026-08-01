from knowledge import LittleKnowledge
from memory import LittleMemory

from belief_engine import BeliefEngine
from reasoning_engine import ReasoningEngine

from response_guard import ResponseGuard

from emotion_router import EmotionRouter
from emotional_reasoning import EmotionalReasoning

from emotional_concept import EmotionalConceptRouter


import random




class LittleSoulChat:



    def __init__(self):


        print("======================")
        print("LittleSoul初始化")
        print("======================")


        # =====================
        # 基础系统
        # =====================


        self.knowledge = LittleKnowledge()


        self.memory = LittleMemory()



        self.belief = BeliefEngine()



        self.guard = ResponseGuard(

            self.belief

        )



        self.reasoning = ReasoningEngine(

            knowledge=self.knowledge,

            memory=self.memory,

            belief=self.belief

        )



        # =====================
        # 情绪系统
        # =====================


        self.emotion_router = EmotionRouter()



        self.emotional_reasoning = EmotionalReasoning(

            self.belief

        )



        self.emotional_concept = EmotionalConceptRouter()



        # =====================
        # fallback人格
        # =====================


        self.fallbacks=[


            "我还不知道该怎么回答，不过我愿意和你一起探索。",


            "这个问题很特别。我想先听听你的想法。",


            "也许答案不是固定的，我们可以慢慢聊。",


            "我没有一个确定答案，但我愿意陪你一起想。"


        ]






    # =====================
    # 安全生成
    # =====================


    def safe_response(

        self,

        answer

    ):



        check=self.guard.check(

            answer

        )



        if check["pass"]:


            return answer



        return (

            "我没有身体，"

            "所以不能进行真实的物理接触，"

            "但我可以陪你交流。"

        )






    # =====================
    # 主聊天
    # =====================


    def chat(

        self,

        text

    ):



        print()

        print(

            "输入:",

            text

        )



        # ---------------------
        # 1 belief + reasoning
        # ---------------------


        result=self.reasoning.reason(

            text

        )



        print(

            "Reasoning:",

            result.get(

                "reasoning",

                {}

            )

        )



        if result.get(

            "answer"

        ):



            return self.safe_response(

                result["answer"]

            )





        # ---------------------
        # 2 情感概念
        # ---------------------


        concept=self.emotional_concept.match(

            text

        )



        if concept:


            return self.safe_response(

                concept["answer"]

            )







        # ---------------------
        # 3 情绪状态
        # ---------------------


        emotion=self.emotional_reasoning.generate(

            text

        )



        if emotion:


            return self.safe_response(

                emotion["answer"]

            )






        # ---------------------
        # 4 emotion memory
        # ---------------------


        emotion_memory=self.emotion_router.match(

            text

        )



        if emotion_memory:


            return self.safe_response(

                emotion_memory["assistant"]

            )






        # ---------------------
        # 5 fallback
        # ---------------------


        return random.choice(

            self.fallbacks

        )









def main():



    soul=LittleSoulChat()



    print()

    print("======================")

    print(

        "LittleSoul启动"

    )

    print(

        "输入 exit 退出"

    )

    print("======================")





    while True:


        try:


            text=input(

                "\n你："

            )



        except KeyboardInterrupt:


            break




        if text.strip()=="exit":


            break




        answer=soul.chat(

            text

        )



        print()



        print(

            "LittleSoul：",

            answer

        )







if __name__=="__main__":


    main()