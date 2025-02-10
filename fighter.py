
class Fighter:
    fighter_registry = []
    def __init__(self, nickname: str, sign: int):
        self.nickname = nickname
        self.sign = sign
        self.fighter_registry.append(self)

    def clash(self, other: "Fighter")-> "Fighter":
        if self.sign * other.sign <= 0:
            return self
        else: 
            return other
    
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
