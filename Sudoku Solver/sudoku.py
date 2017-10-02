from tkinter import *
import tkinter.messagebox
import numpy as np
import re
import solve_sudoku as Sudoku
from PIL import Image
import PIL
class App(Frame) :

    #Highlight only those cells which contain valid numbers
    def is_valid(self,event):
        print(event.widget.get())
        print(type(event.widget.get()))
        in_string = event.widget.get()
        try :
            if int(in_string) > 0 and int(in_string) < 10 :
                event.widget.configure(bg='#1253fd')
                return True
            else :
                tkinter.messagebox.showinfo("Oops!!","Invalid Value Entered")
                event.widget.focus_set()
        except ValueError :
            print(ValueError)
            if in_string :#if not an empty string then we need to raise error and set focus and return False
                tkinter.messagebox.showinfo("Oops!!","Invalid Value Entered")
                event.widget.focus_set()
        return False

    def fetch_data(self):
        
        matrix = Sudoku.module_helper()
        for i in range(self.height):
            for j in range(self.width):
                e = self.matrix[i][j]
                try :
                    matrix[i][j] = int(e.get())
                except ValueError :
                    print("Value not entered")
                    matrix[i][j] = 0
                    pass
        print("Now solving and displaying : ")
        if not self.check(matrix) :
            print("Rules not followed")
            tkinter.messagebox.showinfo("Violating Rules of Sudoku","Few numbers repeated in a row or a column or in one of the grids")
            return False
        if Sudoku.solve():
            self.display(matrix)
        else :
            tkinter.messagebox.showinfo("Alert!!","Solution Not Possible!! \n Possible Errors :")

    def display(self,matrix) :
        for i in range(self.height) :
            for j in range(self.width) :
                self.matrix[i][j].delete(0,END)
                self.matrix[i][j].insert(0,matrix[i][j])

    def check(self,matrix) :
        #Checking row-wise
        for j in range(1,9) :
            present = [False for i in range(1,9)] 

            for i in range(self.height) :
                if present[matrix[j][i]] :
                    return False
                else :
                    present[matrix[j][i]] = True
        #Checking column-wise 
        for j in range(1,9) :
            present = [False for i in range(1,9)]

            for i in range(self.height) :
                if(present[matrix[i][j]]) :
                    return False
                else :
                    present[matrix[i][j]] = True
        #Cheking in each sub-square
        for i in range(3) :#Selecting a square
            present = [False for i in range(1,9)]
            for j in range(3) :#Iterating over 
                for k in range(3) :
                    if present[matrix[j][i+k]] :
                        return False
                    else :
                        present[matrix[j][i+k]] = True
                
         
       

    def __init__(self,master):
        main_frame = Frame(master,width = 50, height = 50,padx=20,pady=20,bg='#ffffff')#Frame within which Sudoku Grid is situated
        self.height, self.width = 9,9
        self.matrix = list(list())

        #Instantiating Entry Widgets
        for i in range(self.height):
            x = []
            for j in range(self.width) :
                e = Entry(main_frame,width=3,font=('Comic Sans MS',17),justify='center',bg='#f12341')
                x.append(e)
                e.bind('<FocusOut>',self.is_valid)
            self.matrix.append(x)

        #Placing in the proper place the Entry Widgets
        for i in range(self.height) :
            for j in range(self.width) :
                self.matrix[i][j].grid(row=i,column=j,padx = 1, pady = 1)
                #Separating mini squares
                if j == 2 or j == 5 :
                    self.matrix[i][j].grid(padx = (1,10))
                if i == 2 or i == 5  :
                    self.matrix[i][j].grid(pady = (1,10))

                self.matrix[i][j].grid(in_=main_frame)

        main_frame.pack(expand=True)

        #Buttons
        button_frame = Frame(master, width=50, height = 50, padx = 10, pady=10, bg='#ffffff')
        button_frame.pack(expand=True)
        solve_button = Button(button_frame, text="Solve",fg="blue",command=self.fetch_data).pack(side=LEFT)
        quit_button = Button(button_frame, text="Quit",fg="red",command=master.quit).pack(side=RIGHT)
        reset_button = Button(button_frame, text="Reset",fg="#121212",command=self.reset).pack(side=RIGHT)


        mainloop()

    #Empty out all the cells
    def reset(self) :
        for i in range(self.height) :
            for j in range(self.width) :
                self.matrix[i][j].delete(0,10)
                self.matrix[i][j].configure(bg="#f12341")
        self.matrix[0][0].focus_set()

root = Tk()
root.title("Sudoku Solver")
width = root.winfo_screenwidth()
height = root.winfo_screenwidth()
root.geometry('{}x{}+{}+{}'.format(int(width/2),int(height/2),350,40))
root.resizable(width=False,height=False)
Obj = App(root)


