def sequence():
    for i in range(1,3):
        print(i*i)
        
sq=sequence()
print(next(sq))
print(next(sq,"no item"))