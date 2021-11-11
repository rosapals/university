// oblig1 Rosa

import java.io.FileNotFoundException;

class Hovedprogram {

  public static void main(String[] args) throws FileNotFoundException {

    // opprette dataklynge-objekt
    Dataklynge abel = new Dataklynge("dataklynge.txt");

    // info til terminal
    String tekst = "Noder min. 32GB: " + abel.nokMinne(32);
    tekst += "\nNoder min. 64GB: " + abel.nokMinne(64);
    tekst += "\nNoder min. 128GB: " + abel.nokMinne(128);
    tekst += "\nProsessorer: " + abel.antPros();
    tekst += "\nRack i bruk: " + abel.antRack() + "\n";
    System.out.println(tekst);
  }

}
