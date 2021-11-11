public class HvitRute extends Rute{

    public HvitRute(int kol, int rad, Labyrint lab){
        super(kol, rad, lab);
    }

    @Override
    public char tilTegn() {
        return '.';
    }
}
