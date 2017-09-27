# the classic checkbox interface
# Radio buttons are defined separately, each with their own variable

# tkinter.Checkbutton(master=None, **options)
#   eg. lab = tkinter.Checkbutton(rootNode, text="Hello")
# - master  : the parent node
# - options : various optional options
#             These options can be set at a later time by using the objects 
#             'config' method
# available options:
#    activebackground=
#        The background color to use when the button is activated. Default value is system specific. (the database name is activeBackground, the class is Foreground)
#    activeforeground=
#        The foreground color to use when the button is activated. Default value is system specific. (activeForeground/Background)
#    anchor
#        ontrols where in the button the text (or image) should be located. Use one of N, NE, E, SE, S, SW, W, NW, or CENTER. Default is CENTER. If you change this, it is probably a good idea to add some padding as well, using the padx and/or pady options. (anchor/Anchor)
#    background, bg
#        The button background color. The default is system specific. (background/Background)
#    bitmap
#        The bitmap to display in the widget. If the image option is given, this option is ignored. 
#        You can either use a built-in bitmap, or load a bitmap from an XBM file. To load the bitmap from file, just prefix the filename with an at-sign (for example “@sample.xbm”). (bitmap/Bitmap)
#    borderwidth, bd
#        The width of the button border. The default is system specific, but is usually one or two pixels. (borderWidth/BorderWidth)
#    command
#        A function or method that is called when the button is pressed. The callback can be a function, bound method, or any other callable Python object. No default. (command/Command)
#    compound
#        Default is NONE. (compound/Compound)
#    cursor
#        The cursor to show when the mouse pointer is moved over the button. (cursor/Cursor)
#    disabledforeground
#        The color to use when the button is disabled. The background is shown in the background color. (disabledForeground/DisabledForeground)
#    font
#        The font to use in the button. The button can only contain text in a single font. The default is system specific. (font/Font)
#    foreground, fg
#        The button foreground color. The default is system specific. (foreground/Foreground)
#    height
#        The size of the button. If the button displays text, the size is given in text units. If the button displays an image, the size is given in pixels (or screen units). If the size is omitted, it is calculated based on the button contents. (height/Height)
#    highlightbackground
#        Default value is system specific. (highlightBackground/HighlightBackground)
#    highlightcolor
#        Default value is system specific. (highlightColor/HighlightColor)
#    highlightthickness
#        Default value is 1. (highlightThickness/HighlightThickness)
#    image
#        The image to display in the widget. If specified, this takes precedence over the text and bitmap options. No default. (image/Image)
#    indicatoron
#        Controls if the indicator should be drawn or not. This is on by default. 
#        Setting this option to false means that the relief will be used as the indicator. If the button is selected, it is drawn as SUNKEN instead of RAISED. (indicatorOn/IndicatorOn)
#    justify
#        Defines how to align multiple lines of text. Use LEFT, RIGHT, or CENTER (default). (justify/Justify)
#    offrelief
#        Default is raised. (offRelief/OffRelief)
#    offvalue
#        The value corresponding to a non-checked button. The default is 0. (offValue/Value)
#    onvalue
#        The value corresponding to a checked button. The default is 1. (onValue/Value)
#    overrelief
#        No default value. (overRelief/OverRelief)
#    padx
#        Button padding. Default value is 1. (padX/Pad)
#    pady
#        Button padding. Default value is 1. (padY/Pad)
#    relief
#        Border decoration. This is usually FLAT for checkbuttons, unless they use the border as indicator (via the indicatoron option). (relief/Relief)
#    selectcolor
#        Color to use for the selector. Default value is system specific. (selectColor/Background)
#    selectimage
#        Graphic image to use for the selector. No default. (selectImage/SelectImage)
#    state
#        Button state. One of NORMAL, ACTIVE or DISABLED. Default is NORMAL. (state/State)
#    takefocus
#        Indicates that the user can use the Tab key to move to this button. Default is an empty string, which means that the button accepts focus only if it has any keyboard bindings (default is on, in other words). (takeFocus/TakeFocus)
#    text
#        The text to display in the button. The text can contain newlines. If the bitmap or image options are used, this option is ignored. (text/Text)
#    textvariable
#        Associates a Tkinter variable (usually a StringVar) with the button. If the variable is changed, the button text is updated.
#        Also see the variable option. (textVariable/Variable)
#    underline
#        Which character to underline, if any. Default value is -1 (no underline). (underline/Underline)
#    variable
#        Associates a Tkinter variable to the button. When the button is pressed, the variable is toggled between offvalue and onvalue. Explicit changes to the variable are automatically reflected by the buttons. (variable/Variable)
#    width
#        The size of the button. See height for details. (width/Width)
#    wraplength
#        Determines when a button’s text should be wrapped into multiple lines. This is given in screen units. Default is no wrapping. (wrapLength/WrapLength)

# Additional methods
#   deselect()
#       Deselects the checkbox; that is, sets the value to offvalue.
#   flash()
#       Redraws the button a couple of times, alternating between active and normal appearance. This can be useful when debugging, or to indicate when some other user action has activate the button.
#   invoke()
#       Calls the command associated with the button.
#   select()
#       Selects the button; that is, sets the value to onvalue.
#   toggle()
#       Toggles the button.








# Example GUI
import tkinter
root = tkinter.Tk()


# Set up checkboxes (created with a list and for loop)
variableArray = []
languages = [
    "Python",
    "Perl",
    "Java",
    "C++",
    "C"
]
for text in languages:
    var = tkinter.IntVar()

    tkinter.Checkbutton(
        root, 
        text = text,
        variable=var
    ).pack(side=tkinter.LEFT)

    variableArray.append(var)


# Button for printing the selections to the console
def getStates(): 
    print("Checkbox States")
    for index,item in enumerate(variableArray):
        print(languages[index] + " " + str(item.get()))
tkinter.Button(root, text='Show', command=getStates).pack(side=tkinter.RIGHT)


root.mainloop()