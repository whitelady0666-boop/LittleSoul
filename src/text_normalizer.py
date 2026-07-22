import re


def normalize(text: str) -> str:
    """
    LittleSoul 输入标准化
    只处理输入格式，不改变语义
    """

    if text is None:
        return ""

    # 去掉首尾空格
    text = text.strip()

    # 全角空格
    text = text.replace("　", " ")

    # 多个空格压缩
    text = re.sub(r"\s+", " ", text)

    # 连续句号
    text = re.sub(r"[。]{2,}", "。", text)

    # 连续问号
    text = re.sub(r"[？?]{2,}", "？", text)

    # 连续感叹号
    text = re.sub(r"[！!]{2,}", "！", text)

    # 连续省略号
    text = re.sub(r"…{2,}", "……", text)

    return text