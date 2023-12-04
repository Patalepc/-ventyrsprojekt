import random as rand


class Bandage:
    def __init__(self):
        self.name = "Bandage"
        self.hp = 10


def main():
    hjältenamn = "P & H"
    hjältehp = 10
    hjältestyrka = rand.randint(0, 10)

    while hjältehp > 0:
        print(
            """
            Välkommen till Äventyrsspelet!

            Vad vill du göra?
            1. Välj dörr
            2. Kolla ryggsäck
            3. Kolla stats
            """
        )

        val = input("")

        if val == "1":
            hjältehp, hjältestyrka = hantera_vald_dörr(
                hjältenamn, hjältehp, hjältestyrka
            )
            print(hjältehp)
        elif val == "2":
            pass  # Implementera logik för att kolla ryggsäcken
        elif val == "3":
            pass  # Implementera logik för att kolla stats
        else:
            print("Välj 1, 2 eller 3!")


def hantera_vald_dörr(hjältenamn, hjältehp, hjältestyrka):
    print("Du står framför tre dörrar.")
    print("Bakom en dörr kan det finnas en belöning, bakom en annan ett monster.")

    vald_dörr = rand.randint(1, 3)

    gissning = int(input("Välj en dörr (1, 2 eller 3): "))

    if gissning == vald_dörr:
        print("Grattis! Du hittade en skatt!")
        skattkista = ["bandage", "svärd"]
        skatt = rand.choice(skattkista)

        if skatt == "bandage":
            bonus_hp = 1.5
            print(
                f"Du fick ett bandage och hjälpte dig själv från {hjältehp} till {hjältehp + bonus_hp}!"
            )
            hjältehp = hjältehp + bonus_hp

        elif skatt == "svärd":
            bonus_styrka = 2
            print(
                f"Du fick ett svärd och höjde din styrka från {hjältestyrka} till {hjältestyrka + bonus_styrka}"
            )
            hjältestyrka = hjältestyrka + bonus_styrka

    else:
        print("Det var ett monster! Du tar skada.")
        skada = rand.randint(1, 5)
        hjältehp -= skada
        print(f"{hjältenamn} har nu {hjältehp} hälsa kvar.")

    return hjältehp, hjältestyrka


if __name__ == "__main__":
    main()
