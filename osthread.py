import os

print("Process (%s) start "%(os.getpid()))
pid=os.fork()
if pid==0:
    print("child process: (%s) parent process:(%s)"%(os.getpid(),os.getppid()))
else:
    print("I (%s) just creat a child process (%s)"%(os.getpid(),pid))


from multiprocessing import Process
def run(name):
    print ("Run chind process %s(%s)"%(name,os.getpid()))

if __name__=='__main__':
    print("parent process %s"%(os.getpid()))
    p=Process(target=run,args=('test',))
    print("Child process will start")
    p.start()
    p.join()
    print("Chind process end")
