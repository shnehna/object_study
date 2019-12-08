class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1

    def __str__(self):
        return "我的名字叫%s,体重是%.2f" % (self.name, self.weight)


xiaoming = Person("小明", 50)
print(xiaoming)
xiaoming.eat()
xiaoming.eat()
xiaoming.eat()
xiaoming.eat()
print(xiaoming)
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
xiaoming.run()
print(xiaoming)
