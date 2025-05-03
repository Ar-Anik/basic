"""
--> use lock for protect the print() function from being used by multiple threads at the same time.

--> join() function use for tell Main thread, please wait here until this thread(t1, t2) finishes its work. Without join() the
    main program might exit early while threads are still running.
"""

import threading

data = [1, 2, 3, 4, 5, 6]
print_lock = threading.Lock()

def worker(start, end):
    for i in range(start, end):
        with print_lock:
            print(f"Thread {threading.current_thread().name} processing {data[i]}")

t1 = threading.Thread(target=worker, args=(0, 3), name="T1")
t2 = threading.Thread(target=worker, args=(3, 6), name="T2")

t1.start()
t2.start()

t1.join()
t2.join()

"""
with print_lock means :
print_lock.acquire()
try:
    print(f"Thread {threading.current_thread().name} processing {data[i]}")
finally:
    print_lock.release()


without lock sometime found result line : Thread T2 processing 4Thread T1 processing 2

Q : If Python runs threads one after another (sequentially), then how do they overlap like this : Thread T2 processing 4Thread T1 processing 2?
--> Python doesn’t run threads strictly one after another : Even though Python threads share one CPU core (due to the Global Interpreter 
Lock (GIL)), the threads are not run completely sequentially. Instead, Python uses cooperative time-slicing — the interpreter switches 
between threads very quickly, even in the middle of a line of code, including print().

So:
    * T2 starts printing: "Thread T2 processing 4"
    * Before it finishes flushing the line (\n), Python switches to T1
    * T1 starts printing: "Thread T1 processing 2"
    
-> it giving the illusion of parallelism.
"""
