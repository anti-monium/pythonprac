import cowsay
import shlex
import cmd

n = 10
field = [[0 for i in range(n)] for j in range(n)]
custom_cows = ['jgsbat']

class Gamer:
    x = 0
    y = 0
    
    def move_to(self, dx, dy):
        self.x = (self.x + dx) % n
        self.y = (self.y + dy) % n
                  
g = Gamer()

  
class Monster:
    def __init__(self, name, x, y, hello, hp):
        self.name = name
        self.hello = hello
        self.hp = hp
        
'''
def encounter(x, y):
    if field[y][x].name in custom_cows:
        f = field[y][x].name + '.cow'
        name = cowsay.read_dot_cow(open(f, 'r'))
        print(cowsay.cowsay(field[y][x].hello, cowfile=name))
    else:
	    print(cowsay.cowsay(field[y][x].hello, cow=field[y][x].name))
'''	    


def encounter(x, y):
    return f'MONSTER {field[y][x].name} {field[y][x].hello}'


def move(x, y):
    g.move_to(x, y)
    ans = f'Moved to ({g.x}, {g.y})'
    if field[g.y][g.x]:
        ans = ans + '\n' + encounter(g.x, g.y)
    return ans
    
    
def addmon(name, hello, x, y, hp):
    ans = f'Added monster {name} to ({x}, {y}) saying {hello}'
    if field[y][x]:
        ans = ans + '\n' + 'Replaced the old monster'
    field[y][x] = Monster(name, x, y, hello, hp)
    
    
def attack(name, damage):
    if not field[g.y][g.x]:
        return 'No monster here'
    monster = field[g.y][g.x]
    if name != monster.name
        return f'No {name} here'
    if monster.hp < damage:
        damage = monster.hp
    monster.hp -= damage
    ans = f'Attacked {monster.name}, damage {damage} hp'
    if monster.hp == 0:
        ans = '\n' + f'{monster.name} died'
        field[g.y][g.x] = 0
    else:
        ans = '\n' + f'{monster.name} now has {monster.hp}'
    return ans
    

async def Dangeon(reader, writer):
    host, port = writer.get_extra_info('peername')
    while not reader.at_eof():
        request = await reader.readline()
        request = request.decode()
        match shlex.split(request):
            case ["move", x, y]:
                ans = move(int(x), int(y))
            case ["addmon", name, hello, x, y, hp]:
                ans = addmon(name, hello, int(x), int(y), int(hp))
            case ["attack", name, damage]:
                ans = attack(name, int(damage))
        writer.write(ans.encode())
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(Dangeon, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()


asyncio.run(main())
