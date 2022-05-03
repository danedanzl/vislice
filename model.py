import random

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = "0"
PONOVLJENA_CRKA = "1"
NAPACNA_CRKA = "2"

ZMAGA = "W"
PORAZ = "D"

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke 
        self.napacne = []
        self.pravilne = []

    def napacne_crke(self):
        return self.napacne

    def pravilne_crke(self):
        return self.pravilne

    def stevilo_napak(self):
        return len(self.napacne)

    def zmaga(self):
        for c in self.geslo:
            if c in self.crke:
                continue
            else:
                return False
        return True

    def poraz(self):
        if len(self.crke) > STEVILO_DOVOLJENIH_NAPAK:
            return True
        else:
            return False

    def pravilni_del_gesla(self):
        out = self.geslo
        for s in self.geslo:
            if s not in self.crke:
                out = out.replace(s, "_")
        return out

    def nepravilni_ugibi(self):
        out = ""
        for c in self.napacne:
            out += c + ", "
        return out[:-2]

    def ugibaj(self, c):
        c = c.upper()
        if c in self.crke:
            return PONOVLJENA_CRKA
        elif c in self.geslo:
            self.crke.append(c)
            self.pravilne.append(c)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(c)
            self.napacne.append(c)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


bazen_besed = []
with open("besede.txt") as f:
    for l in f:
        bazen_besed.append(l[:-1])

def nova_igra():
    geslo = random.choice(bazen_besed)
    geslo = geslo.upper()
    igra = Igra(geslo, [])
    return igra
