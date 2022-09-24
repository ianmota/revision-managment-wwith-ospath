from core.revisionManagment import FileMovimentation
from os import remove, listdir
from os.path import join, basename, isfile
from shutil import move

class FileConflicted():
    def __init__(self,arquivo:str,origem:str,destino:str = "") -> None:
        self.arquivo = arquivo
        self.origem = origem
        self.destino = destino
        self.GlobalVariables()
        
    def GlobalVariables(self):
        self.statusUpdate = False
        self.arquivosAtualizados = []
        self.ValueError = False
        self.statusEqual = False
        self.statusOld = False
        self.statusDeleted = False
        self.statusNewReview = False
        
    def OldConflicted(self):
        flag = False
        for i in ["bak","dwl"]:
            if i in self.arquivo.lower():
                flag = True
                break
        for i in ["dwg","pdf","dxf"]:
            if i in self.arquivo.lower():
                flag2 = False
                break
            else:
                flag2 = True
                
        
        FileType = basename(self.arquivo).split(".")
        if flag:
            remove(self.arquivo)
            self.statusDeleted = True
        elif len(FileType[1])>3:
                self.ValueError = True
        elif flag2:
            self.ValueError = True
        else:
                
                try:
                    update = FileMovimentation(self.arquivo,self.origem)
                    revisaoAvaliada = int(update.NameSplit())
                    
                    dirFiles = list()
                    for i in listdir(self.origem):
                        arquivo = i.lower()
                        dirFiles.append(arquivo)
                    
                    while revisaoAvaliada > 0:
                        fileVerification = basename(update.OldReview()).lower()
                        
                        for filename in dirFiles:
                            if fileVerification[:-4] in filename:
                    
                                arquivo = join(self.origem,filename.upper())
                                arquivoAntigo = join(self.destino,filename.upper())
                                if isfile(arquivoAntigo):
                                    remove(arquivoAntigo)
                                    move(arquivo,self.destino)
                                else:
                                    move(arquivo,self.destino)
                                    
                                
                                self.arquivosAtualizados.append(filename.upper())
                            else:
                                self.statusUpdate = False
                            
                        update = FileMovimentation(update.OldReview(),self.origem)
                        revisaoAvaliada -= 1
                        
                except ValueError:
                    self.ValueError = True
                
    
    def EqualConflicted(self):
        arquivoName = basename(self.arquivo).lower()
        dirFiles = list()
        for i in listdir(self.origem):
            dirFiles.append(i.lower())

        if arquivoName in dirFiles:
            self.statusEqual = True
    
    def NewConflicted(self):
        pass
    
    def NewFile(self):
        arquivoName = basename(self.arquivo).lower()
        dirFiles = list()
        flag = False
        for i in ["bak","dwl"]:
            if i in self.arquivo.lower():
                flag = True
                break
            
        for i in listdir(self.origem):
            aName = i.lower()
            dirFiles.append(aName[:-8])
        
        if flag:
            remove(self.arquivo)
            self.statusDeleted = True
        elif arquivoName[:-8] not in dirFiles:
            self.statusNewReview = True

