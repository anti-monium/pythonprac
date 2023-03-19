import cowsay
import shlex
import cmd

n = 10
field = [[0 for i in range(n)] for j in range(n)]
custom_cows = ['jgsbat']

class Gamer:
    x = 0
    y = 0
    
    def move_to(self, s):
        if s == 'up':
            self.x = (self.x - 1) % n
        elif s == 'down':
            self.x = (self.x + 1) % n
        elif s == 'left':
            self.y = (self.y - 1) % n
        elif s == 'right':
            self.y = (self.y + 1) % n
        print(f'Moved to ({self.x}, {self.y})')
        if field[self.y][self.x]:
            encounter(self.x, self.y)
                  
g = Gamer()

  
class Monster:
    def __init__(self, name, x, y, hello, hp):
        self.name = name
        self.hello = hello
        self.hp = hp
        

def encounter(x, y):
    if field[y][x].name == 'jgsbat':
        name = cowsay.read_dot_cow(open('jgsbat.cow', 'r'))
        print(cowsay.cowsay(field[y][x].hello, cowfile=name))
    else:
	    print(cowsay.cowsay(field[y][x].hello, cow=field[y][x].name))
	    
	    
class Dangeon(cmd.Cmd):
    intro = '<<< Welcome to Python-MUD 0.1 >>>'
    prompt = '>>>>\t'
    def do_up(self, arg):
        g.move_to('up')
    
    def do_down(self, arg):
        g.move_to('down')
    
    def do_left(self, arg):
        g.move_to('left')
    
    def do_right(self, arg):
        g.move_to('right')
    
    def do_addmon(self, arg):
        pass


Dangeon(completekey='tab').cmdloop()


while True:
    s = shlex.split(input())
    match s:
        case ['addmon', *opt]:
            if (len(opt) < 8 or 'hello' not in opt 
                or 'hp' not in opt or 'coords' not in opt):
                print('Invalid arguments')
                continue
            try:
                name = opt[0]
                i = 1
                while i < len(opt):
                    if opt[i] == 'hello':
                        hello = opt[i + 1]
                        i += 2
                    elif opt[i] == 'hp':
                        hp = int(opt[i + 1])
                        i += 2
                    elif opt[i] == 'coords':
                        x = int(opt[i + 1])
                        y = int(opt[i + 2])
                        i += 3
                    else:
                        raise
                _ = field[y][x]
            except:
                print('Invalid arguments')
                continue
            if name not in cowsay.list_cows() and name not in custom_cows:
                print('Cannot add unknown monster')
                continue
            print(f'Added monster {name} to ({x}, {y}) saying {hello}')
            if field[y][x]:
                print('Replaced the old monster')
            field[y][x] = Monster(name, x, y, hello, hp)
        case _:
            print('Invalid command')
