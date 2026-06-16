import os
import datetime


def create_session(target):

    timestamp = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    name = (
        target.replace(".","_")
        +
        "_"
        +
        timestamp
    )


    path = (
        "output/sessions/"
        +
        name
    )


    os.makedirs(
        path,
        exist_ok=True
    )


    return path
