# The classic, single line text input interface
# tkinter.Entry(master=None, **options)
#   eg. lab = tkinter.Entry(rootNode)
# - master  : the parent node
# - options : various optional options
#             These options can be set at a later time by using the objects 
#             'config' method
# available options:
#    background, bg
#        Widget background. The default is system specific. (the option database name is background, the class is Background)
#    borderwidth, bd
#        Border width. The default is system specific, but is usually a few pixels. (borderWidth/BorderWidth)
#    cursor
#        Widget cursor. The default is a text insertion cursor (typically an “I-beam” cursor, e.g. xterm). (cursor/Cursor)
#    disabledbackground
#        Background to use when the widget is disabled. If omitted or blank, the standard background is used instead. (disabledBackground/DisabledBackground)
#    disabledforeground
#        Text color to use when the widget is disabled. If omitted or blank, the standard foreground is used instead. (disabledForeground/DisabledForeground)
#    exportselection
#        If true, selected text is automatically exported to the clipboard. Default is true. (exportSelection/ExportSelection)
#    font
#        Widget font. The default is system specific. (font/Font)
#    foreground, fg
#        Text color. (foreground/Foreground)
#    highlightbackground
#        Together with highlightcolor, this option controls how to draw the focus highlight border. This option is used when the widget doesn’t have focus. The default is system specific. (highlightBackground/HighlightBackground)
#    highlightcolor
#        Same as highlightbackground, but is used when the widget has focus. (highlightColor/HighlightColor)
#    highlightthickness
#        The width of the focus highlight border. Default is typically a few pixels, unless the system indicates focus by modifying the button itself (like on Windows). (highlightThickness/HighlightThickness)
#    insertbackground
#        Color used for the insertion cursor. (insertBackground/Foreground)
#    insertborderwidth
#        Width of the insertion cursor’s border. If this is set to a non-zero value, the cursor is drawn using the RAISED border style. (insertBorderWidth/BorderWidth)
#    insertofftime
#        Together with insertontime, this option controls cursor blinking. Both values are given in milliseconds. (insertOffTime/OffTime)
#    insertontime
#        See insertofftime. (insertOnTime/OnTime)
#    insertwidth
#        Width of the insertion cursor. Usually one or two pixels. (insertWidth/InsertWidth)
#    invalidcommand, invcmd
#        FIXME. No default. (invalidCommand/InvalidCommand)
#    justify
#        How to align the text inside the entry field. Use one of LEFT, CENTER, or RIGHT. The default is LEFT. (justify/Justify)
#    readonlybackground
#        The background color to use when the state is “readonly”. If omitted or blank, the standard background is used instead. (readonlyBackground/ReadonlyBackground)
#    relief
#        Border style. The default is SUNKEN. Other possible values are FLAT, RAISED, GROOVE, and RIDGE. (relief/Relief)
#    selectbackground
#        Selection background color. The default is system and display specific. (selectBackground/Foreground)
#    selectborderwidth
#        Selection border width. The default is system specific. (selectBorderWidth/BorderWidth)te
#    selectforeground
#        Selection text color. The default is system specific. (selectForeground/Background)
#    show
#        Controls how to display the contents of the widget. If non-empty, the widget displays a string of characters instead of the actual contents. To get a password entry widget, set this option to “*”. (show/Show)
#    state
#        The entry state: NORMAL, DISABLED, or “readonly” (same as DISABLED, but contents can still be selected and copied). Default is NORMAL. Note that if you set this to DISABLED or “readonly”, calls to insert and delete are ignored. (state/State)
#    takefocus
#        Indicates that the user can use the Tab key to move to this widget. Default is an empty string, which means that the entry widget accepts focus only if it has any keyboard bindings (default is on, in other words). (takeFocus/TakeFocus)
#    textvariable
#        Associates a Tkinter variable (usually a StringVar) to the contents of the entry field. (textVariable/Variable)
#    validate
#        Specifies when validation should be done. You can use “focus” to validate whenever the widget gets or loses the focus, “focusin” to validate only when it gets focus, “focusout” to validate when it loses focus, “key” on any modification, and ALL for all situations. Default is NONE (no validation). (validate/Validate)
#    validatecommand, vcmd
#        A function or method to call to check if the contents is valid. The function should return a true value if the new contents is valid, or false if it isn’t. Note that this option is only used if the validate option is not NONE. (validateCommand/ValidateCommand)
#    width
#        Width of the entry field, in character units. Note that this controlS the size on screen; it does not limit the number of characters that can be typed into the entry field. The default width is 20 character. (width/Width)
#    xscrollcommand
#        Used to connect an entry field to a horizontal scrollbar. This option should be set to the set method of the corresponding scrollbar. (xScrollCommand/ScrollCommand)

# Additional methods
#    delete(first, last=None)
#        Deletes the character at index, or within the given range. Use delete(0, END) to delete all text in the widget.
#        first - Start of range.
#        last - Optional end of range. If omitted, only a single character is removed.
#
#    get()
#        Gets the current contents of the entry field.
#        Returns: The widget contents, as a string.
#
#    icursor(index)
#        Moves the insertion cursor to the given index. This also sets the INSERT index.
#
#    index(index)
#        Gets the numerical position corresponding to the given index.
#        Returns: The corresponding numerical index.
#
#    insert(index, string)
#        Inserts text at the given index. Use insert(INSERT, text) to insert text at the cursor, insert(END, text) to append text to the widget.
#        string - The text to insert
#
#    scan_dragto(x)
#        Sets the scanning anchor for fast horizontal scrolling to the given mouse coordinate.
#        x - Current horizontal mouse position.
#
#    scan_mark(x)
#        Scrolls the widget contents sideways according to the given mouse coordinate. The text is moved 10 times the distance between the scanning anchor and the new position.
#        x - Current horizontal mouse position.
#
#    selection_adjust(index), select_adjust(index)
#        Adjusts the selection to include also the given character. If index is already selected, do nothing.
#
#    selection_clear(), select_clear()
#        Clears the selection.
#
#    selection_from(index), select_from(index)
#        Starts a new selection. This also sets the ANCHOR index.
#
#    selection_present(), select_present() 
#        Checks if text is selected.
#        Returns: A true value if some part of the text is selected.
#
#    selection_range(start, end), select_range(start, end)
#        Explicitly sets the selection range. Start must be smaller than end. Use selection_range(0, END) to select all text in the widget.
#        start - Start of selection range.
#        end - End of range.
#
#    selection_to(index), select_to(index)
#        Selects all text between ANCHOR and the given index.
#
#    xview(index)
#        Makes sure the given index is visible. The entry view is scrolled if necessary.
#
#    xview_moveto(fraction)
#        Adjusts the entry view so that the given offset is at the left edge of the canvas. Offset 0.0 is the beginning of the entry string, 1.0 the end.
#
#    xview_scroll(number, what)
#        Scrolls the entry view horizontally by the given amount.
#        number - Number of units.
#        what - What unit to use. This can be either “units” (characters) or “pages” (larger steps).







        
import tkinter
root = tkinter.Tk()

tkinter.Label(root, text="First Name").grid(row=0)
tkinter.Label(root, text="Last Name").grid(row=1)

e1 = tkinter.Entry(root)
e2 = tkinter.Entry(root)
e1.insert(10,"Miller")
e2.insert(10,"Jill")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   e1.delete(0,tkinter.END)
   e2.delete(0,tkinter.END)
tkinter.Button(root, text='Quit', command=root.quit        ).grid( row=3, column=0, sticky=tkinter.W, pady=4 )
tkinter.Button(root, text='Show', command=show_entry_fields).grid( row=3, column=1, sticky=tkinter.W, pady=4 )

tkinter.mainloop( )