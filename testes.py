from core.revisionManagment import FileAnalysys as fa
from core.filesConflicted import FileConflicted

# testes de uso
# filepath = "D:\\Dropbox\\Dropbox\\1528 - HM51\\Final\\HM51-EST-EX-051-FUNDA-R00.dwg"
# filepath = "G:\\Meu Drive\\Cubo Engenharia\Projetos (1)\\1544 - Kallas Dracena\\Final\\0733-KZ-EST-PE-1104-FOR-T01-BAR-R01.dwg"
# filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\Final\\Antigo\\0733-KZ-EST-PR-1006-MOD-T01-TIP-R00.pdf"
# filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1528 - HM51\\Forma da fundação\\HM51-EST-EX-052-FUNDA-R00.pdf"
# filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\Final\\0733-KZ-EST-PR-1007-FOR-T01-TIP-R01-Comentado.pdf"
filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\Final\\0733-KZ-EST-PR-3007-FOR-T03-TIP-R00-Comentado.pdf"
# filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\oi.dwg"
# filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\Final\\0733-KZ-EST-PE-1104-FOR-T01-BAR-R00.dwg"

print(fa(filepath).CurrentVersion())
print(fa(filepath).FileNumber())
# # print(fa(filepath).OldVersion())
# # print(fa(filepath).FileNumber())
# print(fa(filepath).Fase())
# print(fa(filepath).FileIndentifier())





# filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\Final\\Antigo\\0733-KZ-EST-PR-1006-MOD-T01-TIP-R00.pdf")
# filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1528 - HM51\\HM055-C01-EST-107-1PF-PR-R02.pdf"
# filedir = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\Final\\Antigo"
# filedir = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1528 - HM51\\Forma da fundação"
# filedir = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\Final"
# filepath = "G:\\Meu Drive\\Cubo Engenharia\\Projetos (1)\\1544 - Kallas Dracena\\Final\\0733-KZ-EST-PR-1007-FOR-T01-TIP-R02.pdf"


# filepath = op.realpath("D:/Dropbox\Dropbox/1528 - HM51/Final/HM51-EST-EX-051-FUNDA-R00.dwg")
# filedir = op.realpath("D:/Dropbox/Dropbox/1528 - HM51/Final")

# teste = FileConflicted(filepath,filedir)
# teste.OldConflicted()
# print(teste.arquivosAtualizados)
# print(teste.EqualFileNumbers())
# print(filepath)