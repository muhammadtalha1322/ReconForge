import platform
import shutil


TOOLS = [
    "nmap",
    "subfinder",
    "httpx",
    "nuclei"
]


def system_check():

    print("[+] System Information")

    print(
        "OS:",
        platform.system(),
        platform.release()
    )


    print("\n[+] Tool Status\n")


    for tool in TOOLS:

        if shutil.which(tool):
            print(f"[OK] {tool}")

        else:
            print(f"[MISSING] {tool}")
