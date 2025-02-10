class Power:
    def __init__(self, nom, description, strength, agility, magic):
        self.name = nom
        self.description = description
        self.strength = strength
        self.agility = agility
        self.magic = magic
    
    def clash(self, other: "Power")->int:
        result = abs(self.strength - other.magic) + \
        abs(self.agility - other.strength) + \
        abs(self.magic - other.agility) - \
        abs(other.strength - self.magic) - \
        abs(other.agility - self.strength) - \
        abs(other.magic - self.agility)
        return result
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description} \n (strength : {self.strength}, agility : {self.agility}, magic : {self.magic})"

    def __repr__(self) -> str:
        return f"(\"{self.name}\", \"{self.description}\", {self.strength}, {self.agility}, {self.magic})"

    @staticmethod
    def get_3_closest_clashes_result(power_list1: list["Power"], power_list2: list["Power"])->int:
        """return the result of the 3 or less(if there is less than 3) clashes the output of 
        which have the smallest absolute value. It is based on the supposition that the players will use
        the most optimal power to counter the adversery's power."""

        power_clash_score_list = []
        for power_of_self in power_list1:
            for power_of_other in power_list2:
                power_clash_score_list.append(
                    power_of_self.clash(power_of_other)
                    )

        power_clash_score_list.sort(key=abs)
        final_score = sum(power_clash_score_list[:min(3, len(power_clash_score_list))])

        return final_score
        