from data import fighters, cheaters
from fighter import Fighter
from power import Power


if __name__ == "__main__":
    for f in fighters:
        Fighter(f[0], list(map(lambda p: Power(p[0], p[1], p[2], p[3], p[4]), f[1])), f[0] in cheaters)
    print(Fighter.tournament())