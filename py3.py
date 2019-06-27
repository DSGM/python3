import os
ContactenLijst = {}

def load():
    with open('contact.txt') as f:
        tempFile = f.read().split("\n")
        print(tempFile)
        return tempFile




def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    global menuregels
    menuregels = 0




def menu():
    clear()
    print("Uw ContactenLijst")
    print("a) Contact toevoegen")
    print("b) Contact verwijderen")
    print("c) Contactenlijst bekijken")
    print("q) Sluiten")
    keuze = input("Kies a, b, c of q: ")
    clear()
    return keuze


def ContactVerwijderen():
    clear()
    print(ContactenLijst)
    print("Als je klaar bent, type: 'done'")
    welkwoord = input("Wie wilt u verwijderen?: ")
    if (welkwoord == "done"):
        save()
        return main()
    else:
        if welkwoord in ContactenLijst:
            del ContactenLijst[welkwoord]
            return ContactVerwijderen()
        else:
            return ContactVerwijderen()


def ContactToevoegen():
    clear()
    print(ContactenLijst)
    print("Als je klaar bent, type: 'done'")
    print("Een contact toevoegen")
    Naam = input("Naam: ")
    if (Naam == "done"):
        save()
        return main()
    elif (Naam == "q"):
        quit()
    else:
        Nummer = "+31" + input("Mobile: ")
        ContactenLijst[Naam] = Nummer
        print(ContactenLijst)
        return ContactToevoegen()

def ContactenlijstBekijken():
    for key, value in ContactenLijst.items():
        print(key, value)
    print("Aantal contacten: " + str(len(ContactenLijst.keys())))
    keuze1 = input("Type done: ")
    if(keuze1 == "done"):
        main()

def save():
    for i in ContactenLijst:
        f = open("contact.txt","w+")
        f.write(str(i) + ", " + str(ContactenLijst[i]))


        
 

def main():
    keuze = menu()
    if(keuze == "q"):
        quit()
    else:
        if(keuze == "a"):
            ContactToevoegen()
        elif(keuze == "b"):
            ContactVerwijderen()
        elif(keuze == "c"):
            ContactenlijstBekijken()
        else:
            print("INCORRECT")
            return main()

main()
