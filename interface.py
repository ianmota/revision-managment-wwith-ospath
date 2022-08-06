import tkinter as tk


class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.resizable(False,False)
        
        self.root.mainloop()
        
Application()
        