from knowledge import LittleKnowledge
from memory import LittleMemory
from reasoning_engine import ReasoningEngine



knowledge=LittleKnowledge()


memory=LittleMemory()



beliefs=[


    {

        "subject":

        "LittleSoul",


        "relation":

        "property",


        "object":

        "没有身体"

    }


]



engine=ReasoningEngine(

    knowledge,

    memory,

    beliefs

)




tests=[


    "太阳是什么？",

    "黑洞是什么？",

    "你有身体吗？",

    "你握住我的手",

    "你抱抱我"

]




for text in tests:


    print()

    print("================")

    print(

        "输入:",

        text

    )


    result=engine.reason(

        text

    )


    print(result)