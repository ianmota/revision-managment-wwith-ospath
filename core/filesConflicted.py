from core.revisionManagment import FileAnalysys as fa
import os.path as op
from os import listdir
import json

class FileConflicted():
    def __init__(self,path_do_arquivo:op,pasta_destino:str,pasta_de_antigos:str = "") -> None:
        self.arquivo = path_do_arquivo
        self.origem = pasta_destino
        self.destino = pasta_de_antigos
        self.GlobalVariables()
        
    def GlobalVariables(self):
  
        self.arquivosAtualizados = list()
        self.erro = str()
        self.statusNewReview = False
    
    def EqualFileNumbers(self) -> list:
        # verificar se já existe arquivo deste tipo na pasta (retorna em todas as fases)
        # quantos e quais
        
        fileNumber = fa(self.arquivo).FileNumber()
        
        fileNames = list()

        if not fileNumber is None:
            for _ in listdir(self.origem):
                
                if op.isfile(op.join(self.origem,_)):
                    
                    if fileNumber == fa(op.join(self.origem,_)).FileNumber():
                        fileNames.append(_)

        return fileNames
    
    def FileExists(self) -> bool:
        if op.basename(self.arquivo) in self.EqualFileNumbers():
            return True
        else:
            return False
        
    def OldConflicted(self) -> list:
        # verificar se há revisões antigas na pasta
  
        if self.EqualFileNumbers():
            if not fa(self.arquivo).CurrentVersion() is None:
                
                for _ in self.EqualFileNumbers():
                    
                        if fa(self.arquivo).CurrentVersion() > 0 and not fa(op.join(self.origem,_)).CurrentVersion() is None:
                            
                            if fa(self.arquivo).CurrentVersion() > fa(op.join(self.origem,_)).CurrentVersion():
                                # colocar a versão desatualizada na pasta antigos
                                self.arquivosAtualizados.append(op.join(self.origem,_))
                            
                            else:
                                self.arquivosAtualizados.append(None)
                            
                        else:
                            return False
            else:
                data = open("core\errorList.json")
                self.erro = json.load(data)["rz2"]
                data.close()

                return self.erro
            
    def NewConflicted(self):
        
        if self.EqualFileNumbers():
            
            if not fa(self.arquivo).CurrentVersion() is None:
                
                i = 0
                for _ in self.EqualFileNumbers():
                    
                    if not _ is None:
                        if fa(self.arquivo).CurrentVersion() < fa(op.join(self.origem,_)).CurrentVersion():
                                # colocar a versão desatualizada na pasta antigos
                                i+=1
                
                if i > 0:
                    return True
                
                if i == 0:
                    return False
                
            else:
                # erro
                pass
    


