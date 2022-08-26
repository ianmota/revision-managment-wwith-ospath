import os
import os.path 

class ReviewUpdate():
    
    def __init__(self,arquivo:str,destino:str) -> None:
        self.arquivo = arquivo
        self.destino = destino

    def CurrentReview(self):
        return self.arquivo[-6:-4]
    
    def OldReview(self):
        if(int(self.CurrentReview())<=10):
            Version = int(self.CurrentReview())-1
            OldReviewDotType = f"0{Version}{self.arquivo[-4:]}"
            CurrentReviewDotType = f"{self.CurrentReview()}{self.arquivo[-4:]}"
            OldReviewBasename = os.path.basename(self.arquivo.replace(CurrentReviewDotType,OldReviewDotType))
            OldReviewFilename = os.path.join(os.path.abspath(self.destino),OldReviewBasename)
            
        elif(int(self.VerPrefix())>10):
            Version = int(self.CurrentReview())-1
            OldReviewDotType = f"{Version}{self.arquivo[-4:]}"
            CurrentReviewDotType = f"{self.CurrentReview()}{self.arquivo[-4:]}"
            OldReviewBasename = os.path.basename(self.arquivo.replace(CurrentReviewDotType,OldReviewDotType))
            OldReviewFilename = os.path.join(os.path.abspath(self.destino),OldReviewBasename)

        return OldReviewFilename
    
    def GetFilesInDir(self):
        return(os.listdir(self.destino))
    

    
    
        
        

    
            
                                                                                                                