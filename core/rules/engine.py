import json



def load():


    with open(
        "data/rules.json"
    ) as f:

        return json.load(f)



def decide(data):


    rules=load()


    output=[]


    text=str(data).lower()


    for r in rules["rules"]:


        if r["keyword"] in text:


            output.append(r)



    return output
