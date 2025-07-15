def event_number():
    for x in range(1000000):
        if x % 2 == 0:
            yield x

events_1 = event_number()

# above equvalent to
events_2 = (x for x in range(1000000) if x % 2 == 0)

print(events_1.__dir__())
print(events_2.__dir__())

print(next(events_1))
print(next(events_2))
