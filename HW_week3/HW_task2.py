def number_in_sequence(n):
    #we know base case, the first number is 8
    if n == 1:
        return 8
    #recursive case for any n above 1, we calculate the nth number based of previous number in sequence
    else:
        previous_number = number_in_sequence(n - 1)
        current_number = previous_number + 7

    return current_number


#test runs
print(number_in_sequence(1))
print(number_in_sequence(5))
print(number_in_sequence(10))