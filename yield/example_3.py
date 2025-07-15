def custom_generator(lst):
    for i in lst:
        print("i -> ", i)
        if i % 2 == 0:
            print(f"Return {i}")
            yield i

lst = [1, 2, 3, 4, 5, 6, 8, 12]
print(list(custom_generator(lst)))


"""
The list() function accepts any iterable as input — including a generator — and Internally iterates through it using for loop 
(or iter() + next() calls), and collects each value into a list.
"""

# So, list(fun(lst)) means:
result = []
gtr = custom_generator(lst)

for item in gtr:
    result.append(item)

# or

while True:
    try:
        item = next(gtr)
        result.append(item)
    except StopIteration:
        break

print("Value : ", result)
