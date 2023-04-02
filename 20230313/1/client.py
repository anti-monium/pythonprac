import cowsay
import shlex
import cmd
import socket

weapons = {'sword': 10, 'spear': 15, 'axe': 20}
custom_cows = ['jgsbat']
n = 10


def print_monster(name, hello):
    if name in custom_cows:
        f = name + '.cow'
        name = cowsay.read_dot_cow(open(f, 'r'))
        print(cowsay.cowsay(hello, cowfile=name))
    else:
	    print(cowsay.cowsay(hello, cow=name))


def request(s):
    global dangeon_socket
    dangeon_socket.send((s + '\n').encode())
    ans = bytearray()
    ans = dangeon_socket.recv(4096)
    ans = ans.decode().rstrip().split('\n')
    for line in ans:
        if line.startswith('MONSTER'):
            line = shlex.split(line)
            print_monster(line[1], line[2])
        else:
            print(line)


class Cli_Dangeon(cmd.Cmd):
    intro = '<<< Welcome to Python-MUD 0.1 >>>'
    prompt = '>>>> '
    
    def do_up(self, arg):
        request('move 0 -1')
    
    def do_down(self, arg):
        request('move 0 1')
    
    def do_left(self, arg):
        request('move -1 0')
    
    def do_right(self, arg):
        request('move 1 0')
    
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
        except:
            print('Invalid arguments')
            return
        if name not in cowsay.list_cows() and name not in custom_cows:
            print('Cannot add unknown monster')
            return
        if x < 0 or x > n - 1 or y < 0 or y > n - 1:
            print('Invalid arguments. Field size is 10x10')
        request(f'addmon {name} \'{hello}\' {x} {y} {hp}')
        
    def do_attack(self, arg):
        arg = shlex.split(arg)
        if len(arg) < 1:
            print('Invalid arguments')
            return
        name = arg[0]
        if name not in cowsay.list_cows() and name not in custom_cows:
            print('Unknown monster')
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
        if line[-1] == 'with':
            return ['sword', 'spear', 'axe']
        elif len(line) >= 2 and 'with'.startswith(prefix):
            return ['with']
        elif len(line) >= 3 and line[-2] == 'with':
            return [weapon for weapon in ['sword', 'spear', 'axe']
                    if weapon.startswith(prefix)]
        else:
            return [name for name in cowsay.list_cows() + custom_cows
                    if name.startswith(prefix)]
                    
                    
    def do_exit(self, arg):
        global dangeon_socket
        dangeon_socket.close()
        return True
                    
                    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as dangeon_socket:
    dangeon_socket.connect(("localhost", 1337))
    Cli_Dangeon(completekey='tab').cmdloop()
