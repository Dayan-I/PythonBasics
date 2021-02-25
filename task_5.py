from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n=int(input('Enter nuber of jokes :')),
              y=(input('Enter Yes if any word can be used more than one time :'))):
    """Creates n jokes taking a one element from noun, adverbs and adjectives """
    new_list = list()
    if y == 'Yes':
        for i in range(n):
            joke = (choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives))
            new_list.append(joke)
    else:
        for i in range(n):
            joke = (choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives))
            to_expect = joke.split(' ')
            nouns.remove(to_expect[0])
            adverbs.remove(to_expect[1])
            adjectives.remove(to_expect[2])
            new_list.append(joke)

    print(new_list)


get_jokes()
