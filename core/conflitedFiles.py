from os import listdir
from os.path import basename,join   
from shutil import move
from core.revisionManagment import ReviewUpdate

class VerifyConflicts():
    def __init__(self,filename:str,origem:str,destino="") -> None:
        self.filename = filename
        self.dirOrigem = origem
        self.dirDestino = destino
        self.GlobalVariables()

    def GlobalVariables(self):
        self.status_verificar = ""
        self.status_atualizada = ""
        self.status_existente = ""
    def OldReviewConflited(self):
        fileDir = join(self.dirOrigem,self.filename)
        
        while True:
            update = ReviewUpdate(fileDir,self.dirOrigem)
            if update.CurrentReview() == "00":
                break
            
            try:
                revisaoAntiga = update.OldReview()  
            except ValueError:
                self.status_verificar = f"{self.filename} --> VERIFICAR" 
                break
           
            if basename(revisaoAntiga) in update.GetFilesInDir():
                if self.dirDestino:
                    move(revisaoAntiga,self.dirDestino)
                self.status_atualizada = f"{basename(revisaoAntiga)} --> ATUALIZADO"
            fileDir = revisaoAntiga
                    
    def EqualReviewConflited(self):

        if basename(self.filename) in listdir(self.dirOrigem):
             self.status_existente = f"{basename(self.filename)} --> JÁ EXISTE"
                    