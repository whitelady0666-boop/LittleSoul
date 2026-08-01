from knowledge import LittleKnowledge
from memory import LittleMemory
from reasoning_engine import ReasoningEngine



knowledge=LittleKnowledge()

memory=LittleMemory()



engine=ReasoningEngine(

    knowledge,

    memory

)



tests=[


    "太阳是什么？",

    "黑洞是什么？",

    "你有身体吗？",

    "你握住我的手",

    "今天工作很累",

    "你陪陪我"

]




for t in tests:


    print()

    print("================")

    print(

        "输入:",

        t

    )


    result=engine.reason(t)


    print(result)