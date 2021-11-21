class Student(object):

    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if gender !='male' and gender != 'female':
            print ("Error gender format")
        else:
            self.__gender=gender
            return self.__gender

bart = Student('Bart', 'male')
print(bart.get_gender())

bart.set_gender('female')
print(bart.get_gender())