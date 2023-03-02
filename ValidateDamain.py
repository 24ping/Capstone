"""
in this part i will be checking the status of the resulted subdomains 
are they a live or not 
"""
import asyncio
import httpx
import time
from subEnum import valid_domain
import ssl

def response_type(response):
     total_responses = []
     total_responses.append(response)

async def check_statusCode(client, url):
    try :    
        protocol_1 = 'https://'
        pokemon = await client.get(protocol_1+url)
        #pokemon = resp.status_code
        print(pokemon)
        return pokemon
    except ssl.SSLCertVerificationError as error:
        print("Error Caught SSL ",error)
    except httpx.ConnectError as error:
        print("Error Caught as httpx exception",error)
    except Exception as error:
        print("Error Caught as plain exception",error)


async def main(urls):
    async with httpx.AsyncClient() as client:
        for url in urls:
            task = asyncio.create_task(check_statusCode(client,url))
            await asyncio.gather(task)


list_dm =["cms.youtube.com","www.youtube.com","checkout.youtube.com"]
asyncio.run(main(valid_domain))
print(valid_domain)
