class LittleFact:


    def __init__(
        self,
        subject,
        relation,
        object,
        confidence=1.0,
        source=None
    ):

        self.subject = subject

        self.relation = relation

        self.object = object

        self.confidence = confidence

        self.source = source



    def to_dict(self):

        return {

            "subject": self.subject,

            "relation": self.relation,

            "object": self.object,

            "confidence": self.confidence,

            "source": self.source

        }



    def __eq__(self, other):

        if isinstance(other, dict):

            return (

                self.subject
                ==
                other.get("subject")

                and

                self.relation
                ==
                other.get("relation")

                and

                self.object
                ==
                other.get("object")

            )


        return False