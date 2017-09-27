# this is a basic demonstration of how to start a TK window

# first, the library
import tkinter

# # TKinter is designed around a tree model, so of course we need the root to get started
"""
root = tkinter.Tk()
# which can take a title
root.title("Window Title")

# this activates the root
root.mainloop()
"""
# subsequent code will not be run until after this window closes








# Connected Variables
#   You need a special type of variable to store data that can be changed by the wiget itself (instead of 
# having the data in some global variable and manually writing code to update it and connected things when 
# something happens/changes)
# They come in handy when using widets such as the text entry and radio buttons
# These variables come from the tkinter module
#   StringVar()     # string    - default: ""
#   IntVar()        # integer   - default: 0
#   DoubleVar()     # float     - default: 0.0
#   BooleanVar()    # boolean   - returns 0 for False and 1 for True
# variables can be edited using their "get()" and "set()" methods







# Parceled GUI Creation
# this is a way of writing your window as a class, thus saving the use of global names
# it's also a handy way of using GUIs from other places, making modules and such
"""
class App:
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        # Quit button
        self.button = tkinter.Button(
            frame, 
            text = "QUIT", 
            fg = "red",
            command = quit
        ).pack(side = tkinter.LEFT)

        # Prints to the console
        self.slogan = tkinter.Button(
            frame,
            text = "Hello",
            command = self.write_slogan
        ).pack(side = tkinter.LEFT)

        # counter and incrementation button
        self.counter = 0
        self.label = tkinter.Label(
            frame, 
            fg = "dark green",
            text = self.counter
        )
        self.label.pack(
            side = tkinter.LEFT
        )
        tkinter.Button(
            frame, 
            text = "++", 
            fg = "red",
            command = self.incrementation
        ).pack(
            side = tkinter.LEFT
        )

    def write_slogan(self):
        print("Tkinter is easy to use!")


    def incrementation(self):
        self.counter += 1
        self.label.config(text=self.counter)


root = tkinter.Tk()
app = App(root)
root.mainloop()
"""

# One can also extend the premade widgets to create new layouts for future use.

class Checkbar(tkinter.Frame):
    def __init__(self, parent=None, picks=[], side=tkinter.LEFT, anchor=tkinter.W):
        tkinter.Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = tkinter.IntVar()
            checkbox = tkinter.Checkbutton(self, text=pick, variable=var)
            checkbox.pack(side=side, anchor=anchor, expand=tkinter.YES)
            self.vars.append(var)
    def state(self):
        return map((lambda var: var.get()), self.vars)


root = tkinter.Tk()

top = Checkbar(
    root, 
    ['Python', 'Ruby', 'Perl', 'C++']
)
top.pack( side=tkinter.TOP )
bottom = Checkbar(
    root, 
    ['English','German']
)
bottom.pack( side=tkinter.LEFT )


def allstates(): 
    print(list(top.state()), list(bottom.state()))
tkinter.Button(root, text='Peek', command=allstates).pack(side=tkinter.RIGHT)

root.mainloop()