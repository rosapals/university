import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class FilLeserTask implements Runnable{

    int lengde; // subsekvens lengde
    String filnavn;
    boolean erSyk;
    Beholder syke, friske, monitor;
    Scanner sc;
    HashSet<String> subsekvenser;
    HashMap<String, SubSekvens> person;

    public FilLeserTask(int subsekvensLengde, String linje, Beholder syke, Beholder friske){
        lengde = subsekvensLengde;
        String[] linjedel = linje.split(",");
        filnavn = linjedel[0];
        erSyk = Boolean.parseBoolean(linjedel[1]);
        this.syke = syke;
        this.friske = friske;
    }

    public void run(){

        try {
            sc = new Scanner(new File(filnavn));
            subsekvenser = new HashSet<>();
            person = new HashMap<>();
            String subsekvens, reseptor;

            // les linjer i filnavn
            while (sc.hasNextLine()) {
                reseptor = sc.nextLine();
                for (int i = 0; i+lengde <= reseptor.length(); i++) {

                    subsekvens = reseptor.substring(i, i+lengde);
                    subsekvenser.add(subsekvens);
                }
            }
            sc.close();

            for (String ss : subsekvenser) {
                person.put(ss, new SubSekvens(ss));
            }

            if (erSyk) {
                syke.leggTil(person);
            }
            else {
                friske.leggTil(person);
            }

            syke.countdown(); // Beholderen syke er monitor

        }
        catch (FileNotFoundException e) {
            System.out.println(e);
        }
    }
}
