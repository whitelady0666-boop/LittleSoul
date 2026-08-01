from belief_engine import BeliefEngine



engine=BeliefEngine()



tests=[

    "你有身体吗？",

    "你握住我的手",

    "你抱抱我"

]



for t in tests:


    print()

    print("================")

    print(

        "输入:",

        t

    )


    print(

        engine.infer(t)

    )