

import random
from tkinter import *

# ---------------------------------------
# Question 1

class RandomColorGUI:
    
    def __init__(self):
        """Sets up the GUI window, and all the widgets in it"""
        self.mainWindow = Tk()
        # define and place widgets here
    
    
    
    def go(self):
        """Sets the GUI in motion; uses the default event loop belonging to the main window."""
        self.mainWindow.mainloop()
        
        
    def makeColorString(self, redVal, greenVal, blueVal):
        """Takes in three integers between 0 and 255, and it returns the color string needed
        by tkinter to specify colors based on RGB values.  If the input values are not between
        0 and 255, then a message is printed and black is returned"""
        if (0 <= redVal <= 255) and (0 <= greenVal <= 255) and (0 <= blueVal <= 255):
            return "#%02x%02x%02x" % (redVal, greenVal, blueVal)
        else:
            print("Error: invalid value for a color string:", (redVal, greenVal, blueVal))
            return '#000000'
        
    # add in other methods as needed
    
# End of class definiton

# Define a function to trigger the GUI.  This allows more than one GUI to be given in the same
# files without them all launching.
def goRandomColor():
    """Sets up and runs the RandomColor GUI program."""
    rcg = RandomColorGUI()
    rcg.go()




# ---------------------------------------
# Question 2

class GuessingGameGUI:
    
    def __init__(self):
        """Sets up the GUI window, and all the widgets in it"""

        self.mainWindow = Tk()
        
                
        # set up a label as a local variable (doesn't need to be accessed)
        titleLabel = Label(self.mainWindow, text = "Guess My Number",
                           font = "Arial 20 bold", relief = RAISED,
                           justify = CENTER, bd = 5)
        titleLabel.grid(row = 0, columnspan = 3, pady = 20)
        
        
        self.messageText = StringVar()
        messageBox = Label(self.mainWindow, textvariable = self.messageText,
                           font = 'Arial 16')
        messageBox.grid(row = 1, column = 1, columnspan = 3, pady=20)
        
        entryLabel = Label(self.mainWindow, text = "Enter guess here:", font = 'Arial 16')
        entryLabel.grid(row = 2, column = 1)
        
        self.userText = StringVar()
        userBox = Entry(self.mainWindow, textvariable = self.userText, font = 'Arial 16 bold')
        userBox.grid(row = 2, column = 2)
        userBox.bind("<Return>", self.respond)
        userBox.bind('<Tab>', self.respond)
        
        
        self.countText = StringVar()
        countLabel = Label(self.mainWindow, textvariable = self.countText, font = 'Arial 16')
        countLabel.grid(row = 2, column = 3)
        
        # set up a button as a local variable (doesn't need to be accessed)
        quitButton = Button(self.mainWindow, text = "Quit",
                            font = "Arial 16", command = self.quit)
        quitButton.grid(row = 4, column = 3, padx = 20, pady = 10)
   
        resetButton = Button(self.mainWindow, text = "Reset Game",
                             font = "Arial 16", command = self.resetGame)
        resetButton.grid(row = 4, column = 1, padx = 20, pady = 10)
        
        # choose number
        self.myNumber = random.randint(1, 10)
        self.count = 0
        self.gameWon = False
        
        self.resetGame()
        
    
    def go(self):
        """Sets the GUI in motion; uses the default event loop belonging to the main window."""
        self.mainWindow.mainloop()
        
                
    def quit(self):
        """Stops the program and closes the main window"""
        self.mainWindow.destroy()

        
    def resetGame(self):
        """This callback function for the Reset button resets the game to its initial state, 
        choosing a new random number and displaying the initial message again, and resetting the
        guess count to zero"""
        pass # YOUR CODE HERE <----------------------------------
        
        
    def respond(self, event):
        """This callback method takes an event as input, but doesn't need to use it.  It
        responds to the user's input.  If the game is over, then nothing happens except that 
        the user's input disappears.  Otherwise it checks for good input, updates the guess count
        and displays an appropriate message."""
        if self.gameWon:
            self.userText.set("")
        else:
            self.count = self.count + 1
            self.countText.set("Guesses = " + str(self.count))
    
            guessStr = self.userText.get()
            self.userText.set("")
            
            if not guessStr.isnumeric():
                self.messageText.set("Enter only an integer between 1 and 10")
            else:
                guess = int(guessStr)
                if guess < 1 or guess > 10:
                    self.messageText.set("Enter only an integer between 1 and 10")
                elif guess == self.myNumber:
                    self.messageText.set("You guessed it!    Click Reset to play again.")
                    self.gameWon = True
                else:
                    self.messageText.set("That wasn't it.  Try again!")
        
        
    
# End of class definiton

# Define a function to trigger the GUI.  This allows more than one GUI to be given in the same
# files without them all launching.
def guessingGame():
    """Sets up and runs the GuessingGame GUI program."""
    game = GuessingGameGUI()
    game.go()



# ---------------------------------------
# Question 3
#A function is a piece of code which can be reused and takes optional input parameters (eg. function(parameter)
#A method is a function associated with an object (eg. the turtle methods: turt.forward(90))
# Put your answer to question three here

