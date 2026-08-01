from inference import LittleInference



engine = LittleInference()



facts = [

    {
        "subject":"太阳",
        "relation":"type",
        "object":"恒星"
    }

]



result = engine.infer(
    facts
)



print("推理结果:")



for item in result["facts"]:

    print(item)



print("\n证据链:")



for item in result["new_facts"]:

    print(
        item["from"],
        "=>",
        item["to"],
        "confidence:",
        item["confidence"]
    )