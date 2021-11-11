// oblig2 Rosa

import java.lang.Math;

public class Blaa extends Resept {

    private int pris;
    
    public Blaa(Legemiddel legemiddel, Lege lege, int pasientId, int reit) {
        super(legemiddel, lege, pasientId, reit);
        pris = legemiddel.hentPris();
    }

    @Override
    public String hentFarge() {
        return "blaa";
    }

    @Override
    public int prisAaBetale() {
        return (int) Math.round(pris*0.25);
    }

}
