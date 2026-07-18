# class Dog:
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age

#     def bark (self):
#         print("woof!") 
#     def a(self):
#         print("gaf!")
# my_dog = Dog("buddy",3)

# my_dog = Dog("buddy",4)
# he_dog = Dog("bars", 3)
# my_dog.bark
# he_dog.a

# задание 3#
# class Car:
#     def __init__(self,color,brand):
#         self.color=color
#         self.brand=brand
#     def a(self):
#         print(f"The{self.color}{self.brand}car is starting the engine.")
# my_car = Car ("blue","Toyota")
# my_car.start_engint()
# hork 4#        
# class House :

#     def _init_(self, area, rooms, address):

#         self.area =area

#         self.rooms =rooms

#         self.address = address

#         self.door_is_opened = False

#     def open_door(self):

#         self.door_is_opened = True

# print("Дверь открыта")

# class MultistoryHouse (House):

#     def _init_(self, area, rooms, address):

#         super().init_(area, rooms, address)

#         self.floors =0

#     def add_floor(self):

#         self.floors += 1

#         print("Добавлен этаж. Текущее количество этажей: (self.floors)")

# # Создание объектов классов
# my_house=House (100, 3, "ул. Примерная, 1")

# my_multistory_house=MultistoryHouse (500, 10, "ул. Высокая, 2")

# # Обращение к методам объектов

# my_house.open_door()

# my_multistory_house.open_door()

# # Обращение к уникальному свойству класса MultistoryHouse

# my_multistory_house.add_floor()

# my_multistory_house.add_floor()

# my_multistory_house.add_floor()

# print(f"Количество этажей в многоэтажном доме: (my_multistory_house.floors)
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age = age
    
    def get_info(self):
        print("имя: {self.name}, возраст: {self.age}")

class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id =student_id
    def get_info(self):
        print(f"имя: {self.name}, возраст: {self.age},Номер сдутенческого билета:{self.student_id}")
person=Person("макс",16)
student=Student("Айтемир",20 ,"A1231467567519249")
print(person.get_info())
print(student.get_info())