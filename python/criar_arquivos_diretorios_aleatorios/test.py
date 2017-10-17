import uuid             # gerar identificador unico
import subprocess       # chamar programa externo fsutil
import os
import binascii

import platform




#print(string.printable)

#print(binascii.b2a_hex(os.urandom(4)))

#for l in range('')
#print(string.ascii_letters)
#print(random.sample(string.ascii_letters, 8))

#print(random.SystemRandom().randint(1))

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

#print(string.punctuation)
#invalid_chars = list(set(string.punctuation) - set('\/:*?"<>|'.split()))

 #. "

# characters = string.ascii_letters + string.digits + "{['$-=};_`,!()~&+]%^@#"

# count = 1
# total_chars = 8
# name = ""
# i = 0

# while i <= 50000:
#     while count <= total_chars:
#         if count > 1 and count < total_chars:
#             name += ''.join(random.sample(characters + ". ", 1))
#         else:
#             name += ''.join(random.sample(characters, 1))

#         count += 1

#     if name[0] in " ." or name[7] in " .":
#         print(name)
#         print('encontrou')
#         break

#     print(i, name)

#     name = ""
#     count = 1
#     i += 1

#print(string.punctuation)
#print("!\"#$%&'()*+,-.:;<=>?@[\]^_`{|}~")
#s = ' '
#s = 'a'
#print(s + ''.join(random.sample(characters + ". ", 1)))
#print(s[0] in '. ')
#print(string.ascii_letters)
#str.join()
#print(string.jo(g1 - g2))
#print(invalid_chars)
#print(string.ascii_letters + string.digits)