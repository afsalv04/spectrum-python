from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        print("car start")



class car(vehicle):
    def start(self):
        print("car started")




c1=car()
c1.start()



