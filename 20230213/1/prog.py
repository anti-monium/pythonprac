from glob import iglob
import zlib
import sys

def commit(commit_hash):
    commit_file = '/home/maria/pythonprac/.git/objects/' + commit_hash[0:2] + '/' + commit_hash[2:].replace('\n', '')
    commit_data = zlib.decompress(open(commit_file, 'rb').read())
    k = commit_data.rindex(b'+0300\n\n')
    commit_msg = commit_data[k + len(b'+0300\n\n'):]
    commit_data = str(commit_data[:k + len(b'+0300\n\n') - 1])
    i = commit_data.index('x00')
    commit_data = commit_data[i+3:len(commit_data) - 1].split('\\n')
    commit_data[2] = commit_data[2].split()
    commit_data[2] = ' '.join(commit_data[2][:len(commit_data[2]) - 2])
    commit_data[3] = commit_data[3].split()
    commit_data[3] = ' '.join(commit_data[3][:len(commit_data[3]) - 2])
    commit_msg = commit_msg.decode()
    commit_msg = commit_msg[:len(commit_msg) - 1]
    commit_data.append(commit_msg)
    return commit_data

def tree(tree_hash):
    tree_file = '/home/maria/pythonprac/.git/objects/' + tree_hash[0:2] + '/' + tree_hash[2:].replace('\n', '')
    tree_data = zlib.decompress(open(tree_file, 'rb').read())
    data = tree_data.partition(b'\x00')[-1]
    while data:
        obj, _, data = data.partition(b'\x00')
        obj_mode, obj_name = obj.split()
        obj_num = data[:20].hex()
        data = data[20:]
        if obj_mode.decode() == '40000':
            obj_type = 'tree'
        if obj_mode.decode() == '100644':
            obj_type = 'blob'
        print(obj_type, obj_num, obj_name.decode())
        
def parent(parent_hash):
    parent_data = commit(parent_hash)
    print("TREE for commit ", parent_hash)
    tree(parent_data[0].split()[1])
    if parent_data[1].split()[0] == 'parent':
        try:
            parent(parent_data[1].split()[1])
        except:
            pass

try:
    param = sys.argv[1]
except:
    print("***ПУНКТ 1***")
    for brunch in iglob('/home/maria/pythonprac/.git/refs/heads/*', recursive=True):
        print(brunch)
        brunch_name = brunch.split('/')[-1]
        print(brunch_name)
else:
    br_name = '/home/maria/pythonprac/.git/refs/heads/' + param
    print("***ПУНКТ 2***")
    commit_hash = open(br_name, 'r').read()
    commit_data = commit(commit_hash)
    print(*commit_data, sep='\n')

    print("\n***ПУНКТ 3***")
    tree_hash = commit_data[0].split()[1]
    tree(tree_hash)
    
    print("\n***ПУНКТ 4***")
    print("TREE for commit ", commit_hash[:len(commit_hash) - 1])
    tree_hash = commit_data[0].split()[1]
    tree(tree_hash)   
    parent_hash = commit_data[1].split()[1]
    parent(parent_hash)
