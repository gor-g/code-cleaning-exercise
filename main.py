from data import fighters
from fighter import Fighter


if __name__ == "__main__":
    for f in fighters:
        Fighter(f[0], f[1])
    print(Fighter.tournament())