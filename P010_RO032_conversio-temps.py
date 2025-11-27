#P009_RO032_conversio-temps.py
t = float(input("temperatura ="))
print(" conversio a ºC =1")
print(" conversio a ºF = 2")
conversio = int(input("prem 1 o 2 segons la conversio que vulguis fer"))

if conversio == 1:
    tc = (5/9) * (t-32)
    print (t, " ºF son " tc, "ºC")
elif conversio ==2:
    tf = 32 + (9/5) * t
    print (t, "ºC son ", tf, " ºF")
    