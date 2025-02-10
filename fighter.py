import random
from power import Power

class Fighter:
    fighter_registry = []
    def __init__(self, nickname: str, powers:list[Power], is_cheater:bool = False):
        self.nickname = nickname
        self.powers = powers
        self.is_cheater = is_cheater
        self.fighter_registry.append(self)

    def clash(self, other: "Fighter")-> "Fighter":
        if self.is_cheater and not other.is_cheater:
            winner = self
        elif other.is_cheater and not self.is_cheater:
            winner = other
        else:
            winner = self._clash(other)
        return winner
    
    def _clash(self, other: "Fighter")-> "Fighter":
        final_score = Power.get_3_closest_clashes_result(self.powers, other.powers)
        if final_score > 0:
            winner = self
        elif final_score < 0:
            winner = other
        else:
            winner = self if random.randint(0, 1) == 0 else other
        return winner

    def __str__(self) -> str:
        return self.nickname

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
                # automatically pass the fighter that doesn't have an opponent
                next_round_fighters.append(fighters[-1]) 
            return Fighter._tournament(next_round_fighters)
