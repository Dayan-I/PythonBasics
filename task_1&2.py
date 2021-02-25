# первое задание, достаточно просто делается, с помощью ветвления
def num_translate():
    n = input("Enter number in english :")
    nums_translation = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                        'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if n in nums_translation.keys():
        print(nums_translation[n])
    else:
        print(None)


num_translate()


# второе задание
def num_translate_adv():
    n = input("Enter number in english :")
    nums_translation = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                        'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if n.lower() in nums_translation.keys() and n[0].isupper():  # здесь надо перевести n в нижний регистр, проверить на
        print(nums_translation[n.lower()].capitalize())  # наличе в ключах словаря  и чтобы первая буква была большая, вывод с большой буквы
    elif n in nums_translation.keys():
        print(nums_translation[n])
    else:
        print(None)


num_translate_adv()
