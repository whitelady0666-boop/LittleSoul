import json


src = "dataset/emotion.jsonl"
dst = "dataset/emotion_fixed.jsonl"


def fix_text(s):

    try:
        return s.encode("gbk").decode("utf-8")
    except:
        return s


with open(
    src,
    "r",
    encoding="utf-8"
) as f:

    lines = f.readlines()


with open(
    dst,
    "w",
    encoding="utf-8"
) as f:

    for line in lines:

        try:

            data = json.loads(line)

            data["user"] = fix_text(
                data["user"]
            )

            data["assistant"] = fix_text(
                data["assistant"]
            )

            f.write(
                json.dumps(
                    data,
                    ensure_ascii=False
                )
                + "\n"
            )

        except Exception as e:

            print(
                "skip:",
                line[:50],
                e
            )


print("done")