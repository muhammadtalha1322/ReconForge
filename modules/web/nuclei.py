from core.runner import run,save_raw



def scan(target,session):


    result=run(

    [

    "nuclei",

    "-u",

    target,

    "-jsonl"

    ]

    )


    save_raw(

        session,

        "nuclei",

        result["stdout"]

    )


    return result["stdout"]
