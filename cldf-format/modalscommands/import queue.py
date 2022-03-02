import queue
import threading
import time

q = queue.Queue()
for i in [3,2,1]:
	def f():
		time.sleep(i)
		q.put(i)
	threading.Thread(target=f).start()

print(q.get())

def buid(sents):
	root ={}
	for sent in sents:
		base = root
		for word in sent.split(' '):
			if not base.get(word):
				base[word] = {}
			base = base[word]
	return root

print(buid(["Hello world", "Hello there"]))

def delete(items):
	i = 0 
	while i < len(items):
		if len(items[i]) == 0:
			del items[i]
		i +=1

names = ['a','','b','','','c']
print(names)
