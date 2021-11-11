// oblig2 Rosa

public class Lege {

    protected String navn;

    public Lege (String navn) {
        this.navn = navn;
    }

    @Override
    public String toString() {
        return navn;
    }

    public String hentNavn() {
        return navn;
    }

}