from core.runner import run_command



def scan_ports(target, session):


    result = run_command(

        [

        "nmap",

        "-sV",

        "-T4",

        target

        ],

        "nmap",

        session

    )


    return result.get(
        "stdout",
        ""
    )
