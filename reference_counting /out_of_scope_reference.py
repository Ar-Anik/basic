import ctypes

address = None
def create_object():
    global address
    obj = [1, 2, 3]
    address = id(obj)
    print(ctypes.c_long.from_address(address).value)

create_object()
print(ctypes.c_long.from_address(address).value)