// oblig2 Rosa

public class Vanedannende extends Sterk {

  public Vanedannende(String navn, int pris, double virke, int styrke) {
    super(navn, pris, virke, styrke);
  }

  @Override
  public int hentStyrke() {
    return styrke;
  }

}
