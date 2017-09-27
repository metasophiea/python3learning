#       The OS module provides access to the functions of the operating system, for example; accessing 
#   the terminal or working with files and directories. Further function and methods working on files 
#   and directories can be found in the module 'shutil'

import os

# Get's the programs current working directory
# (which starts out in this case; as the folder in which the script is contained)
print( os.getcwd() )
print()


# The command is used to change the working directory
os.chdir("..")
print( os.getcwd() )
os.chdir("modules")
print()


# Essentially 'ls' from BASH
print( os.listdir(".") )
print()


#   Creates a directory named "path" with numeric mode "mode", if it doesn't already exist. The default mode
# is 0777 (octal). On some systems, mode is ignored. If it is used, the current umask value is first masked
# out. If the directory already exists, OSError is raised. Parent directories will not be created, if they
# don't exist.
# - mkdir(path[, mode=0755])
# os.mkdir("hello.txt")	

#   Recursive directory creation function. Like mkdir(), but makes all intermediate-level directories needed
# to contain the leaf directory. Raises an error exception if the leaf directory already exists or cannot be
# created.
# - makedirs(name[, mode=511])

#   The file or directory "old" is renamed to "new" If "new" is a directory, an error will be raised. On Unix
# and Linux, if "new" exists and is a file, it will be replaced silently if the user has permission to do so.
# - os.rename(old, new)

#   Works like rename(), except that it creates recursively any intermediate directories needed to make the
# "new" pathname.
# - os.renames(old, new)

#   Removes the file "path"
# os.remove()

#   Removes the directory "path". rmdir() works only if the direcotry "path" is empty, otherwise an 
# error is raised. To remove whole directory trees, shutil.rmdtree() can be used.
# - os.rmdir(path)


# Execute a shell script
os.system("echo \"Hello\"")
# this command pushes the string to the terminal. The text written above works for the BASH Unix shell
# and thus won't work on a Windows machine. The command gets your text to the terminal; it doesn't care
# what happens after that

# Similar to the command above, this command also sends text to the terminal, but can collect the
# response in a list; splitting the different elements into items of that list.
print( os.popen("echo \"Hello\"").readlines() )
print( os.popen("pwd").readlines() )
print( os.popen("ls").readlines() )
# this is the 'pipe-open' function
print()







# Forking
#        Forking is the act of cloning a process in two. Both processes will have the same data, but 
#    are running as two different processes (useful for mulithreading) and can go in different directions.
#        Forking is done using the 'os.fork()' command, which will return the PID of the child process,
#    unless ofcourse you're in the child process itself, in which case this value will be zero. A negative
#    number will be returned in the event of a forking failure. One can use the 'os.getpid()' to retrive 
#    the program's process number.
"""
def child():
    print()
    print("Hello from child process, with PID:",os.getpid())
    os._exit(0)  

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print("Hello from parent process, with PID:",os.getpid(),"seems the child process' PID is",newpid)

        if input("q for quit / c for new fork") == 'c': 
            continue
        else:
            break

parent()
"""






# Process Replacement
#       This is the act of starting a different program from within a python program. The new program doesn't 
#   necessarily have to be of any type, so long as it's executable. The act of starting a new process will
#   destroy the process that called it, giving this new process the same PID.
# There are a number of commands for this action, will small differences between each:
#   os.execl   (file, arg0, arg1, …)
#   os.execle  (file, arg0, arg1, …, env)
#   os.execlp  (file, arg0, arg1, …)
#   os.execlpe (file, arg0, arg1, …, env)
#   os.execv   (path, args)
#   os.execve  (path, args, env)
#   os.execvp  (file, args)
#   os.execvpe (file, args, env)
#   os.exec -  the base name
#   l -        indicates that the arguments to be provided to the ensuing process are written out in the command
#   v -        indicates that the arguments to be provided to the ensuing process are in a list of tuple
#   p -        indicates that the command will use the PATH environment variable to locate the program file
#               When the environment is being replaced, the new environment is used as the source of the PATH variable
#               'path' must contain an appropriate absolute or relative path
#   e -        the env parameter is used and must be a mapping which is used to define the environment variables for 
#               the new process

""" os.execvp("echo",["echo","Hello"]) """
# this seems to be the easiest to get working; here we see the first item is the executable to execute, then the list of 
# arguments. The first argument should be the name of the process (though doesn't particularly have to be) and for this
# 'echo' example is ignored as the second argument is printed out

# os.execlpe("testExe.prog", "test", "other things", {"PATH":os.getcwd()})
"""
env = {"PATH":os.getcwd()}
args = ["test", "other things","like, a lot of other things"]
os.execvpe("testExe.prog", args, env)
"""
# notice how one can affect arg 0, which usually is the name of the program being called







# Pipes
# Pipes are used in the unix environment to allow the easy transfer of data between programs
#   This example shows a simple conversation between a parent and child thread, where the child 
# speaks first while the parent waits. Once the parent receives something is sends it's response
# while the child waits.
"""
def child(pipeFromParent,pipeToParent):
    os.write(pipeToParent, "Hello from child".encode())

    pipeInData = os.read(pipeFromParent, 20)
    while not pipeInData:
        pipeInData = os.read(pipeFromParent, 20)

    print("child thread received:",pipeInData.decode())

def parent():
    parentPipeProducer, parentPipeConsumer = os.pipe()
    childPipeProducer,  childPipeConsumer = os.pipe()

    if os.fork() == 0:
        child(childPipeProducer,parentPipeConsumer)
    else:
        inData = os.read(parentPipeProducer, 20)
        while not inData:
            inData = os.read(parentPipeProducer, 20)

        print("parent thread received:",inData.decode())
        os.write(childPipeConsumer, "Hello from parent".encode())

    os.close(parentPipeProducer) 
    os.close(parentPipeConsumer) 
    os.close(childPipeProducer) 
    os.close(childPipeConsumer) 

parent()
"""







# FIFO Pipe/Files
# This is a special kind of file that is similar to a pipe, but instead of being an anonymous, 
# temporary connection as a pipe it, a FIFO has a name or names like any other file. Processes 
# open the FIFO by name in order to communicate through it.
#   Processes are allowed to write to a FIFO pipe at the same time, but only one can read from it

#   This example shows simple one-way communication between two threads. First check if a Fifo
# pipe with this name has already been created; if not, one is created. Then the forking takes
# place. 
#   The parent thread will be the reader, and a pipe-like object is created with the os.open
# command; which reads in 20 bytes constantly. If the FIFO pipe has less than 20 bytes, all are
# returned. If there are no bytes, the thread stalls until some are there to be retrived.
#   The child thread is constantly printing a counter into the FIFO pipe every second. It opens
# the FIFO pipe with the same command as the parent used, just with a different argument to indicate
# what it would be using the FIFO pipe for.

import time
fifoName = "theBestFifoNameICouldComeUpWith"
if not os.path.exists(fifoName):
    os.mkfifo(fifoName) 

def parent():
    pipeIn = os.open(fifoName, os.O_RDONLY) # os.O_RDONLY = 0
    while True:
        line = os.read(pipeIn,20).decode()
        print("Parent",os.getpid(),"got",line,"at",time.time( ))

def child():
    pipeOut = os.open(fifoName, os.O_WRONLY) # os.O_WRONLY = 1
    counter = 0
    while True:
        time.sleep(1)
        print( "Sending:",("Number "+str(counter)) )
        os.write(pipeOut, ("Number "+str(counter)).encode() )
        counter = (counter+1) % 5

if os.fork() != 0:
    parent()
else:       
    child()