class Human:
    __name = None

    def __init__(self) -> None:
        print("Human")

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name


class Student(Human):
    __age = None
    _school = None

    def __init__(self) -> None:
        super().__init__()

    def setAge(self,age:int):
        self.__age = age

    def getAge(self):
        return self.__age

    def getName(self):
        return "Name: " + super().getName()


dejah = Human()

dejah.setName("Dejah Thoris")
print(dejah.getName())

jhon = Student()
jhon.setName("Jhon Carter")
jhon.setAge(21)
print(jhon.getName())
print(jhon.getAge())
print(jhon._school)
