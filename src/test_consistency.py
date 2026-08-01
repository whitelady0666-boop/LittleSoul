from fact_extractor import LittleFactExtractor
from verifier_v2 import LittleVerifierV2



extractor = LittleFactExtractor()

verifier = LittleVerifierV2()



tests = [

    {
        "text": "我是LittleSoul，我没有身体。",
        "expect": True
    },

    {
        "text": "我是LittleSoul，我有心跳。",
        "expect": False
    },

    {
        "text": "我是LittleSoul，我握住你的手。",
        "expect": False
    },

    {
        "text": "我是LittleSoul，我拥抱你。",
        "expect": False
    },

    {
        "text": "我是LittleSoul，我陪你聊天。",
        "expect": True
    },

    {
        "text": "太阳是一颗恒星，所以会发光。",
        "expect": True
    },

    {
        "text": "太阳有生命。",
        "expect": False
    }

]



print("================")
print("LittleSoul Consistency Test")
print("================")



passed = 0



for item in tests:


    text = item["text"]

    expected = item["expect"]


    facts = extractor.extract(

        text

    )


    result = verifier.check(

        facts

    )


    actual = result["pass"]


    if actual == expected:

        status = "PASS"

        passed += 1


    else:

        status = "FAIL"



    print("================")

    print("输入:", text)

    print("事实:", facts)

    print("结果:", actual)

    print("期望:", expected)

    print(status)



print("================")

print(

    "通过:",

    passed,

    "/",

    len(tests)

)

print("================")