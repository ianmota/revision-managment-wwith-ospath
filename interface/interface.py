import tkinter as tk
from shutil import move
from tkinter import END, filedialog
from tkinter.scrolledtext import ScrolledText
from core.conflitedFiles import VerifyConflicts
from base64 import b64decode
from os import listdir,mkdir
from os.path import basename,exists
# import threading as th

class Application():
    def __init__(self):
        
        
        self.root = tk.Tk()
        self.logo()
        
        self.lc = tk.PhotoImage(data=b64decode(self.logoCubo))
        self.root.iconphoto(True,self.lc)
        
        self.str_DESTINO = tk.StringVar()
        self.str_ARQUIVOS = tk.StringVar()
        self.str_LOCALANTIGO = tk.StringVar()
        
        self.Root01()
        
        self.BotoesRoot01()
        self.LabelsRoot01()
        self.EntryRoot01()
        self.TagConfig()
        
        self.root.mainloop()
        
    
    def Root01(self):
        self.root.title("Revisão Updater")  
        self.root.geometry("600x230")
        self.root.resizable(False,False)
        
    def BotoesRoot01(self):
        
        bt_DESTINO = tk.Button(self.root,text="Local",command=self.AskDirectory)
        bt_DESTINO.place(x=470,y=30,width=120)
        
        bt_ARQUIVOS = tk.Button(self.root,text="Local",command=self.AskOpenFiles)
        bt_ARQUIVOS.place(x=470,y=60,width=120)
        
        bt_LOCALANTIGO = tk.Button(self.root,text="Local",command=self.FilesReload)
        bt_LOCALANTIGO.place(x=470,y=90,width=120)
        
        bt_CONFIRMAR = tk.Button(self.root,text="Confirmar",command=self.VerDir)
        bt_CONFIRMAR.place(x=55,y=195,width=120)
    
    def LabelsRoot01(self):
        lb_RESPONSAVEL = tk.Label(self.root, text= "Nome do responsável: ",border=10 )
        lb_RESPONSAVEL.place(x=7,y=1)
        
        lb_DESTINO = tk.Label(self.root, text= "Selecione o destino: ",border=10 )
        lb_DESTINO.place(x=10,y=26)
        
        lb_ARQUIVOS = tk.Label(self.root, text= "Selecione os arquivos: " )
        lb_ARQUIVOS.place(x=10,y=62.5)
        
        lb_LOCALANTIGO = tk.Label(self.root, text= "Local das revisões antigas: " )
        lb_LOCALANTIGO.place(x=10,y=95)
    
    def EntryRoot01(self):
        
        self.en_RESPONSAVEL = tk.Entry(self.root)
        self.en_RESPONSAVEL.place(x=140,y=7.5,width=320)
        
        en_view_DESTINO = tk.Entry(self.root,state="disabled",textvariable=self.str_DESTINO)
        en_view_DESTINO.place(x=140,y=32.5,width=320)
        
        en_view_ARQUIVOS = tk.Entry(self.root,state="disabled",textvariable=self.str_ARQUIVOS)
        en_view_ARQUIVOS.place(x=140,y=62.5,width=320)
        
        en_view_LOCALANTIGO = tk.Entry(self.root,state="disabled",textvariable=self.str_LOCALANTIGO)
        en_view_LOCALANTIGO.place(x=160,y=95,width=300)
        
        self.en_view_LOGGER = ScrolledText(self.root,state="disabled")
        self.en_view_LOGGER.place(x=230,y=135,width=330, height=80)
        
    def AskDirectory(self):
        self.en_DESTINO = filedialog.askdirectory()
        self.str_DESTINO.set(self.en_DESTINO)

        if self.en_DESTINO:
            if "Antigo" in listdir(self.en_DESTINO):
                self.en_LOCALANTIGO = f"{self.en_DESTINO}\\Antigo"
            else:
                self.en_LOCALANTIGO = f"{self.en_DESTINO}\\Antigos"

            self.str_LOCALANTIGO.set(self.en_LOCALANTIGO)

        
    def AskOpenFiles(self):
        self.en_ARQUIVOS = filedialog.askopenfilenames()
        
        u = ""
        for i in self.en_ARQUIVOS:
            u = u + f"{basename(i)}, "
        

        self.str_ARQUIVOS.set(u[:-1])
    
    def FilesReload(self):
        self.en_LOCALANTIGO = filedialog.askdirectory()
        self.str_LOCALANTIGO.set(self.en_LOCALANTIGO)
        
    def VerDir(self):
        
        try:
            if self.en_DESTINO and self.en_ARQUIVOS:
                self.en_view_LOGGER["state"]="normal"
                self.en_view_LOGGER.delete(1.0,END)
                self.en_view_LOGGER["state"]="disabled"
                add = 0
                not_add = 0
                
                if not exists(self.en_LOCALANTIGO):
                        mkdir(self.en_LOCALANTIGO)
                
                for arquivo in listdir(self.en_DESTINO):
                    conflitosIniciais = VerifyConflicts(arquivo,self.en_DESTINO,self.en_LOCALANTIGO)
                    conflitosIniciais.OldReviewConflited()
                    self.en_view_LOGGER["state"] = "normal"
                    if conflitosIniciais.status_atualizada:
                        self.en_view_LOGGER.insert(END,f"{conflitosIniciais.status_atualizada}\n", "gray")
                    if conflitosIniciais.status_verificar:
                        self.en_view_LOGGER.insert(END,f"{conflitosIniciais.status_verificar}\n", "gray")
                    self.en_view_LOGGER.see(END)
                    self.en_view_LOGGER["state"] = "disabled"
                
                for i in self.en_ARQUIVOS:
                    
                    conflitosNovos = VerifyConflicts(i,self.en_DESTINO,self.en_LOCALANTIGO)
                    conflitosNovos.EqualReviewConflited()
                    
                    if not conflitosNovos.status_existente:
                        
                        conflitosNovos.OldReviewConflited()
                        if conflitosNovos.status_atualizada:
                            self.en_view_LOGGER["state"] = "normal"
                            self.en_view_LOGGER.insert(END,f"{conflitosNovos.status_atualizada}\n", "gray")
                        if conflitosNovos.status_verificar:
                            self.en_view_LOGGER.insert(END,f"{conflitosNovos.status_verificar}\n", "gray")
                            self.en_view_LOGGER.see(END)
                            self.en_view_LOGGER["state"]="disabled"
                        
                        #adicionar verificação para revisões acima
                        
                    elif conflitosNovos.status_existente:
                        self.en_view_LOGGER["state"] = "normal"
                        self.en_view_LOGGER.insert(END,f"{basename(i)} --> JÁ EXISTE\n","red")
                        self.en_view_LOGGER.see(END)
                        self.en_view_LOGGER["state"]="disabled"
                        continue
                    
                    if conflitosNovos.status_atualizada:
                        move(i,self.en_DESTINO,self.en_LOCALANTIGO)
                        add += 1
                        self.en_view_LOGGER["state"] = "normal"
                        self.en_view_LOGGER.insert(END,f"{basename(i)}\n--> REVISÃO ATUALIZADA","green")
                        self.en_view_LOGGER.see(END)
                        self.en_view_LOGGER["state"]="disabled"
                    else:
                        move(i,self.en_DESTINO,self.en_LOCALANTIGO)
                        add += 1
                        self.en_view_LOGGER["state"] = "normal"
                        self.en_view_LOGGER.insert(END,f"{basename(i)}\n --> REVISÃO INICIAL","green")
                        self.en_view_LOGGER.see(END)
                        self.en_view_LOGGER["state"]="disabled"
                        
                self.en_view_LOGGER["state"] = "normal"
                self.en_view_LOGGER.insert(END,f"\n{add} --> ADICIONADOS\n{not_add} --> NÃO ADICIONADOS")
                self.en_view_LOGGER.see(END)
                self.en_view_LOGGER["state"] = "disabled"
            else:
                self.en_view_LOGGER["state"] = "normal"
                self.en_view_LOGGER.delete(1.0,END)
                self.en_view_LOGGER.insert(END,"\nVERIFICAR COERÊNCIA DA SELEÇÃO", "gray")
                self.en_view_LOGGER.see(END)
                self.en_view_LOGGER["state"] = "disabled"
                
        except AttributeError:
                try: 
                    self.en_DESTINO in globals()
                        
                except AttributeError:
                    self.en_view_LOGGER["state"] = "normal"
                    self.en_view_LOGGER.delete(1.0,END)
                    self.en_view_LOGGER.insert(END,"\nO destino não foi adicionado", "red")
                    self.en_view_LOGGER.see(END)
                    self.en_view_LOGGER["state"] = "disabled"

                try:
                    self.en_ARQUIVOS in globals()
                        
                except AttributeError:
                    self.en_view_LOGGER["state"] = "normal"
                    self.en_view_LOGGER.insert(END,"\nArquivos não selecionados", "red")
                    self.en_view_LOGGER.see(END)
                    self.en_view_LOGGER["state"] = "disabled"
        
    
        
    def TagConfig(self):
        self.en_view_LOGGER.tag_config("red", foreground="red")
        self.en_view_LOGGER.tag_config("gray", foreground="gray")
        self.en_view_LOGGER.tag_config("green", foreground="green")

    def logo(self):
        self.logoCubo="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"
        

        
        