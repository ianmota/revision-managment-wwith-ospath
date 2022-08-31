class FileMovimentation():
    
    def __init__(self,arquivo:str,destino:str) -> None:
        self.arquivo = arquivo
        self.destino = destino

    def NameSplit(self):
        return self.arquivo[-6:-4]
    
    def OldReview(self):
        
        if(int(self.NameSplit())<=10):
            versao_ = int(self.NameSplit()) - 1
            versaoAnterior = f"0{versao_}."
            revisaoAntiga = self.arquivo.replace(f"{self.NameSplit()}.",versaoAnterior)
            
        elif(int(self.versao02)>10):
            versao_ = int(self.NameSplit()) - 1
            versaoAnterior = f"{versao_}."
            revisaoAntiga = self.arquivo.replace(f"{self.NameSplit()}.",versaoAnterior)

        return revisaoAntiga
    

        

    
            
                                                                                                                