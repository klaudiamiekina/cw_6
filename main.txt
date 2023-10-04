from collections import OrderedDict

def count_chars(sentence):
    chars_dict = {}
    splitted_sentence = list(sentence)
    for char in splitted_sentence:
        if not char in chars_dict.keys():
            chars_dict[char] = 1
            continue
        chars_dict[char] += 1
    ordered_dict = OrderedDict(sorted(chars_dict.items(), key=lambda t: t[1]))
    return ordered_dict

sentence1 = "skocik piesek"
sentence2 = "włoski lekkoatleta specjalizujący się w biegu na 400 metrów"

print(f'zdanie: {sentence1}')
counted_dict = count_chars(sentence1)
for keys, values in counted_dict.items():
    print(f'{keys}: {values}')
print(f'Liczba elementów: {len(list(counted_dict.keys()))}')

print(f'zdanie: {sentence2}')
counted_dict = count_chars(sentence2)
for keys, values in counted_dict.items():
    print(f'{keys}: {values}')
print(f'Liczba elementów: {len(list(counted_dict.keys()))}')
