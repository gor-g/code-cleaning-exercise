import random


class Fighter:
    fighter_registry = []
    def __init__(self, nickname: str, pouvoirs):
        self.nickname = nickname
        self.sign = pouvoirs
        self.fighter_registry.append(self)

    def clash(self, other: "Fighter")-> "Fighter":

        resultats = []
        for p in self.sign:
            print(p)
            for pp in other.sign:
                print(pp)
                result = abs(p[2+0] - pp[2+2]) + \
                abs(p[2+1] - pp[2+0]) + \
                abs(p[2+2] - pp[2+1]) - \
                abs(pp[2+0] - p[2+2]) - \
                abs(pp[2+1] - p[2+0]) - \
                abs(pp[2+2] - p[2+1])
                resultats.append(result)# ; duel(self, other)
        
        
        resultats.sort(key=abs)
        score = sum(resultats[:min(3, len(resultats))])
        
        if score > 0:
            winner = self
        elif score < 0:
            winner = other
        else:
            winner = self if random.randint(0, 1) == 0 else other
        
        return winner
    
    def __str__(self) -> str:
        return f"{self.nickname}"

    @classmethod
    def tournament(cls)-> "Fighter":
        return cls._tournament(cls.fighter_registry)

    @staticmethod
    def _tournament(fighters: list["Fighter"])->"Fighter":
        if len(fighters) == 1:
            return fighters[0]
        else:
            next_round_fighters = []
            for i in range(0, len(fighters) - 1, 2):
                next_round_fighters.append(fighters[i].clash(fighters[i + 1]))
            if len(fighters) % 2 != 0:
                next_round_fighters.append(fighters[-1]) # automatically pass the fighter that doesn't have an opponent
            return Fighter._tournament(next_round_fighters)

def duel(fighter1, fighter2) -> str:
    if fighter1 not in fighters or fighter2 not in fighters:
        return "Un des combattants n'est pas valide."
    
    score1, score2 = fighters[fighter1], fighters[fighter2]
    
    if score1 > score2:
        return f"{fighter1} remporte le duel !"
    elif score2 > score1:
        return f"{fighter2} remporte le duel !"
    else:
        return "Match nul !"
