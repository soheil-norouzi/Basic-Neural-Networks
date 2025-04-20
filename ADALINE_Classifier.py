# تمرین ۵)
# Computational Inteligence Class
# Soheil Norouzi

import numpy as np
import tkinter as tk

class ADALINE:
    def __init__(self, input_number):
        self.w = np.random.randn(input_number) # categories list
        self.b = np.random.randn(1)
        self.learning_rate = 0.1
        
    def train(self, pattern, label ):
        target = 1 if label == 'X' else -1 # get the target category index
        output = np.dot(self.w, pattern) + self.b # compute output for all categories
        error = target - output
        self.w = self.w + (self.learning_rate * error * pattern)
        self.b = self.b +(self.learning_rate * error)

    def predict(self, pattern):
        output = np.dot(self.w, pattern) + self.b
        return 1 if output >= 0 else 0
     
grid_size = 5 # the grid is 5 by 5, and each square is 60 pixels wide
cell_size = 60

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw you shape here")
        self.canvas = tk.Canvas(root, width=grid_size*cell_size , height=grid_size*cell_size)
        self.canvas.pack()
        self.cell = [] #-1 for white, 1 for black
        for i in range(grid_size):  # we could use this line inplace of for loop: 
            row = [-1]*grid_size    # self.cell = [[-1]*grid_size for _ in range (grid_size)]
            self.cell.append(row)

        self.rect= []
        for i in range(grid_size):  # same for here: 
            row = [None]* grid_size # self.rect = [[None]*grid_size for _ in range (grid_size)]
            self.rect.append(row)

        # define categories and initialize the multi-category perceptron
        self.category = ['O', 'X', 'I']
        self.net = ADALINE(grid_size * grid_size, self.category)

        for i in range(grid_size):
            for j in range(grid_size):
                x1 = j * cell_size
                y1 = i * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2 ,  y2, fill= 'white', outline='black')
                self.rect[i][j] = rect
        
        self.canvas.bind("<Button-1>", self.toggle)

        btns = tk.Frame(root)
        btns.pack()
        tk.Button(btns, text="train as X", command = self.train_X).pack(side=tk.LEFT, padx=5)
        tk.Button(btns, text="train as O", command = self.train_O).pack(side=tk.LEFT, padx=5)
        tk.Button(btns, text="Train as I", command=self.train_I).pack(side=tk.LEFT, padx=5)
        tk.Button(btns, text="predict", command = self.predict).pack(side=tk.LEFT, padx=5)
        tk.Button(btns, text="clear", command = self.clear).pack(side=tk.LEFT, padx=5)
        self.result = tk.Label(root, text="Draw and Train!", font=("Arial", 14))
        self.result.pack(pady=10)
    
    # by clicking on the square it flips between white and black to draw desired patter
    def toggle(self, event):
        rows = event.y // cell_size
        columns = event.x // cell_size
        self.cell[rows][columns] *= -1
        if self.cell[rows][columns] == 1:
            color = 'black'
        else:
            color = 'white'
        self.canvas.itemconfig(self.rect[rows][columns], fill=color)

    def extract_pattern(self):
        flat = [] # turn 5x5 grid into a single list of 25 numbers
        for rows in self.cell:
            for  val in rows:
                flat.append(val)
        #print(flat)
        return np.array(flat)
    def train_X(self):
        self.net.train(self.extract_pattern(), 'X')
        self.result.config(text="trained as X")
    def train_O(self):
        self.net.train(self.extract_pattern(), 'O')
        self.result.config(text="trained as O")
    def train_I(self):
        self.net.train(self.extract_pattern(), 'I')
        self.result.config(text="Trained as I")
    def predict(self):
        result = self.net.predict(self.extract_pattern())
        self.result.config(text=f"Predicts as {result}")
        
    def clear(self):
        for i in range(grid_size):
            for j in range(grid_size):
                self.cell[i][j] = -1
                self.canvas.itemconfig(self.rect[i][j], fill="white")
        self.result.config(text="Draw and Train!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()