// oblig2 Rosa

import java.util.ArrayList;

public class Hovedprogram {

    public static void main(String[] args) {

        // medisiner
        Vanlig spiral = new Vanlig("kyleena", 550, 2.2);
        Narkotisk morfin = new Narkotisk("morfin", 300, 0.2, 3);
        Vanedannende sovemedisin = new Vanedannende("sovemedisin", 200, 0.3, 2);

        ArrayList<Legemiddel> legemidler = new ArrayList<Legemiddel>(3);
        legemidler.add(spiral);
        legemidler.add(morfin);
        legemidler.add(sovemedisin);

        // leger
        Lege allmennLege = new Lege("Dr Vanlig Lege");
        Spesialist spesialist = new Spesialist("Dr Spesialist", "9909");

        ArrayList<Lege> leger = new ArrayList<Lege>(2);
        leger.add(allmennLege);
        leger.add(spesialist);

        // resepter
        ArrayList<Resept> resepter = new ArrayList<Resept>(4);
        resepter.add(new Blaa(sovemedisin, allmennLege, 3536, 1));
        resepter.add(new Hvit(spiral, allmennLege, 2425, 1));
        resepter.add(new PResept(spiral, allmennLege, 2323));
        resepter.add(new Militaer(morfin, spesialist, 4342, 2));

        skriv(legemidler, leger, resepter);
    }



    private static void skriv(ArrayList<Legemiddel> arr1, ArrayList<Lege> arr2, ArrayList<Resept> arr3) {

        System.out.println("\n>Legemidler: ");
        for (Legemiddel l : arr1) {
            System.out.println(l);
        }

        System.out.println("\n>Leger ");
        for (Lege l : arr2) {
            System.out.println(l);
        }

        System.out.println("\n>Resepter ");
        for (Resept r : arr3) {
            System.out.println(r);
        }
    }

}