import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

// en rute beskrives på formen (kol, rad)
public class Labyrint {
    private int antKolonner, antRader;
    private ArrayList<ArrayList<Rute>> rutenett;
    private ArrayList<ArrayList<Tuppel>> utveier;

    public Labyrint(File fil) throws FileNotFoundException {
        rutenett = lesFil(fil);
        registrerNaboer();
        //utveier = new ArrayList<>();
        //navn = filnavn.substring(11, filnavn.length()-3);
    }

    public ArrayList<ArrayList<Tuppel>> finnUtveiFra(int kol, int rad) {
        utveier = new ArrayList<>();
        hentRute(kol, rad).finnUtvei();
        return utveier;
    }

    private ArrayList<ArrayList<Rute>> lesFil(File fil) throws FileNotFoundException {
        Scanner sc = new Scanner(fil);
        ArrayList<ArrayList<Rute>> rutenett = new ArrayList<>();
        ArrayList<Rute> rad = new ArrayList<>();
        int rutensRad = 0;
        int rutensKol = 0;
        Rute nyRute;

        String[] data = sc.nextLine().split(" ");
        antRader = Integer.parseInt(data[0]);
        antKolonner = Integer.parseInt(data[1]);

        while (sc.hasNext()) {
            String[] radArray = sc.nextLine().split("");
            while (rutensKol < antKolonner) {
                if (radArray[rutensKol].equals("#")) {
                    nyRute = new SortRute(rutensKol++, rutensRad, this);
                }
                else if (rutensRad == 0 || rutensRad == antRader-1 || rutensKol == 0 || rutensKol == antKolonner-1) {
                    nyRute = new Aapning(rutensKol++, rutensRad, this);
                }
                else {
                    nyRute = new HvitRute(rutensKol++, rutensRad, this);
                }
                rad.add(nyRute);
            }
            rutenett.add(rad);
            rad = new ArrayList<>();
            rutensRad++;
            rutensKol = 0;
        }
        sc.close();
        return rutenett;
    }

    private void registrerNaboer() {
        int kol, rad;
        for (ArrayList<Rute> row : hentRutenett()) {
            for (Rute rute : row) {

                rad = rute.hentRad();
                kol = rute.hentKolonne();

                rute.settNorthNabo(hentRute(kol, rad-1));
                rute.settSouthNabo(hentRute(kol, rad+1));
                rute.settEastNabo(hentRute(kol+1, rad));
                rute.settWestNabo(hentRute(kol-1, rad));
            }
        }
    }

    public void leggTilUtvei(ArrayList<Tuppel> utvei) {
        hentUtveier().add(utvei);
    }

    private Rute hentRute(int kol, int rad) {
        for (ArrayList<Rute> row : hentRutenett()){
            for (Rute rute : row){
                if (rute.hentKolonne() == kol && rute.hentRad() == rad) {
                    return rute;
                }
            }
        }
        return null;
    }

    private ArrayList<ArrayList<Rute>> hentRutenett() {
        return rutenett;
    }

    public ArrayList<ArrayList<Tuppel>> hentUtveier() {
        return utveier;
    }
    
    @Override
    public String toString() {
        String rutenett = "";
        for (ArrayList<Rute> rad : hentRutenett()){
            for (Rute rute : rad){
                rutenett += rute.tilTegn();
            }
            rutenett += "\n";
        }
        return rutenett;
    }

    // for aa faa oversikt over koordinatene
    public String toStringKoordinat() {
        String rutenett = "";
        for (ArrayList<Rute> rad : hentRutenett()){
            for (Rute rute : rad){
                rutenett += rute;
            }
            rutenett += "\n";
        }
        return rutenett;
    }

    // for aa teste at riktig subklasse av Rute ble opprettet
    public String toStringType() {
        String rutenett = "";
        for (ArrayList<Rute> rad : hentRutenett()){
            for (Rute rute : rad){
                if (rute instanceof Aapning) {
                    rutenett += "A ";
                }
                else if (rute instanceof HvitRute) {
                    rutenett += "H ";
                }
                else {
                    rutenett += "S ";
                }
            }
            rutenett += "\n";
        }
        return rutenett;
    }
}