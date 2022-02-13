from wordlistpl import wordlist
import secrets
from password_strength import PasswordStats

def createpassword():
    ile_rzutow = 5
    wynik_rzutu = []
    lista_slow = []
    ile_slow = 4
    for r in range(ile_slow):
        kostka = ''.join(str(secrets.randbelow(6) + 1) for r in range(ile_rzutow))
        wynik_rzutu.append(kostka)

    for i in wynik_rzutu:
        lista_slow.append(wordlist[i])

    twojehaslo = " ".join(lista_slow).replace(" ", "")
    return lista_slow, twojehaslo


def checkstrength(passwdstring):
    stats = PasswordStats(passwdstring)
    return stats.strength()

