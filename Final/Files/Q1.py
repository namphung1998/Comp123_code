# In this question you are provided a function to determine
# if a string is a palindrome. This function is recursive
# you have several tasks

# 1. Using comments, label each line of code as either
# part of a base case or a recursive case. If there are
# more than one base case or recursive case number the
# cases (I.E. base case 1)

# 2. For each case, explain the case. For base cases,
# please explain what the case is (under what conditions
# the case gets ran) and why the base case is correct
# (the conditions under which the base case is ran, why
# is it correct to return what it does).
# For recursive cases explain in what way the recursive
# call moves closer to a base case.

def palindrome(aString):
    """This function takes a string and returns True
    if the string is a palindrome. (A palindrome is
    any string that is the same forwards and backwards)
    examples: 'a', 'abba', 'qwe r ewq'"""
    if len(aString) <= 1: #base case 1 - gets ran when the string is empty or has only one characters (eg. "")
        return True #the base case is correct because an empty string is the same forward and backward
    elif aString[0] != aString[-1]: #base case 2 - gets ran when the string has more than 1 character
        return False #this case returns false if the first and the last character is not the same.
    else: #recursive case - gets ran when the string has more than 1 character and has the same first and last characters
        return palindrome(aString[1:len(aString)-1]) #the recursive call calls the palindrome function on the second and the second last characters
                                                     #the recursive call goes on to check if these characters are the same and so forth.
print(palindrome(""))  # True
print(palindrome("abba"))  # True
print(palindrome("apa"))  # True
print(palindrome("!"))  # True
print(palindrome("ape"))  # False
print(palindrome("as"))  # False
print(palindrome("aaaapeaaa"))  # False