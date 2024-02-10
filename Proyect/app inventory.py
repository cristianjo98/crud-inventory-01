from Model.model_data import Model
from View.view_interface import View
from tkinter import *

if __name__ == "__main__":
    model = Model()
    
    root = Tk()
    View(root, model)
    root.mainloop()
