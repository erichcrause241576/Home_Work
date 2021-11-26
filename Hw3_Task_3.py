
def thesaurus(*names):
    abbreviation = dict()
    for name in names:
        abbreviation .setdefault(name[0], [])
        abbreviation[name[0]].append(name)
    return abbreviation


print(thesaurus("Александр", "Сергей", "Екатерина"))

