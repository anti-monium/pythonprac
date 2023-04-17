import asyncio
import socket

def sqroots(coeffs: str) -> str:
    a, b, c = coeffs.split()
    a, b, c = int(a), int(b), int(c)
    if a == 0:
        raise ZeroDivisionError
    d = b * b - 4 * a * c
    if d == 0:
        return f'{-b / (2 * a)}'
    elif d < 0:
        return ''
    else:
        return f'{(-b + d ** 0.5) / (2 * a)} {(-b - d ** 0.5) / (2 * a)}' 
        
        
def sqrootnet(coeffs: str, s: socket.socket) -> str:
    s.sendall((coeffs + '\n').encode())
    return s.recv(128).decode().strip()    


async def serv(reader, writer):
    while data := await reader.readline():
        data = data.decode()
        try:
            ans = sqroots(data) + '\n'
        except:
            ans = '\n'
        writer.write(ans.encode())
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(serv, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

def serve():
    asyncio.run(main())
