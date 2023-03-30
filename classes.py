class point():
    def __init__(self, input1, input2 ):
    # __init__ is a method or function that is automatically called everytime we create a new point
    # every argument should start with self
        self.x=input1
        self.y=input2

p=point(2,8)
print(p.x)
print(p.y)

