# solitario4re

Progetto del Solitario dei Quattro Re.
Il programma potrà svolgere due tipi di attività, a seconda dell'opzione specificata nell'argparse iniziale.  

-La prima attività prevede il calcolo della probabilità di vittoria nel solitario dei 4 re, e la creazione di un grafico raffigurante la convergenza ad un valore 
 percentuale costante per un numero di partite sufficientemente elevato.   
-La seconda attività prevede lo svolgimento di una partita utilizzando un mazzo importato da un file di testo, preceduto dalla verifica dell'integrità del mazzo e 
 della correttezza di seme e valore della singola carta.   
 
 
-Saranno pubblicati dei casi di test: i casi di test saranno 6, divisi in 3 casi vincenti e 3 casi perdenti. Ogni caso comprende l'ordine delle carte del mazzo e la
 corrispondenza riga-seme che determina la vittoria. Verranno posizionati nella cartella Custom_Test_Cases.
 Viene pubblicato anche il codice utilizzato per la creazione di casi di test: a scopo illustrativo del ragionamento effettuato viene incluso il procedimento di creazione 
 della cartella e dei casi di test, ma si consiglia di cambiare directory per i test "custom" in modo tale da non sovrascrivere i test "ufficiali".
 Nelle future release verranno migliorati sia il codice principale sia il generatore.


-L'utente può abilitare una delle due attività; nel caso della seconda deve fornire due file di testo, contenenti un mazzo di carte napoletane il primo e le associazioni 
 riga-seme del tavolo da gioco il secondo.; le righe del file che non rispettano la sintassi fornita dalla specifica vengono ignorate dal codice (Valore,Seme). Un mazzo
 verrà considerato nullo se, dopo il controllo successivo all'importazione del file di testo, non contenga le 40 carte previste dal regolamento. 
 
Ad esempio, viene fornito il seguente mazzo: 

-1,3
-4,D
-8,ohjhk
-//commento. 

L'insieme di carte utilizzabili contiene solo il 4 di denara. Il programma verrà interrotto per invalidità del mazzo fornito.


-Verrà creata una cartella Results, dentro cui verranno salvati i grafici previsti dal codice.

 