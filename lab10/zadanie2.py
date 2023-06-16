import asyncio
import websockets

url = "ws://echo.websocket.org:80"
# url = "ws://127.0.0.1:8080"


async def coroutine():
    try:
        async with websockets.connect(url) as websocket:
            await websocket.send("Hello server!")
            res = await websocket.recv()
            print(f"Received from a server: {res}")

    except Exception as error:
        print(error)

asyncio.get_event_loop().run_until_complete(coroutine())
