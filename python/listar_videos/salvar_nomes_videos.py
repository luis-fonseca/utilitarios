# este script lista os arquivos de vídeo no diretório onde está
# salva os nomes em um arquivo, move as legendas para outro diretório
# por fim, permite excluir os vídeos caso o usuário deseje

import glob

for filename in glob.iglob('.', recursive=True):
    print(filename)
