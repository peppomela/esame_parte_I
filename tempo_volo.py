#Programma che determina la durata massima di volo conoscendo la quantia
# di carburante e il consumo orario
print"----------Tempo-di-volo----------"
strcarburante=raw_input("Carburante in galloni = ")
carburante=float(strcarburante)
strconsumo=raw_input("Consumo orario = ")
consumo=float(strconsumo)
print"---------------------------------\n"

if carburante<0:
   print"-----------Attenzione!!------------"
   print"Non puoi inserire un valore nullo!!"
   print"-----------------------------------"
elif consumo<=0:
   print"-----------Attenzione!!------------"
   print"Non puoi inserire un valore nullo!!"
   print"-----------------------------------"
else:

    temp = carburante/consumo 
    ore = int(temp)

    temp= temp - ore
    temp= temp*60 
    minuti= int(temp)

    temp= temp-minuti
    temp= temp*60
    secondi = int(temp)

print"------------Risultato------------"
print "      ",ore, "h", minuti, "min", secondi, "sec"
print"---------------------------------"

