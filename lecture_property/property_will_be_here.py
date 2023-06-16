class ClassWithProperties:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @value.deleter
    def value(self):
        del self.__value


exemplar = ClassWithProperties(5)

print(exemplar.value)
exemplar.value = 10
print(exemplar.value)
del exemplar.value
print(exemplar.value)
