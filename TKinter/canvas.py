# This is an example the Canvas and how one can draw to it and receive events from it

# tkinter.Canvas(master=None, **options)
#   eg. lab = tkinter.Canvas(rootNode, text="Hello")
# - master  : the parent node
# - options : various optional options
#             These options can be set at a later time by using the objects 
#             'config' method

# there is a lot of these; here are some

# options:
# bd, borderwidth	
#     Width of the border around the outside of the canvas; see Section 5.1, “Dimensions”. The default is two pixels.
# bg, background	
#     Background color of the canvas. Default is a light gray, about '#E4E4E4'.
# closeenough	
#     A float that specifies how close the mouse must be to an item to be considered inside it. Default is 1.0.
# confine	
#     If true (the default), the canvas cannot be scrolled outside of the scrollregion (see below).
# cursor	
#     Cursor used in the canvas. See Section 5.8, “Cursors”.
# height	
#     Size of the canvas in the Y dimension. See Section 5.1, “Dimensions”.
# highlightbackground	
#     Color of the focus highlight when the widget does not have focus. See Section 53, “Focus: routing keyboard input”.
# highlightcolor	
#     Color shown in the focus highlight.
# highlightthickness	
#     Thickness of the focus highlight. The default value is 1.
# relief	
#     The relief style of the canvas. Default is tk.FLAT. See Section 5.6, “Relief styles”.
# scrollregion	
#     A tuple (w, n, e, s) that defines over how large an area the canvas can be scrolled, where w is the left side, n the top, e the right side, and s the bottom.
# selectbackground	
#     The background color to use displaying selected items.
# selectborderwidth	
#     The width of the border to use around selected items.
# selectforeground	
#     The foreground color to use displaying selected items.
# takefocus	
#     Normally, focus (see Section 53, “Focus: routing keyboard input”) will cycle through this widget with the tab key only if there are keyboard bindings set for it (see Section 54, “Events” for an overview of keyboard bindings). If you set this option to 1, focus will always visit this widget. Set it to '' to get the default behavior.
# width	
#     Size of the canvas in the X dimension. See Section 5.1, “Dimensions”.
# xscrollincrement	
#     Normally, canvases can be scrolled horizontally to any position. You can get this behavior by setting xscrollincrement to zero. If you set this option to some positive dimension, the canvas can be positioned only on multiples of that distance, and the value will be used for scrolling by scrolling units, such as when the user clicks on the arrows at the ends of a scrollbar. For more information on scrolling units, see Section 22, “The Scrollbar widget”.
# xscrollcommand	
#     If the canvas is scrollable, set this option to the .set() method of the horizontal scrollbar.
# yscrollincrement	
#     Works like xscrollincrement, but governs vertical movement.
# yscrollcommand	
#     If the canvas is scrollable, this option should be the .set() method of the vertical scrollbar.

# methods:
#   create_arc()
#   create_bitmap()
#   create_image()
#   create_line()
#   create_oval()
#   create_polygon()
#   create_rectangle()
#   create_text()
#   create_window()








import tkinter
root = tkinter.Tk()
root.title("Canvas Example")

# basic setup of a canvas
canvasWidth, canvasHeight = 800, 600
element = tkinter.Canvas(
    root, 
    width=canvasWidth,
    height=canvasHeight)
element.pack()

# drawin' stuff
# - line
element.create_line(      0,   0,   50,  20,  fill="#476042", width=3)
element.create_line(      0,   100, 50,  80,  fill="#476042", width=3)
element.create_line(      150, 20,  200, 0,   fill="#476042", width=3)
element.create_line(      150, 80,  200, 100, fill="#476042", width=3)
# - polygon
element.create_polygon(
    [0,0,canvasWidth,canvasHeight/2, 0, canvasHeight], 
    outline="#476042", 
    fill='yellow', 
    width=3
    )
# - rectangle
element.create_rectangle( 50,  20,  150, 80,  fill="#476042")
element.create_rectangle( 65,  35,  135, 65,  fill="yellow" )
# - oval
element.create_oval(50,50,100,100,fill="green")
# - text
element.create_text(canvasWidth/2, canvasHeight/2, text="Python")
# - bitmaps
bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
step_x = int(canvasWidth / len(bitmaps))
for i in range(0, len(bitmaps)):
   element.create_bitmap(
       (i+1)*step_x - step_x/2,
       80, 
       bitmap=bitmaps[i]
       )
# - images
img = tkinter.PhotoImage(file="/Users/metasophiea/Code/Python/learning/TKinter/tuesdayPartTwo.ppm")
element.create_image(500,0, anchor=tkinter.NW, image=img)

# mouse interaction
def paint(event):
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   element.create_oval( x1, y1, x2, y2, fill="#476042" )
element.bind( "<B1-Motion>", paint )

root.mainloop()