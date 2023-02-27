import shlex

#s = input()
#print(shlex.join(shlex.split(s)))

fio = input()
place = input()
res1 = shlex.join(['register', fio, place])
res2 = shlex.split(res1)
print(res2)
