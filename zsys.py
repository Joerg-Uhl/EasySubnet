

def dez_in_misc(wert, basis=2, erg = [0], z=0):
    """Wandelt eine Dezimalzahl 'wert' in eine Zahl eines beliebigen anderen
    Zahlensystems mit Basis 'basis' um.
    Input: wert = Integer; basis = Integer
    Output: Liste, jedes Element (Integer) stellt eine Stelle der neuen Zahl dar"""
    if wert >= basis:
        erg[z] = wert % basis
        z += 1
        erg += [0]
        erg[z] = wert // basis
        dez_in_misc(erg[z], basis, erg, z)
    else:
        erg[z] = wert
    return erg[::-1]


def addierer(l_wert1, l_wert2, basis=256, z=0, l = [0], uebertrag = 0):
    """Addiert 2 Zahlen aus einem beliebigen Zahlensystemen.
    Input: l_wert1, l_wert2 = Zahlen (Listen mit 1 Integer-Element pro Stelle der Zahl)
           basis = Integer (Basis des Zahlensystems)
    Output: Liste, jedes Element ist eine Stelle der Zahl"""
    if z==0:
        l_wert1=l_wert1[::-1]
        l_wert2=l_wert2[::-1]
        if len(l_wert1) > len(l_wert2):
            l_wert2.extend([0]*(len(l_wert1)-len(l_wert2)))
    if l_wert1[z] + l_wert2[z] + uebertrag > basis-1:
        l[z] = l_wert2[z] + uebertrag - (basis - l_wert1[z])
        uebertrag = 1
    else:
        l[z] = l_wert1[z] + l_wert2[z] + uebertrag
        uebertrag = 0
    if len(l_wert2) > z+1 or uebertrag:
        l += [0]
        if len(l) > len(l_wert1):
            l_wert1.append(0)
            l_wert2.append(0)
        z += 1
        addierer(l_wert1, l_wert2, basis, z, l, uebertrag)
    return l[::-1]


def bin_Addierer(bin_Adresse1, bin_Adresse2):
    bin_Adresse1 = "".join(bin_Adresse1)[::-1]
    bin_Adresse2 = "".join(bin_Adresse2)[::-1]
    ergebnis = ""
    übertrag = 0
    for i in range(32):
        if übertrag == 1:
            if bin_Adresse1[i] == "0" and bin_Adresse2[i] == "0":
                ergebnis += "1"
                übertrag = 0
            elif (bin_Adresse1[i] == "0" and bin_Adresse2[i] == "1") or (bin_Adresse1[i] == "1" and bin_Adresse2[i] == "0"):
                ergebnis += "0"
                übertrag = 1
            elif bin_Adresse1[i] == "1" and bin_Adresse2[i] == "1":
                ergebnis += "1"
                übertrag = 1
        elif bin_Adresse1[i] == "0" and bin_Adresse2[i] == "0":
            ergebnis += "0"
            übertrag = 0
        elif (bin_Adresse1[i] == "0" and bin_Adresse2[i] == "1") or (bin_Adresse1[i] == "1" and bin_Adresse2[i] == "0"):
            ergebnis += "1"
            übertrag = 0
        elif bin_Adresse1[i] == "1" and bin_Adresse2[i] == "1":
            ergebnis += "0"
            übertrag = 1
    ergebnis = ergebnis[::-1]
    ergebnis = [ergebnis[i:i+8] for i in range(0,32,8)]
    return ergebnis