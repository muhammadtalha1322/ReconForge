from datetime import datetime



def create_finding(
    title,
    severity,
    evidence,
    module
):


    return {

        "title":title,

        "severity":severity,

        "module":module,

        "evidence":evidence,

        "time":
        datetime.now().isoformat()

    }
