import time
import math

from sympy import *
from sympy.solvers import solve
from sympy.plotting import plot
w, x, y, z = symbols('w x y z')
runtimeDict = {}


def Plotting(symbol, expr):
    x = symbols(symbol)
    p1 = plot(expr, show=False)
    p1.show()

# simplification function
def Simplification(expr):
    print("Before Simplification : {}".format(expr))
    smpl = simplify(expr)  # Use sympy.simplify() method
    print("After Simplification : {}".format(smpl))
    return smpl

# Differention function
def Differentiation(symbol, expr):
    x = symbols(symbol)  # reassiging symbol variable into x (code reuse)
    print("Before Differentiation : {}".format(expr))
    differential = diff(expr, symbol)  # Use sympy.diff() method
    print("After Differentiation : {}".format(differential))
    return differential

# Expansion function
def Expansion(expr):
    print("Before Expansion : {}".format(expr))
    expansion = expand(expr)
    print("After Expansion : {}".format(expansion))
    return expansion

# Substituion function


def Substitution(old, new, expr):
    print("Before Substitution : {}".format(expr))
    expr = parse_expr(expr)
    substitutedExpr = expr.subs(old, new)
    print("After Substitution : {}".format(substitutedExpr))
    return substitutedExpr

# Factorisatin function


def Factorisation(symbol, expr):
    x = symbols(symbol)
    print("Before Factorisation : {}".format(expr))
    factorisation = factor(expr)
    print("After Factorisation : {}".format(factorisation))
    return factorisation

# Solving function


def Solving(expr):
    print("Before Solving : {}".format(expr))
    solving = solve(expr)
    print("After Solving equation : {}".format(solving))
    return solving

# CreateVariable function


def createVariable(symbol, expr):
    with open('readme.txt', 'w+') as f:  # writing into the file
        if symbol in f.readlines():
            f.write(symbol + " " + expr)
        else:
            f.write(symbol + " " + expr)
    f.close()
    if symbol in runtimeDict.keys():
        runtimeDict.update({symbol: expr})
    else:
        runtimeDict[symbol] = expr
    if symbol in runtimeDict.keys():
        runtimeDict.update({symbol: expr})
    else:
        runtimeDict[symbol] = expr

# PrintVariables function


def PrintVariables(varName):
    i = 0
    with open('readme.txt', 'r+') as f:  # read into file
        for line in f:
            values = line.split()
        if varName in values:  # iterating through each value
            while i < len(values):
                if varName == values[i]:
                    print(varName + "=" + values[i+1])
                    break
    f.close()

# RecallVariable function


def RecallVariable(varName):
    i = 0
    with open('readme.txt', 'r+') as f:  # read into file to reacl value from
        for line in f:
            values = line.split()
        if varName in values:
            while i < len(values):
                if varName == values[i]:  # check to see if hey match
                    return (values[1])
                    break
    f.close()
# Addition function


def Addition(NumberOfTerms):
    total = 0
    listOfTerms = []
    for i in range(0, int(NumberOfTerms)):
        newTerm = int(input("Please enter your numbers: "))
        listOfTerms.append(newTerm)
    for term in listOfTerms:
        total += term
    return total

# Subtraction function


def Subtraction(NumberOfTerms):
    listOfTerms = []
    for i in range(0, NumberOfTerms):
        newTerm = int(input("Please enter your numbers: "))
        listOfTerms.append(newTerm)
    total = listOfTerms[0]
    for term in range(1, len(listOfTerms)):
        total -= listOfTerms[term]
    return total

# Division function


def Division(NumberOfTerms):
    listOfTerms = []
    for i in range(0, NumberOfTerms):
        newTerm = int(input("Please enter your numbers: "))
        listOfTerms.append(newTerm)
    total = listOfTerms[0]
    for term in listOfTerms[1:]:
        print(term)
        total /= term
    return total

# Multiplication function


def Multiplication(NumberOfTerms):
    listOfTerms = []
    for i in range(0, NumberOfTerms):
        newTerm = int(input("Please enter your numbers: "))
        listOfTerms.append(newTerm)
    for term in range(1, len(listOfTerms)):
        total = newTerm * NumberOfTerms
    return total

# SquareRoot function


def SquareRoot():
    Number = int(input("Please enter your numbers: "))
    total = math.sqrt(Number)  # python built square root function
    return total

# ModulusCalculator function


def ModulusCalculator(NumberOfTerms):
    listOfTerms = []
    for i in range(0, NumberOfTerms):
        newTerm = int(input("Please enter your numbers: "))
        listOfTerms.append(newTerm)
    for term in range(1, len(listOfTerms)):
        total = newTerm % NumberOfTerms
    return total

# GetNumberOfTerms function


def GetNumberOfTerms():
    numberOfTerms = int(
        input('Please enter how many terms is the operation. "Example: if a operation is 3+3 (this is 2 terms)": '))
    return numberOfTerms

# Helper fuction


def Helper():
    while True:
        try:  # menu options below:
            helpNum = int(input('''Welcome to the help forum.\n\nPlease select the process you need assistance in.\n
0. Plot
1. Simplification
2. Differentiation
3. Expansion
4. Substitution
5. Factorisation
6. Solving equations
7. Simple Maths
8. Create Variable
9. Print Variables in storage

You Have Selected number: '''))
        except ValueError:  # checking if the number is pafrt of the menu
            print("Please enter a valid integer 1-9")
            continue
        print()
        if helpNum >= 0 and helpNum <= 9:
            # all help options below for corresponding functions
            print(f'You entered number: {helpNum}')
            print()
            if (helpNum == 0):
                print("Welcome to plotting help forum.")
            elif (helpNum == 1):
                print("Welcome to the Simplification help forum.\n\n Symbols accepted: w, x, y, z.\n Example formula: (x²+x)/x \n Format to insert forumla: (x**2+x)/x \n After Simplification : x + 1")
            elif (helpNum == 2):
                print("Welcome to the Differentiation help forum.\n\n Symbols accepted: w, x, y, z.\n Example formula:(x³+9x) \n Format to insert formula: (x**3 + 9*x) \n After Differentiation : 3*x**2 + 9")
            elif (helpNum == 3):
                print("Welcome to the Expansion help forum.\n\n Symbols accepted: w, x, y, z.\n Example formula: (x + 1) x (x+3) \n Format to insert formula: (x + 1)*(x+3) \n After Expansion : x**2 + 4*x + 3 ")
            elif (helpNum == 4):
                print("Welcome to the Substitution help forum\n\n Symbols accepted: w, x, y, z. Input symbol to be substituted then new symbol.\n Example formula:(x²+2x+1) \n Substituting x for y \n Formula format: (x**2+2*x+1) \n After Substitution : y**2 + 2*y + 1")
            elif (helpNum == 5):
                print("Welcome to the Factorisation help forum.\n\n Symbols accepted: w, x, y, z. \n Example formula: (x²+2x+1) \n Formula format: (x**2+2*x+1) \n After Factorisation : (x + 1)**2")
            elif (helpNum == 6):
                print("Welcome to the Solving Equations help forum.\n\n Symbols accepted: w, x, y, z.\n Formula format: (x-1) * (x+3) = 0")
            elif (helpNum == 7):
                print(
                    "Welcome to the Simple Maths help forum.\n\n Symbols accepted: w, x, y, z.\n Terms: Total numbers operated on.")
            elif (helpNum == 8):
                print("Welcome to the Create Variables help forum.\n\n Symbols accepted: w, x, y, z.\n Enter forumala to associate with symbol inserted \n Call in 'Print Varaible'")
            elif (helpNum == 9):
                print("Welcome to the Print Variables help forum.\n\n Symbols accepted: w, x, y, z.\n Enter sybmol to view varaibles stored.")
            break
        else:
            print('The integer must be in the range 1-9')

# main menu
def _ini_():

    print('''
      ____  _  __   _______ ____ _____
     / ___|| | \ \ / / ____/ ___|_   _|
     \___ \| |  \ V /|  _| \___ \ | |
      ___) | |___| | | |___ ___) || |
     |____/|_____|_| |_____|____/ |_|

    ''')
    print('(1) Main Program')
    usermode = int(input('Please Choose from above: '))
    print()

    if usermode == 1:
        while True:
            try:  # choose function option
                num = int(input(''' Select a number to operate:                            
    0. Plot
    1. Simplification
    2. Differentiation
    3. Expansion
    4. Substitution
    5. Factorisation
    6. Solving equations
    7. Simple Maths
    8. Create Variable
    9. Retrieve Variables in storage
    10. Help

    You have choosen number: '''))  # menu options regarding functions
            except ValueError:
                print("Please enter a valid integer 1-10")
                continue
            if num >= 0 and num <= 10:
                print()

                # option 0 -> Plotting
                if (num == 0):
                    symbol = input(
                        "insert symbols to plot or enter [H for help]: ")[0]
                    if (symbol == "H".lower()):
                        print()
                        print("Help for Plotting")
                        print()
                        Helper()
                    moreSymbols = input(
                        "do you have additional symbols to add Y/N: ")[0]
                    while moreSymbols == 'Y':
                        additionalSymbol = input(
                            "insert symbols to Plot or enter [H for help]: ")[0]
                        if (symbol == "H".lower()):  # user can navigate to help function if needs be
                            print()
                            print("Help for Plotting")
                            print()
                            Helper()

                        symbol += additionalSymbol
                        moreSymbols = input(
                            "do you have additional symbols to add Y/N: ")[0]
                    decision = input(
                        "do you want to provide a formula[F] or recall a variable[V]")
                    if (decision == 'F'):
                        formula = input("please insert formula: ")
                    elif (decision == 'V'):
                        variable = input("please insert a variable")
                        formula = RecallVariable(variable)
                    Plotting(symbol, formula)

                # option 1 -> Simplification
                elif (num == 1):
                    symbol = input(
                        "insert symbols to simplify or enter [H for help]: ")[0]
                    if (symbol == "H".lower()):
                        print()
                        print("Help for Simplification")
                        print()
                        Helper()
                    moreSymbols = input(
                        "do you have additional symbols to add Y/N: ")[0]
                    while moreSymbols == 'Y':
                        additionalSymbol = input(
                            "insert symbols to simplify or enter [H for help]: ")[0]
                        if (symbol == "H".lower()):  # user can navigate to help function if needs be
                            print()
                            print("Help for Simplification")
                            print()
                            Helper()

                        symbol += additionalSymbol
                        moreSymbols = input(
                            "do you have additional symbols to add Y/N: ")[0]
                    decision = input(
                        "do you want to provide a formula[F] or recall a variable[V]")
                    if (decision == 'F'):
                        formula = input("please insert formula: ")
                    elif (decision == 'V'):
                        variable = input("please insert a variable")
                        formula = RecallVariable(variable)
                    Simplification(symbol, formula)

                # option 2 -> Differentiation
                elif (num == 2):
                    symbol = input(
                        "insert symbols to differentiate or [H for help]: ")[0]
                    if (symbol == "H".lower()):
                        print()
                        print("Help for Differentiation")
                        print()
                        Helper()
                    moreSymbols = input(
                        "do you have additional symbols to add Y/N: ")[0]
                    while moreSymbols == 'Y':
                        additionalSymbol = input(
                            "insert symbols to differentiate or [H for help]: ")[0]
                        if (symbol == "H".lower()):
                            print()
                            print("Help for Differentiation")
                            print()
                            Helper()
                        symbol += additionalSymbol
                        moreSymbols = input(
                            "do you have additional symbols to add Y/N: ")[0]
                    decision = input(
                        "do you want to provide a formula[F] or recall a variable[V]")
                    if decision == 'F':
                        formula = input("please insert formula: ")
                    elif (decision == 'V'):
                        variable = input("please insert a variable")
                        formula = RecallVariable(variable)
                    Differentiation(symbol, formula)

                # option 3 -> Expansion
                elif (num == 3):
                    symbol = input(
                        "insert symbols to expand or [H for help]: ")[0]
                    if (symbol == "H".lower()):
                        print()
                        print("Help for Expansion")
                        print()
                        Helper()
                    moreSymbols = input(
                        "do you have additional symbols to add Y/N: ")[0]
                    while moreSymbols == 'Y':
                        additionalSymbol = input(
                            "insert symbols to expand or [H for help]: ")[0]
                        if (symbol == "H".lower()):
                            print()
                            print("Help for Expansion")
                            print()
                            Helper()
                        symbol += additionalSymbol
                        moreSymbols = input(
                            "do you have additional symbols to add Y/N: ")[0]
                    decision = input(
                        "do you want to provide a formula[F] or recall a variable[V]")
                    if decision == 'F':
                        formula = input("please insert formula: ")
                    elif (decision == 'V'):
                        variable = input("please insert a variable")
                        formula = RecallVariable(variable)
                    Expansion(symbol, formula)

                # option 4 -> Substitution
                elif (num == 4):
                    oldSymbol = input(
                        "insert symbol (or expression) in formula you wish to substitute or [H for help]: ")
                    if (oldSymbol == "H".lower()):
                        print()
                        print("Help for Substitution")
                        print()
                        Helper()
                    subSymbol = input(
                        "insert new symbol (or expression) you wish to replace with or [H for help]: ")
                    if (subSymbol == "H".lower()):
                        print()
                        print("Help for Substitution")
                        print()
                        Helper()
                    decision = input(
                        "do you want to provide a formula[F] or recall a variable[V]")
                    if (decision == 'F'):
                        formula = input("please insert formula: ")
                    elif (decision == 'V'):
                        variable = input("please insert a variable")
                        formula = RecallVariable(variable)
                    Substitution(oldSymbol, subSymbol, formula)

                # option 5 -> Factorisation
                elif (num == 5):
                    symbol = input(
                        "insert symbols to factorise or [H for help]: ")[0]
                    if (symbol == "H".lower()):
                        print()
                        print("Help for Factorisation")
                        print()
                        Helper()
                    moreSymbols = input(
                        "do you have additional symbols to add Y/N: ")[0]
                    while moreSymbols == 'Y':
                        additionalSymbol = input(
                            "insert symbols to factorise or [H for help]: ")[0]
                        if (additionalSymbol == "H".lower()):
                            print()
                            print("Help for Factorisation")
                            print()
                            Helper()
                        symbol += additionalSymbol
                        moreSymbols = input(
                            "do you have additional symbols to add Y/N: ")[0]
                    decision = input(
                        "do you want to provide a formula[F] or recall a variable[V]")
                    if (decision == 'F'):
                        formula = input("please insert formula: ")
                    elif (decision == 'V'):
                        variable = input("please insert a variable")
                        formula = RecallVariable(variable)
                    Factorisation(symbol, formula)

                # option 6 -> Solving
                elif (num == 6):
                    symbol = input(
                        "insert symbols to solve or [H for help]: ")[0]
                    if (symbol == "H".lower()):
                        print()
                        print("Help for Equation")
                        print()
                        Helper()
                    decision = input(
                        "do you want to provide a formula[F] or recall a variable[V]")
                    if (decision == 'F'):
                        formula = input("What is the first equation to solve")
                    elif (decision == 'V'):
                        variable = input("please insert a variable")
                        formula = RecallVariable(variable)

                    formula2 = input("What is the second equation to solve")
                    Solving(formula, formula2, symbol)

                # option 7 -> Simple Maths
                elif (num == 7):
                    print(
                        '1. Addition , 2. Subtraction , 3. Division, 4. Multiplication, 5. Sqare Root, 6. Modulus Calculator or [H for help]')
                    print()

                    num = int(
                        input('Select a number from the list above or [H for help]: '))
                    if (num == "H".lower()):
                        print()
                        print("Help for Calculator")
                        print()
                        Helper()
                        print()
                        print("Help for Addition")
                    print()
                    print("You selected number: ", num)
                    print()

                    if num >= 1 and num <= 6:

                        if num == 1:

                            print('Addition Selected \n')

                            total = Addition(GetNumberOfTerms())
                            print("Your Total Equals to: ", total)
                            print()

                        elif num == 2:
                            print('Subtraction Selected \n')

                            total = Subtraction(GetNumberOfTerms())
                            print("Your Total Equals to: ", total)
                            print()

                        elif num == 3:
                            print('Division Selected \n')

                            total = Division(GetNumberOfTerms())
                            print("Your Total Equals to: ", total)
                            print()

                        elif num == 4:
                            print('Multiplication Selected \n')

                            total = Multiplication(GetNumberOfTerms())
                            print("Your Total Equals to: ", total)
                            print()

                        elif num == 5:
                            print('Square Root Selected \n')

                            total = SquareRoot()
                            print("Your Total Equals to: ", total)
                            print()

                        elif num == 6:
                            print('Modulus Calculator \n')

                            total = ModulusCalculator(GetNumberOfTerms())
                            print("Your Total Equals to: ", total)
                            print()

                # option 8 -> Create Variables
                elif (num == 8):
                    symbol = input("insert symbol or [H for help]: ")[0]
                    if (symbol == "H".lower()):
                        print()
                        print("Help to Create variables")
                        print()
                        Helper()
                    formula = input("please insert formula to associate: ")
                    createVariable(symbol, formula)
                    _ini_()

                # option 9 -> Recall Variable
                elif (num == 9):
                    symbol = input("insert symbol or [H for help]: ")
                    if (symbol == "H".lower()):
                        print()
                        print("Help to print variables")
                        print()
                        Helper()
                    PrintVariables(symbol)
                    _ini_()

                # option 10 -> Help
                elif (num == 10):
                    print()
                    Helper()
                    break
            else:
                print('The integer must be in the range 1-10')
        

test_code = False

# Running the actual code
if __name__ == "__main__":
    #test_code = True

    if not test_code:
        _ini_()
    else:
        pass
