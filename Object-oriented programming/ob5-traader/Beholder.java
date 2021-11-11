import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.locks.ReentrantLock;

public class Beholder {

    private static ReentrantLock laas = new ReentrantLock();
    private CountDownLatch countDownLatch;
    private ArrayList<HashMap<String, SubSekvens>> hashmaps = new ArrayList<>();
    private int antall = 0;

    public Beholder(int antallTraader){
        countDownLatch = new CountDownLatch(antallTraader);
    }

    public int stoerrelse() {
        return antall;
    }

    public void leggTil(HashMap<String, SubSekvens> hashmap){
        laas.lock();
        try {
            if (hashmap != null){
                antall++;
                hashmaps.add(hashmap);
            }
        }finally{
            laas.unlock();
        }
    }

    public HashMap<String, SubSekvens> taUt(){
        if (antall > 0) {
            antall--;
            return hashmaps.remove(0);
        }
        else {
            System.out.println("Kan ikke ta ut innhold fra beholderen. Antall: 0 ");
            return null;
        }
    }

    public static HashMap<String,SubSekvens> flett
      (HashMap<String,SubSekvens> hashMap1, HashMap<String,SubSekvens> hashMap2) {

        HashMap<String,SubSekvens> flettet = hashMap1;
        HashMap<String,SubSekvens> skalFlettesInn = hashMap2;
        for (String nokkel : skalFlettesInn.keySet()) {

            SubSekvens verdi = skalFlettesInn.get(nokkel);

            // nokkel finnes fra for: Verdien oekes foer nytt element legges til
            if (flettet.containsKey(nokkel)) {
                verdi.oek( flettet.get(nokkel).hentAntall() );
            }
            // nytt element legges til
            flettet.put(nokkel, verdi);
        }
        return flettet;
    }

    public void fletteOperasjon() {
        laas.lock();
        try {
            if (antall > 1){
                leggTil( Beholder.flett( taUt(),taUt() ));
            }
        }finally{
            laas.unlock();
        }
    }

    public void countdown(){
        countDownLatch.countDown();
    }

    public void vent() throws InterruptedException{
        countDownLatch.await();
    }
}


