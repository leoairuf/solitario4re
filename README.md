# solitario4re

Progetto del Solitario dei Quattro Re.

Il programma potrà svolgere due tipi di attività, a seconda dell'opzione specificata nell'argparse iniziale.  

-La prima attività prevede il calcolo della probabilità di vittoria nel solitario dei 4 re.
-La seconda attività prevede lo svolgimento di una partita utilizzando un mazzo importato da un file di testo, preceduto dalla verifica dell'integrità del mazzo e 
 della correttezza di seme e valore della singola carta.   
 
 
Saranno pubblicati dei casi di test: i casi di test saranno 8, divisi in 3 casi vincenti, 3 casi perdenti, 1 caso di mazzo contenente errori ma comunque utilizzabile
e 1 caso di mazzo contenente errori ma non utilizzabile. La corrispondenze seme-riga è fissa e uguale per ogni caso.
Verranno posizionati nella cartella Custom_Test_Cases.


-L'utente può abilitare una delle due attività; nel caso della prima, può scegliere la modalità di accoppiamento seme-riga tra tre opzioni (fissa,dinamica,casuale) mediante
 una stringa in input che specifica le regole desiderate e constatare che la scelta non influisce sulla probabilità di vittoria. Nel caso della seconda funzionalità deve fornire
 un file di testo, contenente un mazzo di carte napoletane: le righe del file che non rispettano la sintassi fornita dalla specifica vengono ignorate dal codice (Valore,Seme).
 Un mazzo verrà considerato nullo se, dopo il controllo successivo all'importazione del file di testo, non contenga le 40 carte previste dal regolamento. 

Ad esempio, viene fornito il seguente mazzo: 


-1,3

-4,D

-8,ohjhk

-//commento. 


L'insieme di carte utilizzabili contiene solo il 4 di denara. Il programma verrà interrotto per invalidità del mazzo fornito.


-Nella cartella Results si possono trovare informazioni di carattere generale relative al codice: i 4 file di testo presenti contengono informazioni riguardanti alcune 
 simulazioni condotte, mentre i 3 file PNG sono grafici ottenuti con i dati delle simulazioni.

SIMULAZIONI CONDOTTE:

-Dati_Simulazione_Probabilità_NoIncremento --> 1000 simulazioni da 50000 partite ciascuna: viene calcolata la probabilità di vittoria per ogni ciclo.

-Simulazione_Prob_Incrementata --> 10000 simulazioni da 100 + K x 50 partite (K = 1,2...10000): partendo da una prima simulazione da 100 partite, viene calcolata la probabilità
 di vittoria e poi incrementato il numero di partire del ciclo successivo di 50.

-Simulazione_Tempi_LISTE --> 1000 simulazioni da 1000 partite utilizzando le liste: viene calcolato il tempo di esecuzione per ogni ciclo.

-Simulazione_Tempi_NP --> 1000 simulazioni da 1000 partite utilizzando Numpy: viene calcolato il tempo di esecuzione per ogni ciclo. 
	 
GRAFICI OTTENUTI:

-Convergenza --> grafico ottenuto dai dati contenuti in Dati_Simulazione_Probabilità_NoIncremento.

-Convergenza_Incremento --> grafico ottenuto dai dati contenuti in Simulazione_Prob_Incrementata.

-ParagoneNPL --> grafico che confronta i dati ottenuti da Simulazione_Tempi_LISTE e Simulazione_Tempi_NP. (i tempi sono calcolati in secondi) 

 