import string
import random

class GenerateNames(object):

    def __init__(self):
        alfa_set = string.ascii_letters
        num_set = string.digits
        alfanum_set = alfa_set + num_set
        win_set = "{['$-=};_`,!()~&+]%^@#"
        linux_set = "!\"#$%&'()*+,-.:;<=>?@[\]^_`{|}~ ."

    def generate_random_alfa_name(size):
        """
        A função retorna um nome alfa aleatório.
        size: para definir o tamanho do nome.
        """
        return random.sample(alfa_set, size)

    def generate_random_num_name(size):
        """
        A função retorna um nome numérico aleatório.
        size: para definir o tamanho do nome.
        """
        return random.sample(num_set, size)

    def generate_random_alfanum_name(size):
        """
        A função retorna um nome alfanumérico aleatório.
        size: para definir o tamanho do nome.
        """
        characters = alfa_set + num_set
        return random.sample(characters, size)

    def generate_random_win_name(size):
        """
        A função retorna um nome alfanumérico, incluindo caracteres de pontuação, aleatório
        para o sistema operacional Windows.
        size: para definir o tamanho do nome.
        """
        characters = alfanum_set + win_set
        additional_characters = " ." # caracteres que são incluídos, após o primeiro e antes do último caractere
        return random.sample(characters, size)

    def generate_random_linux_name(size):
        """
        A função retorna um nome alfanumérico aleatório.
        size: para definir o tamanho do nome.
        """
        characters = alfa_set + num_set
        return random.sample(characters, size)

    def generate_random_name(character_set, size):
        """
        a função retorna uma sequencia aleatoria de caracteres para nomear arquivos e
        diretórios
        character_set: 1 -> alfa, 2 -> num, 3 -> alfanum, 4 -> linux, 5 -> windows
        """

        name = ''
        if character_set == 'alfa':
            name = generate_random_alfa_name(size)
        elif character_set == 'num':
            name = generate_random_num_name(size)
        elif character_set == 'alfanum':
            name = generate_random_alfanum_name(size)
        elif character_set == 'linux':
        pass
    else:
        pass

    return alfa_set