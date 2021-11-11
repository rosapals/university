// enveis lenkeliste
public class Lenkeliste<T> implements Liste<T> {

    class Node {
        Node neste = null;
        T data;
    
        Node (T x) {
            data = x;
        }

        @Override
        public String toString() {
            return data.toString();
        }
    }

    public Node start = null;
    public Node slutt = null;

    @Override
    public int stoerrelse() {

        // gaar gjennom lista og teller noder
        int antall = 0;
        Node peker = start;
        while (peker != null) {
            antall ++;
            peker = peker.neste;
        }
        return antall;
    }

    @Override
    public void leggTil(int pos, T x) throws UgyldigListeIndeks {

        Node nyNode = new Node(x);

        // hvis ny node skal ligge fremst i lista
        if (pos == 0) {
            nyNode.neste = start;
            start = nyNode;

            // hvis lista bestaar av kun en node er slutt og start den samme
            if (stoerrelse() == 1) {
                slutt = nyNode;
            }
        }

        else if (pos < 0 || pos > stoerrelse() || stoerrelse() == 0) {
            throw new UgyldigListeIndeks(pos);
        }
        
        else if (pos == stoerrelse()) {
            leggTil(x);
        }

        else {
                // teller oss frem til noden foer der ny node skal ligge
                Node peker = start;
                for (int i = 0; i < pos-1; i++) {
                    peker = peker.neste;
                }

                nyNode.neste = peker.neste;
                peker.neste = nyNode;
        }
    }

    @Override
    public void leggTil(T x) {

        Node nyNode = new Node(x);

        // om lista er tom
        if (stoerrelse() == 0) {
            start = nyNode;
            slutt = start;
        }
       
        // om det finnes element(er) i lista
        else {
            slutt.neste = nyNode;
            slutt = nyNode;
        }
    }

    @Override
    public void sett(int pos, T x) throws UgyldigListeIndeks {

        if (pos < 0 || pos >= stoerrelse()) {
            throw new UgyldigListeIndeks(pos);
        }

        // teller oss frem til noden som skal overskrives
        else {
            Node peker = start;
            for (int i = 0; i < pos; i++) {
                peker = peker.neste;
            }
            peker.data = x;
        }
    }

    @Override
    public T hent(int pos) throws UgyldigListeIndeks {

        if (pos < 0 || pos >= stoerrelse()) {
            throw new UgyldigListeIndeks(pos);
        }

        // gaar gjennom lista og teller oss til rett plass
        else {
            Node peker = start;
            for (int i = 0; i < pos; i++) {
                peker = peker.neste;
            }
            return peker.data;
        }
    }

    @Override
    public T fjern(int pos) throws UgyldigListeIndeks {

        T dataSomFjernes;

        if (pos < 0 || pos >= stoerrelse()) {
            throw new UgyldigListeIndeks(pos);
        }

        else if (stoerrelse() == 1 || pos == 0) {
            dataSomFjernes = fjern();
        }

        else {

            // teller oss frem til noden foer den som skal slettes
            Node peker = start;

            for (int i = 0; i < pos-1; i++) {
                peker = peker.neste;
            }
            dataSomFjernes = peker.neste.data;
            peker.neste = peker.neste.neste;

            // hvis peker-noden naa ble sist maa slutt-variabel peke paa den
            if (peker.neste == null) {
                slutt = peker;
            }
        }
        return dataSomFjernes;
    }

    // fjern forste element i lista
    @Override
    public T fjern() throws UgyldigListeIndeks {
        
        T dataSomFjernes;

        if (stoerrelse() == 0) {
            throw new UgyldigListeIndeks(-1);
        }

        else {
            dataSomFjernes = start.data;

            if (stoerrelse() == 1) {
                start = null;
                slutt = null;
            }
            else {
                start = start.neste;
            }
            return dataSomFjernes;
        }
    }

    @Override
    public String toString() {

        // gaa gjennom alle elementer
        String tekst = "";
        Node peker = start;
        while (peker != null) {
            tekst += peker.toString() + " ";
            peker = peker.neste;
        }
        return tekst + "\nstart:" + start + " slutt:" + slutt + " str:" + stoerrelse();
    }
    
}