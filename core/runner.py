import asyncio
import os



async def execute(command):


    process = await asyncio.create_subprocess_exec(

        *command,

        stdout=asyncio.subprocess.PIPE,

        stderr=asyncio.subprocess.PIPE

    )


    out,err = await process.communicate()


    return {

        "stdout":out.decode(),

        "stderr":err.decode(),

        "code":process.returncode

    }



def run(command):


    return asyncio.run(
        execute(command)
    )



def save_raw(
    session,
    name,
    data
):


    path=session+"/raw"


    os.makedirs(
        path,
        exist_ok=True
    )


    with open(
        f"{path}/{name}.txt",
        "w"
    ) as f:

        f.write(data)
