import asyncio
import websockets


async def connection_handler(websocket, path):
    async for message in websocket:
        print(f"Received from a client: {message}")
        response = message.upper()
        await websocket.send(response)


if __name__ == "__main__":
    start = websockets.serve(connection_handler, "127.0.0.1", 8080)

    asyncio.get_event_loop().run_until_complete(start)

    print("Server is running...")

    asyncio.get_event_loop().run_forever()
