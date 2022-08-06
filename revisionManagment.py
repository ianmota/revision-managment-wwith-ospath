import shutil
import os

arquivos = [os.path.abspath("C:/Users/ian10/Desktop/RBG-EST-E-112-000-04.dwg"),os.path.abspath("C:/Users/ian10/Desktop/RBG-EST-E-103-000-07.dwg"),os.path.abspath("C:/Users/ian10/Desktop/RBG-EST-E-102-000-07.dwg") ]

destino = "C:/Users/ian10/Desktop/1. NOVA REVISÃO"
revisoesAntigas = "Antigos"

for i in arquivos:
    
    os.chdir(destino)
    diretorio = os.listdir(destino)
    nomeArquivos = os.path.basename(i)
    
    quebra01 = nomeArquivos.split("-")
    quebra02 = quebra01[-1].split(".")
    
    versao02 = quebra02[0]
    
    if(int(versao02)<10):
        versao_ = int(versao02)-1
        versaoAnterior = f"0{versao_}"
        revisaoAntiga = nomeArquivos.replace(versao02,versaoAnterior)
    
    if (revisaoAntiga in diretorio):
        arquivo = os.path.abspath(diretorio[diretorio.index(revisaoAntiga)])
    else:
        "ERRO"
        continue
        
    if "Antigo" in diretorio:
        novoDiretorio = os.path.abspath(f'{destino}/Antigo')
        
    elif "Antigos" in diretorio:
        novoDiretorio = os.path.abspath(f'{destino}/Antigos')
        
    else:
        novoDiretorio = os.path.abspath(destino+"/Antigos")
        os.mkdir(novoDiretorio)
        
    shutil.move(arquivo,novoDiretorio)
    shutil.move(i,destino)

    
            
                                                                                                                