// oblig2 Rosa

abstract public class Legemiddel {

  // felles variabler for alle legemidler
  private static int id = 1;
  private int minId;

  private String navn;
  private int pris;
  private double virkestoff;

  public Legemiddel(String navn, int pris, double virke) {
    this.navn = navn;
    this.pris = pris;
    virkestoff = virke;

    minId = id;
    id ++;
  }

  public int settNyPris(int nyPris) {
    pris = nyPris;
    return pris;
  }

  @Override
  public String toString() {
    return navn.substring(0,1).toUpperCase()+navn.substring(1) + " (ID " + minId + ") har " + virkestoff + " mg virkestoff og koster kr " + pris;
  }

  public int hentId() {
    return minId;
  }

  public String hentNavn() {
    return navn;
  }

  public int hentPris() {
    return pris;
  }

  public double hentVirkestoff() {
    return virkestoff;
  }

}
