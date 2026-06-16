
class Konto:
    #Det körs när man skapa ett nytt konto. Vi ger det ett nummer och startarsaldo 0 kr 
    def __init__(self, kontonummer, saldo=0):
        self.kontonummer = kontonummer
        self.saldo = saldo
        
    #Metoden för att lägga in penga i kontot
    def deposit(self, belopp):
        if belopp <= 0:
            print("Du kan inte satsa in 0 eller mindre.")
        elif belopp > 1_000_000:
            #beloppet kan inte vara mer än 1,000,000
            print("Beloppet är för stor! Max insättning är 1 000 000kr.")
        else:
            #Om beloppet funkar bra ökar vi saldot
            self.saldo =  self.saldo + belopp
            print(f"Insättning lyckades. Nytt saldo:{self.saldo} kr")
    
    #Metoden för att ta ut pengar
    def withdraw(self, belopp):
        if belopp <= 0:
            print("felbelopp! Du kan inte ta ut 0 kr")
        elif belopp > self.saldo:
             print("Otillräckligt saldo! Du kan inte ta ut mer än du har.")
        else:
            self.saldo =  self.saldo - belopp 
            print(f"Uttag lyckades. Nytt saldo: {self.saldo} kr")
            
    def add_interest(self, interest_rate):
        count_interest = self.saldo * (interest_rate / 100)
        
        self.saldo = self.saldo + count_interest

        

class Bank:
    def __init__(self):
        self.konton = {} #Skapa en tomlista för att spara alla konto
        self.räknare = 1      
        
    def pay_interest_to_all(self):
        if not self.konton:
            print("Det finns inte konton att betala ut ränta till")
            return
        
        fixed_interest = 2
        
        for konto in self.konton.values():
            konto.add_interest(fixed_interest)
            
        print(f"Ränteutbetalning klar! {fixed_interest}% ränta har lagts till på alla konton")
        
    def meny_loop(self):
        nytt_kontonummer = self.räknare  #Här skapar programmet det allra första kontot automatiskt vid start
        self.konton[nytt_kontonummer] = Konto(nytt_kontonummer, 0)
        self.räknare += 1
        print("Välkommen till banksystem")

        kör = True       #Variabeln för att hålla igång meny loop

        #Loopen som kör ända tills anvöndare väljer avsluta
        while kör:
            print("\n--- BANKSYSTEM ---")
            print("1. Skapa nytt konto")
            print("2. Sätt in pengar")
            print("3. Ta ut pengar")
            print("4. Visa saldo")
            print("5. Betala ut ränta till alla konton")
            print("6. Avslutar")
            
            try:
                val = int(input("Välj alternative (1-6): ")) # Läser in användare val
           
                if val == 1:
                    nytt_kontonummer = self.räknare 
                    self.konton[nytt_kontonummer] = Konto(nytt_kontonummer, 0)  
                    self.räknare = self.räknare + 1
                    print(f"Konto skapat, nummer: {nytt_kontonummer}")  
               
                elif val == 2:
                    kontonummer = int(input("Ange kontonummer: "))
                    if kontonummer in self.konton:
                        konto = self.konton[kontonummer]
                        belopp = int(input("Ange belopp att sätta in: "))
                        konto.deposit(belopp)
                    else:
                        print("Kontot finns inte.")
                        
                elif val == 3:
                    kontonummer = int(input("Ange kontonummer: "))
                    if kontonummer in self.konton:
                        konto = self.konton[kontonummer]
                        belopp = int(input("Ange belopp att ta ut: "))
                        konto.withdraw(belopp)
                    else:
                        print("Kontot finns inte")
                        
                elif val == 4:
                    kontonummer = int(input("Ange kontonummer: "))
                    if kontonummer in self.konton:
                        konto = self.konton[kontonummer]
                        print(f"Saldo för konto {kontonummer}: {konto.saldo:.2f} kr")
                    else:
                        print("Kontot finns inte.")
                        
                elif val == 5:
                    self.pay_interest_to_all()

                elif val == 6:
                    kör = False
                    print("Tack för att du använde Banksystem!")
                    
                else:
                    print("Ogiltigt val, välj en siffra mellan 1 och 6.")

            # HÄR ÄR DET VIKTIGA SOM SAKNAS LÄNGST NER!
            # Detta måste ligga på samma indrags-linje som ordet "try"
            except ValueError:
                print("Fel: Du måste skriva en siffra! Försök igen.")
                
#Startar hela programmet genom Banken
if __name__ == "__main__":
    min_bank = Bank()  # Skapar banken
    min_bank.meny_loop()  # Startar menyn