from glob import iglob

for brunch in iglob('.git/refs/heads/*'):
    brunch_name = brunch.split('/')[-1]
    print(brunch_name)
