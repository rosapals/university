import java.util.ArrayList;

class RackTest {

  public static void main(String[] args) {


    int maksAntNoder = 2;

    Node node1 = new Node(32,1);
    Node node2 = new Node (32,5);

    Rack rack1 = new Rack(maksAntNoder);
    Rack rack2 = new Rack(maksAntNoder);

    rack1.leggTilNode(node1);
    rack1.leggTilNode(node2);

    if (rack1.nokMinne(32) == 2) {
      System.out.println("Legg til node og Noder med nok minne OK");
    } else {System.out.println("Legg til node og Noder med nok minne ikke OK");
  }
    if (Node.totalAntPros == 6) {
      System.out.println("Statisk totalAntPros OK");
    } else {System.out.println("Statisk totalAntPros ikke OK");
  }
  if (Rack.totalAntRack == 2) {
    System.out.println("Statisk totalAntRack OK");
  } else {System.out.println("Statisk totalAntRack ikke OK");
   }



  }
}
