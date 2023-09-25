class Dog:
    species = 'mammal'
    def calAge(self,age):
        print('Dog Age is {}'.format(age*3))

class SomeBread(Dog):
    pass

class SomeOtheraBread(Dog):
    species = 'reptile'
    def calAge(self, age):
        print('Dog Age is {}'.format(age*4))

frank = SomeBread()
print(frank.species)
frank.calAge(5)

beans = SomeOtheraBread()
print(beans.species)
beans.calAge(5)