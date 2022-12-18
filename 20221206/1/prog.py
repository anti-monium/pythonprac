import asyncio
import random

async def merge(a, b, 
		start, middle, finish, 
		event_in1, event_in2, 
		event_out):
	await event_in1.wait()
	await event_in2.wait()
	s1 = start
	s2 = middle
	i = start
	while s1 < middle and s2 < finish:
		if a[s1] > a[s2]:
			b[i] = a[s1]
			s1 += 1
		else:
			b[i] = a[s2]
			s2 += 1
		i += 1
	while s1 < middle:
		b[i] = a[s1]
		i += 1
		s1 += 1
	while s2 < middle:
		b[i] = a[s2]
		i += 1
		s2 += 1
	event_out.set()
	
	
def merge_sort(n, m, a, b, event, tasks):
	if abs(m - n) <= 1:
		event.set()
		return
	ev1 = asyncio.Event()
	ev2 = asyncio.Event()
	tasks.append(asyncio.create_task(merge(a, b, n, (n + m) // 2, m, ev1, ev2, event)))
	merge_sort(n, (n + m) // 2, b, a, ev1, tasks)
	merge_sort((n + m) // 2, m, b, a, ev2, tasks)
	
		
async def mtasks(a):
	b = a.copy()
	tasks = []
	merge_sort(0, len(a), a, b, asyncio.Event(), tasks)
	return tasks, b
	
	
import asyncio

async def main(A):
    tasks, B = await mtasks(A)
    print(len(tasks))
    random.shuffle(tasks)
    await asyncio.gather(*tasks)
    return B


random.seed(1337)
A = random.choices(range(10), k=33)
B = asyncio.run(main(A))
print(*A)
print(*B)
print(B == sorted(A))
