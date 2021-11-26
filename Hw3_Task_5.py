import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    """ Random jokes """
    jokes = []
    for i in range(num):
        i_nouns = random.choice(nouns)
        i_adverbs = random.choice(adverbs)
        i_adjectives = random.choice(adjectives)
        jokes.append(f'{i_nouns} {i_adverbs} {i_adjectives}')
        return jokes


print(get_jokes(1))
print(get_jokes(2))
print(get_jokes(3))
