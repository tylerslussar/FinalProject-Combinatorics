# Tyler Slussar
# Combinatorics Final Project
# Rook Polynomial

import math
from graphics import *
from button import *
import itertools





def possibleSubsets(forbiddenPos):

    subsets = []
    buttonLables = []

    for i in range(len(forbiddenPos)):
        buttonLables.append(forbiddenPos[i].buttonValue())

    for i in range(len(buttonLables) + 1):
        subsets.append(list(itertools.combinations(buttonLables, i)))

    return subsets

def checkAttack(subset, n):

    subsetTwos = []

    subsetTwos.append(list(itertools.combinations(subset, 2)))
    # 6, 15, 8
    # [(6,15), (6,8), (15,8)]
    for i in subsetTwos:
        for subsets in i:
            if (subsets[0] // n == subsets[1] // n) or (subsets[0] % n == subsets[1] % n):
            # attacking is true
                return 0

    return 1





def RookPolynomial(length, n, subsets):

    #rows = getRows(n)
    coef = []

    if len(subsets) >= 1:
        coef.append(1)
    if len(subsets) >= 2:
        coef.append(length)

    for i in range(2, len(subsets)):
        subsetRange = subsets[i]
        sum = 0
        for subset in subsetRange:
            value = checkAttack(subset, n)
            sum += value

        coef.append(sum)

    return coef

def permutations(coef, n):
    total = math.factorial(n)
    change = -1
    for i in range(1, len(coef)):
        if n >= 1:
            total = total + (change * coef[i] * math.factorial(n-1))
            change = change * -1
            n = n-1
    return total



def drawCoef(coef):

    polynomial = ""
    if len(coef) >= 1:
        polynomial = polynomial + f'1'
    if len(coef) >= 2:
        polynomial = polynomial + f' + {coef[1]}x'


    for i in range(2, len(coef)):

        if coef[i] == 0:
            break
        else:
            polynomial = polynomial + f' + {coef[i]}x^{i}'
    return polynomial




def main():

    win = GraphWin("Rook Board", 1000, 800)
    columns = ["R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    rows = ["I", "H", "G", "F", "E", "D", "C", "B", "A"]
    forbiddenButtons = []
    boardColumns = []
    boardRows = []
    n = 0


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
    click = True
    while click:
        click = win.getMouse()
        for b in buttons:
            if b.clicked(click):
                boardSize = b
                click = False
                break

    chooseBoard.undraw()
    for b in buttons:
        b.deactivate()
        b.undraw()

    size = boardSize.getLabel()
    boardButtons = []

    if size == "5x5":
        n = 5
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
        n = 6
        y = 100
        i = 0
        for column in range(6):
            x = 200
            for row in range(6):
                button = Button(win, Point(x,y), 100, 100, "", i)
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
        n = 7
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
        n = 8
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
        n = 9
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



    quitButton = Button(win, Point(900,100), 75, 75, "Quit" )
    quitButton.activate()

    polyText = Text(Point(500,750), "")
    polyText.draw(win)
    polyText.setSize(20)
    permText = Text(Point(900, 775), "")
    permText.draw(win)
    permText.setSize(20)
    click = win.getMouse()

    while click:

        for b in boardButtons:
            if b.clickedColor(click):
                if b not in forbiddenButtons and b.getColor() == 1:
                    forbiddenButtons.append(b)
                    subsets = possibleSubsets(forbiddenButtons)
                    coef = RookPolynomial(len(forbiddenButtons), n, subsets)
                    poly = drawCoef(coef)
                    polyText.setText(poly)
                    perm = permutations(coef, n)
                    permText.setText(f'Permutations: {perm}')


                else:
                    forbiddenButtons.remove(b)
                    subsets = possibleSubsets(forbiddenButtons)
                    coef = RookPolynomial(len(forbiddenButtons), n, subsets)
                    poly = drawCoef(coef)
                    polyText.setText(poly)
                    perm = permutations(coef, n)
                    permText.setText(f'Permutations: {perm}')

        if quitButton.clicked(click):
            win.close()
            break
        click = win.getMouse()


if __name__ == '__main__':
    main()




