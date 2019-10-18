from multiprocessing import Process, Queue

zzz = Queue()
zzz.put("wedq")
print(zzz.get())

def f(zz):
    zz.put([42, None, 'hello'])



if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()