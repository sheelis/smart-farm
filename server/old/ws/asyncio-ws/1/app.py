#!/usr/bin/env python

# open the html file after running this app

import asyncio
import datetime
import random
import websockets


async def time(websocket, path):
    print("browser opened")
    while True:
        now = datetime.datetime.utcnow().isoformat() + ' Z'
        tosend = '{"time":"' + now + '", "word":"bigg"}'
        await websocket.send(tosend)
        await asyncio.sleep(1)

async def button(websocket, path):
    print("shit recaived")

start_server = websockets.serve(time, '127.0.0.1', 5678)
print("server started")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
