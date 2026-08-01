import json
import os



class LittleInference:


    def __init__(
        self,
        rule_path="dataset/rules.json"
    ):


        self.rules = []


        if os.path.exists(rule_path):

            with open(
                rule_path,
                "r",
                encoding="utf-8"
            ) as f:

                self.rules = json.load(f)




    def match(
        self,
        fact,
        condition
    ):


        return (

            fact.get("subject")
            ==
            condition.get("subject")

            and

            fact.get("relation")
            ==
            condition.get("relation")

            and

            fact.get("object")
            ==
            condition.get("object")

        )




    def infer(
        self,
        facts
    ):


        known = list(facts)


        evidence = []


        changed = True



        while changed:


            changed = False



            for rule in self.rules:



                condition = rule["if"]

                conclusion = rule["then"]



                matched = False



                for fact in known:


                    if self.match(
                        fact,
                        condition
                    ):


                        matched = True

                        break



                if matched:



                    new_fact = conclusion.copy()



                    if new_fact not in known:



                        known.append(
                            new_fact
                        )



                        evidence.append(
    {
        "from": condition,

        "to": new_fact,

        "confidence":
            rule.get(
                "confidence",
                1.0
            )
    }
)



                        changed = True




        return {

            "facts": known,

            "new_facts": evidence

        }