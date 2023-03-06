import cowsay

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
    def __init__(self, x, y, s):
        self.hello = s
        

def encounter(x, y, name):
    if name == 'jgsbat':
        name = cowsay.read_dot_cow(open('jgsbat.cow', 'r'))
    print(cowsay.cowsay(field[y][x].hello))


print("<<< Welcome to Python-MUD 0.1 >>>")
g = Gamer()
while True:
    s = input().split()
    match s:
        case [('up' | 'down' | 'left' | 'right')]:
            g.move_to(s[0])
            print(f"Moved to ({g.x}, {g.y})")
            if field[g.y][g.x]:
                encounter(g.x, g.y)
        case ['addmon', *opt]:
            try:
                x, y, hello = int(opt[0]), int(opt[1]), opt[2]
                _ = field[y][x]
            except:
                print('Invalid arguments')
                continue
            print(f"Added monster to ({x}, {y}) saying {hello}")
            if field[y][x]:
                print('Replaced the old monster')
                continue
            field[y][x] = Monster(x, y, hello)
        case _:
            print('Invalid command')
