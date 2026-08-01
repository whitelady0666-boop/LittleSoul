from fact_extractor import LittleFactExtractor


extractor = LittleFactExtractor()


tests = [

    "我是LittleSoul，我握住你的手。",

    "我是LittleSoul，我拥抱你。",

    "我是LittleSoul，我看见你。"

]


for text in tests:

    print("================")

    print("输入:", text)

    result = extractor.extract(text)

    print("事实:")

    for fact in result:

        print(fact)