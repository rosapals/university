class NodeTest {

  public static void main (String[] args) {

    Node nodeA = new Node(16, 1);
    Node nodeB = new Node(32, 2);


    if (nodeA.nokMinne(16)) {
      System.out.println("Nok minne OK");

    } else {
      System.out.println("Nok minne ikke OK");
    }

    // hente statisk variabel i Node klassen
    int total = Node.totalAntPros;
    System.out.println("Antall prosessorer: " + total);
  }
}
