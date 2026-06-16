#!/usr/bin/env python3


import argparse


from core.engine import ReconEngine

from core.detector import system_check

from reports.generator import generate




BANNER="""

██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝


ReconForge
Automated Recon Framework

"""



def main():


    print(BANNER)



    parser=argparse.ArgumentParser(

        prog="reconforge"

    )


    sub=parser.add_subparsers(

        dest="cmd"

    )



    scan=sub.add_parser(

        "scan"

    )


    scan.add_argument(

        "-t",

        "--target",

        required=True

    )



    sub.add_parser(

        "check"

    )



    report=sub.add_parser(

        "report"

    )


    report.add_argument(

        "-i",

        "--input",

        required=True

    )




    args=parser.parse_args()



    if args.cmd=="scan":


        ReconEngine(

            args.target

        ).start()



    elif args.cmd=="check":


        system_check()



    elif args.cmd=="report":


        generate(

            args.input,

            "report.html"

        )



    else:


        parser.print_help()




if __name__=="__main__":

    main()
