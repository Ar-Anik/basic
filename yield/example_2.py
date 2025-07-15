def sequence():
    n = 0
    while True:
        yield n
        n += 1

gtr = sequence()

for i in range(10):
    print(next(gtr), end=" ")


# alternative of for loop
itr = iter(range(10))
while True:
    try:
        value = next(itr)
        i = next(gtr)
        print(i, end=" ")
    except StopIteration:
        break

