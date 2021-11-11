// oblig1 Rosa

public class Rack {

  public static int totalAntRack; /* totalt i hele systemet, litt dumt at den
        er public i tilfelle noen endrer den */
  private Node[] noder;

  // konstruktor
  public Rack (int maks) {

    noder = new Node[maks];
    totalAntRack ++;
  }

  public void leggTilNode(Node n) {

    int i = 0;
    while (i < noder.length && noder[i] != null) {

      // finner indeks med ledig plass
      i++;
    }
    if (noder[i] == null) {

      noder[i] = n;
    }
  }

  // telle noder med nok minne
  public int nokMinne(int min) {

    int antall = 0;

    for (Node n : noder) {

      if (n != null) {

        if (n.nokMinne(min)) {

          antall ++;
        }
      }
    }
    return antall;
  }

  // telle antall noder i rack
  public int antNoder() {

    int antall = 0;

    for (Node n : noder) {

      if (n != null) {

        antall++;
      }
    }
    return antall;
  }

}
