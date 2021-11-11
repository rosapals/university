public class Rekursjon {
    public static void main(String[] args) {
        Lenkeliste<String> lenkeliste = new Lenkeliste<>();

        lenkeliste.leggTil("A");
        lenkeliste.leggTil("B");
        lenkeliste.leggTil("C");

        lenkeliste.skrivUtRekursivt();
    }
}
