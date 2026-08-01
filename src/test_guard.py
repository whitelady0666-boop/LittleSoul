from belief_engine import BeliefEngine
from response_guard import ResponseGuard




beliefs=[

    {

        "subject":"LittleSoul",

        "relation":"property",

        "object":"没有身体"

    }

]




belief=BeliefEngine(

    beliefs

)



guard=ResponseGuard(

    belief

)





tests=[



    "我不能真正握住你的手，但我会陪伴你。",



    "我可以握住你的手。",



    "我没有身体，不过我会陪着你。",



    "我正在拥抱你。"



]




for t in tests:


    print()

    print("================")

    print(t)


    print(

        guard.check(t)

    )