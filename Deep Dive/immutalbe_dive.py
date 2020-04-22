import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value


my_typle = [1,2,'thr33']

my_one1 = 1
print(hex(is(my_one)))


