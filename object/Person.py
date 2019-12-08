class Person:
    def __init__(self, new_name):
        # self.name = "Tom"
        self.name = new_name
        print("这是一个初始化方法")

    def eat(self):
        print("%s 小猫爱吃鱼" % self.name)

    def drink(self):
        print("%s 小猫要喝水" % self.name)

    def __str__(self):
        return "toString()"


tom = Person("Tom")
tom.drink()
tom.eat()
print(tom)
