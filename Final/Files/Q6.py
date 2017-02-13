# There are two bugs in this program. Your job is to find
# these bugs and fix them. If you want full credit you
# need to do three things for each bug:
# 1. In a comment describe the bug
# 2. Fix the bug
# 3. In a comment describe how you fixed the bug.

def grep(fileName, searchWord):
    '''This function reads a file line by line and prints
    out any line that contains the searchWord. It does
    not return any value. Its first and second parameters
    are files, with the first parameter being the name of
    the file that is being searched and the second
    parameter is the word that it is searching for.'''

    f = open(fileName, 'r')
    for line in f: #error: the for loop should loop through the lines in the file. f.readline() is a method
        if searchWord in line:
            line = line.strip() # remove the ending newline
            print(line) #the function should print out the line in question, not return it
    f.close()           # I changed return to print

grep("manInIronMask.txt", "tower")
#When Run, it should print the following:
#the jailer’s girdle made itself heard up to the stories of the towers,
#descending footsteps that they had left the tower, he put the lantern
#present position--and whose summits even yet, as they proudly tower
#accursed towers, and have battered open the gates of this place, and
#“Because, monsieur, there is in front of the square tower of the
