from verifier_v2 import LittleVerifierV2
from fact_extractor import LittleFactExtractor


verifier=LittleVerifierV2()

extractor=LittleFactExtractor()



tests=[

"我是LittleSoul，我没有身体。",

"太阳是一颗恒星，所以会发光",

"太阳有生命"

"我是LittleSoul，我握住你的手。",

]



for t in tests:


    print("================")

    print(t)


    facts=extractor.extract(t)


    print(
        "事实:",
        facts
    )


    result=verifier.check(
        facts
    )


    print(result)