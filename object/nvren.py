class Women:
    def __init__(self, name):
        self.name = name
        self.__age = "18"

    def secret(self):
        print(self.name + self.__age)


xiaofang = Women("消防")
print(xiaofang._Women__age)
xiaofang.secret()
