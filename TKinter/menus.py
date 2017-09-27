#   This is a method of creating items for menu bars. In Windows these bars
# are within in the window, on Mac they are placed at the very top of the 
# screen (and Linux is linux) 


# tkinter.Menu(master=None, **options)
#   eg. lab = tkinter.Menu(rootNode, text="Hello")
# - master  : the parent node
# - options : various optional options
#             These options can be set at a later time by using the objects 
#             'config' method

# available methods:
#    add(type, **options)
#        append an entry of the given type to the menu.
#
#        type - What kind of entry to add. Can be one of “command”, “cascade”, “checkbutton”, “radiobutton”, or “separator”.
#        **options - Menu options
#            activebackground
#            activeforeground
#            accelerator
#            background
#            bitmap
#            columnbreak
#            command
#            font
#            foreground
#            hidemargin
#            image
#            indicatoron
#            label
#            menu
#            offvalue
#            onvalue
#            selectcolor
#            selectimage
#            state
#            underline
#            value
#            variable
#
#    insert(index, itemType, **options) - the same as add, but with an index
#
#    the following commands do what they say, with all the options shown above
#        add_cascade(**options)
#        add_checkbutton(**options)
#        add_command(**options)
#        add_radiobutton(**options)
#        add_separator(**options) 
#
#        insert_cascade(index, **options)
#        insert_checkbutton(index, **options)
#        insert_command(index, **options)
#        insert_radiobutton(index, **options)
#        insert_separator(index, **options)
#
#    config(**options)
#        Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values.
#
#        **options - Widget options.
#            activebackground
#                Default value is ‘SystemHighlight’. (the database name is activeBackground, the class is Foreground)
#            activeborderwidth
#                Default value is 0. (activeBorderWidth/BorderWidth)
#            activeforeground
#                Default value is ‘SystemHighlightText’. (activeForeground/Background)
#            background, bg
#                Default value is ‘SystemMenu’. (background/Background)
#            borderwidth, bd
#                Default value is 0. (borderWidth/BorderWidth)
#            cursor
#                Default value is ‘arrow’. (cursor/Cursor)
#            disabledforeground
#                Default value is ‘SystemDisabledText’. (disabledForeground/DisabledForeground)
#            font
#                Default value is ‘MS Sans Serif 8’. (font/Font)
#            foreground, fg
#                Default value is ‘SystemMenuText’. (foreground/Foreground)
#            postcommand
#                   If this option is specified then it provides a Tcl command to execute each time the menu is posted. The command 
#                is invoked by the post widget command before posting the menu. Note that in Tk 8.0 on Mac and Windows, all post-commands 
#                in a system of menus are executed before any of those menus are posted. This is due to the limitations in the individual 
#                platforms' menu managers.
#                No default value. (postCommand/Command)
#            relief
#                Default value is ‘flat’. (relief/Relief)
#            selectcolor
#                   For menu entries that are check buttons or radio buttons, this option specifies the color to display in the 
#                indicator when the check button or radio button is selected.
#                Default value is ‘SystemMenuText’. (selectColor/Background)
#            takefocus
#                Default value is 0. (takeFocus/TakeFocus)
#            tearoff
#                   This option must have a proper boolean value, which specifies whether or not the menu should include a tear-off 
#                entry at the top. If so, it will exist as entry 0 of the menu and the other entries will number starting at 1. The 
#                default menu bindings arrange for the menu to be torn off when the tear-off entry is invoked.
#                Default value is 1
#            tearoffcommand
#                   If this option has a non-empty value, then it specifies a Tcl command to invoke whenever the menu is torn off. 
#                The actual command will consist of the value of this option, followed by a space, followed by the name of the menu 
#                window, followed by a space, followed by the name of the name of the torn off menu window. For example, if the 
#                option's value is “a b” and menu .x.y is torn off to create a new menu .x.tearoff1, then the command 
#                “a b .x.y .x.tearoff1” will be invoked.
#            title
#                   The string will be used to title the window created when this menu is torn off. If the title is NULL, then the 
#                window will have the title of the menubutton or the text of the cascade item from which this menu was invoked.
#                No default value. (title/Title)
#            type
#                   This option can be one of 'menubar', 'tearoff', or 'normal', and is set when the menu is created. While the string 
#                returned by the configuration database will change if this option is changed, this does not affect the menu widget's 
#                behavior. This is used by the cloning mechanism and is not normally set outside of the Tk library.
#                Default value is ‘normal’. (type/Type)
#
#    delete(index1, index2=None)
#        Deletes one or more menu entries.
#        index1 - The first entry to delete.
#        index2 - The last entry to delete. If omitted, only one entry is deleted.
#
#    entrycget(index, option)
#        The entrycget method.
#
#    entryconfig(index, **options), entryconfigure(index, **options)
#        Reconfigures the given menu entry. Only the given options are changed; the rest are left as is. See add for a list of available 
#        options.
#
#    index(index)
#        Converts an index (of any kind) to an integer index.
#
#    invoke(index)
#        Invoke the action of the menu entry
#
#    post(x, y)
#        Displays the menu at the given position. The position should be given in pixels, relative to the root window.
#
#    type(index)
#        Gets the type of the given menu entry.
#
#    unpost()
#        Removes a posted menu.
#
#    yposition(index)
#        Returns the vertical offset for the given entry. This can be used to position a popup menu so that a given entry is under the 
#        mouse when the menu appears.
#        Returns - The vertical offset, in screen coordinates.








# This example creates some menu bar entries, with sub menus which have functions. It also creates a popup menu when one right-clicks
# the window, which itself has entries and commands.
import tkinter
from tkinter import filedialog

# standard setup
root = tkinter.Tk()
root.title("Menu Example")

# the creation of a menu bar object
menu = tkinter.Menu(root)


# creating a pull-down menu
filemenu = tkinter.Menu(menu)
# - adding items to the menu
def NewFile():
    print("New File!")
filemenu.add_command(label="New", command=NewFile)
def OpenFile():
    name = filedialog.askopenfilename()
    print(name)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
# - adding the menu to the menu bar
menu.add_cascade(label="File", menu=filemenu)


# creating a pull-down menu
helpmenu = tkinter.Menu(menu)
# - adding items to the menu
def About():
    print("This is a simple example of a menu")
helpmenu.add_command(label="About...", command=About)
# - adding the menu to the menu bar
menu.add_cascade(label="Help", menu=helpmenu)


# creating a pop-up menu
popupmenu = tkinter.Menu(root, tearoff=0)

# - adding items to the menu
def popUpFunction():
    print("hello!")
popupmenu.add_command(label="Say Hello", command=popUpFunction)
popupmenu.add_command(label="New", command=NewFile) # same function from the menubar

# - binding the action to root
#       This is the function actually run by the right-click, 
#   and it has to 'post' the x and y values to the popup menu
#   to activate it. These numbers are absolute to the screen
def popup(event):
    popupmenu.post(event.x_root, event.y_root)
root.bind("<Button-2>", popup)


# assigning this menu object to the root (thus activating it)
root.config(menu=menu)

    
# standard starting of interface
root.mainloop()