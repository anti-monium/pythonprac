from glob import iglob
import zlib

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
        


for brunch in iglob('/home/maria/pythonprac/.git/refs/heads/*', recursive=True):
    print(brunch)
    brunch_name = brunch.split('/')[-1]
    print(brunch_name)
    
br_name = '/home/maria/pythonprac/.git/refs/heads/' + input()
commit_hash = open(br_name, 'r').read()
commit_data = commit(commit_hash)
print(*commit_data, sep='\n')

tree_hash = commit_data[0].split()[1]
tree(tree_hash)
    
parent_hash = commit_data[1].split()[1]
parent_file = '/home/maria/pythonprac/.git/objects/' + parent_hash[0:2] + '/' + parent_hash[2:].replace('\n', '')
parent_data = zlib.decompress(open(parent_file, 'rb').read())
print(parent_data)
