# This module is used to start, monitor, interact with and end other processes

import subprocess


# Here, the command is being used with BASH command text to get the local files and their details
# The command's sections are written into separate items of a list, but one can enable the 
# string-only approach ( like os.system() ) by setting 'shell=True'
x = subprocess.Popen(["ls", "-l"])
x = subprocess.Popen("ls -l",shell="True")


# The 'wait' command can be used to stop the python program from continuing until the subprocess has completed
x.wait()


print()


# This command performs the same function as above, except its stdout and stderr pipes are being 
# connected to the subprocess object's pipe holders. In this way, one can capture the streams
process = subprocess.Popen("ls -l",shell="True", stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print("stdout")
print( process.stdout.read().decode("utf-8") )
print("stderr")
print( process.stderr.read().decode("utf-8") )
# the 'read()' function returns a "bytes" object, which can be converted to a regular string with 'decode()'