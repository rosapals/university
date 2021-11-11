import java.util.ArrayList;

public abstract class Rute {
    private int kolonne, rad;
    private Labyrint labyrint;
    private Rute north, south, east, west; // naboer
    private ArrayList<Rute> naboer;

    public Rute(int kol, int rad, Labyrint lab) {
        kolonne = kol;
        this.rad = rad;
        labyrint = lab;
        north = null; south = null; east = null; west = null;
        naboer = new ArrayList<>();
    }

    protected ArrayList<Tuppel> gaa(int forrigeKol, int forrigeRad, ArrayList<Tuppel> sti) {
        // sti: hvor jeg er naa
        // stiKopi: et friskt minne
        sti.add(new Tuppel(hentKolonne(), hentRad()));

        for (Rute nabo : naboer) {
            if (! (nabo.hentKolonne() == forrigeKol && nabo.hentRad() == forrigeRad)) {
                ArrayList<Tuppel> stiKopi = new ArrayList<>(sti);
                nabo.gaa(hentKolonne(), hentRad(), stiKopi);
            }
        }
        return sti;
    }

    public void finnUtvei() {
        gaa(hentKolonne(), hentRad(), new ArrayList<Tuppel>());
    }

    protected void lagreUtvei(ArrayList<Tuppel> utvei) {
        hentLabyrint().leggTilUtvei(utvei);
    }

    public abstract char tilTegn();

    public int hentKolonne() {
        return kolonne;
    }

    public int hentRad() {
        return rad;
    }

    protected Labyrint hentLabyrint() {
        return labyrint;
    }

    public void settNorthNabo(Rute nabo) {
        north = leggTil(nabo);
    }

    public void settSouthNabo(Rute nabo) {
        south = leggTil(nabo);
    }

    public void settEastNabo(Rute nabo) {
        east = leggTil(nabo);
    }

    public void settWestNabo(Rute nabo) {
        west = leggTil(nabo);
    }

    private Rute leggTil(Rute nabo) {
        if (nabo != null) {
            naboer.add(nabo);
            return nabo;
        }
        return null;
    }

    // Brukt til aa teste at naboer er registrert riktig
    public String visNaboer() {
        String tekst = "\nNaboer: ";
        if (north != null) {
            tekst += "\nNorth " + north.toString();
        }
        if (south != null) {
            tekst += "\nSouth " + south.toString();
        }
        if (east != null) {
            tekst += "\nEast " + east.toString();
        }
        if (west != null) {
            tekst += "\nWest " + west.toString();
        }
        if (tekst.equals("\nNaboer: ")) {
            tekst = "Ingen naboer ";
        }
        return tekst;
    }

    @Override
    public String toString() {
        return "(" + kolonne+","+rad + ")";
    }
}
