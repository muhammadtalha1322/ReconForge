import asyncio


async def run_task(task):

    return await task



async def execute(tasks):

    return await asyncio.gather(*tasks)
