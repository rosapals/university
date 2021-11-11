import java.util.ArrayList;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class SortRute extends Rute {

    public SortRute(int kol, int rad, Labyrint lab) {
        super(kol, rad, lab);
    }
    
    @Override
    public char tilTegn() {
        return '#';
    }

    @Override
    protected ArrayList<Tuppel> gaa(int forrigeKol, int forrigeRad, ArrayList<Tuppel> sti) {
        // sort rute er alltid dead end
        return null;
    }

    @Override
    protected void initGUI() {
        super.initGUI();
        setBackground(Color.BLACK);
        setOpaque(true);
    }
}
