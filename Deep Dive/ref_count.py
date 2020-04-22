
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

my_var = "hello"

print('my_var # = {0}'.format(hex(id(my_var))))

print(ref_count(id(my_var)))
