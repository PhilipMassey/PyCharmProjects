import threading
from queue import Queue
import time

def testThread(num):
    print(num)

# if __name__ == '__main__':
#     for i in range(30):
#         t = threading.Thread(target=testThread, args=(i,))
#         t.start()
import threading

import multiprocessing
if __name__ == '__main__':
    for i in range(130):
        p = multiprocessing.Process(target=testThread, args=(i,))
        t = threading.Thread(target=testThread, args=(i,))
        t.start()
        t.join() # this line allows you to wait for processes
