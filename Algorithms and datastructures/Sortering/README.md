# Prekode for Oblig3 oppgave 1

Dette er et skall for oppgave 1 i Oblig3 i IN2010 høsten 2021.

## Prekode for Python

Den består av:
- `oblig3.py` som inneholder `main` og kjører sorteringsalgoritmene dine på en
  gitt inputfil.
- `countcompares.py` inneholder en klasse `CountCompares` som "wrapper"
  elementet som skal sorteres, og øker en teller hver gang elementet
  sammenlignes med et annet.
- `countswaps.py` inneholder en klasse `CountSwaps` som "wrapper" arrayet, og
  eksponerer en `swap`-metode som også teller byttet.
- `oblig3runner.py` står for kjøringen av eksperimenter og skriving til fil.
  Den sørger for at arrayet som sendes til sorteringsalgoritmen er wrappet med
  `CountSwaps` og at elementene er wrappet med `CountCompares`.
  Merk at den inneholder disse konstantene:
  ```python
  # Put the sorting algorithms under test for part 1 here
  ALGS1 = [insertion.sort, quick.sort]
  # Put the sorting algorithms under test for part 2 here
  ALGS2 = [insertion.sort, quick.sort]
  # Time limit for a single sorting in milliseconds
  TIME_LIMIT_MS = 100;
  # How much n grows each iteration for part 2
  INCREMENT = 1;
  ```
  som du kan justere for å få resultatene du ønsker.
- `insertion.py` som inneholder et skall for insertion sort.
- `quick.py` som inneholder et skall for quicksort.

## Kjøre koden

Ved å kjøre for eksempel:
```sh
$ python3 oblig3.py ../inputs/random_100
```

vil du se følgende utskrift:
```
  n, insertion_cmp, insertion_swaps, insertion_time, quick_cmp, quick_swaps, quick_time
```

og det vil ligge tre nye filer i `inputs`-mappen:
- `random_100_insertion.out`
- `random_100_quick.out`
- `random_100_results.csv`

For å gjøre det enklere å utføre eksperimenter har vi lagt inn en
tidsbegrensning på hvor lenge en sorteringsalgoritme kan kjøre for
deloppgave 2. Den kan justeres ved å endre på `TIME_LIMIT_MS` i
`Oblig3Runner.java` eller `oblig3runner.py`. Den er satt til 100 millisekunder,
så om en algoritme overstiger dette, så vil den ikke kjøres for høyere `n` (som
vil si at du får tomme felter i den resulterende tabellen).
