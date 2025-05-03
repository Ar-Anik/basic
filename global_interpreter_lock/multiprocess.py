"""
Pool(processes=2) -> Creates a pool of 2 worker processes. This pool manages a fixed number of processes that can execute tasks in parallel.

pool.apply_async(countdown, [COUNT//2]) -> apply_async() sends the task to the worker pool and immediately returns an AsyncResult object.
Calls the countdown() function asynchronously in a separate process. [COUNT//2] passes half of the COUNT value (25,000,000) as an argument
to the function. Asynchronous execution allows multiple countdowns to run in parallel.

pool.close() -> Prevents any more tasks from being submitted to the pool. we must call this before calling join().

pool.join() -> Blocks the main program until all worker processes in the pool have finished.
"""

from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()

    print("Time taken in Seconds -", end - start)
