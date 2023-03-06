import cowsay
import shlex

n = 10
field = [[0 for i in range(n)] for j in range(n)]

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

  
class Monster:
    def __init__(self, x, y, hello, name):
        self.hello = hello
        self.name = name
        

def encounter(x, y):
    if field[y][x].name == 'jgsbat':
        name = cowsay.read_dot_cow(open('jgsbat.cow', 'r'))
    	print(cowsay.cowsay(field[y][x].hello, cow=name))
    else:
	print(cowsay.cowsay(field[y][x].hello, cow=field[y][x].name))


print("<<< Welcome to Python-MUD 0.1 >>>")
g = Gamer()
while True:
    s = shlex.split(input())
    match s:
        case [('up' | 'down' | 'left' | 'right')]:
            g.move_to(s[0])
            print(f"Moved to ({g.x}, {g.y})")
            if field[g.y][g.x]:
                encounter(g.x, g.y)
        case ['addmon', *opt]:
            try:
                name, x, y, hello = opt[0], int(opt[1]), int(opt[2]), opt[3]
                _ = field[y][x]
            except:
                print('Invalid arguments')
                continue
            if name not in cowsay.list_cows():
                print('Cannot add unknown monster')
                continue
            print(f"Added monster {name} to ({x}, {y}) saying {hello}")
            if field[y][x]:
                print('Replaced the old monster')
            field[y][x] = Monster(x, y, hello, name)
        case _:
            print('Invalid command')
