import shutil
import os

class FileMovimentation():
    
    def __init__(self,arquivo:str,destino:str) -> None:
        self.arquivo = arquivo
        self.destino = destino

    def NameSplit(self):
        quebra01 = self.FileName().split("-")
        quebra02 = quebra01[-1].split(".")
        return quebra02[0]

    def VerPrefix(self):
        if "R" in self.NameSplit():
            return(self.NameSplit().split("R")[1])
    
    def RevisionWithoutPrefix(self):
        
        if(int(self.NameSplit())<=10):
            versao_ = int(self.NameSplit())-1
            versaoAnterior = f"0{versao_}."
            revisaoAntiga = self.FileName().replace(f"{self.NameSplit()}.",versaoAnterior)
            
        elif(int(self.versao02)>10):
            versao_ = int(self.NameSplit())-1
            versaoAnterior = f"{versao_}."
            revisaoAntiga = self.FileName().replace(f"{self.NameSplit()}.",versaoAnterior)

        return revisaoAntiga
    
    def RevisionPrefix(self):
        
        if(int(self.VerPrefix())<=10):
            versao_ = int(self.VerPrefix())-1
            versaoAnterior = f"0{versao_}."
            revisaoAntiga = self.FileName().replace(f"{self.VerPrefix()}.",versaoAnterior)
            
        elif(int(self.VerPrefix())>10):
            versao_ = int(self.VerPrefix())-1
            versaoAnterior = f"{versao_}."
            revisaoAntiga = self.FileName().replace(f"{self.VerPrefix()}.",versaoAnterior)

        return revisaoAntiga
        
    def FileName(self):
        return(os.path.basename(self.arquivo))
    
    def GetFilesInDir(self):
        destino = self.destino
        return(os.listdir(destino))
        

    
            
                                                                                                                