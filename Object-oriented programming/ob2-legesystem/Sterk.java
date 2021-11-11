// oblig2 Rosa

abstract public class Sterk extends Legemiddel {

  protected int styrke;

  public Sterk(String navn, int pris, double virke, int styrke) {
    super(navn, pris, virke);
    this.styrke = styrke;
  }

  abstract public int hentStyrke();
  
}
