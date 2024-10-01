from math import sqrt

#### Fonction secondaire


def isprime(p):
    pass
    for d in range(2, int(sqrt(p)+1)):
        if p % d == 0:
            return False
        else:
            return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        t= isprime(n)
        print(f"({n},{t})", end=" ")

if __name__ == "__main__":
    main()
