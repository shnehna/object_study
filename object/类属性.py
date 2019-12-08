class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool = Tool("斧头")
tool2 = Tool("2斧头")
print(Tool.count)
