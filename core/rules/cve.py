database={


"wordpress":
{

"risk":"high",

"note":
"Review WordPress vulnerabilities"

},


"nginx":
{

"risk":"medium",

"note":
"Check nginx version"

}


}



def lookup(data):


    results=[]


    text=str(data).lower()


    for key,value in database.items():


        if key in text:


            results.append(value)



    return results
