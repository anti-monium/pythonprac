import asyncio

async def echo(reader, writer):
    while not reader.at_eof():
        data = await reader.readline()
        data = data.decode().split(maxsplit=1)
        if data[0] == 'print':
            new_data = data[1]
        elif data[0] == 'info':
            if data[1] == 'host\n':
                new_data = str(writer.get_extra_info('peername')[0]) + '\n'
            else:
                new_data = str(writer.get_extra_info('peername')[1]) + '\n'
        else:
            new_data = 'error\n'
        writer.write(new_data.encode())
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(echo, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
