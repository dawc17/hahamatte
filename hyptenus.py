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

def main():
    print("Beregning av hypotenus i en rettvinklet trekant")
    print("=" * 45)
    
    try:
        # Be brukeren om input
        katet1 = float(input("Skriv inn lengden på den første kateten: "))
        katet2 = float(input("Skriv inn lengden på den andre kateten: "))
        
        # Sjekk at verdiene er positive
        if katet1 <= 0 or katet2 <= 0:
            print("Feil: Begge katetene må være positive tall.")
            return
        
        # Beregn hypotenusen
        hypotenus = beregn_hypotenus(katet1, katet2)
        
        # Vis resultatet
        print(f"\nResultat:")
        print(f"Katet 1: {katet1}")
        print(f"Katet 2: {katet2}")
        print(f"Hypotenus: {hypotenus:.2f}")
        
        # Vis også utregningen
        print(f"\nUtregning:")
        print(f"c² = {katet1}² + {katet2}²")
        print(f"c² = {katet1**2} + {katet2**2}")
        print(f"c² = {katet1**2 + katet2**2}")
        print(f"c = √{katet1**2 + katet2**2}")
        print(f"c = {hypotenus:.2f}")
        
    except ValueError:
        print("Feil: Vennligst skriv inn gyldige tall.")
    except Exception as e:
        print(f"En uventet feil oppstod: {e}")

if __name__ == "__main__":
    main()