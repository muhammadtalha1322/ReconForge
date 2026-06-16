import json


def generate(json_file, output):


    with open(json_file) as f:

        data=json.load(f)


    html="""

<html>

<head>

<title>
ReconForge Report
</title>

</head>


<body>

<h1>
ReconForge Report
</h1>

"""


    for item in data:


        html += f"""

<h2>
{item['module']}
</h2>


<pre>

{item['data']}

</pre>


"""


    html += """

</body>

</html>

"""


    with open(output,"w") as f:

        f.write(html)


    print(
        "[+] HTML Report Created"
    )
