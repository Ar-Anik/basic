"""
Streaming large files using generators in Python is one of the best real-world use cases of generator functions.
It allows you to process a file line by line without loading the entire file into memory—ideal for large logs,
CSVs, or data pipelines.
"""

"""
Q : Why use a generator for large files?
-> Reading a file using readlines() loads everything into memory, which is bad for large files (GBs or more). A generator 
yields one line at a time, so memory usage stays very low, no matter how large the file is.
"""

def read_log_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            yield line.split()

gtr = read_log_file('./large_log.txt')

while True:
    try:
        ln = next(gtr)
        print(ln)
    except StopIteration:
        break

