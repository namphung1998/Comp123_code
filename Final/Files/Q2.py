# Write a function named rev that takes a dictionary as
# an input  and reverses that dictionary. What this means
# is that you will take a dictionary which maps keys to
# values and return a new dictionary where the old values
# are the new keys and the old keys are the new values.
# The included example may help make this more clear if
# you are still confused.

def rev(aDict):
    "a function that takes in a dictionary and reverse it (the keys become the values and vice versa"
    newDict = {}
    for key, value in aDict.items():
        newDict[value] = key
    return newDict

# test code / example.
someDict = {1:'a', 2:'bee', 3:'sea', 'alpha':1, 'beta':2, 4:'b'}

print(rev(someDict))
# should print the following (order may change)
#{'beta': 2, 1: 'a', 2: 'bee', 3: 'sea', 4: 'b', 'alpha': 1}

print(someDict) # should not be changed
