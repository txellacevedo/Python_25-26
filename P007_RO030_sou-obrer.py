#P007_RO030_sou-obrer.py
hores = float(input("hores = "))
preu_hora =float (input("preu per hora = "))
reduccions = float (input("reduccins = "))


if hores ==40:
    sou_setmana = (preru_hora * hores) - reduccions
else:
    sou_setmana = (preu_hora * 40) - reduccions + (1.5 * preu_hora * (hores - 40))

                  
                  