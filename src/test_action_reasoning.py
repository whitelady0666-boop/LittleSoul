from action_reasoning import LittleActionReasoning



engine = LittleActionReasoning()



tests = [

    "握",

    "拥抱",

    "看",

    "跑",

    "不存在"

]


for action in tests:


    result = engine.get_requirement(
        action
    )


    print(
        action,
        "需要:",
        result
    )