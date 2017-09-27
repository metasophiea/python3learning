# tkinter.Label(master=None, **options)
#   eg. lab = tkinter.Label(rootNode, text="Hello")
# - master  : the parent node
# - options : various optional options
#             These options can be set at a later time by using the objects 
#             'config' method
# available options:
#   activebackground
#       What background color to use when the label is active (set with the state option). The default is platform specific. (the option database name is activeBackground, the class is Foreground)
#   activeforeground
#       What foreground color to use when the label is active. The default is platform specific. (activeForeground/Background)
#   anchor
#       Controls where in the label the text (or image) should be located. Use one of N, NE, E, SE, S, SW, W, NW, or CENTER. Default is CENTER. (anchor/Anchor)
#   background, bg
#       The background color. The default is platform specific. (background/Background)
#   bitmap
#       The bitmap to display in the widget. If the image option is given, this option is ignored. (bitmap/Bitmap)
#   borderwidth, bd
#       The width of the label border. The default is system specific, but is usually one or two pixels. (borderWidth/BorderWidth)
#   compound
#       Controls how to combine text and image in the label. By default, if an image or bitmap is given, it is drawn instead of the text. If this option is set to CENTER, the text is drawn on top of the image. If this option is set to one of BOTTOM, LEFT, RIGHT, or TOP, the image is drawn besides the text (use BOTTOM to draw the image under the text, etc.). Default is NONE. (compound/Compound)
#   cursor
#       What cursor to show when the mouse is moved over the label. The default is to use the standard cursor. (cursor/Cursor)
#   disabledforeground
#       What foreground color to use when the label is disabled. The default is system specific. (disabledForeground/DisabledForeground)
#   font
#       The font to use in the label. The label can only contain text in single font. The default is system specific. (font/Font)
#   foreground, fg
#       he label color, used for for text and bitmap labels. The default is system specific. (foreground/Foreground)
#   height
#       The height of the label. If the label displays text, the size is given in text units. If the label displays an image, the size is given in pixels (or screen units). If the size is set to 0, or omitted, it is calculated based on the label contents. (height/Height)
#   highlightbackground
#       What color to use for the highlight border when the widget does not have focus. The default is system specific, but usually the same as the standard background color. (highlightBackground/HighlightBackground)
#   highlightcolor
#       What color to use for the highlight border when the widget has focus. The default is system specific. (highlightColor/HighlightColor)
#   highlightthickness
#       The width of the highlight border. The default is 0 (no highlight border). (highlightThickness/HighlightThickness)
#   image
#       The image to display in the widget. The value should be a PhotoImage, BitmapImage, or a compatible object. If specified, this takes precedence over the text and bitmap options. (image/Image)
#   justify
#       Defines how to align multiple lines of text. Use LEFT, RIGHT, or CENTER. Note that to position the text inside the widget, use the anchor option. Default is CENTER. (justify/Justify)
#   padx
#       Extra horizontal padding to add around the text. The default is 1 pixel. (padX/Pad)
#   pady
#       Extra vertical padding to add around the text. The default is 1 pixel. (padY/Pad)
#   relief
#       Border decoration. The default is FLAT. Other possible values are SUNKEN, RAISED, GROOVE, and RIDGE. (relief/Relief)
#   state
#       Label state. This option controls how the label is rendered. The default is NORMAL. Other possible values are ACTIVE and DISABLED. (state/State)
#   takefocus
#       If true, the widget accepts input focus. The default is false. (takeFocus/TakeFocus)
#   text
#       The text to display in the label. The text can contain newlines. If the bitmap or image options are used, this option is ignored. (text/Text)
#   textvariable
#       Associates a Tkinter variable (usually a StringVar) with the label. If the variable is changed, the label text is updated. (textVariable/Variable)
#   underline
#       Used with the text option to indicate that a character should be underlined (e.g. for keyboard shortcuts). Default is -1 (no underline). (underline/Underline)
#   width
#       The width of the label. If the label displays text, the size is given in text units. If the label displays an image, the size is given in pixels (or screen units). If the size is set to 0, or omitted, it is calculated based on the label contents. (width/Width)
#   wraplength
#       Determines when a label’s text should be wrapped into multiple lines. This is given in screen units. Default is 0 (no wrapping). (wrapLength/WrapLength)






# Adding Text
# import tkinter
# root = tkinter.Tk()

# w = tkinter.Label(root, text="Hello Tkinter!")
# v = tkinter.Label(root, text="Hey everybody")

# w.pack() # this adds the item to the window, informing the container to adjust it's size to fit everything in snugly
# v.pack() # ditto

# root.mainloop()






# Fun With Fonts!
# (note the faster way of adding elements when we don't need to affect them at a later time)
import tkinter
root = tkinter.Tk()

# the font data is contained within a string or in a tuple
# colour data can be one of the defined colour names, or a hex value (with hash prefix)
tkinter.Label(root, 
    text        = "Red Text in Times Font",
    foreground  = "red",
    font        = "Times 50"
    ).pack()
tkinter.Label(root, 
    text        = "Green Text in Helvetica Font",
    foreground  = "light green",
    background  = "dark green",
    font        = ("Helvetica",64,"bold","italic")
    ).pack()
tkinter.Label(root, 
    text        = "Blue Text in Verdana bold",
    fg          = "blue",
    bg          = "#00ffff",
    font        = "Verdana 50 bold"
    ).pack()

root.mainloop()






# Adding an image
# import tkinter
# root = tkinter.Tk()

# logo = tkinter.PhotoImage(file="/Users/metasophiea/Code/git/metasophiea.github.io/lib/image/icon.gif")
# # interestingly, a reference to the image data must be made and kept like this to prevent the interpreter from dumping the image data
# logo = logo.subsample(4) # this can be used to reduce an image's size, here by 1/4. Another argument can be added to adjust x height and width separately (logo.zoom is the opposite method)

# explanation = """At present, only GIF and PPM/PGM
# formats are supported, but an interface 
# exists to allow additional image file
# formats to be added easily.""" # this text is printed as written

# tkinter.Label(
#     root,
#     compound=tkinter.LEFT, # pushes the image to the left. 'CENTER' would place the text on-top of the image
#     text=explanation, 
#     image=logo
# ).pack(side="right")
# root.mainloop()