import java.util.ArrayList;

public class Aapning extends HvitRute {
    
    public Aapning(int kol, int rad, Labyrint lab) {
        super(kol, rad, lab);
    }

    @Override
    protected ArrayList<Tuppel> gaa(int forrigeKol, int forrigeRad, ArrayList<Tuppel> sti) {
        sti.add(new Tuppel(hentKolonne(), hentRad()));
        // lagre stien som ble brukt hit
        lagreUtvei(sti);
        return null;
    }
}
