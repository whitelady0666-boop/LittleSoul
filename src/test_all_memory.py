import json
import os

from memory import LittleMemory



# 初始化

memory = LittleMemory()



# 项目根目录

base_dir = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


data_path=os.path.join(
    base_dir,
    "dataset",
    "emotion.jsonl"
)



total=0

success=0



print("====================")
print("开始测试100条Memory")
print("====================")



with open(
    data_path,
    "r",
    encoding="utf-8"
) as f:


    for line in f:


        item=json.loads(line)


        user=item["user"]

        answer=item["assistant"]



        result=memory.search(
            user
        )



        total+=1



        if result==answer:


            success+=1


            print(
                "PASS:",
                user
            )


        else:


            print(
                "FAIL:",
                user
            )

            print(
                "期望:",
                answer
            )

            print(
                "得到:",
                result
            )



print("====================")

print(
    "测试完成:",
    success,
    "/",
    total
)

print("====================")