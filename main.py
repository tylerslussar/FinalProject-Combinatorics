# Tyler Slussar
# Combinatorics Final Project
# Rook Polynomial

from graphics import *
from button import *
import itertools





def getColumns(n):

    if n == 5:
        return ["V", "W", "X", "Y", "Z"]
    elif n == 6:
        return ["U", "V", "W", "X", "Y", "Z"]
    elif n == 7:
        return ["T", "U", "V", "W", "X", "Y", "Z"]
    elif n == 8:
        return ["S", "T", "U", "V", "W", "X", "Y", "Z"]
    else:
        return ["R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def getRows(n):

    if n == 5:
        return ["A", "B", "C", "D", "E"]
    elif n == 6:
        return ["A", "B", "C", "D", "E", "F"]
    elif n == 7:
        return ["A", "B", "C", "D", "E", "F", "G"]
    elif n == 8:
        return ["A", "B", "C", "D", "E", "F", "G", "H"]
    else:
        return ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

def possibleSubsets(forbiddenPos):

    subsets = []
    buttonLables = []

    for i in range(len(forbiddenPos)):
        buttonLables.append(forbiddenPos[i].buttonValue())

    for i in range(len(buttonLables) + 1):
        subsets.append(list(itertools.combinations(buttonLables, i)))

    return subsets


def RookPolynomial(forbiddenPositions, n, subsets):

    rows = getRows(n)
    columns = getColumns(n)
    coef = []

    for i in range(len(forbiddenPositions)):
        sum = 0
        for j in subsets:
            for k in j:
                if k == ():
                    coef.append(len(forbiddenPositions))







def main():

    win = GraphWin("Rook Board", 1000, 800)
    columns = ["R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    rows = ["I", "H", "G", "F", "E", "D", "C", "B", "A"]
    forbiddenButtons = []
    boardColumns = []
    boardRows = []


    chooseBoard = Text(Point(500,200), "Select Rook Board Size")
    chooseBoard.setSize(25)
    chooseBoard.draw(win)
    five = Button(win, Point(300,450),100, 200, "5x5")
    six = Button(win, Point(400,450), 100, 200, "6x6")
    seven = Button(win, Point(500, 450), 100, 200, "7x7")
    eight = Button(win, Point(600,450), 100, 200, "8x8")
    nine = Button(win, Point(700,450), 100, 200, "9x9")

    buttons = [five, six, seven, eight, nine]
    for b in buttons:
        b.activate()

    boardSize = None
    click = win.getMouse()
    for b in buttons:
        if b.clicked(click):
            boardSize = b
            break

    chooseBoard.undraw()
    for b in buttons:
        b.deactivate()
        b.undraw()

    size = boardSize.getLabel()
    boardButtons = []

    if size == "5x5":
        y = 100
        i = 0
        for column in range(5):
            x = 300
            for row in range(5):
                button = Button(win, Point(x,y), 100, 100, "", i)
                boardButtons.append(button)
                button.activate()
                x += 100
                i += 1

            y += 100

        cPosition = 700
        for column in range(5):
            letter = columns.pop()
            boardColumns.append(letter)
            message = Text(Point(cPosition, 25), letter)
            message.setSize(25)
            message.draw(win)
            cPosition -= 100

        rPosition = 100
        for row in range(5):
            letter = rows.pop()
            boardRows.append(letter)
            message = Text(Point(200, rPosition), letter)
            message.setSize(25)
            message.draw(win)
            rPosition += 100



    elif size == "6x6":
        y = 100
        i = 0
        for column in range(6):
            x = 200
            for row in range(6):
                button = Button(win, Point(x,y), 100, 100, "", 1)
                boardButtons.append(button)
                button.activate()
                x += 100
                i += 1

            y += 100

        cPosition = 700
        for column in range(6):
            letter = columns.pop()
            boardColumns.append(letter)
            message = Text(Point(cPosition, 25), letter)
            message.setSize(25)
            message.draw(win)
            cPosition -= 100

        rPosition = 100
        for row in range(6):
            letter = rows.pop()
            boardRows.append(letter)
            message = Text(Point(100, rPosition), letter)
            message.setSize(25)
            message.draw(win)
            rPosition += 100



    elif size == "7x7":
        y = 100
        i = 0
        for column in range(7):
            x = 200
            for row in range(7):
                button = Button(win, Point(x,y), 80, 80, "", i)
                boardButtons.append(button)
                button.activate()
                x += 80
                i += 1

            y += 80

        cPosition = 680
        for column in range(7):
            letter = columns.pop()
            boardColumns.append(letter)
            message = Text(Point(cPosition, 25), letter)
            message.setSize(25)
            message.draw(win)
            cPosition -= 80

        rPosition = 100
        for row in range(7):
            letter = rows.pop()
            boardRows.append(letter)
            message = Text(Point(100, rPosition), letter)
            message.setSize(25)
            message.draw(win)
            rPosition += 80


    elif size == "8x8":
        y = 100
        i = 0
        for column in range(8):
            x = 200
            for row in range(8):
                button = Button(win, Point(x,y), 75, 75, "", i)
                boardButtons.append(button)
                button.activate()
                x += 75
                i += 1

            y += 75

        cPosition = 725
        for column in range(8):
            letter = columns.pop()
            boardColumns.append(letter)
            message = Text(Point(cPosition, 25), letter)
            message.setSize(25)
            message.draw(win)
            cPosition -= 75

        rPosition = 100
        for row in range(8):
            letter = rows.pop()
            boardRows.append(letter)
            message = Text(Point(100, rPosition), letter)
            message.setSize(25)
            message.draw(win)
            rPosition += 75


    else:
        y = 75
        i = 1
        for column in range(9):
            x = 100
            for row in range(9):
                button = Button(win, Point(x, y), 75, 75, "", i)
                boardButtons.append(button)
                button.activate()
                x += 75
                i += 1

            y += 75

        cPosition = 700
        for column in range(9):
            letter = columns.pop()
            boardColumns.append(letter)
            message = Text(Point(cPosition, 25), letter)
            message.setSize(25)
            message.draw(win)
            cPosition -= 75

        rPosition = 75
        for row in range(9):
            letter = rows.pop()
            boardRows.append(letter)
            message = Text(Point(50, rPosition), letter)
            message.setSize(25)
            message.draw(win)
            rPosition += 75



    quitButton = Button(win, Point(900,700), 75, 75, "Quit" )
    quitButton.activate()

    click = win.getMouse()
    while click:
        for b in boardButtons:
            if b.clickedColor(click):
                if b not in forbiddenButtons and b.getColor() == 1:
                    forbiddenButtons.append(b)
                    subsets = possibleSubsets(forbiddenButtons)
                   # RookPolynomial(boar)
                else:
                    forbiddenButtons.remove(b)
                    subsets = possibleSubsets(forbiddenButtons)
                    #polynomial = function

        if quitButton.clicked(click):
            win.close()
            break
        click = win.getMouse()


if __name__ == '__main__':
    main()




