// oblig2 Rosa

public class PResept extends Hvit {
    
    public PResept (Legemiddel legemiddel, Lege lege, int pasientId) {
        super(legemiddel, lege, pasientId, 3);
    }

    @Override
    public int prisAaBetale() {
        if (pris < 108) {
            return 0;
        }
        else {
            return pris-108;
        }
    }

}
