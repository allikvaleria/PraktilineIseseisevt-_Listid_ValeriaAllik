#1 Sõna/Lause
#sõne=input("Sisestage sõne või lause :")
#volaali=0
#konsonanti=0

#1.1
#from string import *
#vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
#konsonanti="qwrtpsdfghjklzxcvbnm"
#markid=punctuation
#v=k=m=t=0
#tekst=input("Sisestage sõne või lause :").lower() #"ABCD"--->"abcd"
#tekst_list=list(tekst) #["a","b","c","d","!",]
#for sümbol in tekst_list:
#    if sümbol in vokaali:
#        v+=1
#    elif sümbol in konsonanti:
#        k+=1
#    elif sümbol in markid:
#        m+=1
#    elif sümbol==" ":
#        t+=1
#print("Vokaali:",v) #print("Vokaali:",v,"\nKonsonanti:",k) ---> для использования одного print
#print("Konsonanti:",k)
#print("Kirjuvahemärgid:",m)
#print("Tühikud:",t)



#2
#from random import *
#while True :
#    nimi=input("Sisesta 5 nimed :").istitle()
#    nimi_list=list(nimi)
#    nimed.append(nimi)

#2.1
nimed=[]
for i in range(5):
    nimi=input("Sisesta nimi : ").capitalize() #nimi--->Nimi
    nimed.append(nimi)

print("Loetelu oli : ",nimed) #1 var
nimed.sort() #сортировка
print("Loetelu sorteeritud : ",nimed) #2 var
for n in range(len(nimed)):
    print(n+1,".",nimed[n],sep="")
print("Vimasena oli lisatud: ",nimi)

uued_nimed=[]
for nimi in nimed:
    if nimi not in uued_nimed: #1 var
        uued_nimed.append(nimi)
print(uued_nimed)

#uued_nimed=list(set(nimed)) #2 var
