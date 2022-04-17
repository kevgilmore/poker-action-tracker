import asyncio
import time

import websockets

async def handler(websocket):
    while True:
        try:
            await websocket.send("hello from py")
            time.sleep(20)
        except Exception as e:
            print(e)


async def main():
    async with websockets.serve(handler, "", 5000):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
