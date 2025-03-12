ukoly = []          #seznam do kterého se budou ukladat ukoly zadané uživatelem

def pridat_ukol():      # funkce na přidání úkolu uživatelem. Ukoly se přidají do seznamu ukoly
    while True:
         #přidá název úkolu
        pridat_nazev_uzivatel = input("Zadejte název úkolu: ").strip()
        if not pridat_nazev_uzivatel: 
            print ("Název úkolu je povinný údaj. Prosím zadejte název úkolu.")
            continue

        #přidá popis úkolu
        pridat_ukol_uzivatel = input ("Zadejte popis úkolu: ").strip()
        if not pridat_ukol_uzivatel:
            print ("Popis úkolu je povinný údaj. Prosím zadejte popis úkolu.")
            continue

        # přidá úkol do seznamu    
        print (f"\n Úkol {pridat_nazev_uzivatel} byl přidán.\n")
        ukoly.append ((pridat_nazev_uzivatel, pridat_ukol_uzivatel))
        break


def zobrazit_ukol ():       #funkce na zobrazení úkolu ze seznamu ukoly. Ak je seznam ukoly prázdny, informuje uzivatele.
    if not ukoly:
        print ("\n Seznam úkolů je prázdny.\n")
    else:
        print ("\n Seznam úkolů: ")
        for i, (pridat_nazev_uzivatel, pridat_ukol_uzivatel) in enumerate (ukoly, start=1):
            print (f"{i}. {pridat_nazev_uzivatel} - {pridat_ukol_uzivatel}")


def odstranit_ukol():       #funkce na odstranění úkolu ze seznamu ukoly. 
    zobrazit_ukol()
    
    try:
        if not ukoly:
            print ("\n Seznam je prázdny, tedy není možnost odstranit žádny úkol.\n")
        else: 
            odstranit_ukol_uzivatel = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            index = odstranit_ukol_uzivatel - 1

            if 0<= index < len(ukoly):
                odstranit_ukol = ukoly.pop(index) 
                print (f"Ukol {odstranit_ukol} byl odstraněn.\n")
            else:
                print ("Zadané neplatné hodnoty.")
    
    except ValueError:
        print("Chyba! Zadejte platné hodnoty.")

        
def hlavni_menu():          # funkce zobrazuje hlavní menu a přijíma uživatelove volby od 1 - 4
    while True:
        print ("\n Správce úkolů - Hlavní menu \n 1. Přidat nový úkol \n 2. Zobrazit všechny úkoly \n 3. Odstranit úkol \n 4. Konec programu")

        volba = input("\n Vyberte možnost (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukol()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print ("\nKonec programu.\n")
            break
        else:
            print ("\n Neplatná volba, zvolte možnost (1-4)\n")

hlavni_menu()