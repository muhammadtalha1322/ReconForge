from core.runner import run_command



def enumerate_subdomains(target, session):


    result = run_command(

        [

        "subfinder",

        "-d",

        target,

        "-silent"

        ],

        "subfinder",

        session

    )



    subs = result.get(
        "stdout",
        ""
    ).splitlines()



    return {


        "count":

        len(subs),


        "items":

        subs


    }
