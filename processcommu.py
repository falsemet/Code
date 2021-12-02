from multiprocessing import Process,Queue
import os,time,random

def read(q):
    print ('Process to write:%s'%os.getpid())
    for value in['A','B','C']:
        print('put %s to queue ...'%value)
        q.put(value)
        time.sleep(random.random())
def write(q):
    print("process to write:%s"%os.getpid())
    while True:
        value=q.get(True)
        print("get %s from queue "%value)

if __name__=='__main__':
    q=Queue()
    qwrite=Process(target=write,args=(q,))
    qread=Process(target=read,args=(q,))
    qwrite.start()
    qread.start()
    qwrite.join()
    qwrite.terminate()