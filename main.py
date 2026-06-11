from account import Konto

print("Välkommen till banksystem")

konton =  {}
räknare = 1

nytt_kontonummer = räknare
nytt_konto = Konto(nytt_kontonummer, 0)
konton[nytt_kontonummer] = nytt_konto
räknare += 1
print(f"Konto skapat, nummer:  {nytt_kontonummer}")


