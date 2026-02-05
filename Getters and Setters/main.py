class MyClass:

    def __init__(self, value):
        self._value = value
    

    def show(self):
        print(f"Value is {self._value}")
    

    @property
    def value_10x(self):
        return self._value * 10


    @value_10x.setter
    def value_10x(self, new_value):
        self._value = new_value / 10
    

obj = MyClass(10)
print(obj.value_10x)
obj.show()