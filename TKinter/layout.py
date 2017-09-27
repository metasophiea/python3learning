


# there are three layout managers, all come with options:
#   - pack    
#   the simplest of the three, this packs widgets into a cavity relative to each other
#
#       anchor
#           Where the widget is placed inside the packing box. Default is CENTER.
#       expand
#           Specifies whether the widgets should be expanded to fill any extra space in the geometry master. If false (default), the widget is not expanded.
#       fill
#           Specifies whether the widget should occupy all the space provided to it by the master. If NONE (default), keep the widget’s original size. If X (fill horizontally), Y (fill vertically), or BOTH, fill the given space along that direction. 
#           To make a widget fill the entire master widget, set fill to BOTH and expand to a non-zero value.
#       in
#           Pack this widget inside the given widget. You can only pack a widget inside its parent, or in any decendant of its parent. This option should usually be left out, in which case the widget is packed inside its parent. 
#           Note that in is a reserved word in Python. To use it as a keyword option, append an underscore (in_).
#       ipadx
#           Internal padding. Default is 0.
#       ipady
#           Internal padding. Default is 0.
#       padx
#           External padding. Default is 0.
#       pady
#           External padding. Default is 0.
#       side
#           Specifies which side to pack the widget against. To pack widgets vertically, use TOP (default). To pack widgets horizontally, use LEFT. 
#           You can also pack widgets along the BOTTOM and RIGHT edges. You can mix sides in a single geometry manager, but the results may not always be what you expect. 
"""
import tkinter
root = tkinter.Tk()

tkinter.Label(root, text="Red Sun", bg="red", fg="white").pack(
    fill=tkinter.X,
    padx=10,
    pady=10,
    side=tkinter.BOTTOM
    )
tkinter.Label(root, text="Green Grass", bg="green", fg="black").pack(
    fill=tkinter.X
    )
tkinter.Label(root, text="Blue Sky", bg="blue", fg="white").pack(
    fill=tkinter.X,
    ipadx=10,
    ipady=10
    )

root.mainloop()
"""






#   - place
#   this geometry manager allows you explicitly set the position and size of a window, 
#   either in absolute terms, or relative to another window
#    anchor
#        Where the widget is placed inside the placing box. Default is NW
#    bordermode
#        Default is INSIDE
#    height
#        height of the element
#    width
#        width of the element
#    in
#        master relative to which the widget is placed
#    relheight
#        width of this height between 0.0 and 1.0 relative to height of master (1.0 is the same height as the master)
#    relwidth
#        width of this widget between 0.0 and 1.0 relative to width of master (1.0 is the same width as the master)
#    relx
#        locate anchor of this widget between 0.0 and 1.0 relative to width of master (1.0 is right edge)
#    rely
#        locate anchor of this widget between 0.0 and 1.0 relative to height of master (1.0 is bottom edge)
#    x
#        the x position of the element
#    y
#        the y position of the element

# in this example, five labels are being drawn in absolute places with the .pack command
# These labels also happen to have clever code that figures out what the background colour
# is, and sets the text colour to black or white accordingly
"""
import tkinter, random
    
root = tkinter.Tk()
root.geometry("200x200+20+30")  # width x height + x_offset + y_offset:
     
languages = ["Python", "Perl", "C++", "Java", "Tcl/Tk"]
labels = range(5)
for i in range(5):
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
    ct_hex = "%02x%02x%02x" % tuple(ct)
    bg_colour = '#' + "".join(ct_hex)
    l = tkinter.Label(
        root,
        text=languages[i],
        fg='White' if brightness < 120 else 'Black', # clever text colour setting code
        bg=bg_colour
        )
    l.place(
        x = 20, 
        y = 30 + i*30, 
        width=120, 
        height=25
        )

root.mainloop()
"""

#   - grid    
#   arranges widgets in a grid. One simply enters in which column and row the element should be placed,
#   and the grid function automatically figures out where to place it and how to size the cells. 
#   
#    column
#        Insert the widget at this column. Column numbers start with 0. If omitted, defaults to 0.
#    columnspan
#        If given, indicates that the widget cell should span multiple columns. The default is 1.
#    in, in_
#           Place widget inside to the given widget. You can only place a widget inside its parent, or in any 
#        decendant of its parent. If this option is not given, it defaults to the parent.
#           Note that in is a reserved word in Python. To use it as a keyword option, append an underscore (in_).
#    ipadx
#        Optional horizontal internal padding. Works like padx, but the padding is added inside the widget borders. Default is 0.
#    ipady
#        Optional vertical internal padding. Works like pady, but the padding is added inside the widget borders. Default is 0.
#    padx
#        Optional horizontal padding to place around the widget in a cell. Default is 0.
#    pady
#        Optional vertical padding to place around the widget in a cell. Default is 0.
#    row
#        Insert the widget at this row. Row numbers start with 0. If omitted, defaults to the first empty row in the grid.
#    rowspan
#        If given, indicates that the widget cell should span multiple rows. Default is 1.
#    sticky
#           Defines how to expand the widget if the resulting cell is larger than the widget itself. This
#       can be any combination of the constants S, N, E, and W, or NW, NE, SW, and SE.
#           For example, W (west) means that the widget should be aligned to the left cell border. W+E 
#       means that the widget should be stretched horizontally to fill the whole cell. W+E+N+S means that 
#       the widget should be expanded in both directions. Default is to center the widget in the cell.

# The following example produces a table of colours with the names to their left
"""
import tkinter
root = tkinter.Tk()

colours = ['red','green','orange','white','yellow','blue']

r = 0
for c in colours:
    tkinter.Label(root,text=c, relief=tkinter.RIDGE,width=15).grid(row=r,column=0)
    tkinter.Entry(root,bg=c, relief=tkinter.SUNKEN,width=10).grid(row=r,column=1)
    r = r + 1

root.mainloop()
"""