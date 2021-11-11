// oblig2 Rosa

public class Spesialist extends Lege implements Godkjenningsfritak {

    private String kontrollId;

    public Spesialist(String navn, String id) {
        super(navn);
        kontrollId = id;
    }

    @Override
    public String toString() {
        return navn + " (kontrollID " + kontrollId + ")";
    }

    @Override
    public String hentKontrollId() {
        return kontrollId;
    }

}