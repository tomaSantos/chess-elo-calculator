#introdu�ao de variaveis
import sys
elox=elox1=elox2=int(input("coloque o seu elo: "))
if elox<=0:
    sys.exit("O programa nao est� preparado para pessoas sem rating")
eloatingir=int(input("que elo quer atingir? "))
difelo=int(input("insira a diferen�a de elo entre o seu advers�rio e voc� "))
idade=int(input("insira a sua idade "))
njogos=int(input("quantos jogos j� jogou? "))
jogos=jogos2=jogos3=0


if njogos<30 or (elox<2300 and idade<18):
    k=40
elif elox>2400:
    k=10
else:
    k=20

#resultado esperado
Exout=(1/(1+10**(difelo/400)))

print ("o resultado esperado ao jogar contra advers�rios", difelo , 
       "elo acima �", Exout)

#Tratamento de difelo para poder ser utilizado nos calculos seguintes
if difelo>400:
   difelo=400
if difelo<-400:
   difelo=-400    

#elo vitoria
elov=k*((1-(1/(1+(10**(difelo/400))))))
if elox<eloatingir:
    print("o elo ganho por uma vit�ria vai come�ar em,", elov)

if elox<eloatingir:
    while(elox<eloatingir):
        if njogos+jogos<30 or (elox<2300 and idade<18):
            k=40
        elif elox>2400:
            k=10
        else:
            k=20
        elox=k*((1-(1/(1+(10**(difelo/400))))))+ elox
        jogos=jogos+1
    elov=k*((1-(1/(1+(10**(difelo/400))))))
    print ("s�o necessarios", jogos,"jogos para atingir o seu elo desejado")    
    print ("depois de ganhar", jogos ,"jogos seguidos o seu elo ser�", elox)
    print ("vai estar a ganhar", elov ,"elo por vit�ria no seu ultimo jogo")

#elo derrota
if(elox2>eloatingir):
    while(elox2>eloatingir):
        if njogos+jogos3>30 or (elox1<2300 and idade<18):
            k=40
        elif elox1>2400:
            k=10
        else:
            k=20
        elox2=k*((0-(1/(1+(10**(difelo/400))))))+ elox2
        jogos3=jogos3+1
    print("Precisa de perder", jogos3 ,"jogos seguidos para atingir o seu elo desejado")

#elo empate    
if (elox1<eloatingir and difelo>0) or (elox1>eloatingir and difelo<0):
    while(elox1<eloatingir):
        if njogos+jogos2>30 or (elox1<2300 and idade<18):
            k=40
        elif elox1>2400:
            k=10
        else:
            k=20
        elox1=k*((1/2-(1/(1+(10**(difelo/400))))))+ elox1
        jogos2=jogos2+1
    print ("Pode tamb�m empatar",jogos2,"jogos seguidos para atingir o seu elo desejado")
    print ("O elo que vai atingir ap�s", jogos2 ,"empates �", elox1)

#lista
titulos= ["Candidato a Mestre","Mestre Fide","Mestre Internacional","Grande Mestre"]

if eloatingir>=2500:
    title=3
elif eloatingir>=2400:
    title=2
elif eloatingir>=2300:
    title=1
elif eloatingir>=2200:
    title=0

if eloatingir>=2200:
    print("Se atingir o seu elo desejado ir� ter alcan�ado o elo minimo necess�rio para se tornar um"
          , titulos[title])