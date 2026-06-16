from core.runner import run_command



def detect(target, session):


    result = run_command(

        [

        "whatweb",

        target

        ],

        "whatweb",

        session

    )


    return result.get(
        "stdout",
        ""
    )
