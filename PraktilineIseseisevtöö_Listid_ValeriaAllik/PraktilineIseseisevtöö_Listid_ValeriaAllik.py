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

##2.3
#vanused=[]
#for i in range(5):
#    vanus=int(input("Sisesta vanus : "))
#    vanused.append(vanus) #
#maksimum=max(vanused)
#minimum=min(vanused)
#summa=sum(vanused)
#keskmine=summa/len(vanused)
##Kuva ekraanile nimi koos vanusega
#for i in range(5):
#    print(nimed[i], "on" , vanused[i], "aastat vana")


#3 Tärnid
#from random import *
#arvud=[]
#N=int(input("Mitu rida joonistamine? :"))
#S=input("Sisesta sümbol :")
##loendi täitmine
#for p in range(N):
#    arvud.append(randint(1,100))
##diagrammi loomine
#for p in range(N):
#    print(arvud[p]*S)


#4 Postiindex
#Indeksid=[" Tallinn" , "Narva, Narva-Jõesuu" ,"Kohtla-Järve" , "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa" , "Tartu linn" ,"Tartumaa, Põlvamaa, Võrumaa, Valgamaa" , "Viljandimaa, Järvamaa, Harjumaa, Raplamaa" ,"Pärnumaa" , "Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    while True:
#        try:
#            indeks=int(input("Sisesta ima indeks :")) #10000,15478,98564
#            #if 1000<=indeks<=99999:
#            indeks_elementide_arv=len(str(indeks))
#            if indeks_elementide_arv==5:
#                print("5nubriline indeks")

#            else:
#                print("On vaja 5numbriline arv(indeks)")

#    #            break
#        except:
#            print("Vale andmetüüp!")
#    arv1=indeks//10000
#    print(arv1)
#    symbolid=list(str(indeks))
#    print(f"Sa elad piirkonnas {Indeksid[int(symbolid[0])-1]}")
    #sym1=symbolid[0]
    #print(sym1)
    #if indeks==1:
   


from random import *
from string import *
#5 Vahetus
rida=[]
N=randint(2,15)
for i in range(N):
    rida.append(choice(ascii_uppercase))
print(rida)
kogus=int(input("Mitu elemendi vahetame oma vahel "))
if len(rida)//2>=kogus:
    for i in range(kogus):
        a=rida[i]
        rida[i]=rida[len(rida)-i-1]
        rida[len(rida)-1-i]=a
print (rida)


#6 Бесполезные числа
from random import *
N=int(input("Sisesta num :"))
nimekirja=[]
for i in range(N):
    arv=randint(10,100)
    nimekirja.append(arv)
maksimum=nimekirja[0]
for arv in nimekirja:
    if arv>maksimum:
        maksimum=arv
        kasutud_numbrid=maksimum/len(nimekirja)
for i in range(len(nimekirja)):
    if nimekirja[i]==maksimum:
        nimekirja[i]=kasutud_numbrid
print("Esialgne nimekiri:"+str(nimekirja))
