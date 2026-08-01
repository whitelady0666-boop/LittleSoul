from fact_extractor import LittleFactExtractor


extractor = LittleFactExtractor()



tests=[

    "太阳是一颗恒星，所以会发光",

    "LittleSoul没有身体",

    "太阳会发光"

]


for t in tests:

    print(
        t
    )

    print(
        extractor.extract(t)
    )