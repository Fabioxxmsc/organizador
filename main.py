import os
import shutil
import re

dirArquivos = r'../Arquivos/'

def main():
  if os.path.isdir(dirArquivos):
    items = os.listdir(dirArquivos)

    count = 1
    for item in items:
      ext = os.path.splitext(item)
      ehDamSP = re.search('DAMSP', ext[0].upper())

      if (ext[1]).lower() == '.pdf' and count <= 20 and (not ehDamSP is None):
        copiar(item, count)
        print(ext[0], 'Copiado ', item)
        count += 1

def copiar(origem, id):
  dirNovo = r'saida/' + str(id)
  if not os.path.exists(dirNovo):
    os.makedirs(dirNovo)
  shutil.copy(dirArquivos + origem, dirNovo + '/doc.pdf')

  file = open(dirNovo + '/inscricao.txt', 'w')
  file.write('inscricao:')
  file.close()

  file = open(dirNovo + '/valor.txt', 'w')
  file.write('valor:')
  file.close()

  file = open(dirNovo + '/data.txt', 'w')
  file.write('data:')
  file.close()

if __name__ == '__main__':
  main()