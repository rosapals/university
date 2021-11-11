// oblig1 Rosa

class Node {

  public static int totalAntPros; /* for alle noder i systemet, litt dumt at
        den er public i tilfelle noen endrer den */
  private int minne;

  //konstruktor
  public Node (int m, int p) {

    minne = m;

    if (p > 2) {
      totalAntPros += 2;
    } else if (p < 1) {
      totalAntPros += 1;
    } else {
      totalAntPros += p;
    }
  }

  public boolean nokMinne (int min) {

    return minne >= min;
  }

}
