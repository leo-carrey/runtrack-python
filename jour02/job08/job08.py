def nouriture(type,saison):
    if type == 'fruits':
        if saison == 'hiver':
            return 'orange, mandarine et kiwi'
        elif saison == 'ete':
            return 'Poire, fraise, cassis'
    elif type == 'legume':
        if saison == 'hiver':
            return 'carotte, topinambour, endive'
        elif saison == 'ete':
            return 'artichaut, aubergine,navet'

print(nouriture('fruits','hiver'))
print(nouriture('legume','ete'))