import java.util.ArrayList;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

// En hvit rute kan føre en sti til en aapning

public class HvitRute extends Rute {

    public HvitRute(int kol, int rad, Labyrint lab){
        super(kol, rad, lab);
    }

    @Override
    public char tilTegn() {
        return '.';
    }

    @Override
    protected void initGUI() {
        super.initGUI();
        setBackground(Color.WHITE);
        setOpaque(true);

        class Rutetrykk implements ActionListener {
            Labyrint lab = hentLabyrint();
            ArrayList<ArrayList<Tuppel>> utveier;
            ArrayList<Tuppel> utvei;

            @Override
            public void actionPerformed (ActionEvent e) {
                // naar man trykker paa en hvit rute
                utveier = lab.finnUtveiFra(hentKolonne(), hentRad());

                // vask labyrinten forst
                for (ArrayList<Rute> rad : lab.hentRutenett()) {
                    for (Rute rute : rad) {
                        if (rute instanceof HvitRute) {
                            HvitRute hvitRute = (HvitRute) rute;
                            hvitRute.vask();
                        }
                    }
                }
                // vis utvei
                if (utveier.size() > 0) {
                    // for enkelhetens skyld visualiseres alltid forste utvei i listen
                    utvei = utveier.get(0);
                    Tuppel forste = utvei.get(0);
                    // ruten man trykker på viser antall utveier funnet
                    lab.hentRute(forste.y(), forste.x()).setText("1/"+utveier.size());

                    for (Tuppel tuppel : utvei) {
                        HvitRute rute = (HvitRute) lab.hentRute(tuppel.y(), tuppel.x());
                        // rutene som representerer utvei blir farget
                        rute.utveiGUI();
                    }
                }
            }
        }
        addActionListener(new Rutetrykk());
    }

    private void utveiGUI() {
        setBackground(Color.PINK);
        setOpaque(true);
    }

    private void vask() {
        setText("");
        setBackground(Color.WHITE);
        setOpaque(true);
    }
}
