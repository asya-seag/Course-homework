#creating function that will return True if the word if isogram\
#and False if the word is not one
def isogram(examples):
    # need to use lower() so our function is case in-sensitive
    examples = examples.lower()
    for char in examples:
        if examples.count(char) > 1:
            return False

    return True

examples = "isogram" #True
# examples = "madam" #False
# examples = "uncopyrightable" #True
# examples = "ambidextrously”" #True
print(isogram(examples))