def score(level):


    table={

    "critical":10,

    "high":8,

    "medium":5,

    "low":2,

    "info":1

    }


    return table.get(
        level,
        1
    )
