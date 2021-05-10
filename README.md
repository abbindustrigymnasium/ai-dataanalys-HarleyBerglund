# ai-dataanalys-HarleyBerglund
ai-dataanalys-HarleyBerglund created by GitHub Classroom


# AI-Dataanalys

## Table of Contents

- [AI-Dataanalys](#ai-dataanalys)
  - [Table of Contents](#table-of-contents)
- [AI Bootcamp](#ai-bootcamp)
  - [Inledning](#inledning)
  - [Algoritmic Trading](#algoritmic-trading)
      - [Chapter 1](#chapter-1)
      - [Chapter 2](#chapter-2)
  - [Knearest Neighbour](#knearest-neighbour)
  - [Perceptron](#perceptron)
  
- [Projekt Vägmärken](#projekt-vägmärken)
  - [Bakgrund Projekt](#bakgrund-projekt)
  - [Process](#process)
  - [Resultat](#resultat)
  - [Utmaningar](#utmaningar)
- [TrainData](#traindata)


# AI-Bootcamp
## Inledning
Här ligger allt meterial som jag har jobbat med under lektionstid. Det första är Algoritmic Trading, där jag har läst och jobbat i ett dokument som jag fick av Jocke. Jag har även testat att koda lite olika strategier (mer om det under Chapter 1 och Chapter 2). Sedan kommer lite om Knearest Neighbour och Perceptron. 


## Algoritmic Trading
info om algoritmic trading

### [Chapter 1]
Algoritmisk aktiehandel eller automatiserad aktiehandel, fungerar genom att ett program som innehåller en uppsättning av
instruktioner för handelsändamål. Jämfört med en mänsklig aktiehandlare kan denna handel generera
vinster och förluster i högre hastighet. Det här kapitlet handlade om:

Varför handlar vi?
- Introduktion av algoritmhandel och automatisering
- Vad är de viktigaste handelskomponenterna
- Ställa in din första programmeringsmiljö
- Implementera din första inbyggda strategi

### [Chapter 2]
I detta kapitel gick jag igenom några populära metoder för teknisk analys och använde
dessa för att analysera marknadsdata. Jag utförde grundläggande algoritmisk aktiehandel
med hjälp av marknadstrender, stöd och resistens.

Detta kapitel handlade om:

- Designa en handelsstrategi baserad på trend- och momentumbaserade indikatorer. 
- Skapa handelssignaler baserat på grundläggande teknisk analys. 
- Implementering av avancerade koncept, som säsongsvariationer, i handelsinstrument.

## Knearest Neighbour
Här gjode jag 2 olika knearest neighbour pythonscrips, en grundläggande och en annan som gissade vad olika politiker skulle rösta. 
## Perceptron
Här skapade jag en perceptron, som är en del av ett neuralt nätverk. Jag använde mig av javascript-biblioteket P5 för detta. 


# Projekt Vägmärken
## Bakgrund projekt
Bakrunden till mitt projekt är att jag för inte så länge sedan tog körkort och märkte att det ibland kunde vara svårt att förstå och framför allt summera skyltars betydelse. Det jag tänker mest på då är parkeringsskyltar och hur olika tidsregler och betalningsrekler väldigt ofta är svåra att tyda. Och när jag tänkte lite mer på det här kom jag på den idé, nämligen en app där man kunde skanna av vägskyltar och få en skriftlig förklaring på skyltarnas betydelse. Denna app skulle kunna förenkla för nya förare, men även till exempel om du kommer från ett annat land och ska köra i Sverige. 

## Process
Beskrivning av processen

## Resultat
Hur blev då resultatet av mitt projekt?

Man kan börja med att säga att det inte riktigt gick som jag tänkt och planerat ([Utmaningar](#utmaningar)), men jag är fortfarande ganska nöjd med det jag har åstadkommit. Tanken till en början var att hinna med att utveckla någon form av app som man kunde använda för att skanna skyltar med mobiltelefon. Detta var kanske lite väl optimistiskt eftersom vi bara hade ca 12h arbetestid. Man underskattar lätt hur lång tid själva datainsamlingen egentligen tar. 

Jag lyckades med att:

- samla in ett bra urval av bilder från internet.
- konvertera dessa bilder så att jag kunde köra dem genom annotation_tool så att man senare kan genomföra träning. 
- konvertera txt-filerna som man får från annotation_tool till XML format.
- få Yolo att fungera och använda kameran på datorn för att testa med. 

Det jag har kvar/vill göra: 

- Träna vikterna i Google Colab.
- Utveckla en app som kan skanna av skyltarna. 
- Sammla ännu fler bilder och ta egna från lite fler vinklar och avstånd. 
- I framtiden kunna addera skyltars betydelse till en sammanhängande text (exempel parkeringsskylt och huvudled)



## Utmaningar
Vilka utmaningar stötte jag på? 

Som jag tidigare nämnt var det svårt och tidskrävande att hitta bilder som mötte kraven. 

Den största utmaningen jag stötte på, som också slukade den största delen av min tid var träningen i Google Colab. Jag tyckte att jag hade alla filer som behövdes för att göra detta, och det hade jag också. Men det som satte stop för mig var att själva skriptet var uttaterat, dvs att vissa bibliotek inte fungerade likadant som de gjorde för ett år sedan då detta script gjordes. 


# TrainData
Här ligger den datan som jag ska träna min yolo med. Dvs bilderna, annotations i XLM format och startfilen som heter roadsigns.json

