import copy


def check_decoding(binary_numbers_list: list) -> tuple:
    item = 0
    next_item = 0
    suffixes = []
    second_loop = False
    dekodowalny = False
    copy_of_numbers = copy.deepcopy(binary_numbers_list)
    # if len(set(binary_numbers_list)) < len(binary_numbers_list):
    #     return dekodowalny, copy_of_numbers
    while True:
        try:
            if item != next_item:
                prefix = binary_numbers_list[next_item].index(binary_numbers_list[item]) == 0
                suffix = binary_numbers_list[next_item][len(binary_numbers_list[item]):]
                if item != next_item and prefix:
                    if suffix in copy_of_numbers:
                        return dekodowalny, copy_of_numbers
                    if suffix not in suffixes:
                        suffixes.append(suffix)
        except ValueError:
            pass
        next_item += 1
        if next_item == len(binary_numbers_list):
            item += 1
            next_item = 0
        if item == len(binary_numbers_list):
            if second_loop:
                dekodowalny = True
                return dekodowalny, copy_of_numbers
            second_loop = True
            item = 0
            binary_numbers_list += suffixes
            next_item = 0


if __name__ == '__main__':
    lista = check_decoding(['111', '110', '101', '100', '011', '010', '001', '000'])
    print(lista)


