#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    This program simulates a bowling scoreboard.
    Running this program, a scoreboard will display.
    The number of pins hit at each throwing is entered by clicking buttons by users.
    The scores for each frame and final scores are calculated automatically.
'''
from Tkinter import Tk, Text, W, N, E, S
from ttk import Frame, Label, Style, Button
import Tkinter

'''
    Static Variables:
        score: used for storing all the input values by users
        single: used for storing number of pins hit each time
        double: used for storing score for each frame
        singleScore: text variable associated with GUI lables to display number of pins hit each throwing
        doubleScore: text variables associated with GUI lables to display score for each frame
'''
score = []
single = []
double = []

singleScore = []
doubleScore = []
finalScore = []

'''
    Name: bowlingGame
    Input: Frame(root) created by main Function
    Class: Implementation of bowling scoreboard
'''
class bowlingGame(Frame):
    '''
        Name: init
        Input: root of GUI
        Function: initial parent of this class; initial GUI layout
    '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    '''
        Name: buttonClick
        Input: integers 1 to 10 to represent number of pins hit each time;
               integer 11 to represent a re-start of game.
        Function: receive integer 1 to 10, append it to list score;
                  receive integer 11, delete variables in score, single and double lists;
                  trigger display function.
    '''
    def buttonClick(self, number):
        if number <= 10:
            score.append(number)
        else:
            del score[:]
            del single[:]
            del double[:]
        self.display(score) # call display when a new button click is fired

    '''
        Name: display
        Input: score list
        Function: 1) update and calculate single value list;
                  2) update and calculate double value list;
                  3) display singleScore text list with special "X" and "/" marks;
                  4) display doubleScore text list, add up score so far for each frame;
                  5) calculate and display finalScore.
    '''
    def display(self, score):
        # check if re-start of the game, delete all displays, and return
        if len(score) == 0:
            finalScore[0].set("")
            for i in range (0, 21):
                singleScore[i].set("")
            for i in range(0, 10):
                doubleScore[i].set("")
            return
        # check the length of the singleScore, if more than 21, do nothing and return
        if len(single) > 21:
            return
        # check the last frame, if no strick or spare, do nothing and return
        if len(single) == 20:
            if single[18] + single[19] < 10:
                return

        currentInput = score[len(score)-1]
        # update single value list; check if current frame is finished
        if len(single) % 2 == 0:
            single.append(currentInput)
            if currentInput == 10:
                if len(single) != 19 and len(single) != 20 and len(single) != 21:
                    single.append(0)
        elif len(single) % 2 == 1:
            if len(single) == 19 and single[18] == 10:
                single.append(currentInput)
            else:
                if currentInput + single[len(single)-1] <= 10:
                    single.append(currentInput)

        # update double value list;
        f = len(double)*2 # f stands for the current stage of the frame
        if len(double) == 9: # special condition for final frame
            if len(single) >= 20 and single[f] + single[f+1] < 10:
                double.append(single[f] + single[f+1])
            elif len(single) > 20:
                double.append(single[f] + single[f+1] + single[f+2])
        if len(double) < 9:
            if f+1 < len(single):
                if single[f] + single[f+1] < 10: #regular
                    double.append(single[f] + single[f+1])
                elif single[f] + single[f+1] == 10 and single[f] != 10: # spark
                    if f+2 < len(single):
                        double.append(single[f] + single[f+1] + single[f+2])
                elif single[f] + single[f+1] == 10 and single[f] == 10: # strick
                    if len(double) == 8: # special condition for final frame
                        if f+3 < len(single):
                            double.append(single[f] + single[f+1] + single[f+2] + single[f+3])
                    elif f+3 < len(single):
                        if single[f+2] != 10: # strick + non-strick
                            double.append(single[f] + single[f+1] + single[f+2] + single[f+3])
                        elif single[f+2] == 10: # strick + strick
                            if len(double) == 7: # special condition for final frame
                                if f+4 < len(single):
                                    double.append(single[f] + single[f+1] + single[f+2] + single[f+3] + single[f+4])
                            if f+4 < len(single):
                                if single[f+4] == 10: # strick + strick + strick
                                    if f+5 < len(single):
                                        double.append(single[f] + single[f+1] + single[f+2] + single[f+3] + single[f+4] + single[f+5])
                                elif single[f+4] != 10: # strick + strick + non-strick
                                    double.append(single[f] + single[f+1] + single[f+2] + single[f+3] + single[f+4])

        # display singleScore
        if len(single) <= 18:
            pass_in = len(single)/2
        elif len(single) > 18:
            pass_in = 9
        # only handle display singleScore for first nine frames
        for i in range(0, pass_in):
            if single[i*2] == 10:
                singleScore[i*2].set("")
                singleScore[i*2+1].set("X")
            elif single[i*2] + single[i*2+1] == 10:
                singleScore[i*2].set(single[i*2])
                singleScore[i*2+1].set("/")
            else:
                singleScore[i*2].set(single[i*2])
                singleScore[i*2+1].set(single[i*2+1])
        if len(single)%2 == 1:
            singleScore[len(single)-1].set(single[len(single)-1])
        # only handle display singleScore for last tenth frame
        if len(single) > 18:
            if len(single) >= 19:
                if single[18] == 10:
                    singleScore[18].set("X")
                else:
                    singleScore[18].set(single[18])
            if len(single) >= 20:
                if single[19] + single[18] == 10:
                    singleScore[19].set("/")
                elif single[19] == 10:
                    singleScore[19].set("X")
                else:
                    singleScore[19].set(single[19])
            if len(single) >= 21:
                if single[20] == 10:
                    singleScore[20].set("X")
                else:
                    singleScore[20].set(single[20])

        # display doubleScore
        for i in range(0, len(double)):
            count = 0
            for j in range(0, i+1):
                count = count + double[j]
            doubleScore[i].set(count)
        # display finalScore
        final = 0
        for i in range(0, len(double)):
            final = final + double[i];
        finalScore[0].set(final)

    '''
        Name: initUI
        Input: none
        Function: set up the GUI layout, I only implemented a basic layout without decoration:
                  1) buttons for input number of pins hit each times;
                  2) button for re-start a game;
                  3) display labels for single score, frame score and total score.
    '''
    def initUI(self):
        self.parent.title("Bowling Scoreboard")
        # style sheet for buttons and labels
        Style().configure("TButton", padding=(0,5,0,5), foreground="black", background="#8000ff", font='serif 10')
        Style().configure("TLabel", width=8, padding=(0,5,0,5), bg ="white", foreground="black",relief = "ridge",font='serif 10', anchor="center")

        # configures for row and columns
        for i in range(0, 5): # 4 rows
            self.rowconfigure(i)
        for i in range(0, 24): # 23 columns
            self.columnconfigure(i)

        # Intro text at the top
        intro_text = "Welcome to bowling game! Enter the number of pins you want to hit. The max number of pins you can hit is 10, except for last frame."
        msg = Label(self, text=intro_text).grid(row=0, column=0, columnspan=23, sticky=W+E)

        # All the buttons
        zero = Button(self, text=str(0), width=2, command=lambda: self.buttonClick(0)).grid(row=1,column=0)
        one = Button(self, text=str(1), width=2, command=lambda: self.buttonClick(1)).grid(row=1,column=1)
        two = Button(self, text=str(2), width=2, command=lambda: self.buttonClick(2)).grid(row=1,column=2)
        three = Button(self, text=str(3), width=2, command=lambda: self.buttonClick(3)).grid(row=1,column=3)
        four = Button(self, text=str(4), width=2, command=lambda: self.buttonClick(4)).grid(row=1,column=4)
        five = Button(self, text=str(5), width=2, command=lambda: self.buttonClick(5)).grid(row=1,column=5)
        six = Button(self, text=str(6), width=2, command=lambda: self.buttonClick(6)).grid(row=1,column=6)
        seven = Button(self, text=str(7), width=2, command=lambda: self.buttonClick(7)).grid(row=1,column=7)
        eight = Button(self, text=str(8), width=2, command=lambda: self.buttonClick(8)).grid(row=1,column=8)
        nine= Button(self, text=str(9), width=2, command=lambda: self.buttonClick(9)).grid(row=1,column=9)
        ten = Button(self, text=str(10), width=2, command=lambda: self.buttonClick(10)).grid(row=1,column=10)
        new_game = Button(self, text=str("Start New Game"), command=lambda: self.buttonClick(11)).grid(row=1,column=18,columnspan=5)

        # All the frames + Total
        frame = []
        for i in range(1, 10):
            word = "Frame " + str(i)
            current = Label(self, text=word)
            current.grid(row=2, column=(i-1)*2, columnspan=2, sticky=W+E)
            frame.append(current)
        word = "Frame " + str(10)
        current = Label(self, text=word)
        current.grid(row=2, column=(10-1)*2, columnspan=3, sticky=W+E)
        frame.append(current)

        total = Label(self, text="total")
        total.grid(row=2, column=21, columnspan=2, sticky=W+E)

        # All the single scores
        for i in range(0, 22):
            singleScore.append(Tkinter.StringVar());

        single = []
        for i in range(0, 21):
            single.append(Label(self, textvariable=singleScore[i]).grid(row=3, column=i, sticky=W+E))

        # All the frame scores + final score
        for i in range(0, 10):
            doubleScore.append(Tkinter.StringVar());

        double = []
        for i in range(0, 9):
            double.append(Label(self, textvariable=doubleScore[i]).grid(row=4, column=i*2, columnspan=2,sticky=W+E))
        double.append(Label(self, textvariable=doubleScore[9]).grid(row=4, column=9*2, columnspan=3,sticky=W+E))

        finalScore.append(Tkinter.StringVar());
        Label(self, textvariable=finalScore[0]).grid(row=4, column=21, columnspan=2,sticky=W+E)
        self.pack()
'''
    Name: main
    Input: none
    Function: the main function of this program
'''
def main():
    root = Tk()
    app = bowlingGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
