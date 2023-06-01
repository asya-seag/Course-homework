def how_many_squares(x):
    #non recursive case is defined
    if x == 1:
        return 1
    #introducing recursion
    else:
        return x*x + how_many_squares(x-1)
print(how_many_squares(1))
print(how_many_squares(2))
print(how_many_squares(3))