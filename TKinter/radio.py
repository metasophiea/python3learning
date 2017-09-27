# the classic radio interface
# Radio buttons are defined separately, with a common variable connecting them together

# tkinter.Radiobutton(master=None, **options)
#   eg. lab = tkinter.Radiobutton(rootNode, text="Hello")
# - master  : the parent node
# - options : various optional options
#             These options can be set at a later time by using the objects 
#             'config' method
# available options:
#    activebackground
#        What background color to use when the button is active. The default is system specific. (the option database name is activeBackground, the class is Foreground)
#    activeforeground
#        What foreground color to use when the button is active. The default is system specific. (activeForeground/Background)
#    anchor
#        Controls where in the button the text (or image) should be located. Use one of N, NE, E, SE, S, SW, W, NW, or CENTER. Default is CENTER. (anchor/Anchor)
#    background, bg
#        The background color. The default is system specific. (background/Background)
#    bitmap
#        The bitmap to display in the widget. If the image option is given, this option is ignored. (bitmap/Bitmap)
#    borderwidth, bd
#        The width of the button border. The default is platform specific, but is usually 1 or 2 pixels. (borderWidth/BorderWidth)
#    command
#        A function or method that is called when the button is pressed. The callback can be a function, bound method, or any other callable Python object. (command/Command)
#    compound
#        Controls how to combine text and image in the button. By default, if an image or bitmap is given, it is drawn instead of the text. If this option is set to CENTER, the text is drawn on top of the image. If this option is set to one of BOTTOM, LEFT, RIGHT, or TOP, the image is drawn besides the text (use BOTTOM to draw the image under the text, etc.). Default is NONE. (compound/Compound)
#    cursor
#        The cursor to show when the mouse is moved over the button. (cursor/Cursor)
#    disabledforeground
#        The color to use when the button is disabled. The background is shown in the background color. The default is system specific. (disabledForeground/DisabledForeground)
#    font
#        The font to use in the button. The button can only contain text in a single font. The default is system specific. (font/Font)
#    foreground, fg
#        The color to use for text and bitmap content. The default is system specific. (foreground/Foreground)
#    height
#        The height of the button. If the button displays text, the size is given in text units. If the button displays an image, the size is given in pixels (or screen units). If the size is omitted, it is calculated based on the button contents. (height/Height)
#    highlightbackground
#        The color to use for the highlight border when the button does not have focus. The default is system specific. (highlightBackground/HighlightBackground)
#    highlightcolor
#        The color to use for the highlight border when the button has focus. The default is system speciific. (highlightColor/HighlightColor)
#    highlightthickness
#        The width of the highlight border. The default is system specific (usually one or two pixels). (highlightThickness/HighlightThickness)
#    image
#        The image to display in the widget. If specified, this takes precedence over the text and bitmap options. (image/Image)
#    indicatoron
#        If true, the widget uses the standard radio button look. If false, the selected button is drawn as SUNKEN instead. Default is true. (indicatorOn/IndicatorOn)
#        Note: this does not work currently on MacOS, and the buttons will always be in the standard way
#    justify
#        Defines how to align multiple lines of text. Use LEFT, RIGHT, or CENTER. Default is CENTER. (justify/Justify)
#    offrelief
#        Default is raised. (offRelief/OffRelief)
#    overrelief
#        Alternative relief to use when the mouse is moved over the widget. If empty, always use the relief value. (overRelief/OverRelief)
#    padx
#        Extra horizontal padding between the text or image and the border. (padX/Pad)
#    pady
#        Extra vertical padding between the text or image and the border. (padY/Pad)
#    relief
#        Border decoration. One of SUNKEN, RAISED, GROOVE, RIDGE, or FLAT. Default is FLAT if indicatoron is true, otherwise RAISED. (relief/Relief)
#    selectcolor
#        Default value is ‘SystemWindow’. (selectColor/Background)
#    selectimage
#        No default value. (selectImage/SelectImage)
#    state
#        The button state: NORMAL, ACTIVE or DISABLED. Default is NORMAL. (state/State)
#    takefocus
#        Indicates that the user can use the Tab key to move to this button. Default is an empty string, which means that the button accepts focus only if it has any keyboard bindings (default is on, in other words). (takeFocus/TakeFocus)
#    text
#        The text to display in the button. The text can contain newlines. If the bitmap or image options are used, this option is ignored (unless the compound option is used). (text/Text)
#    textvariable
#        Associates a Tkinter variable (usually a StringVar) to the button. If the variable is changed, the button text is updated. (textVariable/Variable)
#    underline
#        Which character to underline, in a text label. Default is -1, which means that no character is underlined. (underline/Underline)
#    value
#        The value associated with this radiobutton. All buttons in the same group should have distinct values. (value/Value)
#    variable
#        The variable that’s associated with this button. To get proper radio behaviour, you need to associate the same variable to all buttons in the same group. (variable/Variable)
#    width
#        The width of the button. If the button displays text, the size is given in text units. If the button displays an image, the size is given in pixels (or screen units). If the size is omitted, or zero, it is calculated based on the button contents. (width/Width)
#    wraplength
#        Determines when a button’s text should be wrapped into multiple lines. This is given in screen units. Default is 0 (no wrapping). (wrapLength/WrapLength)

# Additional methods
#   deselect()
#       Deselects the button.
#   flash()
#       Redraws the button a couple of times, alternating between active and normal appearance. This can be useful when debugging, or to indicate when some other user action has activate the button.
#   invoke()
#       Calls the command associated with the button.
#   select()
#       Selects the button.







# Example GUI
import tkinter
root = tkinter.Tk()


# the TK variable
variable = tkinter.IntVar()
variable.set(1)  # initializing the choice


# Headding label
tkinter.Label(root, 
      text="Choose your favourite programming language:",
      justify = tkinter.LEFT,
      padx = 20).pack()


# The radio buttons (created with a list and for loop)
def ShowChoice():
    print(variable.get())
languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]
for text, mode in languages:
    tkinter.Radiobutton(
        root, 
        text = text,
        variable = variable, 
        command=ShowChoice,
        value = mode
    ).pack(anchor=tkinter.W)


tkinter.mainloop()