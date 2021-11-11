// oblig2 Rosa

public class Hvit extends Resept {

    protected int pris;
    
    public Hvit(Legemiddel legemiddel, Lege lege, int pasientId, int reit) {
        super(legemiddel, lege, pasientId, reit);
        pris = legemiddel.hentPris();
    }

    @Override
    public String hentFarge() {
        return "hvit";
    }

    @Override
    public int prisAaBetale() {
        return pris;
    }
    
}
