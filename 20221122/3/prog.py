import struct
import sys

buf = sys.stdin.buffer.read(44)
hdr = struct.unpack('4sI4s4sIHHIIHH4sI', buf)
pos = [1,5,6,7,10,12]
names = ['Size', 'Type', 'Channels', 'Rate', 'Bits', 'Data size']
ans = {}
for i in range(len(hdr)):
	if i == 2 and hdr[i] != b'WAVE':
		ans = 'NO'
		break
	if i in pos:
		ans[names[0]] = hdr[i]
		names.pop(0)
if ans == 'NO':
	print(ans)
else:
	for k in ans:
		if k != 'Data size':
			print(k, '=', ans[k], sep='', end=', ')
		else:
			print(k, '=', ans[k], sep='')
