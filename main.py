class Father(object):
    def __init__(self):
        super().__init__()
        print("I am Father")


class GrandFather(object):
    def __init__(self):
        super().__init__()
        print("I am GrandFather")

class Mother(object):
    def __init__(self):
        super().__init__()
        print("I am Mother")



class Son(Father,GrandFather,Mother):
    def __init__(self):
        super().__init__()
        print("I am Son")

s  = Son()