import asyncio
import logging

from os import environ
from hydrogram import Client as tgClient
from . import multi_clients,work_loads,TelegramBot

async def initialize_clients():
    allTokens = dict(
        (c + 1, t)
        for c,(_, t) in enumerate(
            filter(
                lambda n: n[0].startswith("MULTI_CLIENT"), sorted(environ.items())
            )
        )
    )
    if not allTokens:
        multi_clients[0] = TelegramBot
        work_loads[0] = 0
        print("no additional clients found, using defatul client")
        return
    

    async def startClients(client_id,token):
        try:
            if len(token) >= 100:
                session_token=token
                bot_token=None
                print(f'Starting Client - {client_id} Using Session String')
            else:
                session_token=None
                bot_token=token
                print(f'Starting Client - {client_id} Using Session String')
            if client_id == len(allTokens):
                await asyncio.sleep(2)
                print("This Will take some time , please wait....")
            client = await tgClient(
                name=str(client_id),
                api_hash=TelegramBot.api_hash,
                api_id=TelegramBot.api_id,
                bot_token=bot_token,
                sleep_threshold=60,
                no_updates=True,
                session_string=session_token,
                in_memory=True
                ).start()

            client_id = (await client.get_me()).id
            work_loads[client_id] = 0
            return client_id,client
        except Exception:
            logging.error(f"Failed starting Client - {client_id} Error:", exc_info=True)

    clients = await asyncio.gather(*[startClients(i, token) for i, token in allTokens.items()])
    multi_clients.update(dict(clients))
    if len(multi_clients) != 1:
        TelegramBot.MULTI_CLIENT = True
        print("Multi-Client Mode Enabled")
    else:
        print("No additional clients were initialized, using default client")
