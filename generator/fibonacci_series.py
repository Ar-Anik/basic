def fibonacci(limit):
    cnt = 1
    a, b = 0, 1
    while cnt <= limit:
        yield a
        a, b = b, a+b
        cnt += 1

gtr = fibonacci(10)

while True:
    try:
        val = next(gtr)
        print(val, end=" ")
    except StopIteration:
        break

