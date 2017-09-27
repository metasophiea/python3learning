# - usual dialogues -
# askokcancel(title=None, message=None, **options)
#     Ask if operation should proceed; return true if the answer is ok
# askquestion(title=None, message=None, **options)
#     Ask a question
# askretrycancel(title=None, message=None, **options)
#     Ask if operation should be retried; return true if the answer is yes
# askyesno(title=None, message=None, **options)
#     Ask a question; return true if the answer is yes
# askyesnocancel(title=None, message=None, **options)
#     Ask a question; return true if the answer is yes, None if cancelled.
# showerror(title=None, message=None, **options)
#     Show an error message
# showinfo(title=None, message=None, **options)
# Show an info message
#     showwarning(title=None, message=None, **options)
#     Show a warning message 








# - Simple Example -
"""
import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.title("Message Box Example")

def answer():
    messagebox.showerror("Answer", "Sorry, no answer available")

def callback():
    if messagebox.askyesno('Verify', 'Really quit?'):
        messagebox.showwarning('Yes', 'Not yet implemented')
    else:
        messagebox.showinfo('No', 'Quit has been cancelled')

tkinter.Button(root,text='Quit', command=callback).pack(fill=tkinter.X)
tkinter.Button(root,text='Answer', command=answer).pack(fill=tkinter.X)
root.mainloop()
"""







# - Starting the 'Open File' dialogue -
"""
import tkinter
from tkinter import filedialog

root = tkinter.Tk()
root.title("Open File Example")

def callback():
    name = tkinter.filedialog.askopenfilename() 
    # this function returns the complete path to the selected file as a string
    print(name)
    
errmsg = 'Error!'
tkinter.Button(root,text='File Open', command=callback).pack(fill=tkinter.X)
root.mainloop()
"""








# - Starting the Colour Chooser -
import tkinter
from tkinter import colorchooser             
root = tkinter.Tk()
root.title("Colour Chooser Example")

def callback():
    result = colorchooser.askcolor(
        color="#6A9662", # initial colour
        title = "World's Greatest Colour Chooser"
        )
    # this function returns a tuple of the RGB values (from 0 to 255, with decimal places) as a tuple, and a string of the hex value
    print(result)

tkinter.Button(root, text='Choose Color', fg="darkgreen", command=callback).pack(side=tkinter.LEFT, padx=10)
tkinter.Button(root, text='Quit', command=root.quit,fg="red").pack(side=tkinter.LEFT, padx=10)
root.mainloop()