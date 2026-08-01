from property_reasoning import LittlePropertyReasoning



reasoning = LittlePropertyReasoning()



tests = [

    "心跳",

    "手",

    "吃饭",

    "不存在"

]



for item in tests:


    parent = reasoning.get_parent_concept(

        item

    )


    print(

        item,

        "属于:",

        parent

    )