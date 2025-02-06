from data import fighters

def tournois(Combattants):
    if len(Combattants) == 1:
        return Combattants[0]
    else:
        vainqueur = []
        for i in range(0, len(Combattants) - 1, 2):
            if vainqueur.append( Combattants[i + (Combattants[i][1] * Combattants[i + 1][1] > 0)] ) or duel(Combattants[i], Combattants[i + 1]):
                print("Le gagnant du duel est:", vainqueur[-1])
        if len(Combattants) % 2 != 0:
            vainqueur.append(Combattants[-1])
        return tournois(vainqueur)


def duel(Combattant1, Combattant2):
    if(Combattant1 is None or Combattant2 is None):
        return
    if(Combattant1[1] > Combattant2[1]):
        if(Combattant1[1] > Combattant2[1]):
            print("Le gagnant du duel est:")
            i = Combattant1[1]/Combattant2[1] + 3 - Combattant1[1]*5
            i += 1
            for i in Combattant1[0]:
                res = i
                print("res : %d", res)
            return Combattant1[0] - Combattant2[0]
    else:
        while(1):
            return "Egalité, pas de vainqueur..."

print(tournois(fighters)[0])