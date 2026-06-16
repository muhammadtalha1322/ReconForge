import json
import os


from core.session import create_session

from core.parser import create_finding

from core.rules.cve import lookup

from core.rules.risk import score


from modules.passive.subdomains import enumerate_subdomains

from modules.active.port_scan import scan_ports

from modules.active.http_probe import probe_hosts

from modules.fingerprint.tech import detect

from modules.web.nuclei import scan




class ReconEngine:


    def __init__(self,target):

        self.target=target

        self.session=create_session(target)

        self.data={}


    def start(self):


        self.data["target"]=self.target



        subs=enumerate_subdomains(

            self.target,

            self.session

        )


        self.data["subdomains"]=subs



        self.data["alive"]=probe_hosts(

            subs["items"]

        )


        self.data["ports"]=scan_ports(

            self.target,

            self.session

        )



        self.data["technology"]=detect(

            self.target,

            self.session

        )



        self.data["nuclei"]=scan(

            self.target,

            self.session

        )



        self.data["cve"]=lookup(

            self.data

        )



        self.data["risk"]=score(
            "medium"
        )


        self.save()



    def save(self):


        os.makedirs(

            self.session,

            exist_ok=True

        )


        with open(

        self.session+"/results.json",

        "w"

        ) as f:


            json.dump(

            self.data,

            f,

            indent=4

            )
