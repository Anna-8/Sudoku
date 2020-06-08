# Sudoku

Class Sudoku: 
Init():
prende in input un Sudoku scritto sotto forma di stringa e costruisce il CSP. In particolare, costruisce vari dizionari che associano a ogni variabile o i valori che essa può assumere o le variabili con cui è vincolata. 

BuildDict():
funzione utilizzata da Init() per costruire il dizionario che ad ogni variabile del CSP associa i valori che essa può assumere in base agli elementi della stringa che rappresenta il Sudoku.

Backtrack():
funzione che esegue la Backtracking Search: assegna un valore casuale tra quelli disponibili a una cella del Sudoku e se è consistente attraverso una funzione di inferenza valuta se questo assegnamento porta o meno alla violazione di vincoli. In caso positivo, "torna indietro" annullando l'assegnazione e tenta con un altro valore.

Inference():
in base al valore di strategy in input chiama ForwardChecking() o MAC().

Select_Unassigned_Variable():
selezionata tra le variabili del sudoku non assegnate quella che ha meno valori disponibili nel dizionario.

MAC():
controlla che tutte le variabili vincolate a una variabile appena assegnata abbiano ancora dei valori a disposizione. In caso negativo, ritorna failure, altrimenti controlla anche quelle a loro volta vincolate a queste variabili, propagando ricorsivamente i vincoli.

ForwardChecking():
esegue gli stessi controlli della funzione MAC() ma solo sulle variabili direttamente vincolate alla variabile appena assegnata.

Test:
file dedicato all'esecuzione di test su una serie di Sudoku memorizzati nella cartella Data. 
Calcola il tempo di risoluzione dei Sudoku utilizzando la Backtrack() prima con la strategia di Forward Checking e poi di Maintaning Arc Consistency.





