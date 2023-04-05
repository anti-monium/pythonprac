import cowsay
import shlex
import asyncio

n = 10
field = [[0 for i in range(n)] for j in range(n)]
custom_cows = ['jgsbat']
players = {}
weapons = {'sword': 10, 'spear': 15, 'axe': 20}
used_nicks = set()


class Gamer:
    x = 0
    y = 0

    def __init__(self, nick):
        self.nick = nick

    def move_to(self, dx, dy):
        self.x = (self.x + dx) % n
        self.y = (self.y + dy) % n


class Monster:
    def __init__(self, name, x, y, hello, hp):
        self.name = name
        self.hello = hello
        self.hp = hp


def encounter(x, y):
    if field[y][x].name in custom_cows:
        f = field[y][x].name + '.cow'
        name = cowsay.read_dot_cow(open(f, 'r'))
        return cowsay.cowsay(field[y][x].hello, cowfile=name)
    else:
        return cowsay.cowsay(field[y][x].hello, cow=field[y][x].name)


def move(g, x, y):
    g.move_to(x, y)
    ans = f'Moved to ({g.x}, {g.y})'
    if field[g.y][g.x]:
        ans = ans + '\n' + encounter(g.x, g.y)
    return ans


def addmon(g, name, hello, x, y, hp):
    ans1 = f'Added monster {name} to ({x}, {y}) saying {hello}'
    if field[y][x]:
        ans1 = ans1 + '\n' + 'Replaced the old monster'
    field[y][x] = Monster(name, x, y, hello, hp)
    ans2 = f'{g.nick} added {name} with {hp} hp'
    return (ans1, ans2)


def attack(g, name, weapon):
    damage = weapons[weapon]
    if not field[g.y][g.x]:
        return 'No monster here'
    monster = field[g.y][g.x]
    if name != monster.name:
        return f'No {name} here'
    if monster.hp < damage:
        damage = monster.hp
    monster.hp -= damage
    ans1 = f'Attacked {monster.name}, damage {damage}'
    ans2 = f'{g.nick} attacked {monster.name} with {weapon}, damage - {damage}'
    if monster.hp == 0:
        ans1 = ans1 + '\n' + f'{monster.name} died'
        ans2 = ans2 + '\n' + f'{monster.name} died'
        field[g.y][g.x] = 0
    else:
        ans1 = ans1 + '\n' + f'{monster.name} now has {monster.hp}'
        ans2 = ans2 + '\n' + f'{monster.name} now has {monster.hp}'
    return (ans1, ans2)


async def Dungeon(reader, writer):
    player = "{}:{}".format(*writer.get_extra_info('peername'))
    print(player)
    players[player] = asyncio.Queue()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(players[player].get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())
                command = shlex.split(q.result().decode())
                match command:
                    case ['login', nick]:
                        if nick in used_nicks:
                            await players[player].put('Nickname already in use')
                            if player in players.keys():
                                del players[player]
                        else:
                            used_nicks.add(nick)
                            me = Gamer(nick)
                            players[me] = players.pop(player)
                            player = me
                            await players[player].put('Successful login')
                            for p in players.keys():
                                if p != player:
                                    await players[p].put(f'{player.nick} in Dungeon!')
                    case ['move', x, y]:
                        await players[p].put(move(player, int(x), int(y)))
                    case ['addmon', name, hello, x, y, hp]:
                        for_me, for_others = addmon(player, name, hello, int(x), int(y), int(hp))
                        await players[player].put(for_me)
                        for p in players.keys():
                            if p != player:
                                await players[p].put(for_others)
                    case ['attack', name, weapon]:
                        for_me, for_others = attack(player, name, weapon)
                        await players[player].put(for_me)
                        for p in players.keys():
                            if p != player:
                                await players[p].put(for_others)
                    case ['sayall', msg]:
                        for p in players.keys():
                            if p != player:
                                await players[p].put(player.nick + ': ' + msg)
                    case ['exit']:
                        await players[player].put('exit')
                        for p in players.keys():
                            await players[p].put(f'{player.nick} came out of the Dungeon :(')
                        used_nicks.remove(player.nick)
                    case _:
                        await players[player].put('<<< error >>>')
            elif q is receive:
                receive = asyncio.create_task(players[player].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    if player in players.keys():
        del players[player]
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(Dungeon, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()


def start():
    asyncio.run(main())
