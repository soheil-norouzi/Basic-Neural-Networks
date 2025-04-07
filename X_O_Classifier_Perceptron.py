import numpy as np
import tkinter as tk

class perceptron():
    def __init__(self, input_size):
        self.w = np.random.randn(input_size)
        self.b = np.random.randn(1)
        self.learning_rate = 0.1
    def train(self,pattern , label):
        if label == "X":
            target = 1
        elif label == "O":
            target = -1
        output = self.predict(pattern)

        if output != target:
            self.w = self.w + self.learning_rate* (target - output) * pattern
            self.b = self.b + self.learning_rate * (target - output)

    def predict(self, pattern):
        Sigma = np.dot(self.w , pattern) + self.b
        if Sigma >= 0:
            return 1
        else:
            return 0
        
grid_size = 5
cell_size = 60

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Draw you shae here")
        self.canvas = tk.Canvas(root, width=grid_size*cell_size , height=grid_size*cell_size)
        self.canvas.pack()
        self.cell = []
        for i in range(grid_size):  # we could use this line inplace of for loop: 
            row = [-1]*grid_size    # self.cell = [[-1]*grid_size for _ in range (grid_size)]
            self.cell.append(row)

        self.rect= []
        for i in range(grid_size):  # same for here: 
            row = [None]* grid_size # self.rect = [[None]*grid_size for _ in range (grid_size)]
            self.rect.append(row)

        self.net = perceptron(grid_size * grid_size)

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
        tk.Button(btns, text="predict", command = self.predict).pack(side=tk.LEFT, padx=5)
        tk.Button(btns, text="clear", command = self.clear).pack(side=tk.LEFT, padx=5)
        self.result = tk.Label(root, text="Draw and Train!", font=("Arial", 14))
        self.result.pack(pady=10)
    
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
        flat = []
        for rows in self.cell:
            for  val in rows:
                flat.append(val)
        #flat = [val for rows in self.cell for val in rows]
        print(flat)
        return np.array(flat)
    def train_X(self):
        self.net.train(self.extract_pattern(), 'X')
        self.result.config(text="trained as X")
    def train_O(self):
        self.net.train(self.extract_pattern(), 'O')
        self.result.config(text="trained as O")
    def predict(self):
        results = self.net.predict(self.extract_pattern())
        if results == 1:
            label = 'X'
        elif results == 0:
            label = 'O'
        
        self.result.config(text=f'predics as {label}')
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