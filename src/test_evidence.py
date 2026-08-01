from inference import LittleInference
from evidence import LittleEvidence



engine = LittleInference()



knowledge = [

    {
        "subject":"太阳",
        "relation":"type",
        "object":"恒星"
    }

]



checker = LittleEvidence(

    engine,

    knowledge=knowledge

)



tests = [


    {
        "subject":"太阳",
        "relation":"property",
        "object":"发光"
    },


    {
        "subject":"太阳",
        "relation":"property",
        "object":"可被观察"
    },


    {
        "subject":"太阳",
        "relation":"property",
        "object":"有生命"
    }

]



for t in tests:


    print(

        t,

        "=>",

        checker.check_fact(t)

    )