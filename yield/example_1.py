def custom_generator():
    yield "Aubdur Rob Anik"
    yield "No Money"

gtr = custom_generator()

print(next(gtr))
print(gtr.__next__())
print(gtr.__next__())
