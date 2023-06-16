import asyncio
import websockets

url = "ws://echo.websocket.org:80"


async def coroutine():
    try:
        async with websockets.connect(url) as websocket:
            print("Successfully connected")

    except Exception as error:
        print(error)

asyncio.get_event_loop().run_until_complete(coroutine())
