#2.1.
input='cat'
input2='cataract'
def consonant_count(input):
    #creating vowels dictionary to exclude them from search
    vowels = {'a', 'e', 'o', 'u', 'i'}
    #list of consonants but we will add only the ones with count 1
    consonants = []
    #keeping track of how many times consonants came up
    count = {}

    #using lower to make sure we avoid counting capital letters as different consonants in case input has them
    for x in input.lower():
        if x.isalpha() and x not in vowels:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
    #adding to consonants list only the ones with count 1
    for key, value in count.items():
        if value == 1:
            consonants.append(key)

    return len(consonants)

print(consonant_count(input))
print(consonant_count(input2))

"""Task 1. B: Time complexity in this case would be o(n) - where (n)  is the length of input word,
 because we meed to go over each item once, which means it increases proportionally to input data.
 Space complexity in this case would be 0(n) as the space used by program changes depending on the size of input
  in this case n - is the size of  input, as we will require new dictionary, called count and list called consonants."""
