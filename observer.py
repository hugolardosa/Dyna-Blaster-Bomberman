class Observer:
    def on_notify(self, event):
        raise NotImplemented

        
class Subject:
    def __init__(self) -> None:
        self.observers = []
        
    def add_observer(self, observer):
        self.observers.append(observer)
    def notify(self):
        for observer in self.observers:
            observer.on_notify()
            
          