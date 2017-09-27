# crappy ICMP Echo request scan
# (there's actually a better one in the 'threading_.py' file)
"""
import os, re, threading

listOfIPs = ["8.8.8.8","0"]
fifoName = "theBestFifoNameICouldComeUpWith"
if not os.path.exists(fifoName):
    os.mkfifo(fifoName) 

def isHostUp(IP):
    response = os.popen("ping "+IP+" -c 1 -W 1 2>&1").readlines()
    for line in response:
        if "packets received" in line:
            return " 0.0% packet loss" in line

def hostChecker(ip):
    print(ip , (isHostUp(ip)) )
    
for ip in listOfIPs:
    t = threading.Thread(target=hostChecker, args=[ip])
    t.start()
"""






# TCP Scan
#   This is a very similar scan to above, but using the 'socket' socket module to perform the actual connection work

listOfIPs = [
    "8.8.8.8",
    "192.30.252.154",
    "google.com",
    "python-course.eu",
    "metasophiea.com",
    "0",
    "13.144.115.180",
    "251.90.224.30",
    "167.164.252.252",
    "225.34.32.80",
    "109.72.46.47",
    "193.152.127.136",
    "55.202.68.154",
    "102.53.196.234",
    "200.156.52.28",
    "230.247.183.18"
]

import socket, threading
def checkHost(IP,port):
    socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)
    socket_obj.settimeout(1)
    result = socket_obj.connect_ex((IP,port))
    socket_obj.close()
    responseCodes = ["Success","Operation not permitted","No such file or directory","No such process","Interrupted system call","Input/output error","No such device or address","Argument list too long","Exec format error","Bad file descriptor","No child processes","Resource temporarily unavailable","Cannot allocate memory","Permission denied","Bad address","Block device required","Device or resource busy","File exists","Invalid cross-device link","No such device","Not a directory","Is a directory","Invalid argument","Too many open files in system","Too many open files","Inappropriate ioctl for device","Text file busy","File too large","No space left on device","Illegal seek","Read-only file system","Too many links","Broken pipe","Numerical argument out of domain","Numerical result out of range","Resource deadlock avoided","File name too long","No locks available","Function not implemented","Directory not empty","Too many levels of symbolic links","Unknown error 41","No message of desired type","Identifier removed","Channel number out of range","Level 2 not synchronized","Level 3 halted","Level 3 reset","Link number out of range","Protocol driver not attached","No CSI structure available","Level 2 halted","Invalid exchange","Invalid request descriptor","Exchange full","No anode","Invalid request code","Invalid slot","Unknown error 58","Bad font file format","Device not a stream","No data available","Timer expired","Out of streams resources","Machine is not on the network","Package not installed","Object is remote","Link has been severed","Advertise error","Srmount error","Communication error on send","Protocol error","Multihop attempted","RFS specific error","Bad message","Value too large for defined data type","Name not unique on network","File descriptor in bad state","Remote address changed","Can not access a needed shared library","Accessing a corrupted shared library",".lib section in a.out corrupted","Attempting to link in too many shared libraries","Cannot exec a shared library directly","Invalid or incomplete multibyte or wide character","Interrupted system call should be restarted","Streams pipe error","Too many users","Socket operation on non-socket","Destination address required","Message too long","Protocol wrong type for socket","Protocol not available","Protocol not supported","Socket type not supported","Operation not supported","Protocol family not supported","Address family not supported by protocol","Address already in use","Cannot assign requested address","Network is down","Network is unreachable","Network dropped connection on reset","Software caused connection abort","Connection reset by peer","No buffer space available","Transport endpoint is already connected","Transport endpoint is not connected","Cannot send after transport endpoint shutdown","Too many references: cannot splice","Connection timed out","Connection refused","Host is down","No route to host","Operation already in progress","Operation now in progress","Stale NFS file handle","Structure needs cleaning","Not a XENIX named type file","No XENIX semaphores available","Is a named type file","Remote I/O error","Disk quota exceeded","No medium found","Wrong medium type"]
    return responseCodes[result]

def hostChecker(ip,port):
    print( ip+":"+str(port),"-",checkHost(ip,port) )

# 25 - mail
# 80 - http
# 443 - https
for ip in listOfIPs:
    t = threading.Thread(target=hostChecker, args=[ip,443])
    t.start()