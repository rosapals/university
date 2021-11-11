import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;

public class VirusAnalyzer {

    private static int lengde = 3; // subsekvens lengde
    private static int antallFletteTraader = 4; // maa vaere et partall for aa gjoere det enkelt
    
    public static void main(String[] args) {
        
        ArrayList<String> filer = null;
        try {
            filer = hentInnhold("metadata.csv");
        }catch (FileNotFoundException e){
            System.out.println(e);
        }
        Beholder syke = new Beholder(filer.size()); // countDownLatch er antall filer
        Beholder friske = new Beholder(antallFletteTraader); // countDownLatch er antallFletteTraader valgt

        for (String filnavn : filer){
            new Thread(new FilLeserTask(lengde, filnavn, syke, friske)).start();
        }

        // Beholderen syke fungerer som countdownlatch
        try {
            syke.vent();
        } catch (InterruptedException e){
            System.out.println("Noe gikk galt. InterruptedException ");
        }

        // Beholderen friske fungerer som monitor
        for (int i = 0; i < antallFletteTraader/2; i++){
            new Thread(new FletteTask(syke, friske)).start();
        }
        
        for (int i = 0; i < antallFletteTraader/2; i++){
            new Thread(new FletteTask(friske, friske)).start();
        }

        // Beholderen friske fungerer som countdownlatch
        try {
            friske.vent();
        } catch (InterruptedException e){
            System.out.println("Noe gikk galt. InterruptedException ");
        }

        System.out.println("\n DATA FERDIG LEST INN \n");

        // statistikk
        HashMap<String, SubSekvens> friskeHashMap = friske.taUt();
        for (SubSekvens subSyk : syke.taUt().values()) {
            for (SubSekvens subFrisk : friskeHashMap.values()) {
                if (subSyk.toString().equals( subFrisk.toString() )){

                    int differanse = subSyk.hentAntall() - subFrisk.hentAntall();
                    if (differanse >= 5){
                        System.out.println(subSyk.toString() +" : syke["+ subSyk.hentAntall() +"]  friske["+ 
                        subFrisk.hentAntall() +"]  diff["+ differanse +"]");
                    }
                }
            }
        }

        System.out.println("\n STATISTIKK FERDIG \n");
    }

    private static ArrayList<String> hentInnhold(String filnavn) throws FileNotFoundException{

        ArrayList<String> innhold = new ArrayList<>();
        Scanner sc = new Scanner(new File(filnavn));
        sc.nextLine(); // hopp over overskrift

        while (sc.hasNextLine()) {
            innhold.add(sc.nextLine());
        }
        sc.close();
        return innhold;
    }
}
