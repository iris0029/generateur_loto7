import random
def generateur_loto7_la_semaine(liste=None):
    if liste is None:
        liste = []
    liste.extend５([random.randint(0,9) for i in range(7)])
    return liste

for i in range(7):
    print(generateur_loto7_la_semaine())
