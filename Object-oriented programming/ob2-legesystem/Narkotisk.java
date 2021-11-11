// oblig2 Rosa

public class Narkotisk extends Sterk {

  public Narkotisk(String navn, int pris, double virke, int styrke) {
    super(navn, pris, virke, styrke);
  }

  @Override
  public int hentStyrke() {
    return styrke;
  }

}
