from abc import ABC, abstractmethod

class bike(ABC):
    @abstractmethod
    def StartEngine(s):
        pass

class startbike(bike):
    print('key on')
    def StartEngine(s):
        print("Engine Started")
    def StartTheBike(s):
        print('bike going to start')
        s.StartEngine()
        print('bike started')

s=startbike()
s.StartTheBike()
