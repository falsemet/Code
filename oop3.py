#! /bin/env python3


class Chain(object):
    def __init__(self,path=''):
        self.__path=path
    def __getattr__(self,path):
        return Chain("%s/%s"%(self.__path,path))
    def __call__(self, path):
    # This step make getattr value into an real function
        return Chain("%s/%s"%(self.__path,path))
    def __str__(self):
        return self.__path
    __repr__=__str__

print (Chain().status.user.timeline.list)
print(Chain().users('Jim').repo)