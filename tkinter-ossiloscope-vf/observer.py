class Subject(object):
    def __init__(self):
        self.observers=[]
    def notify(self):
        for obs in self.observers:
            obs.update(self)
    def attach(self, obs):
        if not hasattr(obs,"update"):
            raise ValueError("Observer must have  an update() method")
        self.observers.append(obs)
    def detach(self, obs):
        if obs in self.observers :
            self.observers.remove(obs)

class Observer:
    def update(self, subject):
        raise NotImplementedError

class ConcreteSubject(Subject):
    def __init__(self):
        Subject.__init__(self)
        self.__data=0
    def get_data(self):
        return self.__data
    def set_data(self,data):
        self.__data=data

    def increase(self):
        print("ConcreteSubject.increase()")
        self.__data+=1
        self.notify()       # call observers update() method
    def decrease(self):
        print("ConcreteSubject.decrease()")
        self.__data-=1
        self.notify()       # call observers update() method

class ConcreteObserver(Observer):
    def __init__(self,name):
        self.name=name

    def get_name(self) :
        return self.name
    def set_name(self,name) :
        self.name=name

    def update(self,subject):
        print("ConcreteObserver.update()")
        print(self.name, " on subject data : ",subject.get_data())

if __name__ == "__main__":
    subject=ConcreteSubject()
    print("Subject data:", subject.get_data())
    name="Observer 1"
    obs=ConcreteObserver(name)
    print("attach:", obs.get_name())
    subject.attach(obs)
    subject.increase()
    name="Observer 2"
    obs=ConcreteObserver(name)
    print("attach:", obs.get_name())
    subject.attach(obs)
    subject.increase()
    print("detach :", obs.get_name())
    subject.detach(obs)
    subject.decrease()