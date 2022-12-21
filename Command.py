import pygame

class Command:
    def execute():
        raise NotImplemented

class Up(Command):
    def execute(self,actor):
        actor.up()
        
class Down(Command):
    def execute(self,actor):
        actor.down()
        
class Left(Command):
    def execute(self,actor):
        actor.left()
    
class Right(Command):
    def execute(self,actor):
        actor.right()
        
class Action(Command):
    def execute(self,actor):
        actor.action()

class InputHandler:   
    def __init__(self) -> None:
        self.commander = {'up':Up(),
                     'down':Down(),
                     'left':Left(),
                     'right':Right(),
                     'action':Action()
                     }
     
    def handleInput(self,event,player, command):
        if event.key in command:
            return self.commander[command[event.key]].execute(player)
