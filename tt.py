import time
import random
import string
import os

logo = ("""
   _____                         _ _      __  __ _                 
  / ____|                       (_) |    |  \/  (_)                
 | (___ _____   ___  ____ _  ___ _| | __ | \  / |_ _ __   ___ _ __ 
  \___ \_  / | | \ \/ / _` |/ __| | |/ / | |\/| | | '_ \ / _ \ '__|
  ____) / /| |_| |>  < (_| | (__| |   <  | |  | | | | | |  __/ |   
 |_____/___|\__, /_/\_\__,_|\___|_|_|\_\ |_|  |_|_|_| |_|\___|_|   
             __/ |                                                 
            |___/                                                  
""")


print (logo)
LicenseKey = input(' [*] Wprowadź klucz Licencyjny: ')
if LicenseKey == "2137-69-420":
    print("     Prawidłowy Klucz")
    time.sleep(0.5)
else:
    os.system('cls')
    print (logo)
    print("     Nieprawidłowy Klucz")
    print("     Wciśnij enter aby wyjść")
    input("")
    exit(123)
os.system('cls')
print (logo)
wallet = input(" [*] Porftel: ")
print("     Łączenie z porftelem... ")
time.sleep(1)
print("     Połączono!")

time.sleep(0.2)
os.system('cls')
print (logo)
print(f"""

[1] Używaj GPU
[2] Używaj CPU

""")
proxies = input("Czego chcesz używać do Miningu: ")
if proxies == "1":
    print("Wybrano GPU ")
else:
    print("Wybrano CPU")
os.system('cls')
time.sleep(0.2)
print("Trwa Przygotowywanie...")
time.sleep(3)
os.system('cls')
print (logo)
print(f"""

[1] BTC-USD
[2] DOGECOIN

""")
curr = input("Wybierz Walutę: ")
if curr == "1":
    def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))


    tries = 0

    while (True):
        if (tries > random.randint(100000000, 1000000000)):  # chance to get fake btc
            print("[-]"" bc1" + id_gen() + " |  ZNALEZIONO  |  " + str(round(random.uniform(0, 2), 4)), "BTC")
            print("Trwa wypłacanie na portfel...")
            time.sleep(10)
            tries = 0
            print("Sukces!")
            time.sleep(1)
        else:
            print("[-]" + " bc1" + id_gen() + " | NiePoprawne |  " + "0.0000 BTC")
            tries += 1
else:
    def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))


    tries = 0

    while (True):
        if (tries > random.randint(100000, 1000000)):  # chance to get fake btc
            print("[-]"" bc1" + id_gen() + " |  ZNALEZIONO  |  " + str(round(random.uniform(0, 2), 4)), "DGCOIN")
            print("Trwa wypłcanie na portfel")
            time.sleep(10)
            tries = 0
            print("Sukces!")
            time.sleep(1)
        else:
            print("[-]" + " bc1" + id_gen() + " | NiePoprawne |  " + "0.0000 DGCOIN")
            tries += 1
