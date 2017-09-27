#       Binding, is the act of attaching code to events that can occur in an interface. These events
# can be specified in the binding method (which is available with all widgets) Handlers can event be
# attached to widgets that already have a event function (eg. a button)
#
#   widget.bind(event, handler)
#       event - a string defining which event will trigger the handler code
#               presented in the form: <modifier-type-detail>
#       handler - the attached code
#
#   Some definable events include:
# <Button>	
#       A mouse button is pressed with the mouse pointer over the widget. The detail part specifies
#   which button, e.g. The left mouse button is defined by the event <Button-1>, the middle button
#   by <Button-2>, and the rightmost mouse button by <Button-3>
#       <Button-4> Defines the scroll up event on mice with wheel support and and <Button-5> the
#   scroll down. If you press down a mouse button over a widget and keep it pressed, Tkinter will
#   automatically "grab" the mouse pointer. Further mouse events like Motion and Release events will
#   be sent to the current widget, even if the mouse is moved outside the current widget. The current
#   position, relative to the widget, of the mouse pointer is provided in the x and y members of the
#   event object passed to the callback. You can use ButtonPress instead of Button, or even leave it
#   out completely: <button-1>, <buttonpress-1>, and <1> are all synonyms.
#
# <Motion>	
#       The mouse is moved with a mouse button being held down. To specify the left, middle or right
#   mouse button use <B1-Motion>, <B2-Motion> and <B3-Motion> respectively. The current position of
#   the mouse pointer is provided in the x and y members of the event object passed to the callback,
#   i.e. event.x, event.y
#
# <ButtonRelease>
#       Event, if a button is released. To specify the left, middle or right mouse button use
#   <ButtonRelease-1>, <ButtonRelease-2>, and <ButtonRelease-3> respectively. The current position
#   of the mouse pointer is provided in the x and y members of the event object passed to the 
#   callback, i.e. event.x, event.y
#
# <Double-Button>
#       Similar to the Button event, see above, but the button is double clicked instead of a single
#   click. To specify the left, middle or right mouse button use <Double-Button-1>, 
#   <Double-Button-2>, and <Double-Button-3> respectively.
#       You can use Double or Triple as prefixes. Note that if you bind to both a single click 
#   (<Button-1>) and a double click (<Double-Button-1>), both bindings will be called.
#
# <Enter>	
#       The mouse pointer entered the widget.
#   Note: This doesn't mean that the user pressed the Enter key!. <Return> is used for this purpose.
#
# <Leave>	
#       The mouse pointer left the widget.
#
# <FocusIn>
#       Keyboard focus was moved to this widget, or to a child of this widget.
#
# <FocusOut>	
#       Keyboard focus was moved from this widget to another widget.
#
# <Return>	
#       The user pressed the Enter key. You can bind to virtually all keys on the keyboard: The
#   special keys are Cancel (the Break key), BackSpace, Tab, Return(the Enter key), Shift_L 
#   (any Shift key), Control_L (any Control key), Alt_L (any Alt key), Pause, Caps_Lock, Escape,
#   Prior (Page Up), Next (Page Down), End, Home, Left, Up, Right, Down, Print, Insert, Delete, F1,
#   F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Num_Lock, and Scroll_Lock.
#
# <Key>	
#       The user pressed any key. The key is provided in the char member of the event object passed
#   to the callback (this is an empty string for special keys).
#
# a	
#       The user typed an "a" key. Most printable characters can be used as is. The exceptions are
#   space (<space>) and less than (<less>). Note that 1 is a keyboard binding, while <1> is a button
#   binding.
#
# <Shift-Up>	
#       The user pressed the Up arrow, while holding the Shift key pressed. You can use prefixes
#   like Alt, Shift, and Control.
#
# <Configure>	
#       The size of the widget changed. The new size is provided in the width and height attributes
#   of the event object passed to the callback. On some platforms, it can mean that the location
#   changed.








"""
# This example creates a simple button, that when clicked, writes text to the console; and when
# double-clicked writes different text and closes the program. Interestingly; double-clicking
# activates the single click event once 
import tkinter
root = tkinter.Tk()
root.title("Clicking")

widget = tkinter.Button(root, text='Mouse Clicks')
widget.pack()

# binding the single click event code
def hello(event):
    print("Single Click, Button-l") 
widget.bind('<Button-1>', hello)

# binding the double click event code
def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 
widget.bind('<Double-1>', quit) 

root.mainloop()
"""








# This example creates a simple display of text; but when a cursor is moved over it, the coordinates of that
# cursor are printed to the console
import tkinter
root = tkinter.Tk()
root.title("Movement")

whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tkinter.Message(root, text = whatever_you_do, bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()

# binding the motion event code
def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return
msg.bind('<Motion>',motion)

root.mainloop()