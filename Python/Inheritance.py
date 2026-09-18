# class vehicle:
#     def start(self):
#         print("vehicle is started")
#     def stop(self):
#         print("vehicle is stopped")   

# class car(vehicle):  
#     def drive(self):
#         print("Im driving a car")

# print ("vehicle:")
# vehicle = vehicle()
# vehicle.start()
# vehicle.stop()

# print ("car:")
# car = car()
# car.start()
# car.drive()
# car.stop()

# class A:
#     def show(self):
#         print("I am in class A")
# class B(A):
#     pass
# class C(A):
#    pass
# class D(B,C):
#     pass  

# D().show()                         

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

dog = Dog()
dog.speak()