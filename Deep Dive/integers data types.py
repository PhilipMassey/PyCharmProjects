y = 0
for i in range(2**100):
    x = sys.getsizeof(i)
    if x != y:
        print(i,x)
        y = x


