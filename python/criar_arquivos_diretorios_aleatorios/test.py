def print_msg(msg, attempts):

    if attempts < 3:
        print(msg)
        return print_msg(msg, attempts + 1)


print_msg('ola', 0)

