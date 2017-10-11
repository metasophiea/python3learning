class Tape(object):
    
    blank_symbol = " "
    
    def __init__(self,tape_string = "",offset = 0):
        self.__tape = dict((enumerate(tape_string,start=offset)))
        # equivalent to:
        #   self.__tape = {}
        #   for i in range(len(tape_string)):
        #       self.__tape[i] = input[i]
        
    def __str__(self):
        s = ""
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())

        for i in range(min_used_index, max_used_index):
            s += self.__tape[i] if i in self.__tape else " "

        return s    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

class TuringMachine(object):

    def __init__(self, tape = "", offset = 0, blank_symbol = " ", initial_state = "", final_states = None, transition_function = None):
        self.__tape = Tape(tape,offset)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state

        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function

        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def get_tape(self): 
        return str(self.__tape)
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        taskData = self.__transition_function[(self.__current_state, char_under_head)]

        if taskData != None:
            # update state
            self.__current_state = taskData[0]
            # update current field
            self.__tape[self.__head_position] = taskData[1]
            # move head accordingly
            if taskData[2] == "R":   self.__head_position += 1
            elif taskData[2] == "L": self.__head_position -= 1

    def final(self):
        return self.__current_state in self.__final_states






# - Testing the Machine - 

# Test One
#   bit flipper
initial_state = "init",
accepting_states = ["final"],
transition_function = {
    ("init","0"):("init", "1", "R"),
    ("init","1"):("init", "0", "R"),
    ("init"," "):("final"," ", "N"),
    }
final_states = {"final"}

t = TuringMachine("010011 ", 
        initial_state = "init",
        final_states = final_states,
        transition_function=transition_function)

print("Input on Tape: ",t.get_tape())
while not t.final():
    t.step()
print("Result on Tape:",t.get_tape())
print()

# Test Two
#   subtracting the smaller number from the larger (in base 1)
initial_state = "0",
accepting_states = ["stop"],
transition_function = {
    ("0"," "):("1", " ", "L"),
    ("0","0"):("0", "0", "L"),
    ("0","1"):("0", "1", "L"),

    ("1"," "):("2", " ", "R"),
    ("1","0"):("1", "0", "L"),
    ("1","1"):("1", "1", "L"),

    ("2"," "):("4", " ", "L"),
    ("2","0"):("2", "0", "R"),
    ("2","1"):("3", "0", "R"),

    ("3"," "):("7", " ", "R"),
    ("3","0"):("3", "0", "R"),
    ("3","1"):("3", "1", "R"),

    ("4"," "):("5", " ", "R"),
    ("4","0"):("4", "0", "L"),
    ("4","1"):("4", "1", "L"),

    ("5"," "):("6", " ", "R"),
    ("5","0"):("5", " ", "R"),
    ("5","1"):("5", "1", "R"),

    ("6"," "):("stop", " ", "L"),
    ("6","0"):("6", " ", "R"),
    ("6","1"):("6", "1", "R"),

    ("7"," "):("stop", " ", "L"),
    ("7","0"):("7", "0", "R"),
    ("7","1"):("0", "0", "L")
    }
final_states = {"stop"}

t = TuringMachine("11 111 ", 
        offset = -3,
        initial_state = "0",
        final_states = final_states,
        transition_function=transition_function)

print("Input on Tape: ",t.get_tape())
while not t.final():
    t.step()
print("Result on Tape:",t.get_tape())
