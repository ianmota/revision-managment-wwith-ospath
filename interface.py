import tkinter as tk
from tkinter import filedialog
import revisionManagment as rm

class Application():
    def __init__(self):
        self.root = tk.Tk()

        self.Root01()
        self.BotoesRoot01()
        
        self.root.mainloop()
    
    def Root01(self):
        self.root.title("Revisão Updater")
        self.root.geometry("600x600")
        self.root.resizable(False,False)
        
    def BotoesRoot01(self):
        self.bt_DESTINO = tk.Button(self.root,text="Destino",command=self.AskDirectory)
        self.bt_DESTINO.place(relx=0.5,rely=0.5)
        
        self.bt_ARQUIVOS = tk.Button(self.root,text="Arquivos",command=self.AskOpenFiles)
        self.bt_ARQUIVOS.place(relx=0.5,rely=0.1)
        
        self.bt_CONFIRMAR = tk.Button(self.root,text="Confirmar",command=self.Move)
        self.bt_CONFIRMAR.place(relx=0.5,rely=0.8)
    
    def AskDirectory(self):
        self.en_DESTINO = filedialog.askdirectory()
    
    def AskOpenFiles(self):
        self.en_ARQUIVOS = filedialog.askopenfilenames()
        
    def Move(self):
        rm.FileMovimentation(self.en_ARQUIVOS,self.en_DESTINO)
        
Application()
        