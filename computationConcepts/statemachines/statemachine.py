#    Below is a generalized statemachine class, which is used in this the other program file.
import sys

class stateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state: 
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try: 
            handler = self.handlers[self.startState]
        except: 
            print("must call .set_start() before .run()",file=sys.stderr)
            return
        
        if not self.endStates: 
            print("at least one state must be an end_state",file=sys.stderr)
            return
    
        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                print("reached:", newState)
                break 
            else: 
                handler = self.handlers[newState.upper()]