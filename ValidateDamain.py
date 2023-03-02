"""
in this part i will be checking the status of the resulted subdomains 
are they a live or not 
"""
import asyncio
import httpx
import time


async def check_statusCode(client, url):
        pokemon = await client.get(url)
        #pokemon = resp.status_code
        print(pokemon)
        # create a function that will keeps storing the values of the status code
        return pokemon

async def main(url):
    async with httpx.AsyncClient() as client:
        task = asyncio.create_task(check_statusCode(client,url))
        test = await asyncio.gather(task)
        print(task)


asyncio.run(main('https://www.youtube.com'))
        