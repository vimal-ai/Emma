import main
import yoloLive
import brightness_det as bd

import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name

   def run(self):
       if(self.name=="mihir"):
           print_mihir()
           main.main()
       elif(self.name=="vimal"):
           yoloLive.main()
           print_vimal()
       elif(self.name=='raxit'):
           print("raxit")
           bd.main()

def print_vimal():
    print("vimal")

def print_mihir():
    print("mihir")

# Create new threads
thread1 = myThread("mihir")
thread2 = myThread("vimal")
#thread3 = myThread("raxit")

# Start new Threads
thread1.start()
thread2.start()
#thread3.start()