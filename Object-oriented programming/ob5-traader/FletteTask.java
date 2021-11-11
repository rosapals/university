public class FletteTask implements Runnable {

    private Beholder beholder;
    private Beholder monitor = null;

    public FletteTask(Beholder beholder, Beholder monitor) {
        this.beholder = beholder; // beholder som skal flettes
        this.monitor = monitor; // beholder som skal brukes som monitor
    }

    @Override
    public void run() {
        try {
            while (beholder.stoerrelse() > 1){
                beholder.fletteOperasjon();
            }
            monitor.countdown();
        }catch (Exception e) {
            System.out.println(e);
        }
    }
}