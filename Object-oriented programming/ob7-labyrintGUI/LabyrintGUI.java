import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

// Hovedprogram

public class LabyrintGUI {
    public static void main(String[] args) {
        File fil = null;
        Labyrint lab = null;
        int antKol, antRad;
        ArrayList<ArrayList<Rute>> rutenett;

        // velg en fil
        JFileChooser velger = new JFileChooser();
        int resultat = velger.showOpenDialog(null);
        if (resultat != JFileChooser.APPROVE_OPTION) {
            System.exit(1);
        }
        fil = velger.getSelectedFile();
        Scanner leser = null;
        try {
            leser = new Scanner(fil);
        } catch (FileNotFoundException e) {
            System.exit(1);
        }

        // opprett labyrinten
        try {
            lab = new Labyrint(fil);
        } catch (FileNotFoundException e) {
            System.out.printf("FEIL: Kunne ikke lese valgt fil ");
            System.exit(1);
        }

        // GUI
        antKol = lab.antKolonner();
        antRad = lab.antRader();
        rutenett = lab.hentRutenett();

        JFrame vindu = new JFrame("Drittbrett");
        vindu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(antRad,antKol));
        for (ArrayList<Rute> rad : rutenett) {
            for (Rute rute : rad) {
                rute.initGUI();
                panel.add(rute);
            }
        }
        vindu.add(panel);
        vindu.pack();
        vindu.setVisible(true);
    }
}