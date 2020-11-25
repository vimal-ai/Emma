import main
import yoloLive

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
       else:
           yoloLive.main()
           print_vimal()

def print_vimal():
    print("vimal")

def print_mihir():
    print("mihir")

# Create new threads
thread1 = myThread("mihir")
thread2 = myThread("vimal")

# Start new Threads
thread1.start()
thread2.start()