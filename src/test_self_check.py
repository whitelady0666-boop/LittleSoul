from belief_engine import BeliefEngine
from self_check import SelfCheckEngine



belief=BeliefEngine()


checker=SelfCheckEngine(

    belief_engine=belief

)



tests=[


    "我没有身体，但我会陪你聊天。",


    "我可以握住你的手。",


    "我正在拥抱你。",


    "我是一个没有身体的AI。"

]



for t in tests:


    print()

    print("================")

    print(t)


    print(

        checker.check(t)

    )