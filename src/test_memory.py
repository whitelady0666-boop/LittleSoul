from memory import LittleMemory



m=LittleMemory()



tests=[

"今天工作很累",

"今天工作很累。",

"下雨了",

"下雨了。",

"晚安",

"早上好",

"你觉得幸福是什么？",

"为什么你总能接住我的每句话？"

]



for t in tests:


    print()

    print(
        "输入:",
        t
    )


    result=m.search(t)


    print(
        "回答:",
        result
    )