class Colors:

    RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    END = "\033[0m"



def info(msg):
    print(
        Colors.BLUE +
        "[*] " +
        msg +
        Colors.END
    )



def success(msg):

    print(
        Colors.GREEN +
        "[+] " +
        msg +
        Colors.END
    )
