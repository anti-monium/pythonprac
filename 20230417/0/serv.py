import asyncio
from prog import sqroots

async def echo(reader, writer):
    while data := await reader.readline():
        data = data.decode()
        writer.write(sqroots(data).encode())
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(echo, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
