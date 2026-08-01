import time


class ContextMemory:


    def __init__(
        self,
        max_history=10
    ):

        self.max_history = max_history


        self.history = []


        self.current_topic = None


        self.emotion_state = None


        self.facts = []





    # ==========================
    # 添加对话
    # ==========================

    def add_turn(
        self,
        user,
        assistant
    ):


        item = {

            "user": user,

            "assistant": assistant,

            "time": time.time()

        }


        self.history.append(

            item

        )


        if len(self.history) > self.max_history:


            self.history.pop(0)





    # ==========================
    # 获取历史
    # ==========================

    def get_history(
        self
    ):


        return self.history





    # ==========================
    # 最近一次对话
    # ==========================

    def last_turn(
        self
    ):


        if not self.history:

            return None


        return self.history[-1]





    # ==========================
    # 设置主题
    # ==========================

    def set_topic(
        self,
        topic
    ):


        self.current_topic = topic





    def get_topic(
        self
    ):


        return self.current_topic





    # ==========================
    # 情绪状态
    # ==========================

    def set_emotion(
        self,
        emotion
    ):


        self.emotion_state = emotion





    def get_emotion(
        self
    ):


        return self.emotion_state





    # ==========================
    # 保存事实
    # ==========================

    def add_fact(
        self,
        fact
    ):


        if fact not in self.facts:


            self.facts.append(

                fact

            )





    def get_facts(
        self
    ):


        return self.facts





    # ==========================
    # 上下文摘要
    # ==========================

    def summary(
        self
    ):


        return {


            "history":

            self.history,


            "topic":

            self.current_topic,


            "emotion":

            self.emotion_state,


            "facts":

            self.facts

        }





    # ==========================
    # 清空
    # ==========================

    def clear(
        self
    ):


        self.history.clear()


        self.current_topic = None


        self.emotion_state = None


        self.facts.clear()