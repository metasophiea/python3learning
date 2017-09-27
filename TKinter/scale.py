# This is an example the Scale widget and how one can work with it

# tkinter.Scale(master=None, **options)
#   eg. lab = tkinter.Scale(rootNode, text="Hello")
# - master  : the parent node
# - options : various optional options
#             These options can be set at a later time by using the objects 
#             'config' method

# available options:
# activebackground
#     Default value is system specific. (the database name is activeBackground, the class is Foreground)
# background, bg
#     Default value is system specific. (background/Background)
# bigincrement
#     Default value is 0. (bigIncrement/BigIncrement)
# borderwidth, bd
#     Default value is 2. (borderWidth/BorderWidth)
# command
#     No default value. (command/Command)
# cursor
#     No default value. (cursor/Cursor)
# digits
#     Default value is 0. (digits/Digits)
# font
#     Default value is system specific. (font/Font)
# foreground, fg
#     Default value is system specific. (foreground/Foreground)
# from
#     Default value is 0. (from/From)
# highlightbackground
#     Default value is system specific. (highlightBackground/HighlightBackground)
# highlightcolor
#     Default value is system specific. (highlightColor/HighlightColor)
# highlightthickness
#     Default value is 2. (highlightThickness/HighlightThickness)
# label
#     No default value. (label/Label)
# length
#     Default value is 100. (length/Length)
# orient
#     Default value is VERTICAL. (orient/Orient)
# relief
#     Default value is FLAT. (relief/Relief)
# repeatdelay
#     Default value is 300. (repeatDelay/RepeatDelay)
# repeatinterval
#     Default value is 100. (repeatInterval/RepeatInterval)
# resolution
#     Default value is 1. (resolution/Resolution)
# showvalue
#     Default value is 1. (showValue/ShowValue)
# sliderlength
#     Default value is 30. (sliderLength/SliderLength)
# sliderrelief
#     Default value is RAISED. (sliderRelief/SliderRelief)
# state
#     Default value is NORMAL. (state/State)
# takefocus
#     No default value. (takeFocus/TakeFocus)
# tickinterval
#     Default value is 0. (tickInterval/TickInterval)
# to
#     Default value is 100. (to/To)
# troughcolor
#     Default value is system specific. (troughColor/Background)
# variable
#     No default value. (variable/Variable)
# width
#     Default value is 15. (width/Width)

# Additional methods
# coords(value=None)
#     Gets the screen coordinate corresponding to the given scale value.
#     value - A scale value. If omitted, this method uses the current setting.
#     Returns - The corresponding screen coordinate, as a 2-tuple.
# get()
#     Gets the current scale value. Tkinter returns an integer if possible, otherwise a floating point value.
#     Returns - The current value, as an integer or floating point value. To make sure you have a floating point value, use float(scale.get()).
# identify(x, y)
#     Checks if an active part of the scale is at the given screen location.
#     x - The horisontal screen coordinate.
#     y - The vertical screen coordinate.
#     Returns - A string identifying what part of the scale is at the given location. This can be “slider”, “through1” (above or to the left of the slider), “through2” (below or to the right), or an empty string for any other part of the widget.
# set(value)
#     Sets the scale value.
#     value - The new scale value.








import tkinter
root = tkinter.Tk()
root.title("Scale Example")


element_1 = tkinter.Scale(
    root, 
    from_=0, 
    to=42,
    tickinterval=10
    )
element_1.pack()
element_2 = tkinter.Scale(
    root, 
    from_=0, 
    to=200, 
    orient=tkinter.HORIZONTAL
    )
element_2.set(19)
element_2.pack()


# Accessing the scale's values
def show_values():
    print (element_1.get(), element_2.get())
tkinter.Button(
    root, 
    text='Show',
     command=show_values
     ).pack()

root.mainloop()