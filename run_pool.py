from multiprocessing import Pool
from multiprocessing import Process
import os,time,random

def longtime(name):
    print('run task %s(%s)'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*4)
    end=time.time()
    print("task %s run %0.2f second"%(name,(end-start)))

if __name__=='__main__':
    print("parent process %s(%s)"%(os.getpid(),os.getppid()))
    p=Pool()
    for i in range(13):
        p.apply_async(longtime,args=(i,))
    print("waiting for all subprocesss run")
    p.close()
    p.join()
    print("all  subprocess done")