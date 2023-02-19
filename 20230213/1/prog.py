from glob import iglob

for brunch in iglob('../pythonprac/.git/refs/heads/*', recursive=True):
    print(brunch)
    brunch_name = brunch.split('/')[-1]
    print(brunch_name)

br_name = input()

