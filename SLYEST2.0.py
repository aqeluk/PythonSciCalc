import matplotlib.pyplot as plt
import matplotlib.figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import SLYEST
from sympy import *
from sympy import Symbol
from sympy.plotting import plot
import tkinter as tk
import tkinter.messagebox as msg
from tkinter import filedialog
import pandas as pd
from fpdf import FPDF

init_printing()  # import everything important from SymPy, including LaTeX printing

expression = ""
number = ""

root = tk.Tk()  # create the root window
formula_input = tk.StringVar(root)
variables_input = tk.StringVar(root)
variables_input2 = tk.StringVar(root)


# make sure you add to the button "command=simplification" and change it to whatever your method is called

def plotting():  # this is the method for plotting graphs
    x = variables_input.get()
    expr = formula_input.get()
    p1 = SLYEST.Plotting(x, expr)
    p1.show()


def substitution():  # this is the method for substitution
    x = variables_input.get()
    y = variables_input2.get()
    expr = formula_input.get()
    subs_expr = SLYEST.Substitution(x, y, expr)
    answerOutput.delete("1.0", tk.END)
    answerOutput.insert(tk.END, subs_expr)
    outputLatex(latex(subs_expr))


def differentiation():
    # reassiging symbol variable into x (code reuse)
    x = variables_input.get()
    expr = formula_input.get()
    differential = SLYEST.Differentiation(x, expr)  # Use sympy.diff() method
    answerOutput.delete("1.0", tk.END)
    answerOutput.insert(tk.END, differential)
    outputLatex(latex(differential))


def Helper():
    # Helped =
    newgui = tk.Toplevel(root)
    newgui.title("HELP")  # application title

    BAR = tk.Frame(newgui, background='#99fb99', height=100)
    main2 = tk.Frame(newgui)
    # L = tk.Label(BAR, text="HELP")
    newgui.geometry("1200x800")
    # topbar2 = tk.Frame(newgui, background='#99fb99', height=100)
    gui22 = tk.Label(BAR, text="HELP", background='#99fb99',
                     font=('Ariel', 35))
    gui22.pack()
    BAR.pack(side="top", fill="x")
    #helpsimplify = msg.showinfo("help ", "help simplification section")

    # def help_simp():

    # msg.showinfo("help ", "lots of tescr")

    # buttons

    main2.columnconfigure(0, weight=1)
    main2.columnconfigure(1, weight=1)
    main2.columnconfigure(2, weight=1)
    main2.columnconfigure(3, weight=1)

    def simp():
        msg.showinfo("how to simplify", "Welcome to the Simplification help forum.\n\n Symbols accepted: w, x, y, z.\n Example formula: (x²+x)/x \n Format to insert forumla: (x**2+x)/x \n After Simplification : x + 1")
    help_Simp = tk.Button(main2, text="Simplification", command=simp)
    help_Simp.grid(row=1, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

    def diff():
        msg.showinfo("how to differentiate", "Welcome to the Differentiation help forum.\n\n Symbols accepted: w, x, y, z.\n Example formula:(x³+9x) \n Format to insert formula: (x**3 + 9*x) \n After Differentiation : 3*x**2 + 9")
    help_Diff = tk.Button(main2, text="Differentiation ", command=diff)
    help_Diff.grid(row=2, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

    def expan():
        msg.showinfo("how to do expansion", "Welcome to the Expansion help forum.\n\n Symbols accepted: w, x, y, z.\n Example formula: (x + 1) x (x+3) \n Format to insert formula: (x + 1)*(x+3) \n After Expansion : x**2 + 4*x + 3 ")
    help_Expansion = tk.Button(main2, text="Expansion",  command=expan)
    help_Expansion.grid(row=3, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

    def sub():
        msg.showinfo("how to substitute", "Welcome to the Substitution help forum\n\n Symbols accepted: w, x, y, z. Input symbol to be substituted then new symbol.\n Example formula:(x²+2x+1) \n Substituting x for y \n Formula format: (x**2+2*x+1) \n After Substitution : y**2 + 2*y + 1")
    help_Substituion = tk.Button(main2, text="Substitution", command=sub)
    help_Substituion.grid(row=4, column=1, sticky=tk.W +
                          tk.E, padx=10, pady=10)

    def fact():  # factorisation
        msg.showinfo("how to factorise", "Welcome to the Factorisation help forum.\n\n Symbols accepted: w, x, y, z. \n Example formula: (x²+2x+1) \n Formula format: (x**2+2*x+1) \n After Factorisation : (x + 1)**2")
    help_Fac = tk.Button(main2, text="Factorisation", command=fact)
    help_Fac.grid(row=5, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

    def solvingE():  # solving equations
        msg.showinfo("how to solve equations",
                     "Welcome to the Solving Equations help forum.\n\n Symbols accepted: w, x, y, z.\n Formula format: (x-1) * (x+3) = 0")
    help_Solving = tk.Button(main2, text="Solving Equations", command=solvingE)
    help_Solving.grid(row=1, column=2, sticky=tk.W + tk.E, padx=10, pady=10)

    def simpM():  # simplifying maths
        msg.showinfo("how to simplify maths",
                     "Welcome to the Simple Maths help forum.\n\n Symbols accepted: w, x, y, z.\n Terms: Total numbers operated on.")
    help_Simple = tk.Button(main2, text="Simple Maths", command=simpM)
    help_Simple.grid(row=2, column=2, sticky=tk.W + tk.E, padx=10, pady=10)

    def createV():  # creating variables
        msg.showinfo("how to create variables",
                     "Welcome to the Create Variables help forum.\n\n Symbols accepted: w, x, y, z.\n Enter forumala to associate with symbol inserted \n Call in 'Print Varaible'")
    help_Create = tk.Button(main2, text="Creating Variables", command=createV)
    help_Create.grid(row=3, column=2, sticky=tk.W + tk.E, padx=10, pady=10)

    def printV():  # printing variables
        msg.showinfo("how to print variables",
                     "Welcome to the Print Variables help forum.\n\n Symbols accepted: w, x, y, z.\n Enter sybmol to view varaibles stored.")
    help_Print = tk.Button(main2, text="Print Variables", command=printV)
    help_Print.grid(row=4, column=2, sticky=tk.W + tk.E, padx=10, pady=10)

    main2.pack(side="top", fill="both", expand=True)

    # msg.showinfo("HELP", 'Welcome to plotting help forum. \n To plot your graph enter maths problem where prompted and press Generate Graph'.upper())

    newgui.mainloop()

    # answerOutput.delete("1.0", tk.END)

    # msg.showinfo("HELP", 'Welcome to plotting help forum. \n To plot your graph enter maths problem where prompted and press Generate Graph'.upper())


def simplification():  # this is the method for simplification
    expr = formula_input.get()  # get formula input
    simplified = SLYEST.Simplification(expr)  # simplify expression
    # remove what's currently in the answer output boxs
    answerOutput.delete("1.0", tk.END)
    # show answer in the answer output box
    answerOutput.insert(tk.END, simplified)
    outputLatex(latex(simplified))


def expansion():  # this is the method for expansion
    expr = formula_input.get()
    expanded = SLYEST.Expansion(expr)
    # remove what's currently in the answer output box
    answerOutput.delete("1.0", tk.END)
    # show answer in the answer output box
    answerOutput.insert(tk.END, expanded)
    outputLatex(latex(expanded))


def solving():  # this is the method for solving equations
    expr = formula_input.get()
    solvequation = SLYEST.Solving(expr)
    # remove what's currently in the answer output box
    answerOutput.delete("1.0", tk.END)
    # show answer in the answer output box
    answerOutput.insert(tk.END, solvequation)
    outputLatex(latex(solvequation))


def simpleMaths():  # this is the method for simple maths
    expr = formula_input.get()  # get formula input
    maths = simplify(expr)  # simplify expression
    # remove what's currently in the answer output box
    answerOutput.delete("1.0", tk.END)
    # show answer in the answer output box
    answerOutput.insert(tk.END, maths)
    outputLatex(latex(maths))


def prmFactors():  # this is the method for prime factorisation
    expr = formula_input.get()
    factors = primefactors(expr)
    answerOutput.delete("1.0", tk.END)
    answerOutput.insert(tk.END, factors)
    outputLatex(latex(factors))


def factorisation():  # this is the method for factorisation
    x = variables_input.get()
    expr = formula_input.get()
    factorised = SLYEST.Factorisation(x, expr)
    answerOutput.delete("1.0", tk.END)
    answerOutput.insert(tk.END, factorised)
    outputLatex(latex(factorised))


def xsquared():
    x = int(variables_input.get())
    squared = x ** 2
    # remove what's currently in the answer output box
    answerOutput.delete("1.0", tk.END)
    # show answer in the answer output box
    answerOutput.insert(tk.END, squared)
    outputLatex(latex(squared))


def clear_text():
    # clear the content of text entry boxes in the GUI
    # clear the formula input box
    formula_input.set("Enter the maths problems here".upper())
    # clear the variable input box
    variables_input.set("Enter the variables here".upper())
    variables_input2.set("Enter the second variables here".upper())
    storageArea.delete(0, tk.END)
    storageArea.insert(tk.END, "Storage area for saved variables".upper())
    answerOutput.delete("1.0", tk.END)  # clear the answer output box
    # show the default text in the answer output box
    answerOutput.insert(tk.END, "ANSWER WILL APPEAR HERE")
    msg.showinfo("SLYEST", "All input fields have been cleared".upper())


def storageSave():
    # Get the contents of the input field
    toStore = answerOutput.get("1.0", tk.END)
    storageArea.insert(0, toStore)  # Get the text area object


def storageUse():  # this is the method for using the storage
    # Get the text area object
    toUse = storageArea.get(storageArea.curselection())
    formulaBox.delete(0, tk.END)
    formulaBox.insert(0, toUse)


def press(num):
    # point out the global expression variable
    global expression
    # concatenation of string33
    expression = expression + str(num)

    expression.set(expression)

    # update the expression by using set method


def outputLatex(toConvert):
    tmptext = "$" + toConvert + "$"
    ax.clear()
    ax.text(0.1, 0.5, tmptext, fontsize=15)
    canvas.draw()


def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                          filetypes=(
                                              ('CSV files', "*.csv"), ("Text files", "*.txt"), ("all files", "*.*")))
    label_file.configure(text="File Loaded: " + filename)


def markAndOutput():  # this is the method for marking and outputting
    df = pd.read_csv(filename)
    studentScores = []

    for index in df.index:  # for each row in the dataframe
        studentID = df['studentID'][index]
        studentName = df['studentName'][index]
        formula = df['formula'][index]
        operation = df['Operation'][index]
        studentAnswer = df['studentAnswer'][index]

        if not any(d['studentID'] == int(studentID) for d in studentScores):
            dictionaryName = {'studentID': int(studentID), 'studentName': str(studentName), 'totalQuestions': 0,
                              'correctQuestions': 0}
            studentScores.append(dictionaryName)

        dictionaryName['totalQuestions'] += 1
        if operation == "SIMPLIFY":
            answer = simplify(formula)
            if str(studentAnswer) == str(answer):
                dictionaryName['correctQuestions'] += 1
        if operation == "FACTORISE":
            answer = factor(formula)
            if str(studentAnswer) == str(answer):
                dictionaryName['correctQuestions'] += 1
        if operation == "EXPAND":
            answer = expand(formula)
            if str(studentAnswer) == str(answer):
                dictionaryName['correctQuestions'] += 1
        if operation == "PRIME":
            answer = primefactors(formula)
            if str(studentAnswer) == str(answer):
                dictionaryName['correctQuestions'] += 1
        if operation == "SIMPLE":
            answer = eval(formula)
            if str(studentAnswer) == str(answer):
                dictionaryName['correctQuestions'] += 1

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size=20)

        pdf.cell(200, 10, txt="Student Scores", ln=1, align='C')

        for i in studentScores:
            studentOutput = i['studentName'] + \
                " has scored " + str(i['correctQuestions'])
            pdf.cell(200, 10, txt=studentOutput, ln=2, align='L')

        pdf.output("markingoutput.pdf")

        label_file.configure(text="PDF REPORT CREATED!")


def main():  # this is the main method
    global ax, answerOutput
    global canvas
    # root.geometry("1200x800")  # set window size
    root.title("SLYEST")  # application title

    topbar = tk.Frame(root, background='#99fb99', height=100)
    main = tk.Frame(root)

    slyestLabel = tk.Label(topbar, text="SLYEST",
                           background='#99fb99', font=('Ariel', 35))
    slyestLabel.pack()

    # Creating two columns for GUI
    left_pane = tk.Frame(main)
    right_pane = tk.Frame(main)
    left_pane.pack(side=tk.LEFT, expand=True)
    right_pane.pack(side=tk.RIGHT, expand=True)

    top_right = tk.Frame(right_pane)

    top_right.columnconfigure(0, weight=3)
    top_right.columnconfigure(1, weight=1)

    global storageArea
    storageArea = tk.Listbox(top_right, width=100)
    storageArea.insert(tk.ACTIVE, "STORAGE FOR SAVED VARIABLES")
    storageArea.grid(row=0, column=0, padx=10, pady=10)

    btn_useStorage = tk.Button(
        top_right, text='USE VARIABLE', command=storageUse)
    btn_useStorage.grid(row=0, column=1, padx=10, pady=10)

    top_right.pack(expand=True)
    top_left = tk.Frame(left_pane)  # top left frame
    top_left.columnconfigure(0, weight=1)
    top_left.columnconfigure(1, weight=1)
    top_left.columnconfigure(2, weight=1)
    top_left.columnconfigure(3, weight=1)
    equation = tk.StringVar()
    # expression_field = Entry(tk, textvariable=equation)

    btn_Simplification = tk.Button(
        top_left, text="Simplification", command=simplification)
    btn_Simplification.grid(row=0, column=0,
                            sticky=tk.W + tk.E, padx=10, pady=10)

    btn_xsquared = tk.Button(top_left, text="x2")

    btn_Differentiation = tk.Button(
        top_left, text="Differentiation", command=differentiation)
    btn_Differentiation.grid(
        row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=10)

    btn_Expansion = tk.Button(top_left, text="Expansion", command=expansion)
    btn_Expansion.grid(row=0, column=2, sticky=tk.W +
                       tk.E, padx=10, pady=10)

    btn_Substitution = tk.Button(
        top_left, text="Substitution", command=substitution)
    btn_Substitution.grid(row=0, column=3,
                          sticky=tk.W + tk.E, padx=10, pady=10)

    btn_Factorisation = tk.Button(
        top_left, text="Factorisation", command=factorisation)
    btn_Factorisation.grid(row=1, column=0,
                           sticky=tk.W + tk.E, padx=10, pady=10)

    btn_Solving = tk.Button(
        top_left, text="Solving Equations", command=solving)
    btn_Solving.grid(row=1, column=1, sticky=tk.W +
                     tk.E, padx=10, pady=10)

    btn_SimpleMaths = tk.Button(
        top_left, text="Simple Maths", command=simpleMaths)
    btn_SimpleMaths.grid(row=1, column=2, sticky=tk.W +
                         tk.E, padx=10, pady=10)

    btn_PrimeFactors = tk.Button(
        top_left, text="Prime Factors", command=prmFactors)
    btn_PrimeFactors.grid(row=1, column=3,
                          sticky=tk.W + tk.E, padx=10, pady=10)

    clear = tk.Button(top_left, text='X2', command=xsquared, fg='green',
                      bg='white', height=1, width=7)  # add command functionality for x squared
    clear.grid(row=5, column='1')

    top_left.pack(expand=True, fill="both", pady=10, padx=10)

    topmiddle_right = tk.Frame(right_pane)

    graphArea = tk.Text(topmiddle_right, height=20)
    graphArea.pack(expand=True, fill='both', padx=15, pady=15)
    graphArea.insert(tk.INSERT, 'REPLACE WITH GRAPH')

    topmiddle_right.pack(expand=True, padx=10, pady=10)
    topmiddle_left = tk.Frame(left_pane)

    global formulaBox
    formulaBox = tk.Entry(topmiddle_left, width=100,
                          textvariable=formula_input)
    formulaBox.insert(0, "Enter the maths problem here".upper())
    formulaBox.pack(padx=10, pady=10)

    topmiddle_left.pack(expand=True, fill='both')

    bottommiddle_right = tk.Frame(right_pane)

    btn_Plotting = tk.Button(
        bottommiddle_right, text='GENERATE GRAPH', command=plotting)
    btn_Plotting.pack(expand=True, fill='both', padx=15, pady=15)

    bottommiddle_right.pack(expand=True)
    bottommiddle_left = tk.Frame(left_pane)

    bottommiddle_left.columnconfigure(0, weight=1)
    bottommiddle_left.columnconfigure(1, weight=1)
    bottommiddle_left.columnconfigure(2, weight=1)
    bottommiddle_left.columnconfigure(3, weight=1)

    variableBox = tk.Entry(
        bottommiddle_left, textvariable=variables_input, width=50)

    variableBox2 = tk.Entry(
        bottommiddle_left, textvariable=variables_input2, width=50)

    # add command functionality for x squared
    variableBox.insert(0, "Enter the variables here".upper())
    variableBox.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    variableBox2.insert(0, "Enter the second set of variables here".upper())
    variableBox2.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    btn_saveVariable = tk.Button(
        bottommiddle_left, text="SAVE TO STORAGE", command=storageSave)
    btn_saveVariable.grid(row=0, column=2, sticky=tk.E, padx=10, pady=10)

    btn_clear = tk.Button(bottommiddle_left, text="CLEAR", command=clear_text)
    btn_clear.grid(row=0, column=3, sticky=tk.E, padx=10, pady=10)

    bottommiddle_left.pack(expand=True, fill='both', pady=10, padx=10)

    global label_file  # global variable for file name
    bottom_right = tk.Frame(right_pane)  # bottom right frame
    bottom_right.columnconfigure(0, weight=1)
    bottom_right.columnconfigure(1, weight=1)
    bottom_right.columnconfigure(2, weight=1)
    bottom_right.columnconfigure(3, weight=1)
    label_file = tk.Label(bottom_right, text="File Loaded: ", width=50)
    label_file.grid(row=0, column=0, padx=10, pady=10)
    btn_import = tk.Button(
        bottom_right, text='IMPORT ANSWERS', command=browseFiles)
    btn_import.grid(row=0, column=1, padx=10, pady=10)
    btn_PDFReport = tk.Button(
        bottom_right, text="PDF REPORT", command=markAndOutput)
    btn_PDFReport.grid(row=0, column=2, padx=10, pady=10)
    btn_Help = tk.Button(bottom_right, text="HELP", command=Helper)
    btn_Help.grid(row=0, column=3, padx=10, pady=10)
    bottom_right.pack(expand=True, padx=10, pady=10)

    bottom_left = tk.Frame(left_pane)

    global answerOutput
    answerOutput = tk.Text(bottom_left)
    answerOutput.pack(expand=True, fill='both', pady=15, padx=15)
    answerOutput.insert(tk.INSERT, "ANSWER WILL APPEAR HERE")
    bottom_left.pack(expand=True)

    label = tk.Label(bottom_left)
    label.pack()

    fig = matplotlib.figure.Figure(figsize=(7, 3), dpi=100)
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=graphArea)
    canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    topbar.pack(side="top", fill="x")
    main.pack(side="top", fill="both", expand=True)

    root.mainloop()


test_code = False  # set to True to run tests, False to run the program

if __name__ == "__main__":
    #  test_code = True

    if not test_code:
        main()
    else:
        pass  # run tests
