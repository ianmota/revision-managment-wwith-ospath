from genericpath import isdir
from revisionManagment import FileMovimentation
import os
import os.path as op
import shutil
class FileConflicted():
    def __init__(self,arquivo:str,origem:str,destino:str = "") -> None:
        self.arquivo = arquivo
        self.origem = origem
        self.destino = destino
        self.GlobalVariables()
        
    def GlobalVariables(self):
        self.statusUpdate = bool()
        self.ValueError = bool()
        self.statusEqual = bool()
        self.statusOld = bool()
        self.statusDeleted = bool()
        self.statusNewReview = bool()
        
    def OldConflicted(self):
        flag = False
        for i in ["bak","dwl"]:
            if i in self.arquivo.lower():
                flag = True
                break
                
        if flag:
            os.remove(self.arquivo)
            self.statusDeleted = True
        else:

                update = FileMovimentation(self.arquivo,self.origem)
                dirFiles = list()
                self.statusDeleted = False
                for i in os.listdir(self.origem):
                    dirFiles.append(i.lower())
                try:
                    if op.basename(update.OldReview()).lower() in dirFiles:
                        arquivo = os.path.join(self.origem,os.path.basename(update.OldReview()))
                        shutil.move(arquivo,self.destino)
                        self.statusUpdate = True
                    else:
                        self.statusUpdate = False
                except ValueError:
                    self.ValueError = True
                
    
    def EqualConflicted(self):
        arquivoName = op.basename(self.arquivo).lower()
        dirFiles = list()
        for i in os.listdir(self.origem):
            dirFiles.append(i.lower())

        if arquivoName in dirFiles:
            self.statusEqual = True
        else:
            self.statusEqual = False
    
    def NewConflicted(self):
        pass
    
    def NewFile(self):
        arquivoName = op.basename(self.arquivo).lower()
        dirFiles = list()
        flag = False
        for i in ["bak","dwl"]:
            if i in self.arquivo.lower():
                flag = True
                break
            
        for i in os.listdir(self.origem):
            dirFiles.append(i.lower())
        
        self.statusDeleted = False
        if flag:
            os.remove(self.arquivo)
            self.statusDeleted = True
        elif arquivoName not in dirFiles:
            self.ValueError = False
            try:
                
                update = FileMovimentation(self.arquivo,self.origem)
                if update.NameSplit() == "00":
                    self.statusNewReview = True
                else:
                    self.statusNewReview = False
            except ValueError:
                self.ValueError = True