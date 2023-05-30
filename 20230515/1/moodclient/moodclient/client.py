import cowsay
import shlex
import cmd
import socket
import threading
import readline

weapons = {'sword': 10, 'spear': 15, 'axe': 20}
custom_cows = ['jgsbat']
n = 10
thread_alive = True
cmdline = None

def recieve():
    global cmdline, thread_alive
    while thread_alive:
        ans = bytearray()
        ans = cmdline.dungeon_socket.recv(4096)
        ans = ans.decode().rstrip()
        if ans == "exit":
            break
        print(f"\n{ans}\n{cmdline.prompt}{readline.get_line_buffer()}", end="", flush=True)


class Cli_Dungeon(cmd.Cmd):
    intro = '<<< Welcome to Python-MUD 0.1 >>>'
    prompt = '>>>> '
    
    def __init__(self, nickname, **params):
        super().__init__(**params)
        global cmdline, thread_alive
        cmdline = self
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.dungeon_socket:
            self.dungeon_socket.connect(("localhost", 1337))
            self.dungeon_socket.send((f'login {nickname}' + '\n').encode())
            ans = self.dungeon_socket.recv(4096).decode().rstrip()
            print(ans)
            if ans != 'Nickname already in use':
                reciever = threading.Thread(target=recieve)
                reciever.start()
                self.cmdloop()
                
    def request(self, s):
        global cmdline
        cmdline.dungeon_socket.send((s + '\n').encode())

    def do_up(self, arg):
        self.request('move 0 -1')

    def do_down(self, arg):
        self.request('move 0 1')

    def do_left(self, arg):
        self.request('move -1 0')

    def do_right(self, arg):
        self.request('move 1 0')

    def do_addmon(self, arg):
        arg = shlex.split(arg)
        if (len(arg) < 8 or 'hello' not in arg or 'hp' not in arg or 'coords' not in arg):
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
        except Exception:
            print('Invalid arguments')
            return
        if name not in cowsay.list_cows() and name not in custom_cows:
            print('Cannot add unknown monster')
            return
        if x < 0 or x > n - 1 or y < 0 or y > n - 1:
            print('Invalid arguments. Field size is 10x10')
            return
        self.request(f'addmon {name} \'{hello}\' {x} {y} {hp}')

    def do_attack(self, arg):
        arg = shlex.split(arg)
        if len(arg) < 1:
            print('Invalid arguments')
            return
        name = arg[0]
        if name not in cowsay.list_cows() and name not in custom_cows:
            print('Unknown monster')
            return
        weapon = 'sword'
        if len(arg) > 1:
            if arg[0] == 'with':
                weapon = arg[1]
            elif arg[1] == 'with':
                weapon = arg[2]
            else:
                print('Invalid arguments')
                return
            if weapon not in weapons.keys():
                print('Unknown weapon')
                return
        self.request(f'attack {name} {weapon}')

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

    def do_sayall(self, arg):
        self.request(f'sayall {arg}')
        
    def do_locale(self, arg):
        if arg == 'en':
            arg = 'en_US.UTF-8'
        elif arg == 'ru':
            arg = 'ru_RU.UTF-8'
        else:
            print('Invalid arguments')
            return
        self.request(f'locale {arg}')

    def do_exit(self, arg):
        global cmdline, thread_alive
        self.request('exit')
        thread_alive = False
        cmdline.dungeon_socket.close()
        return True
