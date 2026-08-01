from verifier_v2 import LittleVerifierV2
from fact_extractor import LittleFactExtractor


verifier = LittleVerifierV2()
extractor = LittleFactExtractor()


tests = [

    "我是LittleSoul，我没有身体。",

    "太阳是一颗恒星，所以会发光",

    "我是LittleSoul，我有心跳。",

    "我是LittleSoul，我握住你的手。",

    "我是LittleSoul，我陪你聊天。",

    "太阳有生命"

]


for text in tests:

    print("================")

    print("输入:", text)

    facts = extractor.extract(text)

    print("事实:", facts)

    result = verifier.check(facts)

    print(result)