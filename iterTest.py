import itertools

str=itertools.repeat("xyz",3)
for x in str:
    print (x)

m=(lambda:x for x in itertools.cycle("ABCDEFG"))
print (m)

for x in itertools.chain("abc",'xyz'):
    print (x)
