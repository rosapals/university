// oblig1 Rosa

import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Dataklynge {

  private int maks; // antall noder per rack
  private ArrayList<Rack> racks;

  // konstruktor
  public Dataklynge (String filnavn) throws FileNotFoundException {

    int antNoder;
    racks = new ArrayList<Rack>();
    Scanner sc = new Scanner(new File(filnavn));

    // les forste linje i fil
    maks = Integer.parseInt(sc.nextLine());

    // les resten av fil
    while (sc.hasNextLine()) {

      String[] data = sc.nextLine().split(" ");
      antNoder = Integer.parseInt (data[0]);

      int i = 0;
      while (i < antNoder) {

        leggTilNode(new Node (Integer.parseInt(data[1]), Integer.parseInt(data[2])));
        i++;
      }
    }
  sc.close();
  }

  // ta imot ny node
  public void leggTilNode(Node n) {

    Rack ledigRack = null;

    int i = 0;
    while (ledigRack == null && i < racks.size()) {

      if (racks.get(i).antNoder() < maks) {

        ledigRack = racks.get(i);
      }
      i++;
    }

    // om ingen ledige rack eksisterer
    if (ledigRack == null) {

      ledigRack = new Rack(maks);
      racks.add(ledigRack);
    }

    ledigRack.leggTilNode(n);
  }

  // telle noder med nok minne
  public int nokMinne(int min) {

    int antall = 0;
    for (Rack r : racks) {

      antall += r.nokMinne(min);
    }
    return antall;
  }

  public int antPros () {

    return Node.totalAntPros;
  }

  public int antRack () {

    return Rack.totalAntRack;
  }

}
