from glob import iglob
import zlib

for brunch in iglob('/home/maria/pythonprac/.git/refs/heads/*', recursive=True):
    print(brunch)
    brunch_name = brunch.split('/')[-1]
    print(brunch_name)
    
br_name = '/home/maria/pythonprac/.git/refs/heads/' + input()
commit_hash = open(br_name, 'r').read()
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
print(*commit_data, commit_msg, sep='\n')
