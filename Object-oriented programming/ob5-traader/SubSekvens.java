public class SubSekvens {

    private String subsekvens;
    private int antall;

    public SubSekvens(String subsekvens) {
        this.subsekvens = subsekvens;
        antall = 1;
    }

    public void oek(int okning) {
        antall += okning;
    }

    public int hentAntall() {
        return antall;
    }

    @Override
    public String toString() {
        return subsekvens;
    }
}