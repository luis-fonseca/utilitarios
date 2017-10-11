# este script cria arquivos e diretórios temporários para teste

import uuid             # gerar identificador unico
import subprocess       # chamar programa externo fsutil
import os

output_dir = os.getcwd()

def generate_random_name():
    """
        a função retorna uma sequencia aleatoria de caracteres
    """
    return uuid.uuid4().hex[0:5]

def create_file(filename, size_kb):
    """
        a função cria um novo arquivo com o valor do argumento
        filename: é o nome do arquivo
        size_kb: é o tamanho do arquivo em kilobyte
    """
    subprocess.call(['fsutil.exe', 'file', 'createnew', filename,
            str(size_kb * 1000)])


def create_folder(parent, foldername, attempts):
    """
        a função cria um novo diretorio com o valor do argumento
        parent: diretório pai de onde ficará o diretório
        foldername: é o nome do diretorio
        attempts: tentativas de se criar um diretório com diferentes nomes
    """
    directory = os.path.join(parent, foldername)
    try:
        os.stat(directory)
    except OSError:
        print('error ' + OSError.args)


#create_file(generate_random_name(), 32)
#create_folder('.', 'test', 0)
