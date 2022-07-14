# importa dependencias
from random import randint

# cria lista de avaliações aleatórias
reviews = [randint(1, 10) for i in range(5)]
print('Lista de avaliações:\n',reviews)

# assigna um rating segundo critério
def popularityRating(n_rev):
    if n_rev == 0:
        rating = 'New'
    elif n_rev >= 1 and n_rev <= 5:
        rating = 'Rising'
    else:
        rating = 'Trading Up'
    return rating

# visualiza a lista de rating
ratings = list(map(popularityRating, reviews))
print('Lista de ratings respectivas:\n', ratings)
