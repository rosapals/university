// oblig2 Rosa

abstract public class Resept {

    private static int id = 1;
    private int minId;
    private Legemiddel legemiddel;
    private Lege lege;
    private int pasientId;
    private int reit;

    public Resept(Legemiddel legemiddel, Lege lege, int pasientId, int reit) {
        this.legemiddel = legemiddel;
        this.lege = lege;
        this.pasientId = pasientId;
        this.reit = reit;
        minId = id;
        id ++;
    }

    abstract public String hentFarge();
    abstract public int prisAaBetale();

    public boolean bruk() {
        if (reit > 0) {
            reit --;
            return true;
        }
        else {
            return false;
        }
    }

    @Override
    public String toString() {
        return hentFarge().substring(0,1).toUpperCase()+hentFarge().substring(1) + " resept paa " +
               legemiddel.hentNavn() + " (ID " + minId + "). Reit " + reit + ", pris " + prisAaBetale() +
               "\n  Utskrevet av " + lege + " til pasient " + pasientId;
    }

    public int hentId() {
        return minId;
    }

    public Legemiddel hentLegemiddel() {
        return legemiddel;
    }

    public Lege hentLege() {
        return lege;
    }

    public int hentPasientId() {
        return pasientId;
    }

    public int hentReit() {
        return reit;
    }

}