// oblig2 Rosa

public class Militaer extends Hvit {

    public Militaer(Legemiddel legemiddel, Lege lege, int pasientId, int reit) {
        super(legemiddel, lege, pasientId, reit);
    }

    @Override
    public int prisAaBetale() {
        return 0;
    }
    
}
