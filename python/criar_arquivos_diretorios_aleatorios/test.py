import uuid             # gerar identificador unico
import subprocess       # chamar programa externo fsutil
import os
import binascii

def generate_random_name():
    """
        a função retorna uma sequencia aleatoria de caracteres
    """
    return uuid.uuid4().hex[0:8]


# dirs = []

# start_level = 0
# final_level = 3
# dir_count = 2

# base_dir = os.getcwd()
# output_dir = os.path.join(base_dir, 'saida')

# for level in range(start_level, final_level):
#     len_dir_a = len(dir_a)
#     if len_dir_a == 0:
#         for j in range(0, dir_count):
#             dir_a.insert(0, os.path.relpath(generate_random_name(), output_dir))
#     else:
#         dirs_a_temp = []
#         for j in dir_a:
#             for k in range(0, dir_count):
#                 dir_a_temp.insert(0, os.path.join(j, generate_random_name()))

#         dir_a.clear()
#         dir_a = dir_a_temp[:]


#print(dir_a)
#print(dir_a_temp)

print(binascii.b2a_hex(os.urandom(4)))
