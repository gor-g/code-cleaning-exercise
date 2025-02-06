
class Fighter:
    domain = []
    def __init__(self, nickname: str, sign: int):
        self.nickname = nickname
        self.sign = sign
        self.domain.append(self)

    def clash(self, other: "Fighter")-> "Fighter":
        if self.sign * other.sign > 0:
            return self
        else: 
            return other
    
    def __str__(self) -> str:
        return f"{self.nickname}"

    @classmethod
    def tournament(cls):
        return cls._tournament(cls.domain)

    @staticmethod
    def _tournament(fighters: list["Fighter"]):
        if len(fighters) == 1:
            return fighters[0]
        else:
            winners = []
            for i in range(0, len(fighters) - 1, 2):
                winners.append(fighters[i].clash(fighters[i + 1]))
            if len(fighters) % 2 != 0:
                winners.append(fighters[-1])
            return Fighter._tournament(winners)

