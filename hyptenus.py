import math

def beregn_hypotenus(katet1, katet2):
    """
    Beregner hypotenusen i en rettvinklet trekant
    ved hjelp av Pytagoras' læresetning: c² = a² + b²
    
    Args:
        katet1 (float): Den første kateten
        katet2 (float): Den andre kateten
    
    Returns:
        float: Hypotenusen
    """
    hypotenus = math.sqrt(katet1**2 + katet2**2)
    return hypotenus

def beregn_katet(katet1, hypotenus):
    """
    Beregner den andre kateten i en rettvinklet trekant
    ved hjelp av Pytagoras' læresetning: b = sqrt(c² - a²)

    Args:
        katet1 (float): Den kjente kateten
        hypotenus (float): Hypotenusen

    Returns:
        float: Den ukjente kateten

    Raises:
        ValueError: Hvis input ikke er gyldige (ikke-positive eller hypotenus <= katet1)
    """
    # validate inputs
    if katet1 <= 0 or hypotenus <= 0:
        raise ValueError("Both katet and hypotenuse must be positive numbers.")
    if hypotenus <= katet1:
        raise ValueError("Hypotenuse must be greater than the known katet.")

    return math.sqrt(hypotenus**2 - katet1**2)

def main():
    print("Beregning av en rettvinklet trekant")
    print("=" * 45)

    try:
        valg = input("Velg beregning: (1) Hypotenus fra to kateter, (2) Katet fra katet og hypotenus [1/2]: ").strip()

        if valg == "1":
            katet1 = float(input("Skriv inn lengden på den første kateten: "))
            katet2 = float(input("Skriv inn lengden på den andre kateten: "))

            if katet1 <= 0 or katet2 <= 0:
                print("Feil: Begge katetene må være positive tall.")
                return

            hypotenus = beregn_hypotenus(katet1, katet2)

            print(f"\nResultat:")
            print(f"Katet 1: {katet1}")
            print(f"Katet 2: {katet2}")
            print(f"Hypotenus: {hypotenus:.2f}")

            print(f"\nUtregning:")
            print(f"c² = {katet1}² + {katet2}²")
            print(f"c² = {katet1**2} + {katet2**2}")
            print(f"c² = {katet1**2 + katet2**2}")
            print(f"c = √{katet1**2 + katet2**2}")
            print(f"c = {hypotenus:.2f}")

        elif valg == "2":
            katet1 = float(input("Skriv inn lengden på den kjente kateten: "))
            hypotenus = float(input("Skriv inn lengden på hypotenusen: "))

            if katet1 <= 0 or hypotenus <= 0:
                print("Feil: Verdiene må være positive tall.")
                return
            if hypotenus <= katet1:
                print("Feil: Hypotenusen må være større enn den kjente kateten.")
                return

            katet2 = beregn_katet(katet1, hypotenus)

            print(f"\nResultat:")
            print(f"Kjent katet: {katet1}")
            print(f"Hypotenus: {hypotenus}")
            print(f"Manglende katet: {katet2:.2f}")

            print(f"\nUtregning:")
            print(f"c² = {hypotenus}²")
            print(f"a² = {katet1}²")
            print(f"b² = c² - a² = {hypotenus**2} - {katet1**2} = {hypotenus**2 - katet1**2}")
            print(f"b = √{hypotenus**2 - katet1**2}")
            print(f"b = {katet2:.2f}")

        else:
            print("Ugyldig valg. Avslutter.")

    except ValueError:
        print("Feil: Vennligst skriv inn gyldige tall.")
    except Exception as e:
        print(f"En uventet feil oppstod: {e}")

if __name__ == "__main__":
    main()