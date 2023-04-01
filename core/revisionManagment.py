import os.path
class FileAnalysys():
    
    def __init__(self,path_do_arquivo:os.path) -> None:
        """path_do_arquivo: diretorio completo do arquivo
        
        essa classe controla apenas o nome e especificações dispostas no título do arquivo
        """
        self.fileName = path_do_arquivo
        self.fasesList = ["ap","pe","pr","ex"]
    
    # def ParametersView(self):
    #     if not (os.path.isfile(os.path.abspath(self.fileName)) or ):
        
    def FileIndentifier(self) -> dict:
        # verifica as informações importantes do arquivo
        # revisão, número, etc;
        # adicionar futuramente a verificação de fase também
        
        identificadores = dict()
        identificadores["codigo_da_obra"] = None
        identificadores["revisao"] = None
        identificadores["tipo_do_arquivo"] = None
        identificadores["numero_da_folha"] = None
        identificadores["fase"] = None
        
        if os.path.isfile(os.path.abspath(self.fileName)):
            # verifica se o arquivo existe e se é realmente um arquivo
            
            file = str(os.path.basename(self.fileName)).split(".")[0]
            fileType = str(os.path.basename(self.fileName)).split(".")[1]
            
            parametros = list(file.split("-"))
            
            if len(parametros) >= 3:
                # verifica se o arquivo está no padrão de nomenclatura
            
                identificadores["codigo_da_obra"] = parametros[0]
                del parametros[0]
                
                revisao = str()
                str_var = parametros[-1]
                
                for _ in str_var:
                    if _.isdigit():
                        revisao += _
                
                if revisao:
                    identificadores["revisao"] = revisao
                    del parametros[-1]
                    
                else:
                    revisao = str()
                    str_var = parametros[-2]
                    
                    for _ in str_var:
                        if _.isdigit():
                            revisao += _
                
                    if revisao:
                        identificadores["revisao"] = revisao
                        del parametros[-2]

                    
                identificadores["tipo_do_arquivo"] = fileType
                
                
                
                
                for _ in parametros:
                    # pega o número da folha com base em -xxx-
                    # xxx são números, se tiver duas chaves com números pode dar erro 
                    
                    i = 0
                    if(_.isnumeric() and len(_) >= 3):
                        identificadores["numero_da_folha"] = _
                        del parametros[parametros.index(_)]
                        i += 1
                        
                    if _.lower() in self.fasesList:
                        # retorna a fase com base nos padrões de fases que conheço
                        
                        identificadores["fase"] = _
                    else:
                        # erro na nomenclatura da fase
                        pass
                    if i > 1:
                        # adicionar erro de verificação da versão do arquivo
                        pass
            else:
                # emitir erro de nomenclatura
                
                pass
                
        return identificadores
    
    def FileType(self) -> str:
        # retorna o tipo do arquivo: dwg, pdf, etc
        
        return self.FileIndentifier()["tipo_do_arquivo"]
        
    def Fase(self) -> str:
        # retorna a fase do arquivo com base em uma lista de fase predefinida
        return self.FileIndentifier()["fase"]
    
    def CurrentVersion(self) -> int:
        # verificar qual a revisão atual do arquivo
        
        if not self.FileIndentifier()["revisao"] is None:
            return int(self.FileIndentifier()["revisao"])
        
        else: 
            return self.FileIndentifier()["revisao"]
    
    def FileNumber(self) -> str:
        # retorna o número da folha do arquivo
        
        if self.FileIndentifier()["numero_da_folha"]:
            return str(self.FileIndentifier()["numero_da_folha"])
       
        else:
            return None

    def OldVersion(self) -> str:
        # indica qual a revisão anterior do arquivo
        if self.CurrentVersion():
            if (self.CurrentVersion() > 0):
                _current = self.CurrentVersion() - 1
                return str("{:0>2}".format(_current))
            
            else:
                pass
            





        

    
            
                                                                                                                