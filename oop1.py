class animal(object):
    def run(self):
        print ("animal is running")

class cat(animal):
    pass

class dog(animal):
    def run(self):
        print ("cat is runnig")

def run_twice(Animal):
    Animal.run()
    Animal.run()

run_twice(animal())
run_twice(cat())
run_twice(dog())
print (dir(animal))