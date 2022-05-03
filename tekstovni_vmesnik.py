import model

def izpis_igre(igra):
    return igra.pravilni_del_gesla() + '\n' + "napačne črke: " + igra.nepravilni_ugibi()

def izpis_zmage(igra):
    return "ded je zmago" + '\n' + f"beseda je bila {igra.geslo}"

def izpis_poraza(igra):
    return "ded je zgubo" + '\n' + f"beseda je bila {igra.geslo}"

def zahtevaj_vnos(igra):
    c = input("Ugibaj: ")
    while(len(c) != 1 or not c.isalpha()):
        print("neveljaven vnos - poskusi ponovno")
        c = input("Ugibaj: ")
        
    return c

def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while(True):
        crka = zahtevaj_vnos(igra)
        ugib = igra.ugibaj(crka) 
        if ugib == model.ZMAGA:
            vun = izpis_zmage(igra)
            print(vun)
            break
        elif ugib == model.PORAZ:
            vun = izpis_poraza(igra)
            print(vun)
            break
        else:
            vun = izpis_igre(igra)
            print(vun)

pozeni_vmesnik()
