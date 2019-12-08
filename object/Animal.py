class Animal(object):
    def eat(self):
        print("吃吃吃")

    def drink(self):
        print("hehehe")

    def run(self):
        print("胖胖胖")


class Dog(Animal):
    def find(self):
        print("我能找毒品")

    def run(self):
        super().run()
        print("狗的那种奔跑")


dog = Dog()
dog.find()
dog.run()
