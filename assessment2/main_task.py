number_of_students = 59

def minimum_classes(number_of_students):
    # how many classes we neeed
    if number_of_students <= 60:
        number_of_classes = 2
    else:
        number_of_classes = number_of_students//30 + (number_of_students % 30 > 0)
    #print(number_of_classes)


    #allocating students into classes
    students_per_class = number_of_students//number_of_classes
    #print(students_per_class)
    # find students left
    students_left = number_of_students % number_of_classes
    #print(students_left)


    # create dictionary
    proposed_allocation= {}
    #use loop to go through range of classes and distribute students
    for i in range(number_of_classes):
        class_size = students_per_class
        #redistribute leftover students
        if students_left > 1:
            class_size = class_size + 1
            students_left = students_left - 1
        #not sure how to format dictionary proposed_allocation =  class_size doesn't work

    # printing outputs
    print(f"Proposed Allocation: {number_of_classes} classes")
    print(proposed_allocation)


print(minimum_classes(number_of_students))



