# solitario4re

Progetto del Solitario dei Quattro Re.

Il programma potrà svolgere due tipi di attività, a seconda dell'opzione specificata nell'argparse iniziale. 
Input da terminale: --psingola 'True': se si vuole fare una partita singola.  
                    --psingola 'False': (impostato di default) se si vuole calcolare la probabilità di vittoria. 

-La prima attività prevede lo svolgimento di una partita utilizzando un mazzo importato da un file di testo, preceduto dalla verifica dell'integrità del mazzo e 
 della correttezza di seme e valore della singola carta. le righe del file che non rispettano la sintassi fornita dalla specifica vengono ignorate dal codice (Valore,Seme).
 Un mazzo verrà considerato nullo se, dopo il controllo successivo all'importazione del file di testo, non contenie le 40 carte previste dal regolamento.
  
  Ad esempio, viene fornito il seguente mazzo: 

  -1,3
  -4,D
  -8,ohjhk
  -//commento. 

  L'insieme di carte utilizzabili contiene solo il 4 di denara. Il programma verrà interrotto per invalidità del mazzo fornito.
  L'utente può selezionare in input da terminale il path del file contenente il mazzo specificando: --psingola 'True' --mazzo 'path del file'


-La seconda attività prevede il calcolo della probabilità di vittoria nel solitario dei 4 re. Di default vengono giocate 1000 per 100 volte al fine di calcolare
 la la probabilità di vittoria media con il relativo intervallo di confidenza.

 
 
Sono presenti 8 casi di test, divisi in 3 casi vincenti, 3 casi perdenti, 1 caso di mazzo contenente errori ma comunque utilizzabile
e 1 caso di mazzo contenente errori ma non utilizzabile in quanto non completo. La corrispondenza seme-riga è fissa e uguale per ogni caso.
I casi di test sono posizionati nella cartella Custom_Test_Cases.



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

 
OUTPUT:

-Nel caso si voglia giocare una partita singola il programma stampa il mazzo e l'esito della partita. Se il mazzo caricato non è completo stampa un avviso.

-Nel caso si voglia calcolare la probabilità il programma stampa la probabilità di vettoria media con il relativo intervallo di confidenza.
