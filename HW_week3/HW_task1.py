from collections import deque


def process_queue(txt_file):
    queue = deque()

    #using with open to read file and go through it line by line
    with open(txt_file, 'r') as file:
        for line in file:
            command, name = line.split()

            if command == 'JUMP':
                queue.appendleft(name)
                #appendleft allows us to move objects to the front of the queue

            elif command == 'JOIN':
                queue.append(name)
                # append is used to add persons name to the back of the cue

    # getting the order of the queue after applying deque
    return(list(queue))


#test run
print(process_queue('hw3_task1.txt'))

"""output ['Xanthe', 'Violet', 'Una', 'Theresa', 'Priyanka', 'Odette', 'Nuria', 'Lauren', 'Gloria', 'Frankie',
'Dylan', 'Charlie', 'Belle', 'Amal', 'Evelyn', 'Helen', 'Iman', 'Joey', 'Kimberley', 'Marie', 'Quinn',
'Romily', 'Sofia', 'Wanda', 'Yvonne', 'Zara']"""

"""Task 1. B: Time complexity in this case would be o(n) - where (n)  is the number of lines in the txt_input file,
 because we meed to go over each item once, which means it increases proportionally to input data.
 Space complexity in this case would be 0(1) as the space used by program remains constant regardless of the number
  of people in the queue, it does not create additional data structures or variables"""
