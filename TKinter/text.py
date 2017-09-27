# This is an example the Text widget, a versetile element, capable of being edited 
# while also capable of displaying links, images, and styling

# tkinter.Text(master=None, **options)
#   eg. lab = tkinter.Text(rootNode, text="Hello")
# - master  : the parent node
# - options : various optional options
#             These options can be set at a later time by using the objects 
#             'config' method

# available options:
# autoseparators
#     Default is 1. (autoSeparators/AutoSeparators)
# background, bg
#     Default value is system specific. (the database name is background, the class is Background)
# borderwidth, bd
#     Default value is 2. (borderWidth/BorderWidth)
# cursor
#     Default value is “xterm”. (cursor/Cursor)
# exportselection
#     Default value is 1. (exportSelection/ExportSelection)
# font
#     Default value is system specific. (font/Font)
# foreground, fg
#     Default value is system specific. (foreground/Foreground)
# height
#     Default value is 24. (height/Height)
# highlightbackground
#     Default value is system specific. (highlightBackground/HighlightBackground)
# highlightcolor
#     Default value is system specific. (highlightColor/HighlightColor)
# highlightthickness
#     Default value is 0. (highlightThickness/HighlightThickness)
# insertbackground
#     Default value is system specific. (insertBackground/Foreground)
# insertborderwidth
#     Default value is 0. (insertBorderWidth/BorderWidth)
# insertofftime
#     Default value is 300. (insertOffTime/OffTime)
# insertontime
#     Default value is 600. (insertOnTime/OnTime)
# insertwidth
#     Default value is 2. (insertWidth/InsertWidth)
# maxundo
#     Default is 0. (maxUndo/MaxUndo)
# padx
#     Default value is 1. (padX/Pad)
# pady
#     Default value is 1. (padY/Pad)
# relief
#     Default value is SUNKEN. (relief/Relief)
# selectbackground
#     Default value is system specific. (selectBackground/Foreground)
# selectborderwidth
#     Default value is 0. (selectBorderWidth/BorderWidth)
# selectforeground
#     Default value is system specific. (selectForeground/Background)
# setgrid
#     Default value is 0. (setGrid/SetGrid)
# spacing1
#     Default value is 0. (spacing1/Spacing)
# spacing2
#     Default value is 0. (spacing2/Spacing)
# spacing3
#     Default value is 0. (spacing3/Spacing)
# state
#     Default value is NORMAL. (state/State)
# tabs
#     No default value. (tabs/Tabs)
# takefocus
#     No default value. (takeFocus/TakeFocus)
# undo
#     Default is 0. (undo/Undo)
# width
#     Default value is 80. (width/Width)
# wrap
#     Default value is CHAR. (wrap/Wrap)
# xscrollcommand
#     No default value. (xScrollCommand/ScrollCommand)
# yscrollcommand
#     No default value. (yScrollCommand/ScrollCommand)

# Additional methods
# bbox(index)
#     Calculates the bounding box for the given character.
#     This method only works if the text widget is updated. To make sure this is the case, you can call the update_idletasks method first.
#     index - Character index.
#     Returns - A 4-tuple (x, y, width, height), or None, if the character is not visible.
# 
# compare(index1, op, index2)
#     Compares two indexes. The op argument is one of “<”, “<=”, “==”, “>=”, “>”, or “!=” (Python’s “<>” syntax is not supported).
#     index1 - First index.
#     op - Operator (see above).
#     index2 - Second index.
#     Returns - A true value if the condition is true.
# 
# debug(boolean=None)
#     Enables or disables debugging.
# 
# delete(start, end=None)
#     Deletes the character (or embedded object) at the given position, or all text in the given range. Any marks within the range are moved to the beginning of the range.
# 
#     start - Start index.
#     end = End index. If omitted, only one character is deleted.
# 
# dlineinfo(index)
#     Calculates the bounding box for the line containing the given character.
#     This method only works if the text widget is updated. To make sure this is the case, you can call the update_idletasks method first.
# 
#     index - Character index
#     Returns - A 5-tuple: (x, y, width, height, offset). The last tuple member is the offset from the top of the line to the baseline. If the line is not visible, this method returns None.
# 
# dump(index1, index2=None, command=None, **kw)
#     Dumps the widget contents.
# 
# edit_modified(arg=None)
# edit_redo()
# edit_reset()
# edit_separator()
# edit_undo()
# 
# get(start, end=None)
#     Returns the character at the given position, or all text in the given range.
# 
#     start - Start position.
#     end - End position. If omitted, only one character is returned.
# 
# image_cget(index, option)
#     Returns the current value of the given option. If there’s no image on the given position, this method raises a TclError exception. Not implemented in Python 1.5.2 and earlier.
# 
#     index - Index specifier
#     option - Image option
#     Returns = Option value
# 
# image_configure(index, **options)
#     Modifies one or more image options. If there’s no image on the given position, this method raises a TclError exception. Not implemented in Python 1.5.2 and earlier.
# 
#     index - Index specifier.
#     **options - Image options.
#         align=
#         image= An image object. This must be a PhotoImage or BitmapImage object, or any compatible object.
#         name=
#         padx=
#         pady=
# 
# image_create(index, cnf={}, **kw)
#     Inserts an image at the given position. The image must be a a Tkinter PhotoImage or BitmapImage instance (or an instance of the corresponding PIL classes).
#     This method doesn’t work with Tk versions before 8.0. As a workaround, you can put the image in a Label widget, and use window_create to insert the label widget.
# 
#     index - Index specifier.
#     **options - Image options. See image_config for a complete list.
# 
# image_names()
#     Finds the names of all images embedded in the text widget. Tkinter doesn’t provide a way to get the corresponding PhotoImage or BitmapImage objects, but you can keep track of those yourself using a dictionary (using str(image) as the key).
# 
#     Returns - A tuple containing image names.
# 
# index(index)
#     Returns the “line.column” index corresponding to the given index.
# 
#     index - Index specifier.
#     Returns - The corresponding row/column, given as a “line.column” string.
# 
# insert(index, text, *tags)
#     Inserts text at the given position. The index is typically INSERT or END. If you provide one or more tags, they are attached to the new text.
#     If you insert text on a mark, the mark is moved according to its gravity setting.
# 
#     index - Where to insert the text.
#     text - The text to insert.
#     *tags - Optional tags to attach to the text.
# 
# mark_gravity(self, name, direction=None)
#     Sets the gravity for the given mark. The gravity setting controls how to move the mark if text is inserted exactly on the mark. If LEFT, the mark is not moved if text is inserted at the mark (that is, the text is inserted just after the mark). If RIGHT, the mark is moved to the right end of the text (that is, the text is inserted just before the mark). The default gravity setting is RIGHT.
#     name - The name of the mark.
#     direction - The gravity setting (LEFT or RIGHT). If this argument is omitted, the method returns the current gravity setting.
#     Returns - The current gravity setting, if direction was omitted.
# 
# mark_names()
#     Finds the names of all marks used in the widget. This includes the INSERT and CURRENT marks (but not END, which is a special index, not a mark).
#     Returns - A tuple containing mark names.
# 
# mark_next(index)
# mark_previous(index)
#
# mark_set(name, index)
#     Moves the mark to the given position. If the mark doesn’t exist, it is created (with gravity set to RIGHT). You also use this method to move the predefined INSERT and CURRENT marks.
# 
# mark_unset(name)
#     Removes the given mark from the widget. You cannot remove the builtin INSERT and CURRENT marks.
# 
# scan_dragto(x, y)
#     Scrolls the widget contents. The text view is moved 10 times the distance between the scanning anchor and the new position.
# 
# scan_mark(x, y)
#     Sets the scanning anchor. This anchor is used for fast scrolling.
# 
# search(pattern, index, stopindex=None, forwards=None, backwards=None, exact=None, regexp=None, nocase=None, count=None)
#     Searches for text strings or regular expressions.
# 
# see(index)
#     Makes sure a given position is visible. If the index isn’t visible, scroll the view as necessary.
# 
# tag_add(tagName, index1, *args)
# tag_bind(tagName, sequence, func, add=None)
# tag_cget(tagName, option)
# tag_config(tagName, cnf={}, **kw)
# tag_configure(tagName, cnf={}, **kw)
# tag_delete(*tagNames)
# tag_lower(tagName, belowThis=None)
# tag_names(index=None)
# tag_nextrange(tagName, index1, index2=None)
# tag_prevrange(tagName, index1, index2=None)
# tag_raise(tagName, aboveThis=None)
# tag_ranges(tagName)
# tag_remove(tagName, index1, index2=None)
# tag_unbind(tagName, sequence, funcid=None)
# 
# window_cget(index, option)
#     Returns the current value of the given window option. If there’s no window on the given position, this method raises a TclError exception.
# 
# window_config(index, **options), window_configure(index, cnf=None, **kw)
#     Modifies one or more window options. If there’s no window on the given position, this method raises a TclError exception.
#     index
#     **options
#         align=
#         create=
#         padx=
#         pady=
#         stretch=
#         window=
# 
# window_create(index, **options)
#     Inserts a widget at the given position. You can either create the widget (which should be a child of the text widget itself) first, and insert it using the window option, or provide a create callback which is called when the window is first displayed.
#     index - Index specifier
#     **options - Window options. See window_config for a complete list.
# 
# window_names()
#     Returns a tuple containing all windows embedded in the text widget. In 1.5.2 and earlier, this method returns the names of the widgets, rather than the widget instances.
#     Here’s how to convert the names to a list of widget instances in a portable fashion:
# 
#     windows = text.window_names()
#     try:
#         windows = map(text.nametowidget, windows)
#     except TclError:
#         pass
# 
#     Returns - A list of window names.
# 
# xview(*what)
# xview_moveto(fraction)
# xview_scroll(number, what)
# yview(*what)
# yview_moveto(fraction)
# yview_pickplace(*what)
# yview_scroll(number, what)

import tkinter
root = tkinter.Tk()
root.title("Text Example")


T = tkinter.Text(
    root, 
    height=10, 
    width=60)

# the addition of a scrollbar
S = tkinter.Scrollbar(root)
S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
T.pack(side=tkinter.LEFT, fill=tkinter.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

# putting in text
quote = """HAMLET: To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to. 'Tis a consummation
Devoutly to be wished."""
T.insert(tkinter.END, quote)

# styling
T.tag_configure(
    'bold_italics', 
    font=('Arial', 12, 'bold', 'italic')
    )
T.tag_configure(
    'big', 
    font=('Verdana', 20, 'bold')
    )
T.insert(tkinter.END,'\nWilliam Shakespeare\n', 'big')
T.insert(tkinter.END,'\nwho was an author\n', 'bold_italics')

# inserting an image
photo = tkinter.PhotoImage(file="/Users/metasophiea/Code/Python/learning/TKinter/tuesdayPartTwo.ppm")
T.insert(tkinter.END,'\n')
T.image_create(tkinter.END, image=photo)

root.mainloop()