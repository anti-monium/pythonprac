weapons = {'sword': 10, 'spear': 15, 'axe': 20}


def request(s):
    global dangeon_socket
    dangeon_socket.sendall(s.encode())
    ans = ''
    dangeon_socket.recv_into(ans)
    ans = ans.decode()
    print(ans)


class CLi_Dangeon(cmd.Cmd):
    intro = '<<< Welcome to Python-MUD 0.1 >>>'
    prompt = '>>>>\t'
    
    def do_up(self, arg):
        request('up')
    
    def do_down(self, arg):
        request('down')
    
    def do_left(self, arg):
        request('left')
    
    def do_right(self, arg):
        request('right')
    
    def do_addmon(self, arg):
        arg = shlex.split(arg)
        if (len(arg) < 8 or 'hello' not in arg 
            or 'hp' not in arg or 'coords' not in arg):
            print('Invalid arguments')
            return
        try:
            name = arg[0]
            i = 1
            while i < len(arg):
                if arg[i] == 'hello':
                    hello = arg[i + 1]
                    i += 2
                elif arg[i] == 'hp':
                    hp = int(arg[i + 1])
                    i += 2
                elif arg[i] == 'coords':
                    x = int(arg[i + 1])
                    y = int(arg[i + 2])
                    i += 3
                else:
                    raise
            _ = field[y][x]
        except:
            print('Invalid arguments')
            return
        if name not in cowsay.list_cows() and name not in custom_cows:
            print('Cannot add unknown monster')
            return
        request(f'addmon {name} {hello} {x} {y} {hp}')
        
    def do_attack(self, arg):
        if not field[g.y][g.x]:
            print('No monster here')
            return
        arg = shlex.split(arg)
        monster = field[g.y][g.x]
        if len(arg) == 1 and arg[0] != monster.name:
            print(f'No {arg[0]} here')
            return
        damage = 10
        if len(arg) > 1:
            if arg[0] == 'with':
                weapon = arg[1]
            elif arg[1] == 'with':
                weapon = arg[2]
            else:
                print('Invalid arguments')
                return
            if weapon in weapons.keys():
                damage = weapons[weapon]
            else:
                print('Unknown weapon')
                return
        request(f'attack {name} {damage}')
            
    def complete_attack(self, prefix, line, start, end):
        line = shlex.split(line)
        if len(line) >= 2 and 'with'.startswith(prefix):
            return ['with']
        elif len(line) >= 3 and line[-2] == 'with':
            return [weapon for weapon in ['sword', 'spear', 'axe']
                    if weapon.startswith(prefix)]
        else:
            return [name for name in cowsay.list_cows() + custom_cows
                    if name.startswith(prefix)]
                    
                    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as dangeon_socket:
    dangeon_socket.connect(("localhost", 1337))
    Cli_Dangeon().cmdloop()
