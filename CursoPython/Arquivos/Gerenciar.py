import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
print(ROOT_PATH.parent)


#criar diretorio
os.mkdir(ROOT_PATH / 'novo-diretorio')



#renomear arquivo
#não funcionou
arquivo = open(ROOT_PATH / "novo.txt", 'w')
arquivo.close

os.rename(ROOT_PATH/ 'novo.txt'/ 'alterado.txt')

#remover arquivo

os.remove(ROOT_PATH/ 'alterado.txt')

#mover arquivo

shutil.move(ROOT_PATH / 'novo.txt', ROOT_PATH / 'novo-diretorio'/ 'novo.txt')