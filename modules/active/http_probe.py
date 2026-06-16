from core.runner import run_command



def probe_hosts(hosts):


    if not hosts:

        return []



    result = run_command(

        [

        "httpx",

        "-silent",

        "-l",

        "-"

        ]

    )



    return result.get(
        "stdout",
        ""
    ).splitlines()
