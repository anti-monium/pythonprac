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
            self.y = (self.y - 1) % n
        elif s == 'down':
            self.y = (self.y + 1) % n
        elif s == 'left':
            self.x = (self.x - 1) % n
        elif s == 'right':
            self.x = (self.x + 1) % n
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
    if field[y][x].name in custom_cows:
        f = field[y][x].name + '.cow'
        name = cowsay.read_dot_cow(open(f, 'r'))
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
        print(f'Added monster {name} to ({x}, {y}) saying {hello}')
        if field[y][x]:
            print('Replaced the old monster')
        field[y][x] = Monster(name, x, y, hello, hp)
        
    def do_attack(self, arg):
        if not field[g.y][g.x]:
            print('No monster here')
            return
        arg = shlex.split(arg)
        if len(arg) == 0:
            monster = field[g.y][g.x]
            if monster.hp >= 10:
                damage = 10
            else:
                damage = monster.hp
            monster.hp -= damage
            print(f'Attacked {monster.name}, damage {damage} hp')
            if monster.hp == 0:
                print(f'{monster.name} died')
                field[g.y][g.x] = 0
            else:
                print(f'{monster.name} now has {monster.hp}')
        elif len(arg) == 2:
            if arg[0] != 'with':
                print('Invalid arguments')
                return
            


Dangeon(completekey='tab').cmdloop()
