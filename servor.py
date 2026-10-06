import websockets

def start_server():
    async def handler(websocket, path):
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")

    start_server = websockets.serve(handler, "localhost", 8765)
    return start_server