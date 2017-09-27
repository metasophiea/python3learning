#       This is the act of splitting sections of the program into separate threads for the purposes of multithreading 
#   and parallel processing. Two modules are used; the depreciated 'thread' module (accessable in python3 with '_thread')
#   and 'threading'

# Example using the depreciated 'thread' module
#   Here we see the execution of three instances of the 'heron' function, which is used to determine a square root. The
# '_thread.start_new_thread' function is used to start an instance of this function in a different thread. This function
# returns the thread identifier. The process itself cannot return anything to the calling process, however it can have
# access to global variables.
#   After a thread is started, the calling process continues as normal which in this case would end the program, ending
# the threads. So measures have been implemented to wait for the threads to finish; the 'num_threads' global counts how 
# many threads are running thus forcing the while loop at the bottom of the main process to wait until this number reaches
# zero. Interestingly, sub threads don't start instantly, thus an extra method must be taken to stop the process from ending 
# instantly (the 'thread_started' global) 
#   To edit these globals in a safe way, the thread must be locked. The lock is produced with the '_thread.allocate_lock()'
# command, and used with the 'with lock' command. All code within this block is run to completeion.
#   Note how the thread staring function takes a tuple (or list) of arguments, ending in a comma


# import _thread
#
# num_threads = 0
# thread_started = False
# lock = _thread.allocate_lock()
#
# def heron(a):
#     global num_threads, thread_started
#     with lock:
#         num_threads += 1
#         thread_started = True
# 
#     """Calculates the square root of a"""
#     eps = 0.0000001
#     old = 1
#     new = 1
#     while True:
#         old,new = new, (new + a/new) / 2.0
#         print(old, new)
#         if abs(new - old) < eps:
#             break
#
#     print("the square root of",a,"is",new)
#
#     with lock:
#         num_threads -= 1
#     return new
#
# id1 = _thread.start_new_thread(heron,(99,))
# id2 = _thread.start_new_thread(heron,(999,))
# id3 = _thread.start_new_thread(heron,(1733,))
#
# while not thread_started:
#     pass
# while num_threads > 0:
#     pass 


# Simple example using the 'threading' module
#   Here a simple sleeper function is started 10 times using the 'threading' module's thread staring function.
"""
import time, threading

def sleeper(i):
    print("thread",i,"sleeps for 2 seconds")
    time.sleep(2)
    print("thread",i,"woke up")

for i in range(10):
    t = threading.Thread(target=sleeper, args=[i])
    t.start()
"""

#   This more complex example can be used to calculate whether a number is prime or not, with the idea being that one could
# run this function for many numbers in many threads, thus speeding up the processes of determining whether all those numbers
# were prime or not.
#   This example uses 'threading's object concept. The 'PrimeNumber' class inherits 'threading.Thread'. One then must write
# a 'run' method, which can be started by using the 'obj.start()' command on the created instance of the 'PrimeNumber' class.
# "Stating" a instance like this, run the code contained within the 'run' method in a new thread
#   We see the use of another form of the locking concept, with use of the '.lock.acquire()' and '.lock.release()' commands,
# which are used with the lock created by the 'threading.Lock()' command. 
"""
import threading 
 
class PrimeNumber(threading.Thread):
    prime_numbers = {} 
    lock = threading.Lock()
    
    def __init__(self, number): 
        threading.Thread.__init__(self) 
        self.Number = number
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.release() 
 
    def run(self): 
        counter = 2
        res = True
        while counter*counter < self.Number and res: 
            if self.Number % counter == 0: 
                print("%d is not a prime number, because %d = %d * %d" % ( self.Number, self.Number, counter, self.Number / counter)) 
                res = False 
            counter += 1 

        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[self.Number] = res 
        PrimeNumber.lock.release() 

threads = [] 

while True: 
    inputData = int(input("number: "))
    if inputData < 1: 
        break 
 
    thread = PrimeNumber(inputData) 
    threads += [thread] 
    thread.start() 
 
for x in threads: 
    x.join()

print( PrimeNumber.prime_numbers )
"""

#       This example uses threading to ping a range of IPs. each pinging takes a number of seconds, thus to perform a scan sequentially would
#   take more time than anyone really cares to devote to this nonsense. Splitting the pings into separate threads allows the machine to send 
#   all the pings at once, and await responses simultaneously.

import os, re, threading

pingers = []
class ip_check(threading.Thread):
    lock = threading.Lock()

    def __init__ (self,ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self.__successful_pings = -1

    def run(self):
        global pingersCount
        ping_out = os.popen("ping -q -c2 "+self.ip,"r")
        while True:
            line = ping_out.readline()
            if not line: 
                with ip_check.lock:
                    pingersCount -= 1
                break

            n_received = re.findall(r"(\d) packets received",line)
            if n_received:
                self.__successful_pings = int(n_received[0])

    def status(self):
      if self.__successful_pings == 0:
         return "no response"
      elif self.__successful_pings == 1:
         return "alive, but 50 % package loss"
      elif self.__successful_pings == 2:
         return "alive"
      else:
         return "shouldn't occur"

#       Send out all pings, collecting the objects in a list. This allows us to access the data within those objects at any time, data which is
#   being changed my the sub-thread. In this way we can monitor a thread.
ipSuffixRange = (0,255)
pingersCount = ipSuffixRange[1] + ipSuffixRange[0]
for suffix in range(ipSuffixRange[0],ipSuffixRange[1]+1):
    ip = "192.168.10."+str(suffix)
    current = ip_check(ip)
    pingers.append(current)
    current.start()

# Due to the nature of the job, it makes sense to wait until all the ip checkers have completed their work before going any further
while pingersCount >= 0:
    pass

# Simply printing the results
for element in pingers:
    print( element.ip, "-", element.status() )