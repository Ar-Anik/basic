total = sum(x for x in range(10))
print(total)

# or
def gen_s(rng):
    for x in range(rng):
        yield x

total = 0
gtr = gen_s(10)

while True:
    try:
        val = next(gtr)
        total += val
    except StopIteration:
        break

print(total)
