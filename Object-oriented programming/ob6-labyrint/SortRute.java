import java.util.ArrayList;

public class SortRute extends Rute {

    public SortRute(int kol, int rad, Labyrint lab) {
        super(kol, rad, lab);
    }
    
    @Override
    public char tilTegn() {
        return '#';
    }

    @Override
    protected ArrayList<Tuppel> gaa(int forrigeKol, int forrigeRad, ArrayList<Tuppel> sti) {
        return null;
    }
}
